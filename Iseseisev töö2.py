#Jaanus Paasoja ITT20
#Iseseisev töö 2
#10.02.2021
#Reisijate transport
inimesed=int(input('Kui palju inimesi on vaja transportida? '))
kohad=int(input('Mitu reisijat mahub bussi? '))
bussid=inimesed//kohad
vbuss=inimesed%kohad
if vbuss==0:
    print(f"Transportida on vaja {inimesed} inimest ja ühte bussi mahub {kohad} reisijat. Seega on vaja {bussid} bussi ja viimases bussis sõidab {kohad} reisijat.")
else:    
    print(f"Transportida on vaja {inimesed} inimest ja ühte bussi mahub {kohad} reisijat. Seega on vaja {bussid+1} bussi ja viimases bussis sõidab {vbuss} reisijat.")
#Äratus
yles=int(input("Mitu korda ma sind äratama pean enne kui tööle hiljaks jääd?"))
for i in range(yles):
    print('Tõuse ja sära!')
#Murelikud lapsevanemad
jooks = int(input("Sisesta metsaringide arv: "))
i = 2
summa = 0
while i <= jooks:
 summa += i
 i += 2
print("Lapsed saavad " + str(summa),"porgandit")
#Täringud
from random import randrange
taring=int(input('Mitme täringuga soovid mängida?'))
for i in range(taring):
    suvArv=randrange(1,7) 
    print(suvArv)
#Õunad
import random
ounu=14
kokku=0
summa=0
poisid=int(input('Mitu pöialpoissi tahab õunu? '))
for i in range(poisid):
    valik=random.randrange(1,3)
    print(valik)
    kokku=kokku+valik
summa=ounu-kokku
print('Lumivalgekesele jäi',summa,'õunu')


    
    
