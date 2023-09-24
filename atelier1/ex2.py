def est_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    else:
        return False

def test_est_bissextile():
    annees = [2000, 2004, 2020, 2024, 1900, 2100, 2022]
    for annee in annees:
        if est_bissextile(annee):
            print(f"{annee} est bissextile.")
        else:
            print(f"{annee} n'est pas bissextile.")

test_est_bissextile()
