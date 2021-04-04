from os import system
from datetime import datetime
from replit import db

def add(vards, kods, summa, datums):
    db[vards] = [kods, summa, datums]

start = """BANKAS KREDĪTA REĢISTRS
*********
1 - Iegūt informāciju
2 - Pievienot jaunu informāciju
3 - Aizvērt
"""

start2 = """INFORMĀCIJA
*****
1 - Parādīt visus
2 - Parādīt kuri kavē.
3 - Pārbaudīt personu.
4 - Atgriezties
"""

format = "%d/%m/%Y"

def iegut():
  
  while True:
    system("clear")
    print(start2)
    izvele = input("Opcijas izvēle..")
    if izvele == "1":
        print("")
        for i in db.keys():
          print(f"""* {i} *
Personas kods: {db[i][0]}
Summa: {db[i][1]}$
Atdošanas dat.: {db[i][2]}
"""
          )
        input("Nospied Enter lai turpinātu..")
    elif izvele == "2":
      now = datetime.now()
      now2 = now.strftime("%d/%m/%Y")   
      b = datetime.strptime(now2, format)
      ir = 0
      for i in db.keys():
        a = datetime.strptime(db[i][2], format)
        if a < b:
          c = str(a-b)
          kav = c.split()[:2]
          ir = 1
          print(f"""
* {i} *
Personas kods: {db[i][0]}
Summa: {db[i][1]}$
Kavējums: {' '.join(kav)}
""")
      if ir == 0:
        print("Neviens ieraksts netika atrasts")
      input("Nospied Enter lai turpinātu..")
    elif izvele == "3":
      vards = input("Lūdzu norādiet meklētās personas vārdu uzvārdu: ")
      if db.prefix(vards):
        for i in db.prefix(vards):
          print(f"""
* {i} *
Personas kods: {db[i][0]}
Summa: {db[i][1]}$
Atdošanas dat.: {db[i][2]}
"""
          )
      else:
        print("Persona ar tādu vārdu netika atrasta")
      input("Nospied Enter lai turpinātu..")
    elif izvele == "4":
      break

def pievienot():
    vardsUzvards = input("Vārds uzvārds: ")
    pKods = input("Personas kods: ")

    kredits = input("Aizņēmuma summa: ")
    while True:
        aDatums = input("Atdošanas datums [ dd/mm/yyyy ]: ")
        try:
            datetime.strptime(aDatums, format)
            break
        except ValueError:
            print("Nepareiz datuma formāts")
    add(vardsUzvards, pKods, kredits, aDatums)
    print("Ieraksts veiksmīgi pievienots")
    print(f"""
*
  Vārds uzvārds: {vardsUzvards};
  Personas kods: {pKods};
  Summa: {kredits}$;
  Atdošanas datums: {aDatums}.
""")
    input("Nospied Enter lai turpinātu..")

while True:
    system("clear")
    print(start)
    izv = input("Opcijas izvēle..")
    if izv == "1":
        iegut()
    elif izv == "2":
        pievienot()
    elif izv == "3":
        break