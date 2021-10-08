'''
No soy un experto en programacion, la mayoria de este codigo son snippets que encontre por ahi, van a haber horrores de programacion
si sabes como hacerlo mejor, sos enteramente bienvenido, deja documentado siempre por favor, yo hago lo que puedo, gracias a 
StackOverflow, Google, ehh creo que GeeksForGeeks o algo asi, al alcohol y el cafe que me mantuvo despierto a ciertas horas, 
algunas cosas las hice yo pensandolas o modificando ejemplos, espero que este codigo ayude a la comunidad de pes5
Besitos
'''
import random
import time
from bs4 import BeautifulSoup
from datetime import datetime

'''
#generacion random de stats, esto funcionaba para football manager nada mas, lo dejo a modo ejemplo
def fm_to_pes5(stat):
    start=[40,43,46,49,52,55,58,61,64,67,70,73,76,79,82,85,88,91,94,97]
    stop =[43,46,49,52,55,58,61,64,67,70,73,76,79,82,85,88,91,94,97,100]
    #print(stat)
    stat=round(stat)
    #print(stat)
    pes5_stat=random.randrange(start[stat-1],stop[stat-1])
    #print(pes5_stat)
    return pes5_stat
'''
def fifa_to_PES5_1_a_8(stat):
    start=[1,3,5,7,8]
    stop =[3,5,7,8,9]
    #print(stat)
    stat=round(stat)
    #print(stat)
    pes5_stat=random.randrange(start[stat-1],stop[stat-1])
    #print(pes5_stat)
    return pes5_stat
