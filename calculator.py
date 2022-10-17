nev = str(input("Adjon meg a nevét: "))
print(f"Kedves, {nev}")

try:
    num1 = float(input("Adja meg az első számot: "))
    num2 = float(input("Adja meg a második számot: "))
except Exception as e:
    #print(e)
     print(f"{nev}, számró vót szó te marha...")
     exit(1)

print("1 - Összeadás\n2 - Kivonás\n3 - Szorzás\n4 - Osztás\n")

option = int(input("Válasszon a fenti listából:- "))

if option == 1:
   print(f"Összeadás: {num1 + num2}")
elif option == 2:
   print(f"Kivonás: {num1 - num2}")
elif option == 3:
   print(f"Szorzás: {num1 * num2}")
elif option == 4:
   print(f"Osztás: {num1 / num2}")