import random
import os
import sys
import time
import string
from datetime import date
import mailing
import texting
def decipher(require):
    f=open("cards.txt","r")
    for line in f:
        z=str(line).split()
        a=z[0]
        key=z[1]
        recover=""
        if require==z[2]:
            for i in a:
                k=i-key
                recover=recover+k
        else:
            pass

    return(str(recover[::-1]))

    
        
        
            
    
def cipher(no,ticket):
    x=random.randint(1,9)
    r=""
    for i in str(no):
        i=int(i)+x
        r=r+str(i)

    r=r[::-1]

    try:
        f=open("cards.txt","a")
        f.write(str(r)+" "+str(x)+" "+str(ticket)+"\n")
        f.close()

    except IOError or EOFError:
        print "An error has occured, please try again later"
    

def billing(name,age,gender,airline,sa,sf,ticket,des):
    Distance={"AUS":8485,"USA":1200,"ESP":720,"GER":600,"CHI":260,"NEW":1260}
    Fare={"QAT":30,"ETI":20,"AIR":15}
    print " _____________________________________________________________________________________________________________________________________________________________________"
    print
    bank=raw_input("\t\t\t\t\t\tPlease enter the name of your bank--> ")
    

    cost_basic=3000         #3000 for a ride
    cost_km=2               #2 rs. per km

    cost_seat=Fare[airline]

    cpd=Distance[des]

    c1=cpd*cost_km
    if airline==sa:
        c2=(cost_seat-(cost_seat*(sf/100)))*cpd
    else:
        c2=cost_seat*cpd

    if gender.upper=="FEMALE":
        c2=c2-5000
    if age>=50 and gender.upper()!="FEMALE":
            c2=c2-5000
    
    total=c1+c2+cost_basic
    tax=15
    total=total+(0.15*total)
    print " _____________________________________________________________________________________________________________________________________________________________________"
    print
    
    while True:
        try:
            confirm=raw_input("\t\t\t\t\t\tDo you have an Email Id or/and an internet connection? Y/N :")
            break
        except ValueError:
            print "\t\t\t\t\tY or N.Please"
    if confirm.upper()=="Y":
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        while True:
            try:
                cardno=int(raw_input("\t\t\t\t\t\tEnter your credit card number (no limit on digits)--> "))
                
                break
            except ValueError:
                print "\t\t\t\t\t\tNUMBER, not alphabets"
        
        OTP=random.randint(100000,999999)
        while True:
            try:
                print "\t\t\t\t\t\tWhere do you want to recieve your OTP?\n\t\t\t\t\t\t1.Mobile\n\t\t\t\t\t\t2.Email "
                cho=int(raw_input("\t\t\t\t\t\tPlease Enter your choice: "))
                break
            except ValueError:
                print "\t\t\t\t\t\tPlease Enter 1 or 2"
                
        if str(cho)=="1":
            print " _____________________________________________________________________________________________________________________________________________________________________"
            print
            mob=raw_input("\t\t\t\t\t\tPlease enter your mobile number: ")
            texting.send_OTP(mob,OTP)
        elif str(cho)=="2":
            print " _____________________________________________________________________________________________________________________________________________________________________"
            print
            email=raw_input("\t\t\t\t\t\tPlease enter your email ID: ")
            mailing.email_OTP(email,str(OTP))
            
        cipher(cardno,ticket)
        
        
        directory=bank+" "+name+".txt"
        f=open("OTP.txt","w+")
        f.write(str(OTP))
        f.close()
        if gender.upper()=="female":
            to_write="Mrs "
        else:
            to_write="Mr "
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        print "\t\t\t\t\t\tYour total amount payable is ",total," Rs. only"
        
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        accept=int(raw_input("\t\t\t\t\t\tPlease enter the OTP recieved on your account: "))
        
        while accept==OTP:
            for i in range(0,5):
                print "\t\t\t\t\t\tPlease wait...  .     ."
                time.sleep(1)

            fo=open(directory,"w")
            fo.write("Dear" + to_write +name+":\n")
            fo.write("From your account (card number=" + str(cardno)[:5] +"XXXXX )")
            fo.write("Transaction of "+ str(total) + " rupees was done today \n")
            fo.write(str(date.today().strftime("%d"))+"/"+str(date.today().strftime("%B"))+"/"+str(date.today().strftime("%Y")))
            break
        
        
    elif confirm.upper()=="N":
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        while True:
            try:
                cardno=int(raw_input("\t\t\t\t\t\tEnter your credit card number (no limit on digits)--> "))
                break
            except ValueError:
                print "\t\t\t\t\t\tNUMBER, not alphabets"
        cipher(cardno,ticket)
        OTP=random.randint(100000,999999)
        directory=bank+""+name+".txt"
        f=open("OTP.txt","w+")
        f.write(str(OTP))
        f.close()
        if gender.upper()=="female":
            to_write="Mrs "
        else:
            to_write="Mr "
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        print "\t\t\t\t\t\tYour total amount payable is ",total," Rs. only"

        print
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        accept=int(raw_input("\t\t\t\t\t\tPlease enter the OTP generated on your directory: "))
        print
        while accept==OTP:
            for i in range(0,5):
                print "\t\t\t\t\t\t\t\tPlease wait...  .   ."
                time.sleep(1)

            fo=open(directory,"w")
            fo.write("Dear" + to_write +name+":\n")
            fo.write("From your account (card number=" + str(cardno)[:5] +"XXXXX )")
            fo.write("Transaction of "+ str(total) + " rupees was done today \n")
            fo.write(str(date.today().strftime("%d"))+"/"+str(date.today().strftime("%B"))+"/"+str(date.today().strftime("%Y")))
            break
        
        
        
    

