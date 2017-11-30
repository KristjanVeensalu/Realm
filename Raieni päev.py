import datetime
now = datetime.datetime.now()
today16= now.replace(hour = 16, minute=0, second=0, microsecond=0)
today17= now.replace(hour = 17, minute=0, second=0, microsecond=0)
today18= now.replace(hour = 18, minute=0, second=0, microsecond=0)
today19= now.replace(hour = 19, minute=0, second=0, microsecond=0)
today20= now.replace(hour = 20, minute=0, second=0, microsecond=0)
today21= now.replace(hour = 21, minute=0, second=0, microsecond=0)
today22= now.replace(hour = 22, minute=0, second=0, microsecond=0)
today23= now.replace(hour = 23, minute=0, second=0, microsecond=0)
today00= now.replace(hour = 0, minute=0, second=1, microsecond=0)
today01= now.replace(hour = 1, minute=0, second=0, microsecond=0)
today02= now.replace(hour = 2, minute=0, second=0, microsecond=0)
today03= now.replace(hour = 3, minute=0, second=0, microsecond=0)
Raien = "Üleval"
onUleval = input("Kas Raien on üleval? y/n - ")

if onUleval == "y":
    if now > today21 and Raien == "Üleval" and now <today22:
        print("Raien tahab CSis carryt saada.")
        onUleval = input("Läks magama? y/n - ")
        
    if now > today22 and Raien == "Üleval" and now < today23:
        print("Raien peab magama minema.")
        onUleval = input("Läks magama? y/n - ")
        
    if now > today23 and onUleval == "y" and now < today00:
        print ("Isa on valmis sisse lendama.")
        onUleval = input("Läks magama? y/n - ")
        
    if now > today00 and onUleval == "y" and now < today01:
        print ("Isa võtab sae välja.")
        onUleval = input("Läks magama? y/n - ")

    if now > today01 and onUleval == "y" and now < today02:
        print ("Isa murrab Raieni ust maha.")
        onUleval = input("Läks magama? y/n - ")

    if now > today02 and onUleval == "y" and now < today03:
        print ("Isa matab Raienit aeda.")
        Raien = "Surnud"
        print ("Raien on ", Raien)

    if onUleval == "n":
        print("Putsis, kontrolli tunni pärast uuesti.")
else:
    print("Tatt tudub.")
    
        
