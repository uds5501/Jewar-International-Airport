#security updated
import pickle
import os
def update(li):
    flag=0
    try:
        data=open("database.dat","rb")
        try:
            x=pickle.load(data)
            
            flag=1
        except EOFError:
            pass
        data.close()
        inter=open("new.dat","ab")
        if flag==1:
            a=x
            
            a.append(li)
            pickle.dump(a,inter)
            inter.close()
            os.remove("database.dat")
            os.rename("new.dat","database.dat")
        else:
            a=[]
            a.append(li)
            pickle.dump(a,inter)
            inter.close()
            os.remove("database.dat")
            os.rename("new.dat","database.dat")
            
    
    except IOError or EOFError:
        print "File not found"
        
def check():
    flag=0
    a=open("database.dat","ab+")
    try:
        data=pickle.load(a)
        print data
        flag=1
        
    except EOFError:
        pass
    a.close()
    lines=[]
    if flag==1:
        b=open("Log.txt","r")
        for line in b:
            
            lines.append(line.strip().split())
        print lines
        
        b.close()
        
    elif flag!=1:
        return True

    if data==lines:
        return True
    elif data!=lines:
        return False
        
           

    
