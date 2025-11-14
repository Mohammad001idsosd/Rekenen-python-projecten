
print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Percentage van een getaal berekenen ")
print("[2] Welke percentage is x van y? ")
print("[3] Toename van precentage ")
print("[4] Bedrag na procentuele afname ")
print("[5.1] Met hoeveel is iets gestegen?  ")
print("[5.2] Met heoveel procent is iets gedaald?  ")
print("[6.1] Bedrag voor een precentuele verhoging ")
print("[6.2] Bedrag voor een procentuele verlaging ")

choice = input("Welke optie kies je?")
match choice:
    case "1":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x / 100 * y
        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "% = " + str(x/100) + " en " + str(x/100) + " x " + str(y) + " = " + str(answer))
        print(f"De berekening is: \n {x} : {y} = {x / y}; {x / y} x 100 = {int(round(answer, 0))}")
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

    case "5.1":

        x = float(input("wat is x? "))
        y = float(input("Wat is y? "))
        answer = ((x / y) - 1) * 100
        print(f"De berekening is: x = {x / y}; {x - 1}; {x * 100} = {float(input(round(answer, 0)))}%")

    case "5.2":
        x = float(input("wat is x? "))
        y = float(input("wat is y? "))
        answer = ((y * 100) / x)
        print(f"De berekning is: x = {y * 100}; {y / x}; {100 - y} = {float(input(round(answer, 0)))}")

    case "6.1":
        x = float(input("Wat is x? "))
        y = float(input("Wat is y? "))
        answer = ((x * 100) / (y + 100))
        print(f"De berekning is: x = {x * 100}; {x / y} = {float(input(round(answer, 0)))}")


    case "6.2":
        x = float(input("Wat is x? "))
        y = float(input("Wat is y? "))
        answer = ((x * 100) / y)
        print(f"De berkening is: x = {x * 100}; {x / y} = {float(input(round(answer, 0)))}")
