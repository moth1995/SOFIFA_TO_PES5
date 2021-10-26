import requests
from bs4 import BeautifulSoup
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import sys
import os
import conseguir_jugadores
import jugador
import savefile
from PIL import Image
from idlelib.tooltip import Hovertip

def my_tip(obj, text_info):
    Hovertip(obj, text_info, hover_delay=1000)

def get_list_index_by_element(lista, element):
    return lista.index(element)

def get_teamlist(session,url,web_opt):
    #print(website+url+web_opt)
    #print(web_opt)
    time.sleep(5)
    site=session.get(website+url+web_opt,headers=headnav)
    #print(site.text)
    #print(site.status_code)
    if (site.status_code)==200:
        soup=BeautifulSoup(site.text,'html.parser')
        table=soup.find('table',attrs={'class':'table table-hover persist-area'}).find('tbody').find_all('td',attrs={'class':'col-name-wide'})
        #print(nt_table)
        names=[]
        for tag in table:
            divTags = tag.find_all("div")
            for tag in divTags:
                if tag.find('img'):
                    continue
                names.append(tag.text)
        #print(names)
        links=[]
        for tag in table:
            divTags = tag.find_all("a")
            for tag in divTags:
                if tag.get('rel'):
                    continue
                links.append(tag.get('href'))
        #print(nt_links)
        #print(len(nt_links),len(names))
        if len(links)==len(names):
            return (names,links)
    else:
        return [],[]

def get_leagues(session,web_opt):
    #print(web_opt)
    time.sleep(5)
    lg_site=session.get(website+'/teams?type=club'+web_opt,headers=headnav)
    if (lg_site.status_code)==200:
        soup=BeautifulSoup(lg_site.text,'html.parser')
        lg_az=soup.find('optgroup',attrs={'label':'A-Z'}).find_all('option')
        lg_top5=soup.find('optgroup',attrs={'label':'Top 5'}).find_all('option')
        #print(lg_table)
        lg_names=[]
        lg_values=[]
        for i in lg_top5:
            if i =="" or i.get('value')=="":
                continue
            lg_names.append(i.text)
            lg_values.append(i.get('value'))
        for i in lg_az:
            if i =="" or i.get('value')=="":
                continue
            lg_names.append(i.text)
            lg_values.append(i.get('value'))
        #print(lg_names,lg_values)
        if len(lg_names)==len(lg_values):
            return lg_names,lg_values
    else:
        return [],[]

def convert(team,session,namelist,linklist,gamever):
    if team!="":
        if gamever!=0:
            messagebox.showinfo(title=appname, message="Select the folder where you wanna save your file")
            folder = filedialog.askdirectory(initialdir=os.path.expanduser('~/Documents'),title=appname)
            team=str(linklist[namelist.index(team)])
            time.sleep(5)
            links,filename = conseguir_jugadores.conseguir_jugadores(team,session)
            #print(filename)
            #print("  ")
            players=[]
            total_players = len(links)
            process_players = 0
            counter = 1
            for link in range(len(links)):
                #print(links[link])
                player=jugador.player_scrapper(links[link],session)
                if type(player)==int:
                    messagebox.showerror(title=appname, message="Status code "+str(player))
                    break
                players.append(player)
                bar['value']+=(counter/total_players)*100
                process_players+=counter
                percent.set(str(int((process_players/total_players)*100))+"%")
                progress_text.set(str(process_players)+"/"+str(total_players)+" players converted")
                root.update_idletasks()                
                # Line below is for break the loop only when debugging
                #break
            #print("fin")
            #print(players)
            if players!=[]:
                if gamever==1:
                    #this is for mdb
                    savefile.csv_to_mdb(folder+'/'+filename,savefile.csv_parser(players))
                    messagebox.showinfo(title=appname, message="Your mdb file for "+str(filename) + "\nhas been generated")
                elif gamever==2:
                    #this is for csv
                    savefile.write_csv(folder+'/'+filename,players)
                    messagebox.showinfo(title=appname, message="Your csv file for "+str(filename) + "\nhas been generated")
            else:
                messagebox.showerror(title=appname, message="Couldn't retrieve data for players on " + str(filename))
            bar['value']=0
            percent.set("")
            progress_text.set("")
            root.update_idletasks()
        else:
            messagebox.showerror(title=appname, message="Please select an output file type")
    else:
        messagebox.showerror(title=appname, message="Please select a club")


