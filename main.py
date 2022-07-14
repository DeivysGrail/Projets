from pathlib import Path
import random


# Quoi faire ?
cours_principal = ["Django", "Udemy"]
cours_pratique = ["Projet", "Formation intermédiaire", "Formation hard"]
passe_temps = ["Quiz", "Exercices"]

# Choix aléatoires
choix_01 = random.choice(cours_principal)
choix_02 = random.choice(cours_pratique)
choix_03 = random.choice(passe_temps)

emploie_du_temps_chemin = "/home/bastien/EDT/Schedule.txt"


# Semaine du ? --------------------------------------------------------
unique_input = input("Semaine du lundi:")
unique_input = f"Semaine du lundi {unique_input}"
# Création du fichier --------------------------------------------------
schedule = Path("/home/bastien/EDT")
file_edt = Path(f"/home/bastien/EDT/{unique_input}.txt")
schedule.mkdir(exist_ok=True)
file_edt.touch()

# Modification du fichiers -------------------------------------------
with open(emploie_du_temps_chemin, "r") as f:
    texte = f.read()
    for i in texte:
        texte = texte.replace("MAIN", f"{random.choice(cours_principal)}")
        texte = texte.replace("PRATIQUE", f"{random.choice(cours_pratique)}")
        texte = texte.replace("PASSE_TEMPS", f"")
with open(file_edt, "w") as f:
    f.write(texte)

