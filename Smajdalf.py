from random import randint

# Šmajdalf chlastá místo piva okenu, proměnná pivo tedy bude mít v tomto modulu lokální název okena, globálně se ale jedná stále o pivo

print("------------Načítám balíček Smajdalf----------------")

def boj(vyjimka, síla, obrana, životy, magie, utok_nepritele, obrana_nepritele, zivoty_nepritele, moralka_nepritele):

    aktualni_zivoty_nepritele = zivoty_nepritele

    while True:

        aktualni_zivoty_nepritele = aktualni_zivoty_nepritele - síla + obrana_nepritele

        if magie > 0:
            if input('Chceš jako bonus k útoku použít bojové kouzlo? Za útok kouzlem je bonusové zranění rovno dvojnásobku tvé inteligence.') == 'ano':
                aktualni_zivoty_nepritele = aktualni_zivoty_nepritele - 2 * inteligence
                magie -= 1

        if aktualni_zivoty_nepritele <= 0:
            print("nepřítel je mrtvý")
            break

        elif aktualni_zivoty_nepritele / zivoty_nepritele <= moralka_nepritele:
            print("nepřítel utekl, vyhrál jsi")
            break

        else:
            životy = životy - utok_nepritele + obrana

            if životy <= 0 and vyjimka == False:
                while True:
                    print("Jsi mrtvý. Konec hry")
            if životy <= 0 and vyjimka == True:
                input()
                for i in range(10000000):
                    print('Jsi mrtvý, konec hry?')
                break
    if vyjimka == False:
        print("zbylo ti ", životy, 'životů')
    return vyjimka, síla, obrana, životy, magie