def download_logos(session,league_name,clubnames,clublinks,resize):
    #print(f"resize value is {resize}")
    # size for unknow 466
    size_64 = 64, 64
    # size for unknow 464
    size_32 = 32, 32
    if clublinks!= []:
        messagebox.showinfo(title=appname, message="Select the folder where you wanna save your logos")
        folder = filedialog.askdirectory(initialdir=os.path.expanduser('~/Documents'),title=appname)
        folder = folder + '/' + league_name
        if not os.path.exists(folder):
            os.makedirs(folder)
        total_logos = len(clublinks)
        process_logos = 0
        counter = 1            
        for i in range(0,len(clublinks)):
            time.sleep(5)
            #print (f"downloading https://cdn.sofifa.com/teams/{clublinks[i].split('/')[2]}/360.png")
            img = session.get(f"https://cdn.sofifa.com/teams/{clublinks[i].split('/')[2]}/360.png")
            with open(f"{folder}/{clubnames[i]}.png", "wb") as image:
                image.write(img.content)
            if (resize):
                if not os.path.exists(f"{folder}/64"):
                    os.makedirs(f"{folder}/64")
                if not os.path.exists(f"{folder}/32"):
                    os.makedirs(f"{folder}/32")
                # first we resize to 64x64
                im = Image.open(f"{folder}/{clubnames[i]}.png")
                im.thumbnail(size_64, Image.ANTIALIAS)
                im.save(f"{folder}/64/{clubnames[i]}.png")
                # first we resize to 32x32
                im = Image.open(f"{folder}/{clubnames[i]}.png")
                im.thumbnail(size_32, Image.ANTIALIAS)
                im.save(f"{folder}/32/{clubnames[i]}.png")
            bar['value']+=(counter/total_logos)*100
            process_logos+=counter
            percent.set(str(int((process_logos/total_logos)*100))+"%")
            progress_text.set(str(process_logos)+"/"+str(total_logos)+" logos downloaded")
            root.update_idletasks()
        messagebox.showinfo(title=appname, message="All logos downloaded!")
        bar['value']=0
        percent.set("")
        progress_text.set("")
        root.update_idletasks()                

    else:
        messagebox.showerror(title=appname, message="Please select a League")


def login(username,password,webopt):
    global logedaslbl, fifavers, fifaverslinks, updatename, updatelink, web_opt
    #print(webopt)
    #payload = {'email': username, 'password': password,'submit':''}
    payload = {'email': username, 'password': password,}
    #print (payload)
    login_page = website+'/api/signIn/'
    s = requests.Session()
    s.post(login_page, data=payload,headers=headnav)
    r=s.get(website,headers=headnav)
    login= BeautifulSoup(r.text,'html.parser').find_all('a',{'class':'bp3-button bp3-minimal need-sign-in'})
    if login!=[]:
        #print("error al loguearse")
        return False
    else:
        login=BeautifulSoup(r.text,'html.parser').find('a',{'class':'bp3-button bp3-minimal block dropdown-toggle'}).text
        #print("usted se ha logueado correctamente como "+login)
        logedaslbl.config(text="Login as "+ login)
        #now we load the fifa versions and their updates
        h2=BeautifulSoup(r.text,'html.parser').find('h2')
        for a in h2.find_all('div',attrs={'class':'bp3-menu'})[0].find_all('a',attrs={'class':'bp3-menu-item'}):
            fifavers.append(a.text)
            fifaverslinks.append(a.get('href').replace('/','').replace('?','&'))
        for a in h2.find_all('div',attrs={'class':'bp3-menu'})[1].find_all('a',attrs={'class':'bp3-menu-item'}):
            updatename.append(a.text)
            updatelink.append(a.get('href').replace('/','').replace('?','&'))
        if fifavers!=[] and updatename!=[]:
            fifavercmb.config(values=fifavers)
            fifavercmb.set(fifavers[0])
            updatecmb.config(values=updatename)
            updatecmb.set(updatename[0])
        web_opt = webopt + updatelink[0]
        #print(web_opt)
        return s, web_opt

