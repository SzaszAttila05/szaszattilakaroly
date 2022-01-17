import random
evek=("1988""2001""2006""2010""2021""2022")

def kartyageneralo():
    eredetiSzam=0
    lehetosegekB=("Q""W""E""R""T""Z""U""I""O""P""L""K""J""H""G""F""D""S""A""Y""X""C""V""B""N""M")
    lehetosegekS=("1""2""3""4""5""6""7""8""9")
    betu=random.choice(lehetosegekB)
    szam=random.choice(lehetosegekS)
    print(betu)


    

def gyartasievek():
    ev=random.choice(evek)
    print(ev)
    return evek

def pontszam():
    pontszam=100
    if evek == 1988:
        pontszam+50
    if evek == 2001:
        pontszam+50
    if evek ==2006:
        pontszam*2
    if evek==2021:
        pontszam*2
    if evek==2022:
        pontszam+100/0.8



def nevgenerator():
    Vnevek=("Kovács""Molnár""Kiss""Tóth""Nagy""Horváth""Szabó""Papp""Farkas")
    Knevek=("József""Sándor""Katalin""Béla""Bettina""Éva""Benedek""Péter""Erika")


def kiiro():
    for betusor in range(4):
        kartyageneralo()
    return betusor
kiiro()
