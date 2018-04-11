import database
import mailing
import payment_gateway
import tickets
import re
import time
import os
import security_2
t1=time.time()
def home():

        
    print " _____________________________________________________________________________________________________________________________________________________________________"
    print "|\t\t\t\t\t                               Please Open Full screen mode                                                                   |"
    print "|_____________________________________________________________________________________________________________________________________________________________________|"

    print "|\t\t\t\t\t____________________________                                                                                                  |"
    print "|\t\t\t\t\t____________________________                                                                                                  |"
    print "|\t\t\t\t\t              ||                                                                                                              |"
    print "|\t\t\t\t\t              ||                                                                                                              |"
    print "|\t\t\t\t\t              ||                                                                                                              |"
    print "|\t\t\t\t\t              ||                                                                                                              |"
    print "|\t\t\t\t\t              ||                                                                                                              |"
    print "|\t\t\t\t\t              ||                                                                                                              |"
    print "|\t\t\t\t\t              ||                                                                                                              |"
    print "|\t\t\t\t\t              ||        ________                                   ___                                                        |"
    print "|\t\t\t\t\t              ||       |            \                /   /\       |    \                                                      |"
    print "|\t\t\t\t\t              //       |             \              /   /  \      |     |                                                     |"  
    print "|\t\t\t\t\t             //        |_____         \            /   /____\     |___ /                                                      |"
    print "|\t\t\t\t\t ||         //         |               \    /\    /   /      \    |\                                                          |"
    print "|\t\t\t\t\t ||        //          |                \  /  \  /   /        \   | \                                                         |"
    print "|\t\t\t\t\t  \\\______//           |________         \/    \/   /          \  |  \                                                        |"
    print "|\t\t\t\t\t                                                                                                                              |"  
    print "|_____________________________________________________________________________________________________________________________________________________________________|"
    print "|\t\t\t\t\t                                                                                                                              |"  
    print "|\t\t\t\t\t                             Jewar International Airport                                                                      |"  
    print "|\t\t\t\t\t                                  Jewar \xa9 2017                                                                                |"
    print "|_____________________________________________________________________________________________________________________________________________________________________|"

    print " _____________________________________________________________________________________________________________________________________________________________________"
    print "|\t\t\t\t\t                                                                                                                              |"
    print "|\t\t\t\t\t                          1. Book a new Ticket                                                                                |"
    print "|\t\t\t\t\t                          2. Check your ticket status                                                                         |"
    print "|\t\t\t\t\t                          3. Cancel Your Ticket                                                                               |"
    print "|\t\t\t\t\t                          4. Arrival and Departure News                                                                       |"
    print "|\t\t\t\t\t                          5. Exit                                                                                             |"
    print "|_____________________________________________________________________________________________________________________________________________________________________|"

    x=-1
    while x<0 or x>5:
        while True:
            try:
                x=int(raw_input("\t\t\t\t\t\tPlease enter your choice (1/2/3/4/5): "))
                break
            except ValueError:
                print "Please enter value in 1/2/3/4/5"

    if x==5:
        t2=time.time()
        print "You have run the program for : ",t2-t1," seconds!"
        print "THANK YOU"
        exit()
    elif x==1:
        tickets.ticket_Issue()
        for i in range(5):
            time.sleep(1)
        home()
    elif x==2:
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        a=raw_input("\t\t\t\t\t\t Please enter your ticket number : ")
        tickets.tick_info(a)
        print " _____________________________________________________________________________________________________________________________________________________________________"
        print
        for i in range(5):
            time.sleep(1)
        home()
    elif x==3:
        tickets.cancel()
        for i in range(5):
            time.sleep(1)
            
        home()

    elif x==4:
        database.Arrival()
        for i in range(5):
            time.sleep(1)

        home()
        


home()
    
    
    
    
