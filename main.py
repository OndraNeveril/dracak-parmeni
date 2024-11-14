file = open("save.txt")
hra = None
while True:
    hra = input("a) načíst hru\nb) spustit novou hru\nc) ukončit hru\n")
    if (hra == 'a' or hra == 'b' or hra == 'c'):
        break

if hra == 'b':
    postava = input('Vítej v dračím doupěti s tematikou Pár pařmenů. Vyber si postavu:\nFritol - inteligence 10, síla 8, obrana 2, životy 100, peníze 200, vybavení - čmoudová tráva, pivo\nŠmajdalf - inteligence 12, síla 6, obrana 3, životy 150, peníze 50, vybavení - špičatý kloubouk, čmoudová tráva, hůl\nBimbo - inteligence 10, síla 5, obrana 3, životy 100, peníze 500, vybavení - pivo, ringouš, okena, čmoudová tráva\n')
    tah = 1

p = []
for line in file:
    p.append(line.strip())
s = p.pop(0).split(' ')
if hra == "a":
    postava = s[0]
    tah = int(s[1])
    q = [i.split(" ") for i in p]
    síla, inteligence, obrana, životy, peníze, pivo, tráva, magie = 0,0,0,0,0,0,0,0
    pratele = q[-1]
    for j in q:
        if j[0] == "sila":
            síla = int(j[1])

        if j[0] == "inteligence":
            inteligence = int(j[1])

        if j[0] == "obrana":
            obrana = int(j[1])

        if j[0] == "zivoty":
            životy = int(j[1])

        if j[0] == "penize":
            peníze = int(j[1])

        if j[0] == "pivo":
            pivo = int(j[1])

        if j[0] == "trava":
            tráva = int(j[1])

        if j[0] == "magie":
            magie = int(j[1])

if postava == 'Fritol':
    import Fritol
    if tah == 1:
        síla = 8
        inteligence = 10
        obrana = 2
        peníze = 200
        pivo = 1
        tráva = 1
        životy = 100
        pratele = []
        magie = 0

        síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele = Fritol.Fritol1(síla, inteligence, obrana, životy, peníze, pivo, tráva,pratele)
        if input() != 'Exit':
                tah += 1
    if tah == 2:
        síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele = Fritol.Fritol2(síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele)
        if input() != 'Exit':
            tah += 1
    if tah == 3:
        síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele = Fritol.Fritol3(síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele)
    tah += 1

if postava == 'Smajdalf':
    import smajdalf
    if tah == 1:

        síla = 6
        inteligence = 12
        obrana = 3
        peníze = 100
        pivo = 0
        tráva = 1
        životy = 100
        magie = 3
        pratele = []

        síla, inteligence, obrana, životy, peníze, pivo, tráva,magie, pratele = smajdalf.Smajdalf1(síla, inteligence, obrana, životy, peníze, pivo, tráva,magie, pratele)
        if input() != 'Exit':
            tah += 1
    if tah == 2:
        síla, inteligence, obrana, životy, peníze, pivo, tráva,magie, pratele = smajdalf.Smajdalf2(síla, inteligence, obrana, životy, peníze, pivo, tráva,magie, pratele)
        if input() != 'Exit':
            tah += 1
    if tah == 3:
        síla, inteligence, obrana, životy, peníze, pivo, tráva,magie, pratele = smajdalf.Smajdalf3(síla, inteligence, obrana, životy, peníze, pivo, tráva,magie, pratele)
    tah += 1

if postava == 'Bimbo':
    import Bimbo
    if tah == 1:
        Bimbo.Bimbo1()
        if input() != 'Exit':
            tah += 1
    if tah == 2:
        Bimbo.Bimbo2()
        tah += 1
    tah += 1


if tah == 4:
    print('...')
    print('Právě jsi dohrál hru Pár Pařmenů, podle stejnojmenného filmu od Bandy trotlů. Tuto hru naprogramoval Ondřej Nevěřil v letech 2022-2024 ve svém volném čase. Pokud se vám hra líbila, šiřte ji dál.')
    input()
    tah = 1

fileout = open("save.txt", "w")
fileout.write(postava + ' ' + str(tah))

fileout.write('\nsila' + ' ' + str(síla))
fileout.write('\ninteligence' + ' ' + str(inteligence))
fileout.write('\nobrana' + ' ' + str(obrana))
fileout.write('\nzivoty' + ' ' + str(životy))
fileout.write('\npenize' + ' ' + str(peníze))
fileout.write('\npivo' + ' ' + str(pivo))
fileout.write('\ntrava' + ' ' + str(tráva))
fileout.write('\nmagie' + ' ' + str(magie) + "\n")
for i in pratele:
    fileout.write(i + " ")
input('Nyní hru můžete vypnout stisknutím klávesy enter')