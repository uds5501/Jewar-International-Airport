import pickle
try:
    f=open('database.dat','rb')
    fo=open('Log.txt','r')
    x=pickle.load(f)
    
    print x
    for line in fo:
        print line.strip().split()

    f.close()
    fo.close()

except IOError:
    pass
