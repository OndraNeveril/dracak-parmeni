from random import randint

print("------------Načítám balíček Fritol----------------")

def boj(vyjimka, síla, obrana, životy, utok_nepritele, obrana_nepritele, zivoty_nepritele, moralka_nepritele):
    aktualni_zivoty_nepritele = zivoty_nepritele
    while True:
        aktualni_zivoty_nepritele = aktualni_zivoty_nepritele - síla + obrana_nepritele
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
    return vyjimka, síla, obrana, životy
def Fritol1(síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele):
    vyjimka = False

    prvni_rozhodnuti = input("V dálce vidíš přijíždět Šmajdalfa. Co mu řekneš na uvítanou?\na) Rád tě vidím Šmajdalfe\nb) Kde se flákáš Šmajdalfe!\n")
    if prvni_rozhodnuti == "a":

       print("Já tebe ne. Nebo možná trochu jo, ale nech té sentimentality")

       if input("Jak se má to tlustý prase?\na) Bimbo chystá fakt hustou párty. Sezval už polovinu Krajíce. Ale jak znáš Bimba, udělá z toho ilegální technopárty\nb) Je fakt na šrot, něco chystá\n") == "a":
           print("Tak to už se těším.\nsíla + 1")
           síla = síla + 1
           if input("Co mu odpovíš?\na) Uvidíme se na té pařbě\nb) Šmajdalfe, kde jsi koupil ten skvělý vohoz a špičatý kolobouk\n") == "b":
               print("To víš, sleduju nejnovější módní trendy. Třeba trencle Adidas mi vydržely už 2000 let a to jsem je ani jednou nevyměnil\ninteligence + 1")
               inteligence = inteligence + 1
               if input("Co odpovíš?\na) Teda, to jsem nevěděl, že jsi takové prase\nb) Tak se uvidíme na té pařbe\n") == "a":
                   print("Mlč, nebo tě skopu\nŠmajdalf tě skopal, životy - 5")
                   životy = životy - 5
               print("Tě péro")

       else:
           print('Nepovídej\ninteligence + 1')
           inteligence = inteligence + 1
           if input("Co mu odpovíš?\na) Uvidíme se na té pařbě\nb) Šmajdalfe, kde jsi koupil ten skvělý vohoz a špičatý kolobouk\n") == "b":
               print("To víš, sleduju nejnovější módní trendy. Třeba trencle Adidas mi vydržely už 2000 let a to jsem je ani jednou nevyměnil\ninteligence + 1")
               inteligence = inteligence + 1
               if input("Co odpovíš?\na) Teda, to jsem nevěděl, že jsi takové prase\nb) Tak se uvidíme na té pařbe\n") == "a":
                   print("Mlč, nebo tě skopu\nŠmajdalf tě skopal, životy - 5")
                   životy = životy - 5
               print("Tě péro")

    elif prvni_rozhodnuti == "b":
       print("Magič se nikdy nefláká Fritole Šourku. Jestli se to někomu nelíbí, ať mi klobouk políbí\ninteligence + 1")
       inteligence = inteligence + 1
       if input("A co ty, slyšel jsem, že jsi pořádný pařmen\na) Bude v nejbližší době nějaká pařba? Vyprávěj mi o všem\nb) Bimbo chystá fakt hustou párty. Sezval už polovinu Krajíce. Ale jak znáš Bimba, udělá z toho ilegální technopárty\n" ) == "b":
           print("Tak to už se těším.\nsíla + 1")
           síla = síla + 1
           if input("Co mu odpovíš?\na) Uvidíme se na té pařbě\nb) Šmajdalfe, kde jsi koupil ten skvělý vohoz a špičatý kolobouk\n") == "b":
               print("To víš, sleduju nejnovější módní trendy. Třeba trencle Adidas mi vydržely už 2000 let a to jsem je ani jednou nevyměnil\ninteligence + 1")
               inteligence = inteligence + 1
               if input("Co odpovíš?\na) Teda, to jsem nevěděl, že jsi takové prase\nb) Tak se uvidíme na té pařbe\n") == "a":
                   print("Mlč, nebo tě skopu\nŠmajdalf tě skopal, životy - 5")
                   životy = životy - 5
               print("Tě péro")

       else:
           print('O všem? Si děláš prdel, ne. Snad jen vybrané akce. Brzy bude velká pařba v Naadoru. Potřebuješ vstupenku, ale tu ti seženu na černým trhu.\ninteligence + 1')
           inteligence += 1
           if input("Jak se má to tlustý prase?\na) Bimbo chystá fakt hustou párty. Sezval už polovinu Krajíce. Ale jak znáš Bimba, udělá z toho ilegální technopárty\nb) Je fakt na šrot, něco chystá\n") == "a":
               print("Tak to už se těším.\nsíla + 1")
               síla = síla + 1
               if input("Co mu odpovíš?\na) Uvidíme se na té pařbě\nb) Šmajdalfe, kde jsi koupil ten skvělý vohoz a špičatý kolobouk\n") == "b":
                   print("To víš, sleduju nejnovější módní trendy. Třeba trencle Adidas mi vydržely už 2000 let a to jsem je ani jednou nevyměnil\ninteligence + 1")
                   inteligence = inteligence + 1
                   if input("Co odpovíš?\na) Teda, to jsem nevěděl, že jsi takové prase\nb) Tak se uvidíme na té pařbe\n") == "a":
                       print("Mlč, nebo tě skopu\nŠmajdalf tě skopal, životy - 5")
                       životy = životy - 5
                   print("Tě péro")
           else:
               print('Nepovídej\ninteligence + 1')
               inteligence = inteligence + 1
               if input("Co mu odpovíš?\na) Uvidíme se na té pařbě\nb) Šmajdalfe, kde jsi koupil ten skvělý vohoz a špičatý kolobouk\n") == "b":
                   print("To víš, sleduju nejnovější módní trendy. Třeba trencle Adidas mi vydržely už 2000 let a to jsem je ani jednou nevyměnil\ninteligence + 1")
                   inteligence = inteligence + 1
                   if input("Co odpovíš?\na) Teda, to jsem nevěděl, že jsi takové prase\nb) Tak se uvidíme na té pařbe\n") == "a":
                       print("Mlč, nebo tě skopu\nŠmajdalf tě skopal, životy - 5")
                       životy = životy - 5
                   print("Tě péro")

    print("Bimova technopárty byla úžasná. Všichni pili pivo, líh a hulili čmoudovou trávu. Nakonec si Bimbo připravil proslov")

    while True:
       print("Co budeš dělat na párty?\na) půjdu na Bimbův proslov")
       if tráva >= 1:
           print("b) Zkusím čmoudovou trávu -> životy + 5, síla -1")
       if pivo >= 1:
           print("c) Zkusím pivo -> životy + 5, inteligence - 1")
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
           pivo -= 1
           inteligence -= 1
           životy += 5
       elif párty == "d":
           print("Šel jsi se podívat na trik se špičatým kloboukem. Bylo to opravdové umění, ne ty moderní sračky jako picaso. Plelmír Bramborák a Pervitin Dal ale odpálili obří rachejtli, která letí Bimbovým směrem. Musíš ho varovat!")
           if inteligence >= 10:
               print("a) strhnout Bimba k zemi")
           else:
               print("k odemknutí možnosti a) potřebuješ vyšší inteligenci")
           print("b) Podívěj Bimbo, obří netopýr")

           if input() == "a":
               print("podařilo se ti Bimba včas zachránit\nobrana + 1")
               obrana += 1
           else:
               print("Bimbo se včas sklonil a rachejtle ho minula, ale stihl ti vynadat\nJseš úplnej výmaz, nebo nepoznáš motýla?\ninteligence - 1")
               inteligence -= 1
           print("poté jsi šel na Bimbův proslov")
           break

    print('Bimbův proslov byl velkolepý\nVítejte na mé 111. technopárty. Za těch 111 let vás mám všechny plné zuby. Začínáte mě pěkně srát! Ani polovinu z vás neznám jménem, ale i tak vás mám všech po krk.')
    print('Na párty sis ještě nějaký čas užíval a když jsi večer přišel domů, Bimbo byl pryč. Na podlaze ležel jeho prsten a na křesle seděl Šmajdalf')

    prstenoverozhodnuti = input('Na co se Šmajdalfa zeptáš?\na) Co tu děláš Šmajdalfe?\nb) Nemáš jointa? Fakt dlouho jsem němel, mám příšerný absťák\nc) Co se děje?\n')
    if prstenoverozhodnuti == "a":
       print('To tě nemusí zajímat\ninteligence - 1')
       inteligence -= 1
    elif prstenoverozhodnuti == "b":
       print('Šmajdalf ti dal joint\ntráva + 1')
       tráva += 1
    print('Šmajdalf ukáže na prsten a řekne\n"Bimbova hračka. Šel hledat Matrix, blb. Nesežer to."')

    if input("a) Nejsem tak nenažraný, jak myslíš\nb) Co tím myslíš?\n") == "a":
       obrana += 1
       print("obrana + 1")
       print("Tě péro")
    else:
       print("Přesně to, co jsem řekl")
       if input("Co mu odpovíš\na) A co jsi řekl?\nb) Tě péro\n") == "a":
           print('Prosil jsem tě, abys to nesežral\ninteligence - 1\nTě péro')
           inteligence -= 1

    if input("Šmajdalf si na tebe po 17 letech opět vzpomněl a tak přijel.\nBafiky baf, nesežrals to?\na) Jasně, včera\nb) Co to meleš?\n") == "a":
       while True:
           print("Sežral jsi rongouše, nemáš vstupenku, prohrál jsi")
    else:
       print("obrana + 1")
       obrana += 1
    print('Šmajdalf natáhne ruku a řekne:"ruku Fritole, červené kolečko na dlani je cool". Podáš mu prsten, on ho hodí do ohně. Zeptáš se ho, jestli je zhulený, ale on se tě zeptá, co vidíš')
    print("co mu odpovíš:\na) hovno, hovno tu je\nb) Také klikyháky")
    if inteligence >= 12:
       print("c) taková básnička")
    else:
       print("Pro odemknutí možnosti c) nemáš dostatečnou inteligenci")

    rozhodnuti = input()

    if rozhodnuti == "a":
       print("Šmajdalfovi se tvá odpověď nelíbila\ninteligence - 1")
    elif rozhodnuti == "c":
       print("ty umíš číst? To mě překvapilo\ninteligence + 1")

    print('Je to nějaká ´hatlamatilka a je to hrozně naškrábaný. "To máš recht. Je to taková veselá básnička, ale číst ti ji nebudu."')

    if input("a) prosím Šmajdalfe\nb) dělej ty líný hovado\n") == "b":
       print("síla + 1\nŠmajdalf tě skopal, životy - 5")

    print('"Tak tedy dobrá:\nJeden Ringouš velí všeckym\nDevět lidí sváže\nNa pařbu je přivede\nDo temné garáže. Baf!"')
    print('"To je volňas na tu pařbu pro devět lidí"')

    if input("a) Šmajdalfe, udělej si copek\nb) Šmajdalfe, pojď se mnou\n") == "b":
       if randint(1,4) == 4:
           print("jasně Fritole")
           pratele.append('Šmajdalf')
       else:
           print("Promiň kámo, musím za Smradupánem, je chytrý, zná všechny texty.")

    else:
       print("Ne kámo, zkoušel jsem to. 300 let jsem to nemohl rozplést. Zlomil jsem si na tom troje hrábě. To dokáže bolet, víš")
   
    if 'Šmajdalf' in pratele:
       print('Fritole, jdem na pařbu. Vezmem to přes Kůrku, zastavíme se v Pajzlu U Šílené krávy')
    else:
       print('Firtole, je čas vyrazit na pařbu. Potkáme se po cestě. Počkej na mě v Kůrce v pajzlu U Šílené krávy.')
   
    print('Nevystupuj pod jménem Šourek. Bimbo při své poslasní cestě fakt řádil')

    if input('a) Nevěřím, že se Bimbo mohl takhle zřídit\nb) Dobře Šmajdalfe\n') == 'b':
       síla -= 1
       print('síla - 1')
    else:
       print('inteligence - 1')
       inteligence -= 1

    print('Můj milý chobote, ty ho ale vůbec neznáš. Za jeden týden vypil sto tupláků piva a pak všude pobíhal jako radioaktivní rybička.')
   
    print("V tom za oknem uslyšíš zvuk. Je to Slimsněd Chrupavka a chce jít s tebou na pařbu. Prý slyšel veselou básničku, ale neví, co jeto garáž. Co mu na to řekneš?\na) pojď se mnou\nb) tebe nechci")

    if inteligence >= 14:
       print("c) nepůjdeš se mnou, ale koupím ti vstupenku na jinou pařbu")
    else:
       print('Pro odemknutí možnosti c) nemáš dost velkou inteligenci')

    rozhodnuti = input()

    if rozhodnuti == 'a':
       print('Slim jde s tebou')
       pratele.append('Slim')

    if rozhodnuti == 'c':
       print('Zaplatíš Slimovi vstupenku na jinou párty\npeníze - 50')
       peníze -= 50
   
    if rozhodnuti == 'b':
       if randint(1,2) == 1:
           print('Slim se na tebe naštval a zaútočil na tebe')
           vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 5, 5, 75, 0.5)
       else: print('Slim se na tebe nastval a odešel')

    print('Vyrážíš na pařbu')

    if 'Šmajdalf' not in pratele and 'Slim' not in pratele:
       print('Postupně procházíš Krajícem až narazíš na Plíška s Pepinem.\na) Vezmeš je s sebou\nb) Nevezmeš je s sebou')
       if input() == 'a':
           pratele.append('Plíšek')
           pratele.append('Pepin')
           print('Plíšek i Pepin jdou s tebou')
           síla += 1
           print('síla + 1')
       else:
           print('Oba zklamaně odcházejí')
           inteligence += 1
           print('inteligence + 1')

    if 'Šmajdalf' in pratele and 'Slim' in pratele:
       print('spolu s Šmajdalfem a Slimem postupně procházíte Krajícem až narazíte na Plí=ška s Pepinem. Slim ti radí, abys je vzal s sebou, Šmajdalf, abys je nebral. Koho poslechneš?\na) Slima\nb) Šmajdalfa')
       if input() == 'a':
           pratele.append('Plíšek')
           pratele.append('Pepin')
           print('Plíšek i Pepin jdou s tebou')
           síla += 1
           print('síla + 1')
       else:
           print('Oba zklamaně odcházejí')
           inteligence += 1
           print('inteligence + 1')

    if 'Šmajdalf' in pratele and 'Slim' not in pratele:
       print('Šmajdalf tě vede Krajícem až narazíte na Plíška s Pepinem. Šmajdalf ti doporučuje je s sebou nebrat. Co uděláš? \na) vezmeš je s sebou\nb) poslechneš Šmajdalfa a nevezmeš je s sebou')
       if input() == 'a':
           pratele.append('Plíšek')
           pratele.append('Pepin')
           print('Plíšek i Pepin jdou s tebou')
           síla += 1
           print('síla + 1')
       else:
           print('Oba zklamaně odcházejí')
           inteligence += 1
           print('inteligence + 1')
       
    if 'Šmajdalf' not in pratele and 'Slim'  in pratele:
       print('Šmajdalf vás kousek doprovodí. Říká: Nesežer ho! Vím, že na něj máš chuť. Kdybys měl hlad, sežer raději Slima. Jez ho po kouscích, ať ti zbytek může nosit bágl.')
       print('Slim říká: Mě se chce na záchod. Nejsou tu někde veřejné záchody?')
       if input('a) Tady jsi ještě pořád v Krajíci. Tady žádné veřejné záchody nejsou\nb) Tak to zkus vydržet\n') == 'a':
           print('inteligence + 1')
           inteligence += 1
       print('Spolu se Slimem postupně procházíte Krajícem až narazíte na Plíška s Pepinem. Slim ti radí, abys je vzal s sebou. Co uděláš?\na) vezmeš je s sebou\nb) nevezmeš je s sebou')
       if input() == 'a':
           pratele.append('Plíšek')
           pratele.append('Pepin')
           print('Plíšek i Pepin jdou s tebou')
           síla += 1
           print('síla + 1')
       else:
           print('Oba zklamaně odcházejí')
           inteligence += 1
           print('inteligence + 1')
       
    print('Po nějaké době dorazíš až na konec pole, za kterým je sráz.')

    if 'Plíšek' in pratele and 'Pepin' in pratele:
       print('Plíšek s Pepinem běží a vrazili do tebe. Všichni jste se skutáleli ze srázu dolů na cestu.\nŽivoty - 10')
       životy -= 10

    else:
       print('pomalu sejdete dolů rovnou na cestu.')
   
    if "Slim" in pratele:
       print('Slim to neudržel a počůral se.')

    print('Najednou v dálce uslyšíš Bigbeat')
    if 'Šmajdalf' in pratele:
       print('Šmajdalf tě varuje, že v dálce je Bigbeaťák. Řekne ti, ať se schováš.')
   
       if len(pratele) >= 3 and randint(1,4) == 1:
           print('protože vaše skupinka je moc velká, nepodařilo se vám všem schovat včas a Bigbeaťák si vi vás všiml')
           schovano = False
       
       else:
           schovano = True
   
    elif inteligence >= 15:
       print('Dojde ti, že je něco špatně. Radši se schováš.')
   
       if len(pratele) >= 3 and randint(1,3) == 1:
           print('protože vaše skupinka je moc velká, nepodařilo se vám všem schovat včas a Bigbeaťák si vi vás všiml')
           schovano = False
       
       else:
           schovano = True
           print('Podařilo se vám schovat se.')
   
    else:
       print('Jen tu tupě sedíš a zíráš')
       if randint(1,6) == 6:
           print('Bigbeaťák si vás přesto nevšiml')
           schovano = True
       
       else:
           schovano = False
       
    if schovano:
       print('Bigbeaťák po nějaké době odjel. Můžete se odplížit a odejít oklikou, ale cesta vám bude trvat o hodně déle. Potom napiš oklika. Nebo můžeš riskovat rychlejší cestu při nebezpečí, že vás Bigbeaťák dožene. Taky by jich mohlo být více. Potom napiš krátká')
       cesta = input()
   
    if schovano == False:
       if randint(1,2) == 1:
             print('Nepodařilo se vám schovat a Bigbeaťák na vás zaútočil')
             vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 5, 3, 150, 0.3)
             cesta = input('Boj jste vyhráli. Bigbeaťák odjel, ale to ještě neznamená, že nepřežil a taky jich může být víc. Chceš jít kratší, ale nebezpečnější cestou, nebo delší, ale pomalejší cestou? Napiš krátká, nebo oklika.\n')
         
       else:
           cesta = input('Nevšiml si  vás.\nBigbeaťákovi jste utekli. Můžete se odplížit a odejít oklikou, ale cesta vám bude trvat o hodně déle. Potom napiš oklika. Nebo můžeš riskovat rychlejší cestu při nebezpečí, že vás Bigbeaťák dožene. Taky by jich mohlo být více. Potom napiš krátká\n')
     
    if cesta == 'oklika':
       for i in range(100000000):
           print('dlouha cesta trva moc dlouho')
       
    else:
       if randint(1,3) == 1 or síla + inteligence >= 25:
           print('bigbeaťák si vás nevšiml')
       elif 'Slim' in pratele:
           print("Bigbeaťák si vás všiml, protože něco, nebo někoho cítil.")
           vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 5, 3, 100, 0.2)
       else:
           print('Bigbeaťák si vás všiml')
           vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 5, 3, 100, 0.2)
       
    print('Došli jste do kůrky')

    if input('Co řekneš vrátnému?\na) Hnusný počasí. Nemáš jointa?\nb) Dobrý den. Pusťte nás prosím dovnitř\n') == 'a':
       tráva += 1
       print('tráva + 1')
    if 'Slim' in pratele and 'Plíšek' in pratele and 'Pepin' in pratele:
       if input('Pajzlové. Čtyři pajzlové a ještě k tomu bez vousů.\na) A jeden člověk bez mozku. Nekecej a otvírej.\nb) My jsme choboti, ne pajzlové.\n') == 'b':
           print('intrligence + 1')
           inteligence += 1
       else:
           síla += 1
           print('síla + 1')
    print('Nebijte mě, ó velectěný. Prý tu obcházejí čtyři pajzlové bez vousů. Kdybyste je vidělo, dejte mi vědět. Opatrnosti není nikdy nazbyt.')

    if input('kam půjdeš?\na) hospoda U Skákavého poníka\nb) pajzl U Šílené krávy\n') == 'b':
      print('Přišel jsi správně.\ninteligence + 1')
      inteligence += 1
    else:
      for i in range(1,500000):
          print('Jdeš do špatné hospody, trvá ti, než ti dojde, že jsi špatně a jdeš k Šílené krávě')
     
     
    print('Došel jsi do pajzlu U Šílené krávy. ')

    print('Hra byla uložena. Pokud chceš opustit hru, napiš Exit, jinak zadej cokoli jiného')

    return síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele
