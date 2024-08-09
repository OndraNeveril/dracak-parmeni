from random import randint

#Šmajdalf chlastá místo piva okenu, proměnná pivo tedy bude mít v tomto modulu lokální název okena, globálně se ale jedná stále o pivo

print("------------Načítám balíček Smajdalf----------------")

def Smajdalf1(síla, inteligence, obrana, životy, peníze, okena, tráva, magie, pratele):
    print('Trapnou písničku si zpívám,\nzpívám si trapnou písničku\ntrapnou písničku zpívám\ntu si zpívám já\no jednom malém čaroději, který jede se svým malým koňem na svém malém voze, jede za malým hobitem. A ten malý hobit se ho na něco zeptá... teď!')
    print('Hra byla uložena. Pokud chceš opustit hru, napiš Exit, jinak zadej cokoli jiného')

    return síla, inteligence, obrana, životy, peníze, okena, tráva,magie, pratele
def Smajdalf2(síla, inteligence, obrana, životy, peníze, okena, tráva,magie, pratele):
    print('Lála je nejlepší!')
    print('Hra byla uložena. Pokud chceš opustit hru, napiš Exit, jinak zadej cokoli jiného')

    return síla, inteligence, obrana, životy, peníze, okena, tráva,magie, pratele
def Smajdalf3(síla, inteligence, obrana, životy, peníze, okena, tráva,magie, pratele):
    print('Já nemám čas!!!')
    print('KONEC')
    print('...')
    print('síla: ', síla)
    print('inteligence: ', inteligence )
    print('peníze: ', peníze)
    print('Zbylo ti ', životy, ' životů')
    print('Až na pařbu s tebou došli:')
    return síla, inteligence, obrana, životy, peníze, okena, tráva,magie, pratele