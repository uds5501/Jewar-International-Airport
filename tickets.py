import random
import string
import payment_gateway as bill
import string
import os
from database import Ticket_Identifier as indentify
import mailing
import security_2 as rogue

def tick_info(ticket):
    try:
        f=open("Log.txt","r")
        for line in f:
            a=line.strip().split()
            if a[0]==str(ticket):
                print
                print "\t\t\t\t\t\tTicket number is :",a[0]
                print "\t\t\t\t\t\tName of passenger :",a[1]
                print "\t\t\t\t\t\tDestination :",a[2]
                print "\t\t\t\t\t\tSeat number :",a[3]
                
                print
        f.close()
    except IOError:
        print "\t\t\t\t\t\tPlease try again later"
    except EOFError:
        print "\t\t\t\t\t\tTicket not found."
def cancel():
    print " _____________________________________________________________________________________________________________________________________________________________________"
    print
    ticket=raw_input("\t\t\t\t\t\tPlease enter your ticket number: ")
    
    seat=raw_input("\t\t\t\t\t\tSeat number: ")

    x=indentify(ticket)
    

    try:
        f=open("Log.txt","r")
        fo=open("new.txt","w+")
        for line in f:
            z=line.strip().split()
            if z[0]==ticket:
                fo.write("here\n")
                fo.write(z[0]+" "+z[1]+" "+z[2]+" "+z[3]+" "+z[4]+"\n")
                print
                print "\t\t\t\t\t\tTicket has been cancelled succesfully"
            elif z[0]!=ticket :
                fo.write(line)

        
        
    except EOFError:
        print "\t\t\t\t\t\tTicket not found"
    except IOError:
        print "\t\t\t\t\t\tSome error has occured during cancelling procedure. Please try again."

        fo.close()
        f.close()

        os.remove("Log.txt")
        os.rename("new.txt","Log.txt")

    try:
        f=open(x[0]+"_"+x[1]+".txt","r")
        fo=open("new.txt","w+")
        for line in f:
            if line.strip().split()[0]==seat:
                fo.write(line.strip().split()[0]+" A "+line.strip().split()[2]+"\n")
            elif line.strip().split()[0]!=seat:
                fo.write(line)
    except EOFError:
        pass
    except IOError:
        print "\t\t\t\t\t\tSome error has occured during cancellation. We regret the inconvinience."

    f.close()
    fo.close()
    os.remove(x[0]+"_"+x[1]+".txt")
    os.rename("new.txt",x[0]+"_"+x[1]+".txt")
    

        
            
        
                        
    
def update(air,des,seat):
    try:
        f=open(air+"_"+des+".txt","r")
        fo=open("intermediate.txt","w+")
        for line in f:
            if line.strip().split()[0]== seat:
                fo.write(seat+" "+"R"+" "+line.strip().split()[2]+"\n")
            elif line.strip().split()[0]!= seat:
                fo.write(line)
    except EOFError:
        pass
    except IOError:
        pass
    f.close()
    fo.close()
    os.remove(air+"_"+des+".txt")
    os.rename("intermediate.txt",air+"_"+des+".txt")
                


def Available(airline,des):
    try:
        f=open(airline+"_"+des+".txt","r")
        for line in f:
            x=line.strip().split()
            para1=x[1]          #availability
                      #side

            if x[1]=="A":
                seat=x[0]
                f.close()
                update(airline,des,seat)
                return seat
            
					
				
				
                
            else:
                pass
    except IOError:
        print "Some error has occured, please try again"
    except EOFError:
        return "N"
    
    
