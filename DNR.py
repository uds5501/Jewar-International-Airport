Country={"CHI":"China","USA":"United States of America","ESP":"Spain","GER":"Germany","AUS":"Australia","NEW":"New Zealand"}
Airlines={"ETI":"Etihad Airways","QAT":"Qatar Airines","AIR":"Air India"}

for i in Airlines.keys():
    for j in Country.keys():
        text=i+"_"+j+".txt"
        f=open(text,"w")
        f.write("01"+" "+"A"+" "+"LEFT\n")
        f.write("02"+" "+"A"+" "+"LEFT\n")
        f.write("03"+" "+"A"+" "+"LEFT\n")
        f.write("04"+" "+"A"+" "+"LEFT\n")
        f.write("05"+" "+"A"+" "+"LEFT\n")
        f.write("06"+" "+"A"+" "+"LEFT\n")
        f.write("07"+" "+"A"+" "+"LEFT\n")
        f.write("08"+" "+"A"+" "+"LEFT\n")
        f.write("09"+" "+"A"+" "+"LEFT\n")
        f.write("10"+" "+"A"+" "+"LEFT\n")
        f.write("11"+" "+"A"+" "+"MID\n")
        f.write("12"+" "+"A"+" "+"MID\n")
        f.write("13"+" "+"A"+" "+"MID\n")
        f.write("14"+" "+"A"+" "+"MID\n")
        f.write("15"+" "+"A"+" "+"MID\n")
        f.write("16"+" "+"A"+" "+"MID\n")
        f.write("17"+" "+"A"+" "+"MID\n")
        f.write("18"+" "+"A"+" "+"MID\n")
        f.write("19"+" "+"A"+" "+"MID\n")
        f.write("20"+" "+"A"+" "+"MID\n")
        f.write("21"+" "+"A"+" "+"RIGHT\n")
        f.write("22"+" "+"A"+" "+"RIGHT\n")
        f.write("23"+" "+"A"+" "+"RIGHT\n")
        f.write("24"+" "+"A"+" "+"RIGHT\n")
        f.write("25"+" "+"A"+" "+"RIGHT\n")
        f.write("26"+" "+"A"+" "+"RIGHT\n")
        f.write("27"+" "+"A"+" "+"RIGHT\n")
        f.write("28"+" "+"A"+" "+"RIGHT\n")
        f.write("29"+" "+"A"+" "+"RIGHT\n")
        f.write("30"+" "+"A"+" "+"RIGHT\n")
        
        f.close()
    
