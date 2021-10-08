import pyodbc
import csv
import os
def copymdb(newname):
    # First we remove ascii characters
    newname = newname.encode('ascii',errors='ignore')
    newname = newname.decode()
    #print(newname)
    #print(type(newname))
    
    file=str(newname)+".mdb"
    with open(r'src\template.mdb',"rb") as rf_exe:
        chunk_size=4096
        with open(file,"wb") as wf_exe:
            rf_exe_chunk = rf_exe.read(chunk_size)
            while len(rf_exe_chunk) >0:
                wf_exe.write(rf_exe_chunk)
                rf_exe_chunk = rf_exe.read(chunk_size)
    return file

def csv_parser(csv_data):
    #pes5 nationalities taken from pes5 editor source code
    nationalities = ["Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany", "Greece", 
    "Hungary", "Ireland", "Italy", "Latvia", "Netherlands", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia and Montenegro", 
    "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales", "Cameroon", "Cote d'Ivoire", "Morocco", "Nigeria", 
    "Senegal", "South Africa", "Tunisia", "Costa Rica", "Mexico", "USA", "Argentina", "Brazil", "Chile", "Colombia", 
    "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "China", "Iran", "Japan", "Saudi Arabia", "South Korea", "Australia", "Albania", "Armenia", "Belarus", 
    "Bosnia and Herzegovina", "Cyprus", "Georgia", "Estonia", "Faroe Islands", "Iceland", "Israel", "Lithuania", "Luxembourg", "Macedonia", "Moldova", "Algeria", 
    "Angola", "Burkina Faso", "Cape Verde", "Congo", "DR Congo", "Egypt", "Equatorial Guinea", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", 
    "Libya", "Mali", "Mauritius", "Mozambique", "Namibia", "Sierra Leone", "Togo", "Zambia", "Zimbabwe", "Canada", "Grenada", "Guadeloupe", "Guatemala", "Honduras", 
    "Jamaica", "Martinique", "Netherlands Antilles", "Panama", "Trinidad and Tobago", "Bolivia", "Guyana", "Uzbekistan", "New Zealand", "Free Nationality" ]
    # open file in read mode
    # Get all rows of csv from csv_reader object as list of list
    list_of_list = list(map(list, csv_data))
    #print(list_of_list)
    #index_rem=[73,74,75,76,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
    index_rem=[-2,-1]
    index_text=[1,2,17,18,75,72]
    #here we modify the csv to be compatible with dkz mdb file
    for i in range(0,len(list_of_list)):
        # if we found an id with null we set the number of iteration +1 because player id cant be 0
        if list_of_list[i][0]=="":
            list_of_list[i][0]=i+1
        # removing unused cols
        for n in reversed(index_rem):
            list_of_list[i].pop(n)
        #convert to int all the non text cols
        for m in range(0,len(list_of_list[i])):
            #skiping text cols
            if m in index_text:
                continue
            else:
                list_of_list[i][m]=int(list_of_list[i][m])
        #strong foot
        if list_of_list[i][17]=="R":
            list_of_list[i][17]=0
        elif list_of_list[i][17]=="L":
            list_of_list[i][17]=1
        #favourite side
        if list_of_list[i][18]=="B":
            list_of_list[i][18]=2
        elif list_of_list[i][18]=="L":
            list_of_list[i][18]=1        
        elif list_of_list[i][18]=="R":
            list_of_list[i][18]=0        
        # Injurance tolerance
        if list_of_list[i][72]=="A":
            list_of_list[i][72]=2
        elif list_of_list[i][72]=="B":
            list_of_list[i][72]=1        
        elif list_of_list[i][72]=="C":
            list_of_list[i][72]=0
        #converting nationality to index number
        if list_of_list[i][75] in nationalities:
            list_of_list[i][75]=nationalities.index(list_of_list[i][75])
        else:
            #if nationality wasn't found we set as Free Nationality
            list_of_list[i][75]=nationalities.index("Free Nationality")
    #now that we have everything in place we convert it to tuple, if we have the data in tuple we cant modify it
    list_of_tuples = [tuple(l) for l in list_of_list]
    return list_of_tuples