'''
def fm_to_pes5_A_a_C(stat):
    start=['C','C','C','C','C','B','B','B','B','B','B','B','B','B','A','A','A','A','A','A']
    #print(stat)
    stat=round(stat)
    #print(stat)
    pes5_stat=start[stat-1]
    #print(pes5_stat)
    return pes5_stat
'''
def convert_stats(stats,reg_pos,posiciones,overall,weak_foot, skill_moves,attack_work_rate,defense_work_rate,s_h,traits,age):
    #Defino todas las variables de la columna OFENSIVA
    FIFA_Centros=stats['Attacking']['Crossing']
    FIFA_Definicion=stats['Attacking']['Finishing']
    FIFA_Presicion_cabeza=stats['Attacking']['Heading Accuracy']
    FIFA_Pases_cortos=stats['Attacking']['Short Passing']
    FIFA_Voleas=stats['Attacking']['Volleys']
    #Defino todas las variables de la columna TECNICA
    FIFA_Regates=stats['Skill']['Dribbling']
    FIFA_Efecto=stats['Skill']['Curve']
    FIFA_Presicion_faltas=stats['Skill']['FK Accuracy']
    FIFA_Pases_largos=stats['Skill']['Long Passing']
    FIFA_Control_del_balon=stats['Skill']['Ball Control']
    #Defino todas las variables de la columna MOVIMIENTO
    FIFA_Aceleracion=stats['Movement']['Acceleration']
    FIFA_Velocidad=stats['Movement']['Sprint Speed']
    FIFA_Agilidad=stats['Movement']['Agility']
    FIFA_Reflejos=stats['Movement']['Reactions']
    FIFA_Equilibrio=stats['Movement']['Balance']
    #Defino todas las variables de la columna POTENCIA
    FIFA_Potencia=stats['Power']['Shot Power']
    FIFA_Salto=stats['Power']['Jumping']
    FIFA_Resistencia=stats['Power']['Stamina']
    FIFA_Fuerza=stats['Power']['Strength']
    FIFA_Tiros_lejanos=stats['Power']['Long Shots']
    #Defino todas las variables de la columna MENTALIDAD
    FIFA_Agresividad=stats['Mentality']['Aggression']
    FIFA_Intercepciones=stats['Mentality']['Interceptions']
    FIFA_Colocacion=stats['Mentality']['Positioning']
    FIFA_Vision=stats['Mentality']['Vision']
    FIFA_Penaltis=stats['Mentality']['Penalties']
    FIFA_Compostura=stats['Mentality']['Composure']
    #Defino todas las variables de la columna DEFENSA
    FIFA_Conciencia_defensiva=stats['Defending']['Defensive Awareness']
    FIFA_Robos=stats['Defending']['Standing Tackle']
    FIFA_Entrada_agresiva=stats['Defending']['Sliding Tackle']
    #Defino todas las variables de la columna PORTERO
    FIFA_GK_Estirada=stats['Goalkeeping']['GK Diving']
    FIFA_GK_Paradas=stats['Goalkeeping']['GK Handling']
    FIFA_GK_Saques=stats['Goalkeeping']['GK Kicking']
    FIFA_GK_Colocacion=stats['Goalkeeping']['GK Positioning']
    FIFA_GK_Reflejos=stats['Goalkeeping']['GK Reflexes']
    #defino todas las variables de stats para pes en 0 en caso de que falle
    PES5_Weak_Foot_Accuracy=PES5_Weak_Foot_Frequeency=PES5_Attack =PES5_Defense =PES5_Balance =PES5_Stamina =PES5_Speed =PES5_Acceleration =PES5_Response =PES5_Agility =PES5_Dribble_Accuracy =PES5_Dribble_Speed =PES5_Short_Pass_Accuracy =PES5_Short_Pass_Speed =PES5_Long_Pass_Accuracy =PES5_Long_Pass_Speed =PES5_Shot_Accuracy =PES5_Shot_Power =PES5_Shot_Technique =PES5_Free_Kick_Accuracy =PES5_Curling =PES5_Heading =PES5_Jump =PES5_Technique =PES5_Agression =PES5_Mentality =PES5_GK_Skills =PES5_Team_Work =PES5_Consistency=PES5_Condition=0
    #defino en 0 todas las variables de las habilidades especiales 
    PES5_Dribbling =PES5_Tactical_Dribble =PES5_Positioning =PES5_Reaction =PES5_Playmaking =PES5_Passing =PES5_Scoring =PES5_1_1_Scoring =PES5_Post_Player =PES5_Lines =PES5_Middle_Shooting =PES5_Side =PES5_Centre =PES5_Penalties =PES5_1_Touch_Pass =PES5_Outside =PES5_Marking =PES5_Sliding =PES5_Covering =PES5_D_Line_Control =PES5_Penalty_Stopper =PES5_1_On_1_Stopper =PES5_Long_Throw =0
    if reg_pos!=0:
        #convertir de fifa a pes 5 para jugadores
        PES5_Weak_Foot_Accuracy=fifa_to_PES5_1_a_8(weak_foot)
        PES5_Weak_Foot_Frequeency=fifa_to_PES5_1_a_8(weak_foot) - 1
        PES5_Attack = FIFA_Colocacion
        PES5_Defense = round((FIFA_Conciencia_defensiva+FIFA_Robos+FIFA_Entrada_agresiva+FIFA_Intercepciones)/4)
        PES5_Balance = FIFA_Fuerza
        PES5_Stamina = FIFA_Resistencia
        PES5_Speed = FIFA_Velocidad
        PES5_Acceleration = FIFA_Aceleracion
        PES5_Response = FIFA_Reflejos
        PES5_Agility = FIFA_Agilidad
        PES5_Dribble_Accuracy = FIFA_Regates
        PES5_Dribble_Speed = FIFA_Velocidad
        PES5_Short_Pass_Accuracy = FIFA_Pases_cortos
        PES5_Short_Pass_Speed = FIFA_Potencia
        if FIFA_Pases_largos>FIFA_Centros:
            PES5_Long_Pass_Accuracy = FIFA_Pases_largos
        elif FIFA_Pases_largos<FIFA_Centros:
            PES5_Long_Pass_Accuracy = FIFA_Centros
        elif FIFA_Pases_largos==FIFA_Centros:
            PES5_Long_Pass_Accuracy = FIFA_Pases_largos
        PES5_Long_Pass_Speed = FIFA_Potencia
        PES5_Shot_Accuracy = FIFA_Definicion
        PES5_Shot_Power = FIFA_Potencia
        if FIFA_Voleas>FIFA_Tiros_lejanos:
            PES5_Shot_Technique = FIFA_Voleas
        elif FIFA_Voleas<FIFA_Tiros_lejanos:
            PES5_Shot_Technique = FIFA_Tiros_lejanos
        elif FIFA_Voleas==FIFA_Tiros_lejanos:
            PES5_Shot_Technique = FIFA_Voleas
        PES5_Free_Kick_Accuracy = FIFA_Presicion_faltas
        PES5_Curling = FIFA_Efecto
        PES5_Heading = FIFA_Presicion_cabeza
        PES5_Jump = FIFA_Salto
        PES5_Technique = FIFA_Control_del_balon
        PES5_Agression = 75
        PES5_Mentality = FIFA_Compostura
        PES5_GK_Skills = 50
        PES5_Team_Work = FIFA_Vision
        if round((FIFA_Compostura+FIFA_Resistencia)/2)>=86:
            PES5_Consistency =8
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<86 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=80:
            PES5_Consistency =7
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<80 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=73:
            PES5_Consistency =6
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<73 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=68:
            PES5_Consistency =5
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<68 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=60:
            PES5_Consistency =4
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<60 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=50:
            PES5_Consistency =3
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<50 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=40:
            PES5_Consistency =2
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<40 and round((FIFA_Compostura+FIFA_Resistencia)/2)>0:
            PES5_Consistency =1
        if overall>=90:
            PES5_Condition =8
        elif overall<90 and overall>=85:
            PES5_Condition =7
        elif overall<85 and overall>=80:
            PES5_Condition =6
        elif overall<80 and overall>=75:
            PES5_Condition =5
        elif overall<75 and overall>=70:
            PES5_Condition =4
        elif overall<70 and overall>=65:
            PES5_Condition =3
        elif overall<65 and overall>=60:
            PES5_Condition =2
        elif overall<60:
            PES5_Condition =1
    else:
        #convertir de fifa a pes 5 para arqueros
        PES5_Weak_Foot_Accuracy=fifa_to_PES5_1_a_8(weak_foot)
        PES5_Weak_Foot_Frequeency=fifa_to_PES5_1_a_8(weak_foot) - 1
        PES5_Attack = 30
        PES5_Defense = FIFA_GK_Colocacion
        if PES5_Defense<95:
            PES5_Defense=PES5_Defense+5
        PES5_Balance = FIFA_Fuerza
        if PES5_Balance<95:
            PES5_Balance=PES5_Balance+5
        PES5_Stamina = 50
        PES5_Speed = FIFA_Velocidad
        if PES5_Speed<90:
            PES5_Speed=PES5_Speed+10
        PES5_Acceleration = FIFA_Aceleracion
        if PES5_Acceleration<90:
            PES5_Acceleration=PES5_Acceleration+10
        PES5_Response = FIFA_GK_Reflejos
        if PES5_Response<95:
            PES5_Response=PES5_Response+5
        PES5_Agility = FIFA_Reflejos
        if PES5_Agility<90:
            PES5_Agility=PES5_Agility+10
        PES5_Dribble_Accuracy = 50
        PES5_Dribble_Speed = FIFA_Velocidad
        if PES5_Dribble_Speed<90:
            PES5_Dribble_Speed=PES5_Dribble_Speed+10
        PES5_Short_Pass_Accuracy = FIFA_Pases_cortos
        PES5_Short_Pass_Speed = 50
        if FIFA_Pases_largos>FIFA_Centros:
            PES5_Long_Pass_Accuracy = FIFA_Pases_largos
        elif FIFA_Pases_largos<FIFA_Centros:
            PES5_Long_Pass_Accuracy = FIFA_Centros
        elif FIFA_Pases_largos==FIFA_Centros:
            PES5_Long_Pass_Accuracy = FIFA_Pases_largos
        PES5_Long_Pass_Speed = 50
        PES5_Shot_Accuracy = 50
        PES5_Shot_Power = FIFA_GK_Saques
        if PES5_Shot_Power<95:
            PES5_Shot_Power=PES5_Shot_Power+5
        PES5_Shot_Technique = 50
        if FIFA_Presicion_faltas>50:
            PES5_Free_Kick_Accuracy=FIFA_Presicion_faltas
        else:
            PES5_Free_Kick_Accuracy=50
        if FIFA_Efecto>50:
            PES5_Curling=FIFA_Efecto
        else:
            PES5_Curling = 50
        PES5_Heading = 50
        PES5_Jump = FIFA_Salto
        if PES5_Jump<95:
            PES5_Jump=PES5_Jump+5
        PES5_Technique = 50
        PES5_Agression = 75
        PES5_Mentality = FIFA_Compostura
        if PES5_Mentality<75:
            PES5_Mentality=PES5_Mentality+25
        PES5_GK_Skills = FIFA_GK_Paradas
        if PES5_GK_Skills<95:
            PES5_GK_Skills=PES5_GK_Skills+5
        PES5_Team_Work = FIFA_Vision
        if PES5_Team_Work<75:
            PES5_Team_Work=PES5_Team_Work+25
        if round((FIFA_Compostura+FIFA_Resistencia)/2)>=86:
            PES5_Consistency =8
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<86 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=80:
            PES5_Consistency =7
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<80 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=73:
            PES5_Consistency =6
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<73 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=68:
            PES5_Consistency =5
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<68 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=60:
            PES5_Consistency =4
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<60 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=50:
            PES5_Consistency =3
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<50 and round((FIFA_Compostura+FIFA_Resistencia)/2)>=40:
            PES5_Consistency =2
        elif round((FIFA_Compostura+FIFA_Resistencia)/2)<40 and round((FIFA_Compostura+FIFA_Resistencia)/2)>0:
            PES5_Consistency =1
        if overall>=90:
            PES5_Condition =8
        elif overall<90 and overall>=85:
            PES5_Condition =7
        elif overall<85 and overall>=80:
            PES5_Condition =6
        elif overall<80 and overall>=75:
            PES5_Condition =5
        elif overall<75 and overall>=70:
            PES5_Condition =4
        elif overall<70 and overall>=65:
            PES5_Condition =3
        elif overall<65 and overall>=60:
            PES5_Condition =2
        elif overall<60:
            PES5_Condition =1
    if 'Speed Dribbler (AI)' in traits:
        PES5_Dribbling = 1
    if 'Technical Dribbler (AI)' in traits:
        PES5_Tactical_Dribble = 1
    if 'Poacher' in s_h:
        PES5_Positioning = 1
    #PES5_Reaction = 1 #no hay formula para esta habilidad especial todavia
    if 'Playmaker' in s_h:
        PES5_Playmaking = 1
    if 'Playmaker (AI)' in traits:
        PES5_Passing = 1
    if 'Complete Forward' in s_h:
        PES5_Scoring = 1
    if 'Clinical Finisher' in s_h:
        PES5_1_1_Scoring = 1
    #PES5_Post_Player = 1 #no hay formula para esta habilidad especial todavia
    #PES5_Lines = 1 #no hay formula para esta habilidad especial todavia
    if 'Distance Shooter' in s_h:
        PES5_Middle_Shooting = 1
    if 'Crosser' in s_h:
        PES5_Side = 1
    if 'Complete Midfielder' in s_h:
        PES5_Centre = 1
    if FIFA_Penaltis>=85:
        PES5_Penalties = 1
    if 'Flair' in traits:
        PES5_1_Touch_Pass = 1
    if 'Outside Foot Shot' in traits:
        PES5_Outside = 1
    if 'Complete Defender' in s_h:
        PES5_Marking = 1
    if 'Tackling' in s_h:
        PES5_Sliding = 1
    if FIFA_Conciencia_defensiva>85:
        PES5_Covering = 1
    if 'Complete Defender' in s_h:
        PES5_D_Line_Control = 1
    #PES5_Penalty_Stopper = 1 #no hay formula para esta habilidad especial todavia
    if 'Saves with Feet' in traits:
        PES5_1_On_1_Stopper = 1
    if 'Long Throw-in' in traits:
        PES5_Long_Throw = 1
    PES5_Injury_Tolerance= 'B'
    if 'Solid Player' in traits:
        PES5_Injury_Tolerance= 'A'
    elif 'Injury Prone' in traits:
        PES5_Injury_Tolerance= 'C'
    stats_99=[PES5_Attack ,PES5_Defense ,PES5_Balance ,PES5_Stamina ,PES5_Speed ,
    PES5_Acceleration ,PES5_Response ,PES5_Agility ,PES5_Dribble_Accuracy ,PES5_Dribble_Speed ,PES5_Short_Pass_Accuracy ,PES5_Short_Pass_Speed ,
    PES5_Long_Pass_Accuracy ,PES5_Long_Pass_Speed ,PES5_Shot_Accuracy ,PES5_Shot_Power ,PES5_Shot_Technique ,PES5_Free_Kick_Accuracy ,
    PES5_Curling ,PES5_Heading ,PES5_Jump ,PES5_Technique ,PES5_Agression ,PES5_Mentality ,PES5_GK_Skills ,PES5_Team_Work]
    #print(stats_99)
    for stat in range(len(stats_99)):
        if stats_99[stat]!=99:
            stats_99[stat]=random.randrange(stats_99[stat]-1,stats_99[stat]+2)
        else:
            stats_99[stat]=random.randrange(stats_99[stat]-1,stats_99[stat]+1)
    #print(stats_99)
    PES5_stats=[PES5_Weak_Foot_Accuracy,PES5_Weak_Foot_Frequeency]+stats_99+ [PES5_Consistency,
    PES5_Condition,PES5_Dribbling ,PES5_Tactical_Dribble ,PES5_Positioning ,PES5_Reaction ,PES5_Playmaking ,PES5_Passing ,PES5_Scoring ,
    PES5_1_1_Scoring ,PES5_Post_Player ,PES5_Lines ,PES5_Middle_Shooting ,PES5_Side ,PES5_Centre ,PES5_Penalties ,PES5_1_Touch_Pass ,
    PES5_Outside ,PES5_Marking ,PES5_Sliding ,PES5_Covering ,PES5_D_Line_Control ,PES5_Penalty_Stopper ,PES5_1_On_1_Stopper ,PES5_Long_Throw ,
    PES5_Injury_Tolerance]
    return PES5_stats

