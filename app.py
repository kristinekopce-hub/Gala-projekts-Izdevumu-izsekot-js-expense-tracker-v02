# izveido kategoriju sarakstu
from secrets import choice
# datumu apstrāde 
from datetime import date
import re

Kategorijas = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Citi"]
# izdevumu izsekotals" 
def izdevumu_izsekotajs():
    print ("-------------------")
    print ("Izdevumu izsekotājs")
    print ("-------------------")
    print ()
    print("1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt CSV")
    print("7) Iziet")
# !!! \n  nozīmē jauna rinda 
# while true izsauc ciklu līdz beidzas ar BREAK, 
# if pamatnosacījums if x=1 Elif > lielāks par xx else < mazāks par xx ar papilus nosacījumu 
while True:
    choice = input("Izvēlieties darbību (1-7): ")

    print("Tu izvēlējies:", choice)
    if choice == "7":
        print("Programma beidzas.")
        break
    elif choice == "1": 
# pievienot izdevumus
        print("\nPievienot izdevumu")
# Datuma izvēle ar noklusējuma datumu šodien

        today = date.today().strftime("%Y-%m-%d")
        datums = input(f"Ievadiet datumu (YYYY-MM-DD)[{today}]: ")

        if datums == "":
            datums = today 
        elif not re.match(r"\d{4}-\d{2}-\d{2}", date_input):
            print("Datumu:", datums)
# kategorijas izvēle
        print("\nKategorijas:")
        while True:
            Kategorijas_izvēle = input(f"Ievadiet kategoriju ({', '.join(Kategorijas)}): ")
            print("Tu izvēlējies:", Kategorijas_izvēle)
            if Kategorijas_izvēle in Kategorijas:
                break
            else:  
                print("Nederīga kategorija. Lūdzu, izvēlieties no saraksta.")
# ievadi summu 0.00 EUR
        while True:
            summa_input = input("Ievadiet summu (EUR): ")
            try:
                summa = float(summa_input)
                #pazinojums ja summa ir negativa
                if summa < 0:
                    print("Summa ir negatīva!")
                # Apstiprina summu un noapalo lidz 2 zimes aiz komanta
                summa = round(summa, 2)
                break
            except ValueError:
                print("Ievadi summu (EUR)")
# ievadi aprakstu
        apraksts = input("Ievadiet aprakstu (pēc izvēles): ")

# saglabā izdevumu datubāzē
izdevumi = []
izdevumu_izsekotajs = {
    "datums": datums,
    "kategorija": Kategorijas_izvēle,
    "summa": summa,
    "apraksts": apraksts
}
izdevumi.append(izdevumu_izsekotajs)
# apstiprina pievienošanu
print(f"\nIzdevums pievienots:", izdevumu_izsekotajs)
