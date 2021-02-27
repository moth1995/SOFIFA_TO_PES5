import requests
from bs4 import BeautifulSoup
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys

import conseguir_jugadores
import jugador
import savefile
#from requests.sessions import session

def get_teamlist(session,url,web_opt):
    #print(website+url+web_opt)
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
            team=str(linklist[namelist.index(team)])
            time.sleep(5)
            links,filename = conseguir_jugadores.conseguir_jugadores(team,session)
            #print(filename)
            #print("  ")
            players=[]
            for link in range(len(links)):
                #print(links[link])
                player=jugador.player_scrapper(links[link],session)
                if type(player)==int:
                    messagebox.showerror(title=appname, message="Status code "+str(player))
                    break
                players.append(player)
            #print("fin")
            #print(players)
            if players!=[]:
                if gamever==1:
                    #this is for mdb
                    savefile.csv_to_mdb(filename,savefile.csv_parser(players))
                    messagebox.showinfo(title=appname, message="Your mdb file for "+str(filename) + "\nhas been generated")
                elif gamever==2:
                    #this is for csv
                    savefile.write_csv(filename,players)
                    messagebox.showinfo(title=appname, message="Your csv file for "+str(filename) + "\nhas been generated")
                else:
                    messagebox.showerror(title=appname, message="The game version doesnt have support yet")
            else:
                messagebox.showerror(title=appname, message="Couldn't retrieve data for players on " + str(filename))
        else:
            messagebox.showerror(title=appname, message="Please select a PES Version")
    else:
        messagebox.showerror(title=appname, message="Please select a club")

def login(username,password):
    global logedaslbl, fifavers, fifaverslinks,updatename,updatelink
    payload = {'email': username, 'password': password,'submit':''}
    #print (payload)
    login_page = website+'/signIn/'
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
            fifaverslinks.append(a.get('href'))
        for a in h2.find_all('div',attrs={'class':'bp3-menu'})[1].find_all('a',attrs={'class':'bp3-menu-item'}):
            updatename.append(a.text)
            updatelink.append(a.get('href'))
        if fifavers!=[] and updatename!=[]:
            fifavercmb.config(values=fifavers)
            fifavercmb.set(fifavers[0])
            updatecmb.config(values=updatename)
            updatecmb.set(updatename[0])
        return s

def load_clubs(*args):
    global clubnames,clublinks
    league_selected=lgcmb.get()
    clubnames,clublinks=get_teamlist(login_session,'/teams?type=club&lg[]='+str(leag_val[leag_names.index(league_selected)]),web_opt)
    clubcmb.config(values=clubnames)
    clubcmb.set("")


def load_cmb(session,web_opt):
    global ntnames,ntlinks,leag_names,leag_val
    ntnames,ntlinks=get_teamlist(session,'/teams?type=national',web_opt)
    leag_names,leag_val=get_leagues(session,web_opt)
    #print(len(ntnames))
    if ntnames!=[]:
        ntcmb.config(values=ntnames)
    if leag_names!=[]:
        lgcmb.config(values=leag_names)
    

def login_action(user,pw,webopt):
    #print (user,pw)
    global login_session
    login_session=login(user,pw)
    if login_session:
        root.deiconify()
        loginsc.destroy()
        load_cmb(login_session,webopt)
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
web_opt='&hl=en-US&attr=classic&layout=new&units=mks'
appname='SOFIFA to PES Converter'
ntnames,ntlinks,leag_names,leag_val,clubnames,clublinks=[],[],[],[],[],[]
fifavers,fifaverslinks,updatename,updatelink=[],[],[],[]
fifavers_available=['FIFA 21','FIFA 20']
root = Tk()
root.title(appname)
w = 800 # width for the Tk root
h = 700 # height for the Tk root
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



username_lbl = Label(loginsc, text = 'Username:')
username_entry = Entry(loginsc,width=30)
password_lbl = Label(loginsc, text = 'Password:')
password_entry = Entry(loginsc,width=30)
login_button=Button(loginsc,text='Login', command=lambda:login_action(username_entry.get(),password_entry.get(),web_opt))
exit_button = Button(loginsc,text='Cancel', command=lambda:close(username_entry.get(),password_entry.get(),web_opt))
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

fifavercmb=ttk.Combobox(root,state="readonly", value=fifavers,width=8)
updatecmb=ttk.Combobox(root,state="readonly", value=updatename,width=14)
ntcmb = ttk.Combobox(root,state="readonly", value=ntnames,width=20)
lgcmb = ttk.Combobox(root,state="readonly", value=leag_names,width=24)
clubcmb = ttk.Combobox(root,state="readonly", value=clubnames,width=24)
lgcmb.bind("<<ComboboxSelected>>", load_clubs)
fifavercmb.bind("<<ComboboxSelected>>", print(fifavercmb.get()))
verlbl=Label(root,text='Select your PES Version')
option=IntVar()
option.set('1')
rbtn1=Radiobutton(root, text='mdb file', variable=option, value=1)
rbtn2=Radiobutton(root, text='csv file', variable=option, value=2)
nt_convert_btn=Button(root,text='Convert National Team', command=lambda:convert(ntcmb.get(),login_session,ntnames,ntlinks,option.get()))
club_convert_btn=Button(root,text='Convert Club Team', command=lambda:convert(clubcmb.get(),login_session,clubnames,clublinks,option.get()))
#con el codigo de abajo creamos un spinbox y le seteamos el valor default a mostrar en 2
#sb = Spinbox(root, from_=1, to=12)
#sb.delete(0,"end")
#sb.insert(0,2)
logedaslbl.place(x=0,y=0)
#fifavercmb.place(x=0,y=60)
#updatecmb.place(x=80,y=60)
ntcmb.place(x=250,y=200)
lgcmb.place(x=400,y=200)
clubcmb.place(x=400,y=240)
nt_convert_btn.place(x=250,y=280)
#verlbl.place(x=340,y=320)
#rbtn1.place(x=350,y=340)
#rbtn2.place(x=410,y=340)
club_convert_btn.place(x=410,y=280)
root.resizable(False, False)
root.withdraw()
root.mainloop() 