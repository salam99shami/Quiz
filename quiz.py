print("Welkom bij onze Python Quiz!")
print("Test hier wat je hebt geleerd tijdens de opleiding.")

naam = input("Wat is je naam? ")
print("Hallo", naam, "! Laten we beginnen.")

antwoord = input("Wat is Python? ")
if antwoord.lower() == "programmeertaal":
    print("Goed antwoord!")
else:
    print("Helaas, dat is niet het juiste antwoord.")