'''
def lbs_to_kg(weight):
    lbs=float(weight.strip("lbs"))
    kg = round(lbs * 0.453592)
    return kg

def inches_to_cm(height):
    foot=int(height.split('\'')[0])
    inches=int(height.split('\'')[1].strip("\""))
    inches+=foot*12
    cm=round(inches*2.54)
    return cm
'''
def get_fav_side(posiciones):
    fav_side='B'
    both_sides=0
    left_side=0
    right_side=0
    for l in range(len(posiciones)):
        if posiciones[l][0]=='L':
            left_side=left_side+1
        elif posiciones[l][0]=='R':
            right_side=right_side+1
        else:
            both_sides=both_sides+1
    if both_sides>left_side and both_sides>right_side:
        fav_side='B'
    elif left_side>both_sides and left_side>right_side:
        fav_side='L'
    elif right_side>both_sides and right_side>left_side:
        fav_side='R'
    return fav_side

def get_pos_reg(pos):
    return {
        'GK': 0,
        'CB': 2,
        'LB': 3,
        'RB': 3,
        'CDM': 4,
        'LWB': 5,
        'RWB': 5,
        'CM': 6,
        'LM': 7,
        'RM': 7,
        'CAM': 8,
        'LW': 9,
        'RW': 9,
        'LF': 10,
        'RF': 10,
        'CF': 10,
        'ST': 11   
    }.get(pos, 0)    # si no encontramos la posicion devolvemos 0 que es GK


