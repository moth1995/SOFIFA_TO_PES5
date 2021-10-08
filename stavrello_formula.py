## You can find the formula in here http://foro.pesretro.net/showthread.php?tid=11634

def stavrello(stats,reg_pos,posiciones,overall,weak_foot, skill_moves,attack_work_rate,defense_work_rate,s_h,traits,int_reputation,age):
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
        # sofifa to pes for outfield players
        # definition of EXP varibles
        EXP_value = 1.179
        EXP_IDvalue = 1.405

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
