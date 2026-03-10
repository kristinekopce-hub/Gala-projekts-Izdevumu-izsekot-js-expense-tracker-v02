# izveido kategoriju sarakstu
from secrets import choice


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
    if choice == "1": 
# pievienot izdevumus
        if choice == "1":
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
                amount = round(amount, 2)
                break
            except ValueError:
                print("Ievadi summu (EUR)")
 

# pievieno aprakstu brīva formā
description = input("Apraksts: ")

# saglabā izdevumu datubāzē
izdevumi = {
    "datums": datums,
    "kategorija": Kategorijas_izvēle,
    "summa": summa,
    "apraksts": description
}
izdevumi.append(izdevumi)
# apstiprina pievienošanu
print(f"\nIzdevums pievienots:", izdevumi)