def ticket_Issue():
    Country={"CHI":"China","USA":"United States of America","ESP":"Spain","GER":"Germany","AUS":"Australia","NEW":"New Zealand"}
    Airlines={"ETI":"Etihad Airways","QAT":"Qatar Airines","AIR":"Air India"}

    right= ['01','02', '03', '04','05','06','07','08', '09', 10]
    middle=[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    left=[21,22,23,24,25,26,27,28,29,30]

    
    special_airline=random.choice(Airlines.keys())
    special_fare=random.randint(5,15)
    print " _____________________________________________________________________________________________________________________________________________________________________"
        
    print "\t\t\t\t\t\t\t\t\t Ticket Center"
    print " _____________________________________________________________________________________________________________________________________________________________________"
    print
    while True:
        try:
            
            
            name=str(raw_input("\t\t\t\t\t\t1. Please Enter your name:  "))
            break
        except ValueError:
            print "\t\t\t\t\tNumbers not allowed in names"
    

    while True:
        try:
            gender=str(raw_input("\t\t\t\t\t\t2. Please enter your gender:  "))
            break
        except ValueError:
            print "\t\t\t\t\t\tNumbers not allowed in gender"   


    while True:
        try:
            age=int(raw_input("\t\t\t\t\t\t3. Please enter your age: "))
            break
        except ValueError:
            print "\t\t\t\t\t\tCharacters are not allowed in Age"     
    
    print " _____________________________________________________________________________________________________________________________________________________________________"
    print
    while age>=18:
        option1=Country.values()
        print "\t\t\t\t\t\tPlease enter your Desired destination"
        for i in range (len(option1)):
            print "\t\t\t\t\t\t",i+1,"---->",option1[i]
        while True:
            try:
                print
                t1=str(raw_input("\t\t\t\t\t\tName the place (not the number) : "))
                break
            except ValueError:
                print "\t\t\t\t\t\tPlease enter full name in this section. Not numbers"

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

        x=Airlines.get(special_airline)
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        print "\t\t\t\t\t\t**SPECIAL FARES WITH ",x,"**"
        print "\t\t\t\t\t\t*WHOLE ",special_fare," % ON EVERY TICKET!!**"
        option2=Airlines.values()
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        print "\t\t\t\t\t\tPlease select your Preferred airlines"
        for j in range(len(option2)):
            print "\t\t\t\t\t\t",j+1,"--->",option2[j]
        print
        while True:
            try:
                t2=str(raw_input("\t\t\t\t\t\tEnter your option (In names)--->"))
                break
            except ValueError:
                print "\t\t\t\t\t\tPlease enter your choice in full letters eg: etihad"
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print    
        print "\t\t\t\t\t\tEnter the way you want to travel  "
        print "\t\t\t\t\t\tBusiness Class \n\t\t\t\t\t\tEconomy Class \n\t\t\t\t\t\tLuxury Class"
        print
        while True:
            try:
                t3=str(raw_input("\t\t\t\t\t\tEnter your option (in full letters)-->"))
                break
            except ValueError:
                print "\t\t\t\t\t\tPlease enter the value like this : Business"
                
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

        if gender.upper()=="MALE":
            T4=str(random.randint(100,500))
        elif gender.upper()=="FEMALE":
            T4=str(random.randint(500,999))
        
        x=Available(T2,T1)
        while x!="N":
            Ticket=T2+T1+T3+T4+x
            bill.billing(name,str(age),gender,T2,special_airline,special_fare,Ticket,T1)
            print " _____________________________________________________________________________________________________________________________________________________________________"
            print    
            print "\t\t\t\t\t\tAre you currently online ? "
            while True:
                try:
                    confirm=str(raw_input("\t\t\t\t\t\tPlease enter your choice in Y/N--->"))
                    break
                except ValueError:
                    print "\t\t\t\t\t\tEnter Y or N"

            print " _____________________________________________________________________________________________________________________________________________________________________"
            print
            if confirm.upper()=="Y":
                email=raw_input("\t\t\t\t\tPlease enter your email ID: ")
                mailing.email_Ticket(email,[Ticket,name,str(age),x,t1])
                directory=name+".txt"
                fo=open(directory,"w+")
                fo.write("\n**********************TICKET INFORMATION************************")
                fo.write("\nName :"+name)
                
                fo.write("\nAge  :"+str(age))
               
                fo.write("\nDestination :"+t1)
                fo.write("\nTicket Number :"+Ticket)
                fo.write("\nSeat Number :"+x)
                
                fo.write("\nHAVE A SAFE JOURNEY!!")
                fo.close()

                
                fo=open("Log.txt","a+")
                fo.write(Ticket+" "+name+" "+t1+" "+x+" "+str(age)+"\n")
                fo.close()
                x="N"

                rogue.update([Ticket,name,t1,x,str(age)])
            elif confirm.upper()=="N":
                directory=name+".txt"
                fo=open(directory,"w+")
                fo.write("\n**********************TICKET INFORMATION************************")
                fo.write("\nName :"+name)
                
                fo.write("\nAge  :"+str(age))
               
                fo.write("\nDestination :"+t1)
                fo.write("\nTicket Number :"+Ticket)
                fo.write("\nSeat Number :"+x)
                
                fo.write("\nHAVE A SAFE JOURNEY!!")
                fo.close()
                print " _____________________________________________________________________________________________________________________________________________________________________"
                print
                print "\t\t\t\t\t\tFind your Ticket at ",directory
                fo=open("Log.txt","a+")
                fo.write(Ticket+" "+name+" "+t1+" "+x+" "+str(age)+"\n")
                fo.close()
                x="N"
                rogue.update([Ticket,name,t1,x,str(age)])
        break
    
    if age<18:
        print "\t\t\t\t\tSorry sir but you have to be minimum of 18 years to fly."
    

    
            
                

            
                    
                
            