def load_clubs(*args):
    global clubnames,clublinks
    league_selected=lgcmb.get()
    #print(web_opt)
    clubnames,clublinks=get_teamlist(login_session,'/teams?type=club&lg[]='+str(leag_val[leag_names.index(league_selected)]),web_opt)
    clubcmb.config(values=clubnames)
    clubcmb.set("")


def load_cmb(session,web_opt):
    #print(web_opt)
    global ntnames,ntlinks,leag_names,leag_val
    ntnames,ntlinks=get_teamlist(session,'/teams?type=national',web_opt)
    leag_names,leag_val=get_leagues(session,web_opt)
    #print(len(ntnames))
    if ntnames!=[]:
        ntcmb.config(values=ntnames)
    if leag_names!=[]:
        lgcmb.config(values=leag_names)

def update_webopt(fifa_ver, update_selected, session):
    global web_opt, updatename
    # If update_selected is empty then it comes from fifavercmb
    if update_selected == "":
        #print(fifa_ver)
        #print(fifaverslinks[get_list_index_by_element(fifavers,fifa_ver)])
        temp = fifaverslinks[get_list_index_by_element(fifavers,fifa_ver)]
        webopt='&hl=en-US&attr=classic&layout=new&units=mks'
        web_opt = webopt + temp
        updatename = []
        updatelink = []
        r = session.get(f"{website}/{web_opt}")
        h2=BeautifulSoup(r.text,'html.parser').find('h2')
        for a in h2.find_all('div',attrs={'class':'bp3-menu'})[1].find_all('a',attrs={'class':'bp3-menu-item'}):
            updatename.append(a.text)
            updatelink.append(a.get('href').replace('/','').replace('?','&'))
        if  updatename!=[]:
            updatecmb.config(values=updatename)
            updatecmb.set(updatename[0])
        load_cmb(session,web_opt)
    # Else comes from updatecmb
    elif fifa_ver == "":
        #print(update_selected)
        #print(updatelink[get_list_index_by_element(updatename,update_selected)])
        temp = updatelink[get_list_index_by_element(updatename,update_selected)]
        webopt='&hl=en-US&attr=classic&layout=new&units=mks'
        web_opt = webopt + temp
        load_cmb(session,web_opt)

def login_action(user,pw,web_opt):
    #print (user,pw)
    global login_session
    login_session, web_opt=login(user,pw,web_opt)
    if login_session:
        root.deiconify()
        loginsc.destroy()
        load_cmb(login_session,web_opt)

    else:
        messagebox.showerror(title=appname, message="Login error please check again your credencials")

def toggle_password():
    global password_entry, checkbutton
    if checkbutton.var.get():
        password_entry['show'] = "*"
    else:
        password_entry['show'] = ""


def close():
    loginsc.destroy()
    root.destroy()
    sys.exit()


