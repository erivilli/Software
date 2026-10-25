# Exercici 1: Determinar el més gran de dos nombres

print("\nExercici 1:")
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))

if num1 > num2:
    print(f"{num1} és més gran que {num2}")
elif num2 > num1:
    print(f"{num2} és més gran que {num1}")
else:
    print("Els nombres són iguals")


# Exercici 2: Calculadora senzilla

num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
operacio = input("Introdueix l'operació (+, -, *, /): ").strip()

if operacio == "/" and num2 == 0:
    print("Error: no es pot dividir per zero.")
elif operacio == "+":
    resultat = num1 + num2
    print(f"El resultat és: {resultat}")
elif operacio == "-":
    resultat = num1 - num2
    print(f"El resultat és: {resultat}")
elif operacio == "*":
    resultat = num1 * num2
    print(f"El resultat és: {resultat}")
elif operacio == "/":
    resultat = num1 / num2
    print(f"El resultat és: {resultat}")
else:
    print("Operació no vàlida.")


# Exercici 3: Any de traspàs

any_triat = int(input("Introdueix un any: "))

if (any_triat % 4 == 0 and any_triat % 100 != 0) or any_triat % 400 == 0:
    print(f"{any_triat} és un any de traspàs.")
else:
    print(f"{any_triat} no és un any de traspàs.")

# Exercici 4: Classificar edats

edat = int(input("Introdueix una edat: "))
if edat >= 0:
    if edat <= 2:
        print("Nadó")
    elif edat <= 12:
        print("Infant")
    elif edat <= 17:
        print("Adolescent")
    elif edat <= 64:
        print("Adult")
    else:
        print("Persona gran")
else:
    print("Edat no vàlida.")


# Exercici 5: Qualitat del senyal Wi-Fi

rssi = float(input("Introdueix el nivell de senyal RSSI en dBm: "))

if rssi >= -50:
    print("Cobertura excel·lent.")
elif rssi >= -67:
    print("Cobertura bona.")
elif rssi >= -75:
    print("Cobertura feble.")
else:
    print("Cobertura molt feble.")


# Exercici 6: Nivell de recepció d'una connexió de fibra òptica

potencia = float(input("Introdueix la potència òptica rebuda en dBm: "))

if -8>= potencia >=-27:
    print("El nivell és acceptable.")
elif potencia > -8:
    print("El nivell és massa alt.")
else:
    print("El nivell és massa baix.")


# Exercici 7: Consum mensual de dades mòbils

consum_gb = float(input("Introdueix el consum mensual de dades en GB: "))

if consum_gb <= 20:
    print("El consum està dins del límit de 20 GB.")
else:
    extra_gb = consum_gb - 20
    print(f"S'ha superat el límit en {extra_gb:.2f} GB.")


# Exercici 8: Diagnòstic d'una connexió de fibra

los_encès = input("L'indicador LOS està encès? (s/n): ").strip().lower()
internet_encès = input("L'indicador d'Internet està encès? (s/n): ").strip().lower()

if los_encès == "s":
    print("Cal revisar el cable de fibra.")
elif internet_encès != "s":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")


# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)

bateria = float(input("Introdueix el percentatge de bateria del SAI: "))

if bateria < 0 or bateria > 100:
    print("El percentatge ha d'estar entre el 0 % i el 100 %.")
elif bateria < 20:
    print("Nivell de bateria crític.")
elif bateria < 50:
    print("Nivell de bateria baix.")
else:
    print("Nivell de bateria suficient.")


# Exercici 10: Qualitat d'una connexió de xarxa

latencia = float(input("Introdueix la latència en ms: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0:
    print("La latència no pot ser negativa.")
elif perdua < 0 or perdua > 100:
    print("La pèrdua de paquets ha d'estar entre el 0 % i el 100 %.")
elif latencia <= 30 and perdua <= 1:
    print("La connexió és excel·lent.")
elif latencia <= 80 and perdua <= 3:
    print("La connexió és bona.")
elif latencia <= 150 and perdua <= 5:
    print("La connexió és acceptable.")
else:
    print("La connexió és deficient.")


# Exercici 11: Cost mensual d'un pla de dades

pla = input("Introdueix el tipus de pla (bàsic o plus): ").strip().lower()
consum = float(input("Introdueix el consum mensual en GB: "))

if consum < 0:
    print("El consum no pot ser negatiu.")
elif pla == "bàsic":
    cost = 10
    if consum > 10:
        cost += (consum - 10) * 1.50
    print(f"El cost total és: {cost:.2f} €")
elif pla == "plus":
    cost = 20
    if consum > 30:
        cost += (consum - 30) * 0.75
    print(f"El cost total és: {cost:.2f} €")
else:
    print("Tipus de pla no vàlid.")


# Exercici 12: Accés a un compte de client

compte_actiu = input("El compte està actiu? (s/n): ").strip().lower()
contrasenya_correcta = input("La contrasenya és correcta? (s/n): ").strip().lower()

if compte_actiu != "s":
    print("Accés denegat: el compte està desactivat.")
elif contrasenya_correcta != "s":
    print("Accés denegat: la contrasenya és incorrecta.")
else:
    codi_correcte = input("El codi de doble verificació és correcte? (s/n): ").strip().lower()
    if codi_correcte == "s":
        print("Accés permès.")
    else:
        print("Accés denegat: el codi de doble verificació és incorrecte.")


# Exercici 13: Diagnòstic d'un router

router_encès = input("El router està encès? (s/n): ").strip().lower()

if router_encès != "s":
    print("Cal encendre el router.")
else:
    los_encès = input("L'indicador LOS està encès? (s/n): ").strip().lower()
    internet_encès = input("L'indicador d'Internet està encès? (s/n): ").strip().lower()

    if los_encès == "s":
        print("Cal revisar el cable de fibra.")
    elif internet_encès != "s":
        print("Cal contactar amb el proveïdor.")
    else:
        print("La connexió funciona correctament.")


# Exercici 14: Prioritat d'una incidència de xarxa

servei_critic = input("La incidència afecta un servei crític? (s/n): ").strip().lower()
usuaris = int(input("Quants usuaris estan afectats? "))

if usuaris < 0:
    print("El nombre d'usuaris no pot ser negatiu.")
else:
    alternativa = input("Hi ha una alternativa de connexió? (s/n): ").strip().lower()

    if (servei_critic == "s" and alternativa != "s") or (usuaris >= 50 and alternativa != "s"):
        print("Prioritat crítica.")
    elif usuaris >= 10 or servei_critic == "s":
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")