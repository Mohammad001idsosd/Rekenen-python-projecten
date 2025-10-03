#Mijn manier met behulp met chatgpt:
# import random

#def dobbelspel():
#    dobbelsteen = random.randint(1, 10)
#    gok = int(input("Raad het dobbelsteen-getal (1 t/m 10):"))
#    if gok == dobbelsteen:
#        print(f"Goed gedaan! 🎉 Het getal was inderdaad {dobbelsteen}.")
#    else:
#        print(f"Helaas, fout. Het getal was {dobbelsteen}.")
#dobbelspel() 



#De docent manier:
import random

worp = random.randint(1,6)
gok = int(input("Gok het getaal:"))
if (worp == gok):
    print("goed gegokt")
else:
    print("Fout gegokt")
