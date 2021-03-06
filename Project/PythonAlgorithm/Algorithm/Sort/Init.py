import pygame
from Config import *

pokers = []
Tmp = []

def pokersinit(size):
    if USEC:
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CA.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x0E))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C2.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x02))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C3.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x03))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C4.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x04))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C5.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x05))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C6.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x06))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C7.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x07))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C8.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x08))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_C9.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x09))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CT.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x0A))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CJ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x0B))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CQ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x0C))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_CK.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x0D))
    if USED:
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DA.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x1E))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D2.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x12))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D3.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x13))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D4.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x14))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D5.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x15))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D6.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x16))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D7.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x17))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D8.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x18))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_D9.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x19))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DT.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x1A))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DJ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x1B))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DQ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x1C))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_DK.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x1D))
    if USES:
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SA.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x2E))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S2.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x22))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S3.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x23))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S4.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x24))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S5.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x25))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S6.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x26))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S7.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x27))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S8.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x28))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_S9.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x29))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_ST.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x2A))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SJ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x2B))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SQ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x2C))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_SK.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x2D))
    if USEH:
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HA.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x3E))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H2.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x32))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H3.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x33))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H4.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x34))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H5.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x35))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H6.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x36))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H7.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x37))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H8.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x38))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_H9.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x39))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HT.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x3A))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HJ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x3B))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HQ.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x3C))
        pokers.append((pygame.transform.smoothscale(pygame.image.load('../../PokerImages/card_HK.png').convert_alpha(),(int(size[0]/Resize), int(size[1]/Resize))), 0x3D))