def Fritol2(síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele):
    vyjimka = False
    print('Došel jsi do pajzlu U Šílené krávy. ')
    if input ('Teda pánové, takovéhle ksichty jsem tu ještě neviděl. Nabízíme služby všeho druhu pane?\na) Fritol Šourek\nb) Bond. James Bond\n') == 'b':
       if input('a) Dám si pivo. Protřepat, nemíchat\nb) Dám si kofolu\n') == 'a':
           if input('Bylo ti už osmnáct, smrade?\na) ano\nb) ještě ne\n') == 'a':
               print('Nemáš u sebe nějaké doklady? Jsme slušný pajzl, nechceme mít problémy')


    print('Slyšíš, jak k tobě promlouvá čip')

    o = True
    a = 0

    while o:
       if input('Pivo\n') == 'pivo':
           a += 1
       else:
           o = False
       
       if a == 4:
           pivo += 1
           print('Pivo + 1')
           o = False
       
    if a >= 1 and 'Plíšek' in pratele and 'Pepin' in pratele:
       print('Plíšek se vykecává s ostatními hosty. Tak pivo? Tamtomu ho nechtěli načepovat. Prý mu ještě nebylo osmnáct. Poldové mu ani nedovolí sedět vpředu na koni')
       if input('Jak zareaguješ?\na) Se slovy ty blboune zaútočíš na Pepina\nb) Budeš to ignorovat\n') == 'a':
           print('Strčíš do Pepina. Uklouzneš ale a prsten ti sklouzne na ruku. Vidíš upoutávku na pařbu v nádoru. Slyšte, slyšte! Už brzy bude velká pařba v nádoru. Sežeň dalších o lidí a vyraž přímo za nosem. Potom si zase jdeš objednat.')

    print('Za nocleh zaplatíš 25 za každého člena tvé skupinky.')
    print(pratele)
    p = len(pratele) * 25 + 25

    peníze -= p

    print(' Utratil jsi', p, 'Zbylo ti', peníze)
    print('máš', tráva, 'trávy a ', pivo,'piva')

    if peníze >= 20:
       print('Zbyly ti ještě nějaké peníze, můžeš si koupit pivo nebo trávu, každé stojí 50')
   
       while True:
       
           if peníze >= 20:
   
               nákup = input('Co si koupíš?\na) pivo\nb) trávu\nc) nic\n')
   
               if nákup == 'a':
                   print('Pivo + 1\nPeníze - 20')
                   pivo += 1
                   peníze -= 20
       
               elif nákup == 'b':
                   print('Tráva + 1\nPeníze - 20')
                   tráva += 1
                   peníze -= 20
       
               elif nákup == 'c' or peníze <= 19:
                    break
               
           else: break
               
    print('máš', tráva, 'trávy a ', pivo,'piva a ', peníze, 'peněz')


    while True:
   
       if 'Šmajdalf' in pratele:
           print('Co budeš dělat v hospodě?\na) Zeptám se Šmajdalfa, co je zač ten maňas v koutě, který mě pozoruje')
       else:
           print("Co budeš dělat v hospodě?\na) Zeptám se hospodského, co je zač ten maňas v koutě, který mě pozoruje")

       if tráva >= 1:

           print("b) Zkusím čmoudovou trávu -> životy + 5, síla -1")

       if pivo >= 1:

           print("c) Zkusím pivo -> životy + 5, inteligence - 1")

       párty = input()

       if párty == "a":

           break

       elif párty == "b":

           tráva -= 1

           životy += 5

           síla -= 1

       elif párty == "c":

           pivo -= 1

           inteligence -= 1

           životy += 5
    if 'Šmajdalf'  in pratele:
       print('To je Chodník, Paragon, velký pařmen. Pojď se k němu připojit, stejně nás ještě není devět')
   
    else:
   
       print('Dědku, co je zač ten maňas v koutě. Vypadá jako hobitofil. Hostinský odpovídá. Je od celníků. Tady mu říkáme Chodník. Prý hledá nějakého agenta 007')

       print('Chodník za tebou přijde a řekne Čauky hošku, já jsem velký hodný hobitofil\na) půjdeš s ním dobrovolně nahoru do jeho pokoje\nb) řekneš mu ať táhne pryč')
   
       if input() == 'b':
           print('Odtáhne pryč, ale řekne ti, že to byla chyba')
           print()
   
           print('V noci na vaši hospodu zaútočí vyhulové. Ty ani nikdo z tvých přátel to nečekal. Najsou si váš pokoj, zabijí vás ve spánku a seberou ti vstupenku.')
   
           input()
   
           while True:
               print('Zatímco jsi mrtvý, Vyhulové si užívají na party')
       
       print('Protože toto je slušná hra, nebude zde uvedeno, k čemu všemu došlo mezi chobotem a hobitofilem, když byli sami a nikdo je neviděl')
   
       if input('a) Kdo jsme?\nb) Já se tě nebojím\n') == 'b':
           print('Ale já tebe jo. Máš velký a ostrý zoubky. Jsem sice tvrďák, umím zhasnout svíčku holýma rukaama, ale zuby mám menší.')
           síla += 1
           print('síla + 1')
       
       else:
           print('Nevím, a vy?')
           inteligence -= 1
           print('inteligence -1')
   
       if len(pratele) >= 1:
           print('Ostatní choboti přiběhnou a dižadují se, aby tě pustil. On se ale zeptá, jestli se k vám může přidat, protože se vyhulů sám bojí.')
     
    input('V noci na Kůrku zaútočí vyhulové.\na) Co jsou zač?\n')
    print('To jsou vyhulové. Kdysi to byli lidé, dokud nespáchali ten nejhorší zločin. Začali poslouchat bigbeat. Jdou fanaticky za každou příležitostí fakt pořádně si zapařit. Mají doma reprosoustavy, jaké by ti urvaly uši')
    if input('a) To mě teda neznáš.\nb) zůstaneš mlčet\n') == 'a':
       print('Jó, fakt?')
       print('inteligence - 1')
       inteligence -= 1
   
    print('Druhého dne jste vyrazili na cestu.')

    if 'Šmajdalf' in pratele:
       print('Bezpečně jste došli do Rohlenky')
   
    else:
       if len(pratele) >= 1:
           print('Ostatní mu neveří. Co když to ani není chobot?')
           if input('a) Třeba je to Pajzl\nb) Protože to je člověk\n') == 'b':
               print('inteligence + 1')
               inteligence += 1
           
           else:
               inteligence -= 1
               print('inteligence - 1')
           
       print('Pánové, co takhle skupinové foto')
       if input('a) A máš vůbec foťák\nb) jasně\n') == 'a':
           inteligence += 1
           print('inteligence + 1')
       else:
           print('udělali jste si skupinové foto.')
       
       print('Došli jste ke kopci, na kterém stojí rozpadlá stavba. \nTady jsem kdysi byl býval bydlívával. \nPodá vám nože\nsíla + 1\nJe to na maso. Nesežerte to. Jdu pařit')
       síla += 1
   
       if 'Slim' in pratele or 'Plíšek' in pratele or 'Pepin' in pratele:
           if input('Mezitím co je Paragon pryč, ostatní si udělají malé opékání.\na) připojím se k ostatním\nb) Vy jste blbouni.\n') == 'a':
               print('Užil sis piknik')
               print('Druhéhi dne jste opět vyšli na cestu. Po nějakém čase jste došli do Rohlenky.')
           else:
               print('Začneš kopat do ohně. Ten je ale moc teplý, asi jako Márty, a začne tě pálit. Začneš křičet "Au, to pálí. Jau, jau, jau!" tak hlasitě, že tě slyšeli nedaleko kempující vyhulové a rozhodli se, že chtějí pařit a pokusí se ti vzít vstupenku.')
               vyjimka = True
               for i in range(5):
                   vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 10, 5, 150, 0.1)
               vyjimka = False
               print()
               print('Matrix je všude')
               životy = 50
               print()
           
               if input('a) Kde to jsem\nb) Co se stalo?\n') == 'b':
                   print('Zaútočili na vás vyhulové. Chtěli získat vstupenku na pařbu. Propíchli tě mečem. Chodník tě nemohl ami dorazit ani uzdravit, tak čekal, až umřeš, aby tě mohli sníst, protože ostatní už měli hlad. Pak se tam ale objevila Karmen s turbokoněm a dovezla tě do Rohlenky. Mají tu výborné kuchaře. Ty jsi to ale všechno zkazil, protože jsi se vzbudil.\ninteligemce + 2')
                   inteligence += 2
               else:
                   print('Jsi přece v Matrixu. Je právě tolik, kolik je. Datum není důležité, čas taky ne.\ninteligence + 1')
                   inteligence += 1
                   rozhodnuti = input('a) Nedůležité?\nb)Co to meleš? Táhme z tebe hélium.\nc)budeš mlčet\n')
                   if rozhodnuti == 'b':
                       print('Řádili jsme. Nechal jsem se unést.')
                   elif rozhodnuti != 'c':
                       rozhodnuti = input('A co je tedy důležité?\na) To bych teda taky rád věděl\nb) Co to meleš? Táhne z tebe hélium\nc) budeš mlčet\n')
                       if rozhodnuti == 'b':
                           print('Řádili jsme. Nechal jsem se unést.')
                       elif rozhodnuti != 'c':
                           rozhodnuti = input('Řeknu ti to takhle. Ví už Slim, co je to garáž? To vlastně taky není důležité.\ninteligence - 1\na) Co to meleš? Táhne z tebe hélium\nb) budeš mlčet\n')
                           inteligence -= 1
                           if rozhodnuti != 'c':
                               print('Řádili jsme. Nechal jsem se unést.')
       else:
           print('Druhého dne jste opět vyšli na cestu. Po nějakém čase jste došli do Rohlenky.')

    rozhodnuti = input('V Rohlence jsi potkal Bimba\na) Dědo!\nb) Bimbo!\nc) Kde se flákáš?\n')
    if rozhodnuti == 'a':
       if input('A ktetej seš ty?\n') == 'Fritol':
           print('Á, Fritol...\ninteligence + 1')
           inteligence += 1
    elif rozhodnuti == 'c':
       print('To máš říct Šmajdalfovi, ne mě. Cítím chybu v Matrixu. Zřejmě byl změněn, a s ním i scénář.\ninteligence - 1')
       inteligence -= 1
    print('Bimbo ti ukáže knihu, kterou napsal. Vaříme s konopím, kuchařka chobota Bimba Šourka. "Tam ti mají takové plantáže a oni vymysleku tolik způsobů, jak ho dělat k kuřatům, divočákům, hodným nekromantům a dokonce i k mořským plodům."')
    if input('a) Jů, omalovánka\nb) Hezká kniha\n') == 'a':
       print('Rád jsem omalovával, když jsi dělal mapy. Když jsem se pal v patnácti rozhodoval, co dál dělat, barvičky pro mě byla jasná volba. A pak jsem začal pařit.')
       síla += 1
       print('síla + 1')
       if 'Slim' in pratele:
           print('Slim už si balí na cestu. "A ještě voskovky pro Friťáka...Máma na mě doma čeká s večeří. Už měsíc. Z kůrky jsem jí psal e-mail, ale psala mi, že večeře již stydne.')
           if input('a) Tak teda jdi domů\nb) Půjdeme domů, nejdřív ale půjdeme pařit\n') != 'b':
               print('Tak já jdu domů!')
               pratele.remove('Slim')
           
    while True:
           
        print("Co budeš dělat v Rohlence?\na) Půjdu na schůzi pro odvykání závidlosti na drsné hudbě")
        if tráva >= 1:
           print('b) Zkusím čmoudovou trávu -> životy + 5, síla -1')
        if pivo >= 1:

           print("c) Zkusím pivo -> životy + 5, inteligence - 1")

        párty = input()

        if párty == "a":

            break

        elif párty == "b":

           tráva -= 1

           životy += 5

           síla -= 1

        elif párty == "c":

           pivo -= 1

           inteligence -= 1

           životy += 5

    if 'Slim' in pratele and 'Plíšek' in pratele and 'Pepin' in pratele:
        pratele.clear()
        pratele.append('Slim')
        pratele.append('Pepin')
        pratele.append('Plíšek')
    elif 'Slim' in pratele:
        pratele.clear()
        pratele.append('Slim')
    elif 'Plíšek' in pratele and 'Pepin' in pratele:
        pratele.clear()
        pratele.append('Pepin')
        pratele.append('Plíšek')
    else:
        pratele.clear()
    print('Hra byla uložena. Pokud chceš opustit hru, napiš Exit, jinak zadej cokoli jiného')

    return síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele

