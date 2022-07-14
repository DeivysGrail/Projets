from pathlib import Path
import random

# Quoi faire ?
cours_principal = ["Django", "Formation complète Python"]
cours_pratique = ["Projet", "Formation intermédiaire", "Formation hard"]
pratique_rapide = ["Quiz", "Exercices"]

# Choix aléatoires
choix_01 = random.choice(cours_principal)
choix_02 = random.choice(cours_pratique)
choix_03 = random.choice(pratique_rapide)

emploie_du_temps_chemin = Path.home() / "EDT" / "Schedule.txt"


# Semaine du ? --------------------------------------------------------
unique_input = input("Semaine du lundi:")
unique_input = f"Pour la semaine du lundi {unique_input}"

# Création du fichier --------------------------------------------------
schedule = Path.home() / "EDT"
file_edt = schedule / f"{unique_input}.txt"
schedule.mkdir(exist_ok=True)
file_edt.touch()

# Modification du fichiers -------------------------------------------
with open(emploie_du_temps_chemin, "r") as f:
    texte = f.read()
    for i in texte:
        texte = texte.replace("MAIN", f"{random.choice(cours_principal)}")
        texte = texte.replace("PRATIQUE", f"{random.choice(cours_pratique)}")
        texte = texte.replace("PASSE_TEMPS", f"{random.choice(pratique_rapide)}")
with open(file_edt, "w") as f:
    f.write(texte)

print(f"\033[32;1;20mVotre emploi du temps est prêt à être utilisé dans le dossier {schedule} !")
