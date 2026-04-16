"exercice 1"

a = 1
b = "FRANCE"
c = 36.2

print(a, b, c)
print(type(a))
print(type(b))
print(type(c))


# exercice 2

ch = "salut"
ch = "ca va"
print(ch)

# exercice 3
x = str(3)
y = str(8.5)
print(type(x))
print(type(y))

# exercice 4
poids = int(input("Quel est votre poids en kg ? "))
print(f"Le poids de l'utilisateur est {poids} kg")

# exercice 5
var = "bonjour"

if type(var) == str:
    print("c'est une chaine de caracter")

elif type(var) == int:
    print("c'est un entier")

# exercice 6
d = int(5)

if d >= 0:
    print("positiv")
else:
    print("negativ")

# exercice 7
age = int(input("Quel age avez vous ?"))

if age >= 18:
    print("L'utilisateur est majeur")
else:
    print("L'utilisateur est mineur")

# exercice 8
for i in range(1, 21):
    print(i)


compteur = 1
while compteur <= 20:
    print(compteur)
    compteur += 1

# exercice 9
for i in range(10, 21):
    if i % 2 == 0:
        print(i)

compteur = 10
while compteur <= 20:
    if compteur % 2 == 0:
        print(compteur)
    compteur += 1

# exercice 10
L = [i for i in range(1, 11)]
print(L)

# exercice 11
L = [i for i in range(1, 11) if i % 2 == 0]
print(L)
# exercice 12
L = [6, 8, 3, 4, 1, 12, 2, 9.2]
L.sort()
print(L)

# exercice 13
L = [3, 2, 2, 1, 4, 3, 5, 1, 2]
L.count(2)  # Compte le nombre de fois que 2 apparaît dans la liste
L.count(3)  # Compte le nombre de fois que 3 apparaît dans la liste
print(L.count(2))
print(L.count(3))