def Fritol3(síla, inteligence, obrana, životy, peníze, pivo, tráva, pratele):
    vyjimka = False
    print('Vítejte na dvanácté jubilejní schůzi pro odvykání závislosti na drsné hudbě.')
    rozhodnuti = input('Fritole, dej sem to rádio.\na) Jistě Elbonde\nb) Je moje a jen moje\nc) Jaké rádio, to je prsten\n')
    if rozhodnuti == 'b':
       síla += 1
       print('síla + 1\nPo delším přemlouvání nakonec rádio vydáš')
    elif rozhodnuti == 'c':
       print('inteligence + 1\nTo je jedno, dej mi ho.')
       inteligence += 1
    print('Předložíš rádio. "Toto je vstupenka na pařbu v Nádoru pro devět lidí. Tento multifunkční tentonons dává devíti z vás jedinečnou příležitostzúčadtnit se největší pařby století."')
    print('"V Naadoru už jsem párkrát pařil. Měli tam takhle velký a dobrý jednohubky. Bylo na nich úplné všecko. Marinovaná vředí očička, vrlcí chlupaťoučcí slimáci. Určitě půjdu."')
    print('"Když půjdeš ty, tak já taky". "Kdo nevstane do tří sekund, tomu na místě ukousnu hlavu!" "Mně nikdo hlavu kousat nebude, protože mám moc hezké vousy". Spustí se hádka')
    rozhodnuti = input('a) Běžte si na pařbu sami. Já si chci nechat svou hlavu\nb) Já půjdu. Ale bojím se vás\nc) To radši prodám vstupenku Bigbeaťákům\n')
    if rozhodnuti == 'c':
       while True:
           print('Prodal jsi vtupenku Bigbeaťákům. Peníze +100.\nNešel jsi na pařbu a ostatní si užívali bez tebe.')
    elif rozhodnuti == 'a':
       while True:
           print('Nešel jsi  na pařbu a ostatní si užívali bez tebe')
    else:
       print('Ostatní se na tebe otočí')
    if input('Šmajdalf říká: "Jsem rád, že mě vezmeš s sebou. Nebo snad ne?"\na) Jistě\nb) Nevezmu tě\n') == 'a':
       pratele.append('Šmajdalf')
   
    if input('Paragon říká: "Doufám, že půjsu taky, protože mám fakt sexy hlas. Vezmeš si mě?"\na) Jistě má lásko\nb) Vrať se k celníkům hobitofile.\n') == 'a':       pratele.append('Paragon')
   
    if input('Legoland říká: "Chcete mně?"\na) Ne!\nb) Jasně, pojď.\n') == 'b':
       pratele.append('Legoland')
    if 'Paragon' in pratele:
       if input('Krimli říká: "Půjdu za svědka"\na) dobře\nb) Tebe nechci\n') == 'a':
           pratele.append('Krimli')
    else:
       if input('Krimli říká: "Já chci jít taky"\na) Jasně, pojď\b) ne, děkuji\n') == 'a':
           pratele.append('Krimli')
       
    if input('Bobromil chce jít taky\na) Ne, ten ne\nb) Ať jde\n') == 'b':
       pratele.append('Bobromil')
       print('Teď už nám chybí jenom kuchař, debil a věštec.')
    if 'Slim' in pratele:
       print('Já umím celkem slušně vařit.\nA taky celkem slušně smrdíš. Poznal jsem to, protože všem veverkám pukly hlavy.')
    if 'Plíšek' in pratele and 'Pepin' in pratele:
       print('Mimochodem, já jsem tak trochu věštec. Neříkal tady někdo něco o slimácích?\nA já jsem tak trichu debil. Trošku, maličko, fakt!\noni si všimli, Pepine')
   
    print('Zajdeš za Bimbem. Podává ti nůž: "Můj dtarý nůž na sýr, párátko. Je to kvalitní americká práce od Vietnamců')
    if input('a) Je tupý jak řiť\nb) Dobrý!\n') == 'b':
       print('síla + 1')
       síla += 1
    else:
       print('inteligence + 1')
       inteligence += 1
    print('A ještě tu mám jednu srandu. Kostým! Z hvězdných válek, šitý na Jodu.')
    if len(pratele) <= 7 and inteligence >= 15:
       if input('Chceš přemluvit Bimba, aby šel s tebou?\na) Jasně\nb) Radši ne\n') == 'a':
           print('Bimbo jde s tebou')
           pratele.append('Bimbo')
    if len(pratele) <= 7 and inteligence >= 20:
       if input('Chceš přemluvit Elbonda, ať jde s tebou?\na) Tak jo\nb) Radši ne\n') == 'a':
           if randint(1,5) == 5:
               print('Elbond jde s tebou')
               pratele.append('Elbond')
           
    print('Z Rohlenky jste vyrazili na pařbu')

    if 'Bobromil' in pratele:
       print('Dneska vám došel toaleťák. Ulovili jste veverky a pak vám z nich Bobromil na svém štítu upekl kuře')
    else:
       print('Dneska vám došel toaleťák. Ulovili jste ale veverky.')
   
    print('Najednou nad vámi proletěly divné věci')
    if len(pratele) >= 1:
       print('Veverky se mstí!')
    if síla + inteligence + obrana >= 30:
       print('Podařilo se vám schovat se')
    else:
       print('Veverky vás napadly\nživoty - 10')
       životy -= 10

    if životy <= 0:
        while True:
            input()
            print('Jsi mrtvý')
   
    if 'Krimli' in pratele:
       print('Krimli navrhuje, že můžete zajít na fotbal')
    print('Pokračujete na pařbu, až dojdete do hor.')
    if "Legoland" in pratele or "Šmajdal" in pratele or "Paragon" in pratele or "Bobromil" in pratele or 'Krimli' in pratele:
       print('"Stouni mají zase turné. Jabadabadů!"')
       print('a) pokračujem na pařbu\nb) zajdem na stouny')
       if "Krimli" in pratele:
           print('c) Zajdem na fotbal')
       rozhodnuti = input()
       if rozhodnuti == 'c':
           aktivita = 'fotbal'
       elif rozhodnuti == 'b':
           aktivita = 'stouni'
       else:
           aktivita = 'pařba'
    else:
       aktivita = 'pařba'
    if aktivita == 'pařba':
       print('Jdete rovnou na pařbu, až dojdete do lesa')
    elif aktivita == 'stouni':
       print('Na koncertu stounů jste si pořádně užili.')
       print("I can't get no satisfaction")
       print("I can't get no satisfaction")
       print("'Cause I try, and I try, and I try, and I try")
       print("I can't get no, I can't get no")
       print('...')
       print('Potom jdete na pařbu, dokud nedojdete do lesa')

    elif aktivita == 'fotbal':
       if "Šmajdalf" in pratele:
           print('Stadion otevřen každou sobotu a neděli, denně od pondělí do úterý.\nA to tady jako máme čekat do víkendu?\nNo tak hele, zkusím zatlačit a třeba to půjde\nHle, již Šmajdalf tlečí vléže, nedá pokoj až tam vleze. Šmajdalf ještě venku je, a tak stále brejkuje. Klika cvakla, dvéře letí, Šmajdalf vchází do dveří.')
           if input('a) Tak to prostě rozflákej\nb) A co takhle "Baong"\n') == 'b':
               print('Píšou tady: Řekněte "Baong"" a vstupte. Šmajdalfe, řekni "Baong"\ninteligence + 1')
               inteligence += 1
           else:
               print('A o co se tu asi celou dobu snažím?\nsíla +  1\ninteligence - 1')
               síla += 1
               inteligence -= 1
           
           print('Konečně jste se dostali dovnitř.')
           print('Krimli říká: Už se těším na pořádně našlapaný mač. Velkej kotel a hodně vlajek. Všude maso a hodně krve. Už to ale vypadá, že jsme přišli pozdě. Náš tým asi prohrál zápas. To ale nevadí, nevadí, soupeři tu pořád ještě budou.')
       
           print('Jdete skrz stadion po tmě')
           if input('a) Nemá tady někdo baterku?\n'):
               print('Mám tady jen tohle světýlko o svítivosti asi tři a půl chcíplé světlušky.')
           
           if input('Kdesi ve tmě uvidíš divného tvora\na) Opičky žijí v podzemí?\nb) Šmajdalfe, tamhle někdo je\n') == 'b':
               print('To je chlup\nsíla + 1')
               síla += 1
           else:
               print('A co sis myslel? Víš vůbec co žerou?')
               if input('a) Snad ne choboty\nb) Nemám páru. Jsem pod parou\n') == 'a':
                   print('inteligence - 1')
                   inteligence -= 1
               else:
                   print('Okusují chobotí prsty\n inteligence - 2')
                   inteligence -= 2
               print('Tenhle je speciální případ.')
           print('Má oči větší než mozek, a proto musí chodit po čtyřech, aby nepřepadl. Narodil se v rodině chudých arabských šejků. Rodiče ho v mládí zavrhli. Nechali ho uprostřed ropných polí. Ujali se ho lední medvědi. Ukázalo se, že medvědi byli rasisti. Úplně ho celého vyvrhli. Jeho to naštěstí vůbec nepoznamenalo. Vytvořil síť fastfoodů nabízejících McMedvěd burger. Když mu došly zásoby medvědů, zbankrotoval.')
           if input('a) Můžu si ho nechat? \nb) Chudáček opička\n') == 'a':
                   if inteligence + síla >= 30 and len(pratele) <= 7:
                       print('No tak teda jo, no')
                       pratele.append("Chlup")
                   else:
                       print('To by asi nešlo. Dodneška ti musím zavazovat tkaničky sám. Vždyť ti chcípnul kaktus, protože jsi ho málo krmil. Nechtěl jsem ti to připomínat, protože vím, jak jsi ho měl rád. Neboj, naklonuju ti nový.')
           print('S opičkou si nedělej starosti, neboť jsem celou dobu jenom hloupě a bezmyšlenkovitě kecal. Kecal!\nUž jsi dokecal?\nNe , nedokecal. Už mě pouze přestalo bavit lhát vám do očí.')
   
           print('Pokračujete dál, dokud nenarazíte na pajzlí sbírku telegrafních sloupů 20. století. Pokračujete dál do zadní místnosti, kde naleznete něčí hrob.\nZde leží Dablin, kouč pajzlí stojednadvacítky. Je knokout, budou další.\nŠmajdalf nalezl nějaký deník, ve kterém se psalo o tom, jak tento tým prohrál zapas.')
           if "Plíšek"in pratele and "Pepin" in pratele:
               print('Pepin se opřel o kostru a omylem ji shodil do studny\nTos zeslonil! To je jako zkonil, ale milionkrát víc.')
           
           print('Do místnosti najrdnou vtrhlo mnoho skřetů a jeden obr. Spustí se boj a obr zaútočí přímo na tebe')
           vyjimka = True
           vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 25, 5, 300, 0.3)
           print('Podle scénáře máš být už dávno mrtvý. Tohle přežívaní si pro příště odpustíš.')
           print('Pokračujete, až dojdete k můstku, cestou vás začne pronásledovat rothodčí, bramborg.')
           print('Šmajdalf s ním začal bojovat a používal svoje nejmocnější kouzla\nNemám čas!\nTahne ti z kotle\nTeď na tebe sešlu těžkou válečnou světlušku verze 2.8.1 s upgradem\nJá nemám čas!!!')
           print('Nakonec Bramborg spadne z mostu dolů, ale Šmajdalfe stáhne s sebou dolů. Smajdalf vám ještě stihne říct "Trochu se proletím".')
       else:
           print('Došli jste až ke vstupu na stadion, ale nepoeařilo se vám dostat dovnitř.')
       print('')
       print('Pokračujete na pařbu, dokud nedojdete do lesa')
    else:
       print('Toš ty jsi fakt debil')
   
    if "Krimli" in pratele:
       print('Krimli říká: "Zase jsi mi šlápl na fousy, úchyle. Nech si je narůst taky a pak se můžem bavit jako fousatý s fousatým. Chtějí mi ukrást fousy"\nUslyšíš divný hlas: "Pro fousaté tu není místo. Fousy šíří lepru, smrad a pajzly."\nKrimli pokračuje: "A co ze všeho nejvíc nesnáším je, když mi nafintění blonďáci míří šípem na fousy."')
   
    print('Já jsem Bábin Úd. Bohatým beru, na chudý seru.')

    if "Krimli" in pratele:
       print('Držte mě, nebo se neudržím. Neudržel jsem to!')
       print('Myslíte, že si nadělal do trenek, nebo do slipů? Pojďme to zjistit.')
   
    print('Došli jste do lesa plného Zwelfů.\nNěco tady smrdí. Že bych to byl já? Ne, já to být nemohu, včera jsme se myli, že drahá.\nAno, myli. Naštestí je tady Ariel pro všechny. Skočte si do naší společné pračky, zapíná se přesně v osm hodin\nA potom zbav se těch smraďochů, Fríťo voňavý.')

    while True:
           
        print("Co budeš dělat v lese?\na) Půjdu do společné pračky")
        if tráva >= 1:
           print('b) Zkusím čmoudovou trávu -> životy + 5, síla -1')
        if pivo >= 1:
            print("c) Zkusím pivo -> životy + 5, inteligence - 1")
        print('d) Půjdu spát')

        párty = input()

        if párty == 'a':
            print('Vykoupal jsi se v pračce\nživoty + 10')
            životy += 10
            if input('Půjdeš za Ariel?\na) Ne díky\nb) Tak jo\n') == 'b':
                print('Čus Fríťo. Od Šmajdalfa jsem se naučila pár kouzelnických triků. Naliju vodu do lavoru. Simsala bim, ž svi la pisin. Dokážu si s tebou povídat, i když vůbec nehýbám pusou. Je to takový specialní filmový trik. Nejdřív se to namluví a pak se tam pustí obraz, na kterém mlčím. Ještě něco umím. S mými vlasi si hraje vítr, jsem úplně šílená. Tenhle trik mi jde lépe než Šmajdalfovi, víc mi při něm svítí oči.')
                if input('a) Pro dnešek už stačilo\nb) Pak vím, co mám udělat, ale mám strach\n') != 'a':
                    print('Takový malý piďižvýk jako jsi ty nemůže mít velký strach\nsíla - 1\ninteligence - 1')
                    síla -= 1
                    inteligence -= 1
            break
       
        if párty == 'd':
            print('Vykoupal jsi se v pračce\nživoty + 10')
            životy += 10
            break

        elif párty == "b":
           tráva -= 1
           životy += 5
           síla -= 1

        elif párty == "c":
           pivo -= 1
           inteligence -= 1
           životy += 5

    print('A tady máš žárovku. Bohužel nefunguje.')

    if input('Plujete po řece, až uvidíte dvě velký sochy\na) Hele fašisti. Ale jsou tupí, hajlují špatnou rukou.\nb) To jsou ale hezké sochy\n') == 'a':
       print('inteligence + 1')
       inteligence += 1
    else:
       print('Fritole, to jsou fašisti. Ale jsou tupí, hajlují špatnou rukou')
   
    print('Dopluli jste na břeh')
    problem = False

    if input('a) Uděláme piknik!\nb) Půjdu se radši projít\n') == 'b':
       if "Bobromil" in pratele:
           print('Po nějakém čase jsi narazil na Bobromila.\nFritole, podívej se, to jsou ale hezké klacky. Nechceš si taky nějaký vzít na památku.')
           if input('a) Vezmu si klacek\nb) nevezmu si klacek\n') == 'a':
               print('Síla + 1')
               síla += 1
           else:
               print('Plíšek mi řekl, že brzo umřu. Sbírám si ty klacky na rakev')
               if input('a) Sbírej ty černé, lépe se z nich řežou trámy a černá zeštíhluje\nb) To je mi líto, že umřeš\n') == 'b':
                   print('Vrátil ses z procházky.')
               else:
                   problem = True
       else:
           print('Užil sis procházku.')
       
    else:
       print('Mohli bychom pozvat vředy. Kempujou na druhým břehu. A kdyby jich přišlo moc, tak je sníme')
       if input('a) Jasně, dobrý nápad\nb) Když vředa, tak jen s bagetou a žabými stehýnky\n') == 'b':
           print('Já sním všechno')
           print('Udělali jste si piknik. Snědli jste vředy a udělalo se ti špatně\nŽivoty - 10')
           životy -= 10
       else:
           print('Udělali jste si piknik. Přišli vředi a všechno snědli. Máš hlad.')

    if problem:

       if input('To jako že jsem tlustej? To odvoláš!\na) Jsi děsnej špekoun\nb) Ne, nejsi tlustý\n') == 'b':
           print('Tak to máš štěstí.')
           print('Vrátil ses z ptocházky')
           problem = False

       else:

           print('Tak to odvoláš! Ale nejdřív z tebe vymlátím tvoubduši a ty peníze, co mi dlužíš za nastřelení těch modrých očí.')

           if input('a) Nasaď si ringouše, uteč!\nb) Nikdy se nevzdávej, bojuj až do konce. Banzai!\n') == 'b':
               vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 15, 10,5, 0)
               print('Bobromil ti dal pokoj')

           else:
               print('Nasadil sis ringouše a utekl Bobromilovi.')
           print('Potkal jsi Paragona, řekl ti čéče')

           if input('a) Neříkej mi čéče, zní to úchylně\nb) Čau\n') == 'a':
               print('inteligence + 1')
               inteligence += 1
               print('Úchyl? Já přece nejsem úchyl.')
               if input('a) Já bych řekl, že možná trochu jo. Máš dvě oči\nb) Já si jen dělal legraci\n') == 'a':
                   print('síla + 1')
                   síla += 1
               else:
                   print('No proto')
           print('Přiběhli sem vředi a zaútočili na vás.')

           if input('a) Uteč\nb) Boj!\n') == 'b':
               vyjimka, síla, obrana, životy = boj(vyjimka, síla, obrana, životy, 100, 10, 10000, 0.001)
           print('Podařilo se ti utéct.')
       
    if problem:
       print('Utíkáš pryč od vředů k řece.')
       if "Plíšek" in pratele and "Pepin" in pratele:
           if input('Potkal jsi Plíška s Pepinem a říkají ti, ať jdeš za nimi, že mají jídlo\na) Ne, nemám čas, jdu pryč\nb) Rychle, vemte jídlo s sebou, spěcháme\n') == 'b':
               print('Plíšek a Pepin si pospíší s tebou')
           else:
               print('Opustíš Plíška a Pepina')
               pratele.remove("Plíšek")
               pratele.remove("Pepin")
       print('Nasedneš do lodičky.')
       if "Slim" in pratele:
           if input('Potkáš Slima a říká ti ať neutíkáš, že pojede s tebou\na) Odprejskni, plav pryč\nb) Pojď sem má lásko') == 'b':
               print('Slim nasedl do loďky')
           else:
               print('Slim plave pryč')
               pratele.remove("Slim")

    print('Spolu s ostatními jste vyrazili na pařbu\nDošli jste do Nádoru, ukazal jsi vstupenku a pustili vás na pařbu')
    if inteligence >= 20:
       print('Roztavil jsi ringiuše, vydělal sis na hulení\npeníze + 1000')
       peníze += 1000
   
    print('KONEC')
    print('...')
    print('síla: ', síla)
    print('inteligence: ', inteligence )
    print('peníze: ', peníze)
    print('Zbylo ti ', životy, ' životů')
    print('Až na pařbu s tebou došli:')
    if "Slim" in pratele:
       print('Slim')
    if "Plíšek" in pratele and "Pepin" in pratele:
       print('Plíšek')
       print('Pepin')
    if "Šmajdalf" in pratele:
       print('Šmajdalf')
    if "Paragon" in pratele:
       print('Paragon')
    if "Legoland" in pratele:
       print('Legoland')
    if "Krimli" in pratele:
       print('Krimli')
    if "Bobromil" in pratele:
       print('Bobromil')
    if "Bimbo" in pratele:
       print('Bimbo')
    if "Elbond" in pratele:
       print('Elbond')
    if "Chlup" in pratele:
       print('Chlup')

    return 0, 0, 0, 0, 0, 0, 0, []