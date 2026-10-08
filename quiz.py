import random
import os 

vragen=[
    {
        "vak":"programmeren",
        "vraag":"Wat is Python?",
        "antwoorden":["Programmeertaal","Soort slang","Scripts taal","Framework"],
        "goed":"Programmeertaal"
    },
    {
        "vak":"programmeren",
        "vraag":"Wat is het moeilijkste programmeertaal ter wereld?",
        "antwoorden":["Lua", "Python", "C+", "Malbolge"],
        "goed":"Malbolge"
    },
    {
        "vak":"programmeren",
        "vraag":"Hoeveel verdient een Java developer gemiddeld per maand?",
        "antwoorden":["1.200 tot 1.500 Euro per maand", "4.200 tot 5.140 per maand", "4.000 tot 5.000 per maand", "9.000 tot 10.000 per maand"],
        "goed":"4.200 tot 5.140 per maand"
    },
    {
        "vak":"programmeeren",
        "vraag":"Waarom wordt 'Hello World' gebruikt aan de begin van een code?",
        "antwoorden":["Om 'Hallo' tegen de computer te zeggen", "Om de computer jou te laten groeten","Om simpelweg te testen en controleren of het programma juist werkt", "Zodat je een computer laat weten dat je gaat coderen"],
    }
]

# Highscore laden 
def highscore_laden():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt","r") as bestand:
            inhoud=bestand.read().strip()
            if inhoud!="":
                return int(inhoud)            
    return 0

# Highscore opslaan
def highscore_opslaan(score):
    with open("highscore.txt","w") as bestand:
        bestand.write(str(score))


def quiz():
    score=0

    # Vragen door elkaar
    random.shuffle(vragen)

    print()
    print("========================================")
    print("       MODULE 01 - OPLEIDINGSQUIZ")
    print("========================================")
    print()
    print("Test hoeveel jij weet over de opleiding!")
    print()
    for vraag in vragen:
        print(f"Vak: {vraag['vak']}")
        print(f"Vraag: {vraag['vraag']}")
        for i in range(4):
            print(f"{i+1}. {vraag['antwoorden'][i]}")
        user_input = input("Kies het juiste antwoord (1-4): ")
        if vraag['antwoorden'][int(user_input)-1] == vraag['goed']:
            print("Correct!")
            score += 1
        else:
            print(f"Fout! Het juiste antwoord is: {vraag['goed']}")
        print(f"Je score is: {score}")

    totaal = len(vragen)
    percentage = (score / totaal) * 100
    print("========================================")
    print("              QUIZ KLAAR!")
    print("========================================")
    print()
    print(f"Je hebt {score} van de {totaal} vragen goed.")
    print(f"Percentage: {(score / totaal) * 100:.0f}%")
    print()

    # Beoordeling
    if percentage == 100:
        print("Perfect! Jij weet echt heel veel over de opleiding!")
    elif percentage >= 80:
        print("Heel goed! Je kent de opleiding goed.")
    elif percentage >= 60:
        print("Goed gedaan! Er is nog wat ruimte om te oefenen.")
    elif percentage >= 50:
        print("Voldoende. Je kunt nog wat meer leren over Module 01.")
    else:
        print("Je kunt de onderwerpen van Module 01 nog wat beter oefenen.")

    oude_highscore=highscore_laden()
    if score> oude_highscore:
        print()
        print("Nieuwe Highscroe!")
        print(f"Je oude score is: {oude_highscore}")
        print(f"Je nieuwe score is: {score}")

        highscore_opslaan(score)
    else:
        print(f"De huidige highscore is: {oude_highscore}")


while True:
    quiz()
    opnieuw = input("Wil je nog een keer spelen? (ja/nee): ")
    if opnieuw.lower() != "ja":
        print()
        print("Bedankt voor het spelen!")
        print("Tot de volgende keer!")
        break
        