website='https://sofifa.com'
headnav={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
login_session=False
logedusername=""
web_opt='&hl=en-US&attr=classic&layout=new&units=mks'#+'&r=210064&set=true'
appname='SOFIFA to PES5/WE9/LE Stats Converter'
ntnames,ntlinks,leag_names,leag_val,clubnames,clublinks=[],[],[],[],[],[]
fifavers,fifaverslinks,updatename,updatelink=[],[],[],[]
root = Tk()
root.title(appname)
w = 800 # width for the Tk root
h = 600 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


loginsc = Toplevel()
loginsc.title(appname)
tw=400
th=350
tx = (ws/2) - (tw/2)
ty = (hs/2) - (th/2)
loginsc.geometry('%dx%d+%d+%d' % (tw, th, tx, ty))
loginsc.resizable(False, False)



username_lbl = Label(loginsc, text = 'E-Mail:')
username_entry = Entry(loginsc,width=30)
password_lbl = Label(loginsc, text = 'Password:')
password_entry = Entry(loginsc,width=30)
login_button=Button(loginsc,text='Login', command=lambda:login_action(username_entry.get(),password_entry.get(),web_opt))
exit_button = Button(loginsc,text='Cancel', command=lambda:close())
logedaslbl=Label(root)
loginsc.wm_protocol("WM_DELETE_WINDOW", lambda: close())
root.wm_protocol("WM_DELETE_WINDOW", lambda: close())
username_entry.bind('<Return>', lambda e: login_action(username_entry.get(),password_entry.get(),web_opt))
password_entry.bind('<Return>', lambda e: login_action(username_entry.get(),password_entry.get(),web_opt))
password_entry.default_show_val = password_entry['show']
password_entry['show'] = "*"
checkbutton = Checkbutton(loginsc,text="Hide password",onvalue=True,offvalue=False,command=toggle_password)
checkbutton.var = BooleanVar(value=True)
checkbutton['variable'] = checkbutton.var


username_lbl.pack()
username_entry.pack()
password_lbl.pack()
password_entry.pack()
checkbutton.pack()
login_button.pack()
exit_button.pack()


fifavercmb = ttk.Combobox(root,state="readonly", value=fifavers,width=8)
updatecmb = ttk.Combobox(root,state="readonly", value=updatename,width=14)
ntcmb = ttk.Combobox(root,state="readonly", value=ntnames,width=20)
lgcmb = ttk.Combobox(root,state="readonly", value=leag_names,width=24)
resize_ckbtn = Checkbutton(root,text="Resize to 64 & 32 px?",onvalue=True,offvalue=False)
resize_ckbtn.var = BooleanVar(value=False)
resize_ckbtn['variable'] = resize_ckbtn.var

download_btn = Button(root,text="Download League Logos", command=lambda:download_logos(login_session,lgcmb.get(),clubnames,clublinks,resize_ckbtn.var.get()))

# Info to the user about the resize option
my_tip(resize_ckbtn, "If you enable this option it will download all the images\n\
in their original size but also it will create two folders inside\n\
one call 64 and other 32 where you can find your resized images")

clubcmb = ttk.Combobox(root,state="readonly", value=clubnames,width=24)
lgcmb.bind("<<ComboboxSelected>>", load_clubs)
fifa_ver_lbl = Label(root,text='FIFA Version')
update_lbl = Label(root,text='Update Date')
fifavercmb.bind("<<ComboboxSelected>>", lambda e: update_webopt(fifavercmb.get(), "", login_session))
updatecmb.bind("<<ComboboxSelected>>", lambda e: update_webopt("", updatecmb.get(), login_session))
verlbl = Label(root,text='Select your output file type')
option = IntVar()
option.set('0')
rbtn1 = Radiobutton(root, text='mdb file', variable=option, value=1)
rbtn2 = Radiobutton(root, text='csv file', variable=option, value=2)
nt_lbl = Label(root,text='National teams')
club_lbl = Label(root,text='Club teams')
nt_convert_btn = Button(root,text='Convert National Team', command=lambda:convert(ntcmb.get(),login_session,ntnames,ntlinks,option.get()))
club_convert_btn = Button(root,text='Convert Club Team', command=lambda:convert(clubcmb.get(),login_session,clubnames,clublinks,option.get()))
#con el codigo de abajo creamos un spinbox y le seteamos el valor default a mostrar en 2
#sb = Spinbox(root, from_=1, to=12)
#sb.delete(0,"end")
#sb.insert(0,2)

percent = StringVar()
progress_text = StringVar()
percent.set("")
progress_text.set("")
bar = ttk.Progressbar(root,orient=HORIZONTAL,length=300)
bar.place(x = 260, y = 380)
percentLabel = Label(root,textvariable=percent).place(x = 260, y = 410)
taskLabel = Label(root,textvariable=progress_text).place(x = 260, y = 430)

copyright_lbl = Label(root,text='Developed by PES Indie Team ©')

logedaslbl.place(x = 0, y= 0)
fifa_ver_lbl.place(x=1,y=35)
update_lbl.place(x=80,y=35)
fifavercmb.place(x=1,y=60)
updatecmb.place(x=80,y=60)
nt_lbl.place(x = 250, y = 175)
club_lbl.place(x = 400, y = 175)
ntcmb.place(x = 250, y = 200)
lgcmb.place(x = 400, y = 200)
download_btn.place(x = 600, y = 200)
resize_ckbtn.place(x = 600, y = 240)
clubcmb.place(x = 400, y = 240)
nt_convert_btn.place(x = 250, y = 280)
club_convert_btn.place(x = 410 , y = 280)
verlbl.place(x = 340, y = 320)
rbtn1.place(x = 340, y = 340)
rbtn2.place(x = 420, y = 340)
copyright_lbl.place(x = 1, y = 580)
root.resizable(False, False)
root.withdraw()
root.mainloop() 