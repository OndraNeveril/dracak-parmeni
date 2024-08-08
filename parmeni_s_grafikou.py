import pygame
from random import randint

def prekryvaji_se_intervaly(a, c, delka_a=100, delka_c=100):
    return a <= c < a + delka_a or c <= a < c + delka_c

def prekryvaji_se(a, b, c, d, delka_a=100, sirka_b=100, delka_c=100, sirka_d=100):
    return prekryvaji_se_intervaly(a, c, delka_a, delka_c) and prekryvaji_se_intervaly(b, d, sirka_b, sirka_d)

def je_uvnitr(pozice, a, b, c, d):
    x, y = pozice
    return a <= x < a + c and b <= y < b + d

def text(text, x, y):
    obrazovka.blit(pygame.font.SysFont("Calibri", 40, True, False).render(str(text), True, CERNA), (x, y))

def vstup(num, odpovedi):
    pygame.draw.rect(obrazovka, CERVENA, (700, 400, 50, 50))
    text("a", 715, 405)
    pygame.draw.rect(obrazovka, ZELENA, (770, 400, 50, 50))
    text("b", 785, 405)
    if num >= 3:
        pygame.draw.rect(obrazovka, MODRA, (840, 400, 50, 50))
        text("c", 855, 405)
    if num >= 4:
        pygame.draw.rect(obrazovka, ZLUTA, (910, 400, 50, 50))
        text("d", 925, 405)
    if kliknuto and je_uvnitr(kurzor, 700, 400, 50, 50):
        return 1
    elif kliknuto and je_uvnitr(kurzor, 770, 400, 50, 50):
        return 2
    elif num >= 3 and kliknuto and je_uvnitr(kurzor, 840, 400, 50, 50):
        return 3
    elif num >= 4 and kliknuto and je_uvnitr(kurzor, 910, 400, 50, 50):
        return 4

pygame.init()

CERNA = (0, 0, 0)
CERVENA = (255, 0, 0)
MODRA = (0, 0, 255)
ZELENA = (0, 255, 0)
ZLUTA = (255, 255, 0)
BILA = (255, 255, 255)


#fritol = pygame.image.load("images\Fritol.jpg")
#slim = pygame.image.load("images\slim.jpg")
#plisek_a_pepin = pygame.image.load("images\plisek_a_pepin.jpg")
#paragon = pygame.image.load("images\paragon.jpg")
#smajdalf = pygame.image.load("images\smajdalf.jpg")
#bimbo = pygame.image.load("images\Bimbo.jpg")
#legoland = pygame.image.load("images\legoland.jpg")
#krimli = pygame.image.load("images\krimli.jpg")
#bobromil = pygame.image.load("images\Bobromil.jpg")
#elbond = pygame.image.load("images\elbond.jpg")

odpoved = None

hodiny = pygame.time.Clock()
obrazovka = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Pár pařmenů")
pygame.display.set_icon(fritol)

spusteno = True

while spusteno:
    kliknuto = False
    kurzor = pygame.mouse.get_pos()
    for udalost in pygame.event.get(): # Projdi vsechny udalosti
        if udalost.type == pygame.QUIT: # Pokud se mas vypnout
            spusteno = False            # vypni se
        if udalost.type == pygame.MOUSEBUTTONDOWN: # Pokud je kliknuto mysi
            kliknuto = True # rekni, ze je kliknuto

    stisk = pygame.key.get_pressed() # Vytvor objekt s informacemi, co je zmacknuto
    if odpoved == None:
        odpoved = vstup(4)
        text(str(odpoved), 800, 300)
    obrazovka.fill(BILA) # Premazni obrazovku cernou barvou
    if stisk[pygame.K_SPACE]:
        #obrazovka.blit(fritol, (100,200))
        pygame.draw.rect(obrazovka, CERNA, (99,199,402,1))
        pygame.draw.rect(obrazovka, CERNA, (99,199,1,402))
        pygame.draw.rect(obrazovka, CERNA, (500,199,1,402))
        pygame.draw.rect(obrazovka, CERNA, (99,600,402,1))

    pygame.draw.rect(obrazovka, CERNA, (0,0,1200,5))
    pygame.draw.rect(obrazovka, CERNA, (0,0,5,700))
    pygame.draw.rect(obrazovka, CERNA, (1195,0,5,1200))
    pygame.draw.rect(obrazovka, CERNA, (0,695,1200,5))

    pygame.display.flip()
    hodiny.tick(10)


pygame.quit()