def get_pos(posicion,posiciones):
    equivalencias= {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11   
    }
    indice=equivalencias.get(posicion)
    posiciones[indice]=1
    return posiciones


def nombre(name):
    x=""
    x=name.split()
    if len(x)==1:
       name=x[0]
    else:
        primer_nombre = x[0]
        apellido = x[-1]
        name=primer_nombre[0] + ". " + apellido
        if len(name)>16:
            name=apellido
            if len(name)>16:
              name=apellido[:15]
    
    return name

def nombre_remera(name):
    x=name.split()
    name=x[-1].upper()
    #saco los caracteres que el pes editor no toma
    a,b = 'ÁÀÉÈÍÌÓÒÚÙÜÑĆ','AAEEIIOOUUUNC'
    trans = str.maketrans(a,b)
    name=name.translate(trans)
    if len(name)>8:
        if len(name)>16:
            name[:15]
        name=name
    elif len(name)<5:
        name="  ".join(name)
    elif len(name)<9:
        name=" ".join(name)
    return name

'''
esta logica la pueden cambiar segun a ustedes les parezca, PES5 tiene solo 2 opciones para la pierna buena
'''


def pierna_buena(foot):
    if foot=="Left":
        foot="L"
    elif foot=="Right":
        foot="R"
    return foot


