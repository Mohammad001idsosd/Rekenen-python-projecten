# # 1. maak eerst een programmaatje dat random een naam kiest
# # 2. maak dan een programmaatje dat random 2 namen kiest (niet 2 dezelfde)
# # 3. maak dan een programmaatje dat random x namen kiest (niet 2 dezelfde), de gebruiker mag x kiezen
# # 4. vanuit dat programmaatje breiden we het programma uit naar y groepjes van x personen – de gebruiker mag een keuze maken


# # lijst met namen: 
# # Daan A 
# # Abdul
# # Yaroslav
# # Beam 
# # Luo Xi
# # Dima
# # Damien
# # Matthew 
# # Ahmed 
# # Winay
# # Jarrod
# # Mohammad 
# # Jaimy
# # Maurizio
# # Jay-Quan
# # Safa
# # Kiyara
# # Marouf
# # Annemare
# # Semen
# # Ajay
# # Bert
# # Rogier
# # Daan V
# # Kateryna

# import random


namen = [
    "Daan A", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damien", "Matthew",
    "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa",
    "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V", "Kateryna"
]

# while True:
#     print("\n1. Eén naam\n2. Twee namen\n3. x namen\n4. Groepjes maken\n5. Stoppen")
#     keuze = input("Maak een keuze (1-5): ")

#     if keuze == "1":
#         print(random.choice(namen))

#     elif keuze == "2":
#         print(random.sample(namen, 2))

#     elif keuze == "3":
#         x = int(input("Hoeveel namen wil je? "))
#         print(random.sample(namen, min(x, len(namen))))

#     elif keuze == "4":
#         x = int(input("Hoeveel personen per groepje? "))
#         random.shuffle(namen)  # schudt de hele lijst door elkaar
#         for i in range(0, len(namen), x):
#             groep = namen[i:i+x]
#             print(f"Groep {i//x + 1}: {', '.join(groep)}")

#     elif keuze == "5":
#         print("Programma afgesloten 👋")
#         break

#     else:
#         print("Ongeldige keuze!")


import random 
groepje = 0
groepjes = int(input("Hoeveel groepen wil je?: "))
personen = int(input("Hoeveel personen wil je?: "))
huidigeNaam = 0
namen = [
    "Daan A", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damien", "Matthew",
    "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa",
    "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V", "Kateryna"
]

for i in range(groepjes):
    groepjes += 1
    print("------")
    print(f"groep{groepjes}:")
    print("------")
    for i in range(personen):
        huidigeNaam = random.choice(namen)
        print(huidigeNaam)
        namen.remove(huidigeNaam)