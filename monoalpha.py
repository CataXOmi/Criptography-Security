from string import *

def invert_dict(dict):
    inverse_dict = {}
    for key, value in dict.items():
        inverse_dict[value] = key
    return inverse_dict

def encrypt(mesaj, dict):
    mesaj_criptat = ''
    for letter in mesaj:
        mesaj_criptat += dict[letter.upper()]
    return mesaj_criptat

def decrypt(mesaj, dict):
    return encrypt(mesaj, invert_dict(dict))

mono_alpha = dict()

poz = []
for i in range(26):
    poz.append(0)

print(poz)

litera = str(input("Dati litera din dictionar:"))
while litera not in ascii_letters or len(litera) != 1:
    litera = str(input("Dati litera din dictionar:"))

while len(mono_alpha) < 26:
    for idx in range(26):

        if len(mono_alpha) == 26:
            break

        if bool(mono_alpha) == False:
            mono_alpha[chr(ord('A') + idx)] = litera.upper()
            poz[idx] = 1
            litera = str(input("Dati litera din dictionar:"))
            while litera == '':
                litera = str(input("Dati litera din dictionar:"))

        else:
            if litera.upper() not in mono_alpha.values():
                if poz[idx] == 0:
                    mono_alpha[chr(ord('A') + idx)] = litera.upper()
                    poz[idx] = 1
                    litera = str(input("Dati litera din dictionar:"))
                    while litera not in ascii_letters or len(litera) != 1:
                        litera = str(input("Dati litera din dictionar:"))
                else:
                    continue

            else:
                litera = str(input("Dati o alta litera care nu este deja in dictionar:"))
                while litera not in ascii_letters or len(litera) != 1:
                    litera = str(input("Dati o alta litera care nu este deja in dictionar:"))

print(mono_alpha)
mono_alpha_sort = {}
for i in sorted(mono_alpha.keys()):
    mono_alpha_sort[i] = mono_alpha[i]
print(len(mono_alpha_sort), mono_alpha_sort)

text_clar = str(input("Dati textul clar fara caractere speciale si cifre:\n"))
print("Textul criptat este:\n")
print(encrypt(text_clar.replace(' ', ''), mono_alpha_sort))

text_criptat = str(input("Dati textul criptat fara caractere speciale si cifre:\n"))
print("Textul clar este:\n")
print(decrypt(text_criptat.replace(' ', ''), mono_alpha_sort))