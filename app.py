# datumu apstrāde
from datetime import date
import re

# savienojums ar storage.py
from storage import load_expenses, save_expenses
#izveikdo tabulas izveide
from tabulate import tabulate   
Kategorijas = [
    "Ēdiens", 
    "Transports", 
    "Izklaide", 
    "Komunālie maksājumi", 
    "Veselība", "Iepirkšanās", 
    "Citi"
    ]

# ielādē esošos izdevumus
izdevumi = load_expenses()

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
# 7 IZVELE
while True:
    choice = input("Izvēlieties darbību (1-7): ")

    print("Tu izvēlējies:", choice)
    if choice == "7":
        print("Programma beidzas.")
        break
    elif choice == "1": 

# 1 IZVELE
# pievienot izdevumus
        print("\nPievienot izdevumu")
# Datuma izvēle ar noklusējuma datumu šodien

        today = date.today().strftime("%Y-%m-%d")
        datums = input(f"Ievadiet datumu (YYYY-MM-DD)[{today}]: ")

        if datums == "":
            datums = today 
        elif not re.match(r"\d{4}-\d{2}-\d{2}", datums):
            print("Datumu:", datums)
            continue
# kategorijas izvēle
        print("\nKategorijas:")
        print(", ".join(Kategorijas))

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
# jauns izdevums izveide
        jauns_izdevums = {
        "datums": datums,
        "kategorija": Kategorijas_izvēle,
        "summa": summa,
        "apraksts": apraksts
        }

# pievieno jaunu izdevumu izdevumu sarakstam
        izdevumi.append(jauns_izdevums)
# saglabā izdevumus datubāzē
        save_expenses(izdevumi)
        print("Izdevums pievienots:", jauns_izdevums)
# ___2 IZVELE 
    # parādīt izdevumus
    elif choice == "2":  
        print("\nIzdevumi:")
        if not izdevumi:
            print("Nav pievienotu izdevumu.")
        else:
            tabula = []
    # tabulas galvas izveidi jāievēro <12> -12 simbolu platums, <10> - 10 simbolu platums, <20> - 20 simbolu platums
            for izdevumu_saraksts in izdevumi:
                tabula.append([
                    izdevumu_saraksts["datums"],
                    f"{izdevumu_saraksts['summa']:.2f} EUR",
                    izdevumu_saraksts["kategorija"],
                    izdevumu_saraksts["apraksts"]
                ])
            print(tabulate(
                tabula, 
                headers=["Datums", "Summa (EUR)", "Kategorija", "Apraksts"], 
                tablefmt="grid",
                maxcolwidths=[12, 12, 20, 30]
            ))
    else:
        print("Nederīga izvēle. Lūdzu, izvēlieties darbību no 1 līdz 7.")   


