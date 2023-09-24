from datetime import date

# Fonction pour vérifier si une date est valide
def date_est_valide(jour, mois, annee):
    if mois < 1 or mois > 12:
        return False
    if jour < 1:
        return False
    if mois in [1, 3, 5, 7, 8, 10, 12]:
        return jour <= 31
    elif mois in [4, 6, 9, 11]:
        return jour <= 30
    elif est_bissextile(annee):
        return jour <= 29
    else:
        return jour <= 28

# Fonction pour saisir une date de naissance
def saisie_date_naissance():
    while True:
        try:
            annee = int(input("Entrez l'année de naissance : "))
            mois = int(input("Entrez le mois de naissance : "))
            jour = int(input("Entrez le jour de naissance : "))
            if date_est_valide(jour, mois, annee):
                return date(annee, mois, jour)
            else:
                print("Date de naissance invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer des nombres valides.")

# Fonction pour calculer l'âge
def age(date_naissance):
    aujourdhui = date.today()
    annee_naissance = date_naissance.year
    mois_naissance = date_naissance.month
    jour_naissance = date_naissance.day

    age = aujourdhui.year - annee_naissance - ((aujourdhui.month, aujourdhui.day) < (mois_naissance, jour_naissance))
    return age

# Fonction pour vérifier si une personne est majeure
def est_majeur(date_naissance):
    return age(date_naissance) >= 18

# Procédure pour tester l'accès
def test_acces():
    date_naissance = saisie_date_naissance()
    if est_majeur(date_naissance):
        print(f"Bonjour, vous avez {age(date_naissance)} ans, Accès autorisé.")
    else:
        print(f"Désolé, vous avez {age(date_naissance)} ans, Accès interdit.")

# Tester la procédure
test_acces()