def Smajdalf1(síla, inteligence, obrana, životy, peníze, okena, tráva, magie, pratele):
    rozhodnuti = input('Jedeš za Bimbem a Fritolem, co budeš cestou dělat?\na) Zpívat si trapnou písničku\nb) budu se soustredit na kouzla\nc) zapálím si čmoudovou trávu (životy + 5, síla - 1)\n')
    if rozhodnuti == 'c':
        print('Tráva - 1\nživoty + 5\nsíla - 1')
        tráva -= 1
        životy += 5
        síla -= 1
    elif rozhodnuti == 'b':
        print('Doplnil sis sloty kouzel\nmagie + 1')
        magie += 1
    elif rozhodnuti == 'a':
        print('Trapnou písničku si zpívám,\nzpívám si trapnou písničku,\ntrapnou písničku zpívám,\ntu si zpívám já.\nO jednom malém čaroději který jede se svým malým koňem na svém malém voze, jede za jedním hobitem. A ten hobit se ho na něco zeptá... teď!')
        print('Síla + 1\ninteligence + 1')
        síla += 1
        inteligence += 1
    print('Potkal jsi Fritola')

    print('Kde se flákáš Šmajdalfe?')
    if input('a) Omlouvám se, už to nikdy neudělám\nb) Magič se nikdy nefláká, Fritole Šourku, A jestli se to někomu nelíbí, ať mi klobouk políbí\n') == 'b':
        print('obrana + 1\ninteligence + 1')
        obrana += 1
        inteligence += 1
    else:
        print('síla - 1')
        síla -= 1
    print('Fritol se začal smát')

    if input('Měl jsi mi aspoň poslat esemesku.\na) Chtěl jsem, ale ti hajzli mi zase zablokovali simku.\nb) Však sis to ani nezasloužil ty cype\n') == 'b':
        print('síla + 1')
        síla += 1
    else:
        print('síla - 1')
        síla -= 1

    if input('Bude v nejbližší době nějaká pařba? Vyprávěj mi o všem\na) No, brzy bude jedna velká pařba v Naadoru, potřebuješ tam vstupenku, ale tu ti seženu na černém trhu\nb) O všem? Si děláš prdel, ne?\n') == 'a':
        print('inteligence + 1')
        inteligence += 1
    else:
        print('inteligence - 1')
        inteligence -= 1

    input('a) Jak se má to tlustý prase, slyšel jsem, že pořádá nějakou pařbu?\n')
    print('No víš, jak znáš Bimba, nejspíš z toho udělá nelegální technopárty. Něco chystá.')
    if input('a) Nepovídej...\nb) Jo, má plán, chystá se na pořádný vodvaz, chtěl by zjistit, co to je Matrix\n') == 'a':
        print('Dobrá, nech si svá tajemeství.')
    else:
        print('Ten hajzl mi o tom vůbec neřekl!')

    print('Šmajďáku, kde jsi koupil ten vohoz a špičatý klobouk?')
    skopano = False
    if input('a) Tak to by tě zajímalo?\nb) To víš, sleduji nejnovější trendy. Třeba trencle adidas mi vydržely už 2000 let a to jsem je ani jednou nevyměnil, prostě fakt doporučuji.\n') == 'b':
        print('Teda to jsem nevěděl, že jsi takové prase.')
    if input('a) Nech toho prosím\nb) Mlč, nebo tě skopu\n') == 'b':
        print('Skopal jsi Fritola')
        skopano = True
        print('síla + 1')
        síla += 1
    else:
        print('síla - 1')
        síla -= 1
    if not skopano:
        if input('Běží za vámi děcka a volají "Šmajdalfe, Šmajdalfe, udělej trik se špičatým kloboukem!\na) udělám trik se špičatým kloboukem\nb) Parchanti jedni usoplení!\n') == 'a':
            print('Udělal jsi trik se špičatým kloboukem.')
            magie -= 1
        print('Tak se tedy uvidíme na té pařbě, tě péro!\nFritol odešel.')
    else:
        print('Fritol se na tebe naštval a odešel.')
        if input('Běží za vámi děcka a volají "Šmajdalfe, Šmajdalfe, udělej trik se špičatým kloboukem!\na) udělám trik se špičatým kloboukem\nb) Parchanti jedni usoplení!\n') == 'a':
            print('Udělal jsi trik se špičatým kloboukem.')
            magie -= 1

    if input('Dojel jsi k Bimbovi domů. Co uděláš?\na) Zaklepu\nb) Otevři ty starý prase!\n') == 'b':
        print('Jasně, promiň Šmajďáku\nsíla + 1')
        síla += 1
    else:
        if input('Odprejskni!!! Už mám dost všech těch podomních prodejců erotických pomůcek!\na) Ale já žádné erotické pomůcky neprodàvám\nb) A co takhle trik se špičatým kloboukem?\n') == 'b':
            print('Šmajdalf?\ninteligence + 1\nmagie + 1')
            inteligence += 1
            magie += 1
        else:
            input('To je jedno, už mám dost všech těch známých, z každé pařby mi uděla retropárty. Táhni pryč!\n')
            while True:
                print('Prohrál jsi')

    if input('Bimbo ti otevřel dveře. "Hnusný počasí Šmajdalfe, ty jeden pařmene."\na) Tobě taky ty tlustý prase. Vůbec ses nezměnil.\nb) Že já jsem sem jel, ty mi za to nestojíš! Tě péro.\n') != 'a':
        while True:
            print('Odjel jsi pryč, prohràl jsi!')
    slibeno = False
    if input('"Dáš si líh, nebo něco ostřejšího? Mám ještě několik lahví zkvašených slimáků. Opravdu dobrý ročník. Skoro tak chlupatí jako já.Nakládal je ještě můj táta.Jsou velcí asi jako prasopes, dáš si?"\na) Jen okenu, díky.\nb) A trávu bys neměl?\n') == 'b':
        print('To víš že jo, mám sotva pro sebe')
    else:
        slibeno = True
    if input('Jak se těšíš na to mejdlo? Bude to fakt smažba. Fritol sehnal od kamaráda nový repráky. Ilegální velikost. Bude to fakt hukot.\nSlíbils mi ten trik se špičatým kloboukem.\nNic tu nemám všechno sežral Fritol...\nNebo ne? Žáby, žáby... tady někde byly žáby...Usmažím ti pár žab, kdybys...\na) Tak já ti teda předvedu trik se špičatým kloboukem\nb) Jen okenu, díky.\n') == 'a':
        print('Udělal jsi trik se špičatým kloboukem.')
        magie -= 1
    else:
        slibeno = True

    print('Někdo venku valá na Bimba "Bimbo! Bimbo Šourku!"\n"Zařvi na ně vy hajzlové! Už mám po krk všech těch známých Z každé pařby udělají RETRO párty. Já chci metal. Metal, Šmajdalfe. A potom potřebuju najít nějakého překupníka s chlupatými slimáky."')
    if slibeno:
        print('Á, okena\nokena + 1')
        okena += 1
    input('a) Takže chceš uskutečnit svůj plán?\n')
    print('Ano. Všechno je již připraveno. Už jsem všecko zařídil.')
    if input('a) No když myslíš, že to bude fungovat...\nb) Fritol něco vyčmuchal.\n') == 'b':
        print('Nesmysl. Je to blbeček,10 let nepřišel na to,|že mu upíjím alpu.')
        input('a) Řekneš mu to někdy?\n')
        print('Asi jo. Asi by šel se mnou, kdybych mu řekl. Myslím, že by taky rád někdy slyšel techno,hardrock...metal..a tak.')
    print('Jsem starý, Šmajdalfe. Vím, že vypadám na 30, ale už 60 let pobírám důchod. Připadám si jako vyžvýkaná žvýkačka. Nebo jako Dvakrát použitý toaleťák. Potřebuju vodvaz. Pořádně velký vodvaz. A nečekám,že se vrátím. Vlastně... ani nehodlám...')

    if tráva >= 1 and input('Bimbo si zapálil trávu. Přidáš se taky?\na) ano\nb) ne\n') == 'a':
        print('Šmajdalfe, ty jeden vyhulenče, tohle bude památná noc.\ntráva - 1\nsíla - 1\nživoty + 1')
        tráva -= 1
        síla -= 1
        životy += 5

        while True:
            print("Co budeš dělat na párty?\na) půjdu na Bimbův proslov")
            if tráva >= 1:
                print("b) Zkusím čmoudovou trávu -> životy + 5, síla -1")
            if okena >= 1:
                print("c) Zkusím okenu -> životy + 5, inteligence - 1")
            if magie >= 1:
                print("d) půjdu se podívat na Šmajdalfův trik se špičatým kloboukem")
            párty = input()
            if párty == "a":
                inteligence += 1
                print("inteligence + 1")
                break
            elif párty == "b":
                tráva -= 1
                životy += 5
                síla -= 1
            elif párty == "c":
                okena -= 1
                inteligence -= 1
                životy += 5
            elif párty == "d":
                magie -= 1
                print("magie - 1\nUdělal jsi trik se špičatým kloboukem")

    print('Bimbův proslov byl velkolepý\nVítejte na mé 111. technopárty. Za těch 111 let vás mám všechny plné zuby. Začínáte mě pěkně srát! Ani polovinu z vás neznám jménem, ale i tak vás mám všech po krk.Teď vám musím něco předvést. Učil jsem se to fakt dlouho. Nebude to lepší, než trik se špičatým kloboukem, ale dobře ... bude to fakt bžunda ... Tě péro.\nNajednou Bimbo zmizel.')
    if input('Jdeš za Bimbem domů, aby sis s ním promluvil.\na) To bylo opravdu úžasné, krásný trik\nb) Myslíš si, že jsi lepší než já?\n') == 'b':
        print('Dej pokoj, jsi starý, nejsi lepší než já.')

    print('Hra byla uložena. Pokud chceš opustit hru, napiš Exit, jinak zadej cokoli jiného')

    return síla, inteligence, obrana, životy, peníze, okena, tráva, magie, pratele

def Smajdalf2(síla, inteligence, obrana, životy, peníze, okena, tráva, magie, pratele):
    print('Lála je nejlepší!')
    print('Hra byla uložena. Pokud chceš opustit hru, napiš Exit, jinak zadej cokoli jiného')

    return síla, inteligence, obrana, životy, peníze, okena, tráva, magie, pratele

def Smajdalf3(síla, inteligence, obrana, životy, peníze, okena, tráva, magie, pratele):
    print('Já nemám čas!!!')
    print('KONEC')
    print('...')
    print('síla: ', síla)
    print('inteligence: ', inteligence)
    print('peníze: ', peníze)
    print('Zbylo ti ', životy, ' životů')
    print('Až na pařbu s tebou došli:')
    return síla, inteligence, obrana, životy, peníze, okena, tráva, magie, pratele