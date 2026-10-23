import tkinter as tk
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
        "vak":"programmeren",
        "vraag":"Waarom wordt 'Hello World' gebruikt aan de begin van een code?",
        "antwoorden":["Om 'Hallo' tegen de computer te zeggen", "Om de computer jou te laten groeten","Om simpelweg te testen en controleren of het programma juist werkt", "Zodat je een computer laat weten dat je gaat coderen"],
        "goed":"Om simpelweg te testen en controleren of het programma juist werkt"
    },
    {
        "vak":"programmeren",
        "vraag":"Hoeveel verdient een web developer?",
        "antwoorden":["6.000 tot 7.000 Euro per maand", "3.470 tot 5.760 Euro per maand", "2.761 tot 3.4561 Euro per maand", "3.394 tot € 3.693 Euro per maand"],
        "goed":"3.394 tot € 3.693 Euro per maand"
    },
]

# Highscore laden 
def highscore_laden():
    # controleert of highscore.txt bestaat.
    if os.path.exists("highscore.txt"):
        # opent het bestand om te lezen.
        with open("highscore.txt","r") as bestand:
            # leest de inhoud van het bestand.
            # verwijdert overtollige witruimte aan het begin en einde.
            inhoud=bestand.read().strip()
            if inhoud!="":
                # zet de tekst om naar een geheel getal.
                return int(inhoud)
    # geeft nul terug als er nog geen score is opgeslagen.
    return 0


# Highscore opslaan
def highscore_opslaan(score):
    # Hier opent "w" het bestand om te schrijven 
    # "w" overschrijft de bestaande inhoud. Dat is hier de bedoeling, omdat je alleen de nieuwe hoogste score wilt bewaren.
    with open("highscore.txt","w") as bestand:
        bestand.write(str(score))


class QuizApp:
    # is de constructor. Deze wordt automatisch uitgevoerd wanneer je een object van de klasse maakt.
    def __init__(self, root):
        # initialize the main window
        # root is het hoofdvenster dat aan de klasse wordt doorgegeven.
        # self verwijst naar het huidige quizobject.
        self.root = root
        # set window title
        self.root.title("Module 01 - Opleidingsquiz")
        # set window size
        # stelt de beginbreedte in op 600 pixels en de hoogte op 450 pixels.
        self.root.geometry("600x450")

        self.score = 0
        self.index = 0
        self.quiz_vragen = []

        self.titel = tk.Label(
            root, text="MODULE 01 - OPLEIDINGSQUIZ",
            font=("Arial", 18, "bold")
        )

        # pack plaatst het label in het venster
        # pady=20 voegt verticale ruimte toe.
        self.titel.pack(pady=20)

        self.vraag_label = tk.Label(
            root, text="", font=("Arial", 13),
            # wraplength=520 zorgt ervoor dat lange tekst over meerdere regels wordt verdeeld.
            wraplength=520
        )
        self.vraag_label.pack(pady=15)

        self.knoppen = []
        for i in range(4):
            knop = tk.Button(
                root, text="", font=("Arial", 11),
                width=45,
                # command bepaalt welke functie wordt uitgevoerd wanneer de gebruiker op de knop klikt.
                command=lambda keuze=i: self.controleer(keuze)
            )
            knop.pack(pady=4)
            self.knoppen.append(knop)

        self.feedback = tk.Label(root, text="", font=("Arial", 11))
        self.feedback.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.volgende_knop = tk.Button(
            root, text="Volgende vraag",
            command=self.volgende_vraag,
            # Dat betekent dat de gebruiker er nog niet op kan klikken. Eerst moet een antwoord worden gekozen.
            state="disabled"
        )
        self.volgende_knop.pack(pady=10)

        self.start_quiz()

    def start_quiz(self):
        self.score = 0
        self.index = 0
        self.quiz_vragen = vragen.copy()
        random.shuffle(self.quiz_vragen)
        # config() verandert de tekst van het scorelabel.
        self.score_label.config(text="Score: 0")
        self.volgende_vraag()

    def volgende_vraag(self):
        if self.index >= len(self.quiz_vragen):
            self.eindscherm()
            return

        vraag = self.quiz_vragen[self.index]
        self.vraag_label.config(
            text=f"Vraag {self.index + 1}/{len(self.quiz_vragen)}\n"
                 f"{vraag['vraag']}"
        )

        self.antwoorden = vraag["antwoorden"].copy()
        random.shuffle(self.antwoorden)

        # enumerate() levert zowel het nummer als het bijbehorende element op. state="normal" maakt de knoppen weer klikbaar.
        for i, knop in enumerate(self.knoppen):
            knop.config(
                text=self.antwoorden[i],
                state="normal"
            )

        self.feedback.config(text="")
        self.volgende_knop.config(state="disabled")

    def controleer(self, keuze):
        vraag = self.quiz_vragen[self.index]
        antwoord = self.antwoorden[keuze]

        if antwoord == vraag["goed"]:
            self.score += 1
            self.feedback.config(text="Correct!")
        else:
            self.feedback.config(
                text=f"Fout! Het juiste antwoord is: {vraag['goed']}"
            )

        self.score_label.config(text=f"Score: {self.score}")

        for knop in self.knoppen:
            knop.config(state="disabled")

        self.volgende_knop.config(state="normal")
        self.index += 1

    def eindscherm(self):
        percentage = self.score / len(self.quiz_vragen) * 100
        oude_score = highscore_laden()

        if self.score > oude_score:
            highscore_opslaan(self.score)
            highscore_tekst = "Nieuwe highscore!"
        else:
            highscore_tekst = f"Highscore: {oude_score}"

        for knop in self.knoppen:
            # pack_forget() haalt de knoppen uit de zichtbare indeling van het venster, maar verwijdert de knoppen niet definitief.
            knop.pack_forget()

        self.vraag_label.config(
            text=f"Quiz klaar!\n\n"
                 f"Je hebt {self.score} van "
                 f"{len(self.quiz_vragen)} vragen goed.\n"
                 f"Percentage: {percentage:.0f}%\n\n"
                 f"{highscore_tekst}"
        )

        self.feedback.config(text="Goed gedaan!")
        self.volgende_knop.config(
            text="Opnieuw spelen",
            state="normal",
            command=self.opnieuw
        )

    def opnieuw(self):
        for knop in self.knoppen:
            knop.pack(pady=4)

        self.volgende_knop.config(
            text="Volgende vraag",
            command=self.volgende_vraag
        )
        self.start_quiz()

# maakt het hoofdvenster.
root = tk.Tk()
# maakt een object van je quizklasse en bouwt de interface op.
app = QuizApp(root)
# start the GUI event loop
# Houdt het venster open en verwerkt gebruikersacties.
root.mainloop()