def csv_to_mdb(mdb,rows):
    #create the new mdb
    file=copymdb(mdb)
    #print(pyodbc.drivers())
    driver = [i for i in pyodbc.drivers() if i.startswith('Microsoft Access Driver')][0]
    #print(file)
    file = os.path.abspath(file)
    #print(file)
    #now we open the created db
    conn = pyodbc.connect(fr'Driver={driver};DBQ={file};')
    cursor = conn.cursor()
    #please check the template and view the description to understand the name of every col
    sql = ('''
                    INSERT INTO tblPlayers (
                        ID,t_0,t_1,t_16,t_17,t_18,t_19,t_20,t_21,t_22,t_23,t_24,t_25,t_26,
                        t_27,t_14,t_124,t_5,t_15,t_56,t_57,
                        t_28,t_29,t_30,t_31,t_32,t_33,t_34,t_35,t_36,t_37,t_38,t_39,t_40,t_41,t_42,t_43,t_44,t_45,
                        t_46,t_47,t_48,t_49,t_50,t_51,t_52,t_53,t_54,t_55,
                        t_58,t_59,t_60,t_61,t_62,t_63,t_64,t_65,t_66,t_67,t_68,t_69,t_70,t_71,t_72,t_73,t_74,t_75,t_76,t_77,t_78,
                        t_79,t_80,
                        t_6,t_4,t_125,t_3
                        )
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?)
            ''')
    #now we iterate every row in the list of tuple
    for row in rows:
        #print(row)
        cursor.execute(sql, row)
    conn.commit()
    cursor.close()

def create_csv(filename):
    #creamos el csv
    file=filename+'.csv'
    with open(file, 'w',newline='', encoding='utf-8') as f:
        csv_escribir = csv.writer(f)
        csv_escribir.writerow(["ID","NAME","SHIRT_NAME","GK  0","CWP  2","CBT  3","SB  4","DMF  5","WB  6","CMF  7","SMF  8","AMF  9",
        "WF 10","SS  11","CF  12","REGISTERED POSITION","HEIGHT","STRONG FOOT","FAVOURED SIDE","WEAK FOOT ACCURACY","WEAK FOOT FREQUENCY",
        "ATTACK","DEFENSE","BALANCE","STAMINA","TOP SPEED","ACCELERATION","RESPONSE","AGILITY","DRIBBLE ACCURACY","DRIBBLE SPEED",
        "SHORT PASS ACCURACY","SHORT PASS SPEED","LONG PASS ACCURACY","LONG PASS SPEED","SHOT ACCURACY","SHOT POWER","SHOT TECHNIQUE",
        "FREE KICK ACCURACY","CURLING","HEADING","JUMP","TECHNIQUE","AGGRESSION","MENTALITY","GOAL KEEPING","TEAM WORK","CONSISTENCY",
        "CONDITION / FITNESS","DRIBBLING","TACTIAL DRIBBLE","POSITIONING","REACTION","PLAYMAKING","PASSING","SCORING","1-1 SCORING",
        "POST PLAYER","LINES","MIDDLE SHOOTING","SIDE","CENTRE","PENALTIES","1-TOUCH PASS","OUTSIDE","MARKING","SLIDING","COVERING",
        "D-LINE CONTROL","PENALTY STOPPER","1-ON-1 STOPPER","LONG THROW","INJURY TOLERANCE","AGE","WEIGHT","NATIONALITY","CLUB TEAM","CLUB NUMBER"])
    return file

def write_csv(filename,players):
    file=create_csv(filename)
    with open(file, 'a',newline='', encoding='utf-8') as f:
        csv_out=csv.writer(f)
        #csv_out.writerows(players)
        for player in players:
            #print(player)
            csv_out.writerow(player)