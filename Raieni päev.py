import datetime
now = datetime.datetime.now()
timeList = []
today00= now.replace(hour = 0, minute=0, second=1, microsecond=0)
timeList.append(today00)
today01= now.replace(hour = 1, minute=0, second=0, microsecond=0)
timeList.append(today01)
today02= now.replace(hour = 2, minute=0, second=0, microsecond=0)
timeList.append(today02)
today03= now.replace(hour = 3, minute=0, second=0, microsecond=0)
timeList.append(today03)
today04= now.replace(hour = 4, minute=0, second=0, microsecond=0)
timeList.append(today04)
today05= now.replace(hour = 5, minute=0, second=0, microsecond=0)
timeList.append(today05)
today06= now.replace(hour = 6, minute=0, second=0, microsecond=0)
timeList.append(today06)
today07= now.replace(hour = 7, minute=0, second=0, microsecond=0)
timeList.append(today07)
today08= now.replace(hour = 8, minute=0, second=0, microsecond=0)
timeList.append(today08)
today09= now.replace(hour = 9, minute=0, second=0, microsecond=0)
timeList.append(today09)
today10= now.replace(hour = 10, minute=0, second=0, microsecond=0)
timeList.append(today10)
today11= now.replace(hour = 11, minute=0, second=0, microsecond=0)
timeList.append(today11)
today12= now.replace(hour = 12, minute=0, second=0, microsecond=0)
timeList.append(today12)
today13= now.replace(hour = 13, minute=0, second=0, microsecond=0)
timeList.append(today13)
today14= now.replace(hour = 14, minute=0, second=0, microsecond=0)
timeList.append(today14)
today15= now.replace(hour = 15, minute=0, second=0, microsecond=0)
timeList.append(today15)
today16= now.replace(hour = 16, minute=0, second=0, microsecond=0)
timeList.append(today16)
today17= now.replace(hour = 17, minute=0, second=0, microsecond=0)
timeList.append(today17)
today18= now.replace(hour = 18, minute=0, second=0, microsecond=0)
timeList.append(today18)
today19= now.replace(hour = 19, minute=0, second=0, microsecond=0)
timeList.append(today19)
today20= now.replace(hour = 20, minute=0, second=0, microsecond=0)
timeList.append(today20)
today21= now.replace(hour = 21, minute=0, second=0, microsecond=0)
timeList.append(today21)
today22= now.replace(hour = 22, minute=0, second=0, microsecond=0)
timeList.append(today22)
today23= now.replace(hour = 23, minute=0, second=0, microsecond=0)
timeList.append(today23)
Raien = "Üleval"
onUleval = input("Kas Raien on üleval? y/n - ")

if onUleval == "y":
    if now > today06 and onUleval == "y" and now <today07:
        kasArkab = input("Kas Raien ärkas üles? y/n - ")
        if kasArkab == "y":
            print("Raien veereb voodist põrandale") 
        else:
            print("Raien pekstakse kulbiga voodist välja")
        
    if now > today07 and onUleval == "y" and now <today08:
        print("Raien pannakse oma lasteistmesse ja viiakse kooli.")
        
    if now > today08 and onUleval == "y" and now <today09:
        print("Raien mõnuleb hommikuses matas.")
        
    if now > today09 and onUleval == "y" and now <today10:
        print("Raien mõnuleb hommikuses matas vol 2.")
        
    if now > today10 and onUleval == "y" and now <today11:
        print("Raien mõnuleb hommikuses matas vol 3.")
        
    if now > today11 and onUleval == "y" and now <today12:
        print("Raien sureb vaikselt nälga.")
        
    if now > today12 and onUleval == "y" and now <today13:
        print("Raien jookseb relvaga sööklasse, et järjekorras lõigata.")
        
    if now > today13 and onUleval == "y" and now <today14:
        print("Raien on toidukoomas.")
        
    if now > today14 and onUleval == "y" and now <today15:
        print("Raien saab Hugos katsumist.")
        
    if now > today15 and onUleval == "y" and now <today16:
        print("Raien saab Ilanas vähki.")
        
    if now > today16 and onUleval == "y" and now <today17:
        print("Raien vingub Ilana üle.")
        
    if now > today17 and onUleval == "y" and now <today18:
        print("Raien pelab teiste kididega.")
        
    if now > today18 and onUleval == "y" and now <today19:
        print("Raien shitpostib Discordis.")
        
    if now > today19 and onUleval == "y" and now <today20:
        print("Raien kaob suvaliselt ära, et süüa võtta.")
        
    if now > today20 and onUleval == "y" and now <today21:
        print("Raien spammib discordis kellegi nime.")
        
    if now > today21 and onUleval == "y" and now <today22:
        print("Raien tahab CSis carryt saada.")
        onUleval = input("Läks magama? y/n - ")
        
    if now > today22 and onUleval == "y" and now < today23:
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

    if now > today02 and onUleval == "y" and now < today06:
        print ("Isa matab Raienit aeda, kuna ta ei läinud magama. GG")
        Raien = "Surnud"
        print ("Raien on ", Raien)

    if onUleval == "n":
        print("Putsis, kontrolli tunni pärast uuesti.")
else:
    print("Tatt tudub.")
    
        