'''
aca lo que hacemos es calcular la edad que tiene nuestro jugador, segun su fecha de nacimiento contra el dia de hoy
'''

def edad_actual(born_date):
   edad_hoy= datetime.now().year - born_date.year
   return edad_hoy

'''
si encuentro la nacionalidad simplemente devuelvo la misma variable que me dieron, si no la encontro
entonces devuelvo free nationalitiy, que seria el ultimo valor en nuestra lista de nacionalidades
'''


def get_pes_5_nationality(nation,nationalities):
    if nation in nationalities:
        resp=nation
    else:
        resp=nationalities[-1]
    return resp

def conseguir_info_jugador(jugador,s):
    '''
    aca hacemos todo el parseo de texto, primero recibimos s que es la variable que contiene nuestra sesion inicia en la pagina
    con nuestro user y password asi no nos dropea el sitio por ser un bot, luego le pasamos jugador que es la url del jugador
    con habilidades a parsear y todo eso, todo lo demas que vas a ver abajo es simple y comun parseo de texto
    '''
    #print(jugador)
    #startTime = datetime.now()
    name, dorsal, height, weight, foot, age, nation, club, stats,posicion_reg,posiciones,overall,weak_foot, skill_moves,attack_work_rate,defense_work_rate,s_h,traits,status_code="",0,0,0,"","","","",{},"",[],0,0,0,0,0,[],[],200
    page = s.get(jugador, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    #print(page.status_code)
    if page.status_code==200:
        status_code=page.status_code
        soup = BeautifulSoup(page.text, 'html.parser')
        name=soup.find_all('h1',attrs={'class':'bp3-text-overflow-ellipsis'})[0].text
        #print(name)
        overall=int(soup.find_all('section',attrs={'class':'spacing'})[0].select_one('span').text)
        #print(overall)
        sofifa_stats=soup.find_all('div',attrs={'class':'card'})
        #print(len(sofifa_stats))
        #print(sofifa_stats[8])
        indexes=[]
        for tag in sofifa_stats:
            h5Tags = tag.find_all("h5")
            for tag in h5Tags:
                indexes.append(tag.text)
        #print(indexes)
        ofensiva={}
        #print(sofifa_stats[indexes.index('Attacking')])
        #ofensiva= {(item.select_one('span:nth-child(even)').text) :int(item.select_one('span:nth-child(odd)').text) for item in sofifa_stats[indexes.index('Attacking')].select('li')}
        a=[]
        b=[]
        for item in sofifa_stats[indexes.index('Attacking')].select('li'):
            a.append(int(item.select_one('span:nth-child(odd)').text))
            b.append(item.find('span',attrs={'class':'tooltip multiline'}).text)
        ofensiva = dict(zip(b, a))
        
        #print(ofensiva)
        #ofensiva = dict((v,k) for k,v in ofensiva.items())
        #print(ofensiva)
        tecnica={}
        #tecnica= {(item.select_one('span:nth-child(even)').text) : int(item.select_one('span:nth-child(odd)').text) for item in sofifa_stats[indexes.index('Skill')].select('li')}
        a=[]
        b=[]
        for item in sofifa_stats[indexes.index('Skill')].select('li'):
            a.append(int(item.select_one('span:nth-child(odd)').text))
            b.append(item.find('span',attrs={'class':'tooltip multiline'}).text)
        tecnica = dict(zip(b, a))
        
        #print(tecnica)
        #tecnica = dict((v,k) for k,v in tecnica.items())
        #print(tecnica)
        movimiento={}
        #movimiento= {(item.select_one('span:nth-child(even)').text) : int(item.select_one('span:nth-child(odd)').text) for item in sofifa_stats[indexes.index('Movement')].select('li')}
        a=[]
        b=[]
        for item in sofifa_stats[indexes.index('Movement')].select('li'):
            a.append(int(item.select_one('span:nth-child(odd)').text))
            b.append(item.find('span',attrs={'class':'tooltip multiline'}).text)
        movimiento = dict(zip(b, a))

        #movimiento = dict((v,k) for k,v in movimiento.items())
        #print(movimiento)
        potencia={}
        #potencia= {(item.select_one('span:nth-child(even)').text) : int(item.select_one('span:nth-child(odd)').text) for item in sofifa_stats[indexes.index('Power')].select('li')}
        a=[]
        b=[]
        for item in sofifa_stats[indexes.index('Power')].select('li'):
            a.append(int(item.select_one('span:nth-child(odd)').text))
            b.append(item.find('span',attrs={'class':'tooltip multiline'}).text)
        potencia = dict(zip(b, a))
        
        #print(potencia)
        #potencia = dict((v,k) for k,v in potencia.items())
        #print(potencia)
        mentalidad={}
        d=[]
        e=[]
        for item in sofifa_stats[indexes.index('Mentality')].select('li'):
            #print(item.find_all('span'))
            d.append(int(item.select_one('span:nth-child(odd)').text))
            if (item.select_one('span:nth-child(even)')) is not None:
                if item.find('span',attrs={'class':'tooltip multiline'}) is not None:
                    e.append(item.find('span',attrs={'class':'tooltip multiline'}).text)
                else:
                    e.append(item.text.split()[-1])
            else:
                e.append(item.text.split()[-1])
            #e.append(item.find('span',attrs={'class':'tooltip multiline'}).text)
        mentalidad = dict(zip(e, d))
        #print(mentalidad)
        defensa={}
        #defensa= {(item.select_one('span:nth-child(even)').text) : int(item.select_one('span:nth-child(odd)').text) for item in sofifa_stats[indexes.index('Defending')].select('li')}
        a=[]
        b=[]
        for item in sofifa_stats[indexes.index('Defending')].select('li'):
            a.append(int(item.select_one('span:nth-child(odd)').text))
            b.append(item.find('span',attrs={'class':'tooltip multiline'}).text)
        defensa = dict(zip(b, a))
        
        #defensa = dict((v,k) for k,v in defensa.items())
        #print(defensa)
        portero={}
        portero= {(item.text.split()[-2]+' '+item.text.split()[-1]) : int(item.find('span').text) for item in sofifa_stats[indexes.index('Goalkeeping')].select('li')}
        #print(portero)
        #portero = dict((v,k) for k,v in portero.items())
        #print(portero)
        stats={}
        stats['Attacking']=ofensiva
        stats['Skill']=tecnica
        stats['Movement']=movimiento
        stats['Power']=potencia
        stats['Mentality']=mentalidad
        stats['Defending']=defensa
        stats['Goalkeeping']=portero
        #print(stats)
        work_rate=sofifa_stats[indexes.index('Profile')].find_all('li')[4].find('span').text.split('/ ')
        attack_work_rate=0
        if work_rate[0]=='High':
            attack_work_rate=75
        elif work_rate[0]=='Medium':
            attack_work_rate=50
        elif work_rate[0]=='Low':
            attack_work_rate=25
        defense_work_rate=0
        if work_rate[1]=='High':
            defense_work_rate=75
        elif work_rate[1]=='Medium':
            defense_work_rate=50
        elif work_rate[1]=='Low':
            defense_work_rate=25
        specialities=sofifa_stats[indexes.index('Player Specialities')]
        s_h=[]
        if specialities.find_all('li')!=s_h:
            lis=specialities.find_all('li')
            s_h=[lis[x].find('a').text.strip('#') for x in range(len(lis))]
        #print (s_h)
        if s_h!=[]:
            for i in range(len(s_h)):
                s_h[i]=s_h[i].replace(u'\xa0', u'')
        traits=[]
        if 'Traits' in indexes:
            spans=sofifa_stats[indexes.index('Traits')].find_all('span')
            traits=[spans[x].text for x in range(len(spans))]
        #print(traits)
        foot = sofifa_stats[indexes.index('Profile')].find_all('li')[0].find('label').findNextSibling(text=True)
        #print (foot)
        weak_foot = int(sofifa_stats[indexes.index('Profile')].find_all('li')[1].find('span').findPreviousSibling(text=True))
        #print(weak_foot)
        skill_moves = int(sofifa_stats[indexes.index('Profile')].find_all('li')[2].find('span').findPreviousSibling(text=True))
        #print(skill_moves)
        posiciones=[soup.find_all('div',attrs={'class':'meta bp3-text-overflow-ellipsis'})[0].find_all('span')[x].text for x in range(len(soup.find_all('div',attrs={'class':'meta bp3-text-overflow-ellipsis'})[0].find_all('span')))]
        #print(posiciones)
        posicion_reg=posiciones[0]
        #print(posicion_reg)
        dorsal=int(soup.find('ul', attrs={'class':'bp3-text-overflow-ellipsis pl'}).find_all('li')[2].find('label').findNextSibling(text=True))
        #print(dorsal)
        #club=soup.find('div', attrs={'class':'player-card double-spacing'}).find('a').text
        club=indexes[2]
        #print(club)
        nation=soup.find_all('div',attrs={'class':'meta bp3-text-overflow-ellipsis'})[0].find('a').get('title')
        #print(nation)
        personal_data=soup.find_all('div',attrs={'class':'meta bp3-text-overflow-ellipsis'})[0].find_all('span')[-1].findNextSibling(text=True).split(') ')
        #print(personal_data)
        age = datetime.strptime((personal_data[0].split('(')[1]), '%b %d, %Y').date()
        #print(age)
        height=(personal_data[1].split()[0].strip('cm'))
        weight=(personal_data[1].split()[1].strip('kg'))
    else:
        status_code=page.status_code
    #print(datetime.now() - startTime)
    #print(name, dorsal, height, weight, foot, age, nation, club, stats,posicion_reg,posiciones,overall,weak_foot, skill_moves,attack_work_rate,defense_work_rate,s_h,traits,status_code)
    return name, dorsal, height, weight, foot, age, nation, club, stats,posicion_reg,posiciones,overall,weak_foot, skill_moves,attack_work_rate,defense_work_rate,s_h,traits,status_code


def player_scrapper(link,session):
    #print (f"el link del jugador es {link}")
    nationalities = ["Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany", "Greece", 
    "Hungary", "Ireland", "Italy", "Latvia", "Netherlands", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia and Montenegro", 
    "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales", "Cameroon", "Cote d'Ivoire", "Morocco", "Nigeria", 
    "Senegal", "South Africa", "Tunisia", "Costa Rica", "Mexico", "USA", "Argentina", "Brazil", "Chile", "Colombia", 
    "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "China", "Iran", "Japan", "Saudi Arabia", "South Korea", "Australia", "Albania", "Armenia", "Belarus", 
    "Bosnia and Herzegovina", "Cyprus", "Georgia", "Estonia", "Faroe Islands", "Iceland", "Israel", "Lithuania", "Luxembourg", "Macedonia", "Moldova", "Algeria", 
    "Angola", "Burkina Faso", "Cape Verde", "Congo", "DR Congo", "Egypt", "Equatorial Guinea", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", 
    "Libya", "Mali", "Mauritius", "Mozambique", "Namibia", "Sierra Leone", "Togo", "Zambia", "Zimbabwe", "Canada", "Grenada", "Guadeloupe", "Guatemala", "Honduras", 
    "Jamaica", "Martinique", "Netherlands Antilles", "Panama", "Trinidad and Tobago", "Bolivia", "Guyana", "Uzbekistan", "New Zealand", "Free Nationality" ]

    time.sleep(20)
    name, dorsal, height, weight, foot, age, nation, club, stats,posicion_reg,posiciones,overall,weak_foot, skill_moves,attack_work_rate,defense_work_rate,s_h,traits,status_code=conseguir_info_jugador('https://sofifa.com'+link+'?hl=en-US&attr=classic&layout=new&units=mks',session)
    if status_code==200:
        csv_NAME=nombre(name)
        if len(csv_NAME)>16:
            csv_NAME=nombre(csv_NAME)
        csv_SHIRT_NAME=nombre_remera(name)
        csv_REGISTERED_POSITION=get_pos_reg(posicion_reg)
        csv_POSICIONES=[0,0,0,0,0,0,0,0,0,0,0,0]
        #ponemos 1 a la posicion registrada
        csv_POSICIONES=get_pos(get_pos_reg(posicion_reg),csv_POSICIONES)
        #ahora le pasamos todas las demas posiciones para que se pongan como secundarias
        for i in range(len(posiciones)):
            csv_POSICIONES=get_pos(get_pos_reg(posiciones[i]),csv_POSICIONES)
        csv_HEIGHT = height
        csv_WEIGHT = weight
        csv_STRONG_FOOT=pierna_buena(foot)
        csv_FAVOURED_SIDE=get_fav_side(posiciones)
        csv_AGE=edad_actual(age)
        PES5_stats=convert_stats(stats,csv_REGISTERED_POSITION,csv_POSICIONES,overall,weak_foot, skill_moves,attack_work_rate,defense_work_rate,s_h,traits,csv_AGE)
        csv_CLUB_NUMBER=dorsal
        csv_NATIONALITY=get_pes_5_nationality(nation,nationalities)
        csv_CLUB_TEAM=club
        #return tuple([""]+[csv_NAME]+[csv_SHIRT_NAME]+csv_POSICIONES+[csv_REGISTERED_POSITION]+[int(csv_HEIGHT)]+[csv_STRONG_FOOT]+
            #[csv_FAVOURED_SIDE]+PES5_stats+[1,1,1,1]+[csv_AGE]+[int(csv_WEIGHT)]+[csv_NATIONALITY]+[1,0,1,0,0,0,0,0,0,0,0,0,0,0,'N','None',0,0]+
            #[csv_CLUB_TEAM]+[csv_CLUB_NUMBER])
        return tuple([""]+[csv_NAME]+[csv_SHIRT_NAME]+csv_POSICIONES+[csv_REGISTERED_POSITION]+[int(csv_HEIGHT)]+[csv_STRONG_FOOT]+
            [csv_FAVOURED_SIDE]+PES5_stats+[csv_AGE]+[int(csv_WEIGHT)]+[csv_NATIONALITY]+
            [csv_CLUB_TEAM]+[csv_CLUB_NUMBER])

    #print('el sitio esta dando un status code: '+str(status_code))
    else:
        return status_code
        
#conseguir_info_jugador('https://sofifa.com/player/207862/matthias-ginter/200061/?r=210007&set=true&attr=classic',requests.Session())
