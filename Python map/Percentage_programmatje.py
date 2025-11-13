
print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y? ")
print("[2] Hoeveel % is x van y? ")
print("[3] Hoeveel % neemt toe van y? ")
print("[4] Hoeveel % neemt af van y? ")
print("[5] Hoeveel y toegenomen naar x? ")
print("[6] Hoeveel is y toegenomen met x%? ")

choice = input("Welke optie kies je?")
match choice:
    case "1":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x / 100 * y
        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "% = " + str(x/100) + " en " + str(x/100) + " x " + str(y) + " = " + str(answer))
        print(f"De berekening is: \n {x} : {y} = {x / y}; {x / y} x 100 = {int(round(answer, 0))}%")
    case "2":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x / 100 * y
        print(f"De berekening is: \n {x} : {y} = {x / y}; {x / y} x 100 = {int(round(answer, 0))}%")

    case "3":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        #answer = x + 100 / 100
        answer = y * ((x /100) + 1)
        print(f"De berekening is: \n {x} + 100 = {x + 100}; {x / 100}; {x * y} = {float(round(answer, 1))}%")

    case "4":
        x = float(input("wat is x? "))
        y = float(input("wat is y? "))
        answer = (((100 - x) * y) / 100)
        print(f"De berekening is: \n 100 - x = {100 - x}; x = {x * y} : {x / 100}; = {float(answer)}")

    case "5":
        x = float(input("wat is x? "))
        y = float(input("Wat is y? "))
        answer1 = ((x / y) - 1) * 100
        # answer2 = ((y * 100) / x)
        print(f"De berekening is: x = {x / y}; {x - 1}; {x * 100} = {float(input(round(answer1, 0)))}%")
        # print(f"De berekning is: x= {y * 100}; {y / x}; {100 - y} = {float(input(round(answer2, 0)))}%")

    case "6":
        x = float(input("Wat is x? "))
        y = float(input("Wat is y? "))
        answer1 = ((x * 100) / (y + 100))
        # answer2 = ((x * 100) / y)
        print(f"De berekning is: x = {x * 100}; {x / y} = {float(input(round(answer1, 0)))}")
        # print(f"De berekning is: x = {x * 100}; {x / y} = {float(input(round(answer2, 0)))}")
