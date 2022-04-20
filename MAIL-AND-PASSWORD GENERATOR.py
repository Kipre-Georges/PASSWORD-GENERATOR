import random
from re import U

alphabet = "abcdefghijklmnopqrstuvwxyz"
majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffre  = "123456789"
special  = "@[]^-!#$£%&()*+,-./:;{}<>=~?"
ensemble = alphabet + chiffre + special + majuscule

lenght = int(input("Definissez la longueur de votre mot de passe : "))
mdp_gen = []

for i in range(lenght) : 
    mdp_gen.append(random.choice(ensemble))
  
for i in range (10) : 
    print("")

print(" ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ ")
print("||M |||A |||I |||L |||       |||G |||E |||N |||E |||R |||A |||T |||O |||R ||")
print("||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__||")
print("|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|")
print("")
print("Votre mot de passe est : ","".join(mdp_gen))  
