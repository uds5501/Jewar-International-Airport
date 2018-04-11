def tick(t1,t2,t3,t4,x):
#t1=destination


    if t1.upper()=="CHINA" :
        T1="CHI"

    elif t1.upper()=="USA" or t1.upper()=="AMERICA" :
        T1="USA"

    elif t1.upper()=="SPAIN":
        T1="ESP"
        
    elif t1.upper()=="GERMANY":
        T1="GER"

    elif t1.upper()=="AUSTRALIA":
        T1="AUS"

    elif t1.upper()=="NEW ZEALAND":
        T1="NEW"


    
    if t3.upper()=="BUSINESS":
            T3=str(random.choice(['2','4','6','8']))
    elif t3.upper()=="ECONOMY":
        T3=str(random.choice(['1','3','5','7','9']))
    elif t3.upper()=="LUXURY":
        T3="0"

    if gender.upper()=="MALE":
            T4=str(random.randint(99,500))
    elif gender.upper()=="FEMALE":
        T4=str(random.randint(500,999))        
    
    if t2.upper()=="ETIHAD":
        T2="ETI"
    elif t2.upper()=="QATAR":
        T2="QAT"
    elif t2.upper()=="AIR INDIA":
        T2="AIR"
