cislo = int(input("uzivateli zadej nejake cislo"))
n1 = int("%s" % cislo)
n2 = int("%s""%s" % (cislo,cislo) )
n3 = int("%s""%s""%s" % (cislo,cislo,cislo))

try: print ("vysledne cislo je:", n1 + n2 + n3)
except: print("nekde je neco blbe")

# ziskana cisla muzu libovolne skladat za sebe, staci kdyz je vypisu pomoci "es-ka" za sebe
# try a except je pro odychtavani vyjimek - kdyz je to ok, spusti se try, kdyz to neni dobre tak se spusti except