import random

vragen=[
    {
        "vak":"programmeren",
        "vraag":"Wat is Python?",
        "antwoorden":["Programmeertaal","Soort slang","Scripts taal","Framework"],
        "goed":"Programmeertaal"
    },
]

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
    


while True:
    quiz()
    opnieuw = input("Wil je nog een keer spelen? (ja/nee): ")
    if opnieuw.lower() != "ja":
        print()
        print("Bedankt voor het spelen!")
        print("Tot de volgende keer!")
        break