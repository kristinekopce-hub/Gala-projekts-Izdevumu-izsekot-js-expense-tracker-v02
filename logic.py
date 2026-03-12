# logic.py
# Biznesa loģika izdevumu apstrādei, filrēšanai, kopsavilkuma veidošanai un dzēšanai
from collections import defaultdict
# ____#3 filtrēt pēc mēneša
def filtrēt_pēc_mēneša(izdevumi, mēnesis):
    filtrēti = []
    for izdevumu_saraksts in izdevumi:
        if izdevumu_saraksts["datums"].startswith(mēnesis):
            filtrēti.append(izdevumu_saraksts)
    return filtrēti
#aprēķina kopejo summu
def aprēķināt_kopējo_summu(izdevumi):
    total_summa = 0
    for izdevumu_saraksts in izdevumi:
        total_summa += izdevumu_saraksts["summa"]
    return round(total_summa, 2)
#kopsavilkums pēc kategorijas
def kopsavilkums_pēc_kategorijas(izdevumi):
    kopsavilkums = defaultdict(float)
    for izdevumu_saraksts in izdevumi:
        kategorija = izdevumu_saraksts["kategorija"]
        summa = izdevumu_saraksts["summa"]
        kopsavilkums[kategorija] += summa
    return {kategorija: round(summa, 2) for kategorija, summa in kopsavilkums.items()}
# izvedod sarakstu tabuludef izvade_tabula(izdevumi):
def izvade_tabula(izdevumi):
    tabula = []
    for izdevumu_saraksts in izdevumi:
        tabula.append([
            izdevumu_saraksts["datums"],
            izdevumu_saraksts["kategorija"],
            f"{izdevumu_saraksts['summa']:.2f} EUR",
            izdevumu_saraksts["apraksts"]
        ])
    return tabula
