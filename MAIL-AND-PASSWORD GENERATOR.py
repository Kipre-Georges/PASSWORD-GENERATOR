import random
from re import U

nom = str(input("Saisissez votre nom :"))
prenom = str(input("Saisissez votre prénom :"))
annee = int(input("saisissez votre année de naissance : "))
reste = "@gmail.com"

LIST_MAIL=[]
LIST_MAIL.append(nom+prenom+str(annee)+reste)



alphabet = "abcdefghijklmnopqrstuvwxyz"
chiffre  = "123456789"
special  = "~#{[[|`\^@]}£¨%µ§/.?@"
ensemble = alphabet + alphabet + alphabet + chiffre + special 




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

print("votre adresse mail est :","".join(LIST_MAIL))
print("Votre mot de passe est : ","".join(mdp_gen))  