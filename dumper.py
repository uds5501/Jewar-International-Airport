import pickle
x=["ACe11089a94f8481e1f7d4a4331ce02838","f4b094441a1e6e3e1e1c5d82984dabd0"]
f=open('twilio_info.dat','wb')
pickle.dump(x,f)
print "done"
