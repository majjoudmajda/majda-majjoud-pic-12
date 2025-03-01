while True :
    try:
        x = int(input("Entrer un nombre :"))
        F = 1
        for i in range(1,x+1):
            F = F*i
        print(f"le factoriel de {x} est :{F}")
        break
    except ValueError :
        print("ce n'est pas un nombre valid")
        