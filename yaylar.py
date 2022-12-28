import pygame
import sys
import random 
import time
from pygame.locals import *
 
ekranGenisligi = 800 # Ekran boyutları tanımlanıyor.
ekranYuksekligi = 600
 
FPS = 60 # Saniyede çizdirilecek kare sayısı tanımlanıyor.
 
SIYAH = (0,0,0) # Kullanılacak renkler tanımlanıyor
BEYAZ = (255, 255, 255)
 
pygame.init() # Pygame kütüphanesi başlatılıyor.  
ekran = pygame.display.set_mode((ekranGenisligi, ekranYuksekligi)) # Pencere boyutları ayarlanıyor.
pygame.display.set_caption("PROJE ÖDEVİ") # Pencere başlığı atanıyor.
saat = pygame.time.Clock() # Saat verisi alınıyor.
 
yayFX = pygame.image.load("Spaceship.png").convert() # Yay görseli alınıyor.
kup_10FX =pygame.image.load("küp10.png").convert()


class yay(pygame.sprite.Sprite): # Yay için bir sınıf oluşturuluyor.
    def __init__(self): # Sınıfın ana parametrelerini taşıyacak fonksiyon oluşturuluyor.
        pygame.sprite.Sprite.__init__(self) 
        self.image = yayFX # Karakterin görseli atanıyor.
        self.image.set_colorkey(BEYAZ)  # Görseldeki arkaplan temizleniyor.
        self.rect = self.image.get_rect() # Karakterin haraketi ve çarpışması için bir dikdörtgen oluşturuluyor. 
        self.rect.centerx = ekranGenisligi - 700 # Karakterin başlangıç koordinatları atanıyor.
        self.rect.bottom = ekranYuksekligi - 350
        self.hizx = 0 # Karakterin x ekseninde hareketini sağlayacak hiz değişkeni tanımlanıyor. 
        # self.hizy = 0

class kup_10(pygame.sprite.Sprite): # Küp için bir sınıf oluşturuluyor.
    def __init__(self): # Sınıfın ana parametrelerini taşıyacak fonksiyon oluşturuluyor.
        pygame.sprite.Sprite.__init__(self) 
        self.image = kup_10FX # Karakterin görseli atanıyor.
        self.image.set_colorkey(BEYAZ)  # Görseldeki arkaplan temizleniyor.
        self.rect = self.image.get_rect() # Karakterin haraketi ve çarpışması için bir dikdörtgen oluşturuluyor. 
        self.rect.centerx = ekranGenisligi - 80 # Karakterin başlangıç koordinatları atanıyor.
        self.rect.bottom = ekranYuksekligi - 150
        self.hizx = 0 # Karakterin x ekseninde hareketini sağlayacak hiz değişkeni tanımlanıyor. 
        self.hizy = 0

    def update(self): # Aksiyonların ekrana yansıtılması için güncelleyici fonksiyon çağrılıyor.
        self.hizx = 0 # Hız sıfırlanıyor.
        tusdurumu = pygame.key.get_pressed() # Tuşa basılma olayı bir değişkene çekiliyor.
        if tusdurumu[pygame.K_LEFT]: # Sol ok tuşuna basıldı ise,
            self.hizx = -6 # Hız verisine gereken değer atanıyor. 
        if tusdurumu[pygame.K_RIGHT]:
            self.hizx = 6


    def update(self):
        self.hizy = 0
        tusdurumu = pygame.key.get_pressed()
        if tusdurumu[pygame.K_UP]:
            self.hizy = 8
        if tusdurumu [pygame.K_DOWN]:
            self.hizy = -8


    
        self.rect.x += self.hizx # Karaktere hız verisi ekleniyor.
        if ekranGenisligi < self.rect.right : # Karakterin pencere içinde kalması sağlanıyor.
            self.rect.right = ekranGenisligi
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.y += self.hizy
        if ekranYuksekligi < self.rect.down :
            self.rect.down = ekranYuksekligi
        if self.rect.up < 0 :
            self.rect.up = 0


oyunBitti = True
oyun = True
 
while oyun: # Ana oyun döngüsü oluşturuluyor.
 
    if oyunBitti: # Oyun bitmiş ise,
        tumkarakterler = pygame.sprite.Group() # Karakterler ekrana çizdirmek için "sprite.Group()" olarak tanımlanıyor.
        yay = yay()
        kup_10 = kup_10()
        tumkarakterler.add(yay)
        tumkarakterler.add(kup_10)
             
        oyunBitti = False # Değişken resetleniyor.
 
    for event in pygame.event.get(): # Olaylar denetleniyor.
 
        if event.type == pygame.QUIT: # Oyundan Çıkma isteği gelirse,
            oyun = False # Oyun ekranından çıkılıyor.
 
    saat.tick(FPS) # Saniyede 60 kare çizdiriliyor.
    tumkarakterler.update() # Bütün karakterler güncelleniyor.
     
    ekran.fill(BEYAZ) # Arkaplan siyaha boyanıyor.
    tumkarakterler.draw(ekran) # Bütün karakterler render edilip ekrana çizdiriliyor.
    pygame.display.flip() # Ekran güncelleniyor.