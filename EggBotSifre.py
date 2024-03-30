import random

sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def EggBot(length):
    sonuc = ''
    for i in range(length):
        sonuc += (random.choice(sifre))
    return sonuc