import pygame
import sys
import random 
import time
from pygame.locals import *
 
 # Ekran boyutları tanımlanıyor.
ekranGenisligi = 800 
ekranYuksekligi = 600
 
# Saniyede çizdirilecek kare sayısı tanımlanıyor.
FPS = 60 
 
# Kullanılacak renkler tanımlanıyor
SIYAH = (0,0,0)
BEYAZ = (255, 255, 255)
KIRMIZI =(300,300,300)
 
pygame.init() # Pygame kütüphanesi başlatılıyor.  
ekran = pygame.display.set_mode((ekranGenisligi, ekranYuksekligi)) # Pencere boyutları ayarlanıyor.
pygame.display.set_caption("PROJE ÖDEVİ") # Pencere başlığı atanıyor.
saat = pygame.time.Clock() # Saat verisi alınıyor.
 
yayFX = pygame.image.load("yay.png").convert() # Yay görseli alınıyor.
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
    def __init__(self,x,y): # Sınıfın ana parametrelerini taşıyacak fonksiyon oluşturuluyor.
        pygame.sprite.Sprite.__init__(self) 
        self.image = kup_10FX # Karakterin görseli atanıyor.
        self.image.set_colorkey(BEYAZ)  # Görseldeki arkaplan temizleniyor.
        self.rect = self.image.get_rect() # Karakterin haraketi ve çarpışması için bir dikdörtgen oluşturuluyor. 
        self.rect.centerx = ekranGenisligi - 80 # Karakterin başlangıç koordinatları atanıyor.
        self.rect.bottom = ekranYuksekligi - 150
        self.hizx = 0 # Karakterin x ekseninde hareketini sağlayacak hiz değişkeni tanımlanıyor. 
        self.hizy = -7

    def update(self): # Aksiyonların ekrana yansıtılması için güncelleyici fonksiyon çağrılıyor.
        self.hizx = 0 # Hız sıfırlanıyor.
        tusdurumu = pygame.key.get_pressed() # Tuşa basılma olayı bir değişkene çekiliyor.
        if tusdurumu[pygame.K_LEFT]: # Sol ok tuşuna basıldı ise,
            self.hizx = -6 # Hız verisine gereken değer atanıyor. 
        if tusdurumu[pygame.K_RIGHT]:
            self.hizx = 6    
        self.rect.x += self.hizx # Karaktere hız verisi ekleniyor.
        if ekranGenisligi < self.rect.right : # Karakterin pencere içinde kalması sağlanıyor.
            self.rect.right = ekranGenisligi
        if self.rect.left < 0:
            self.rect.left = 0



    # def update(self): # Aksiyonların ekrana yansıtılması için güncelleyici fonksiyon çağrılıyor.
    #     self.hizy = 0 # Hız sıfırlanıyor.
    #     tusdurumu = pygame.key.get_pressed() # Tuşa basılma olayı bir değişkene çekiliyor.
    #     if tusdurumu[pygame.K_UP]: # yukarı ok tuşuna basıldı ise,
    #         self.hizy = -6 # Hız verisine gereken değer atanıyor. 
    #     if tusdurumu[pygame.K_DOWN]:
    #         self.hizy = 6
    #     self.rect.y += self.hizy
    #     # if self.rect.bottom < self.rect.bottom: # Lazer pencere dışına çıktı ise,
    #     #     self.rect.down= ekranYuksekligi
    #     # if self.rect.bottom < 0:
    #     #     self.rect.up = 0
    #     if ekranYuksekligi < self.rect.down:
    #         self.rect.down = ekranYuksekligi
    #     if self.rect.up < 0 :
    #         self.rect.up = 0ö



# FİZİK DENKLEMLERİ
# F= -k*x
# E=1/2*k*x*x
# G arttıkça x artar orantılı bir şekilde G=x  2G=2x
# k değerini değiştirilebilsin
# bir yaya bağlı nesnelerin simülasyonu , kinetik ve potansiyel enerjilerinin hesaplanması

# N=("newton")
# font =pygame.font.Font(None,30)
# text_F =font.render("zaman=%.1f N" % N, 1, (10,10,10))
# test_F_pos =font.render(0,500)
# ekran.blit(text_F  ,text_F_pos)



oyunBitti = True
oyun = True
 
while oyun: # Ana oyun döngüsü oluşturuluyor.
 
    if oyunBitti: # Oyun bitmiş ise,
        tumkarakterler = pygame.sprite.Group() # Karakterler ekrana çizdirmek için "sprite.Group()" olarak tanımlanıyor.
        yay = yay()
        kup_10 = kup_10()
        # screenDawText=screenDawText()
        tumkarakterler.add(yay)
        tumkarakterler.add(kup_10)
        # tumkarakterler.add(screenDawText)
             
        oyunBitti = False # Değişken resetleniyor.
 
    for event in pygame.event.get(): # Olaylar denetleniyor.
 
        if event.type == pygame.QUIT: # Oyundan Çıkma isteği gelirse,
            oyun = False # Oyun ekranından çıkılıyor.

    
    saat.tick(FPS) # Saniyede 60 kare çizdiriliyor.
    tumkarakterler.update() # Bütün karakterler güncelleniyor.
     
    ekran.fill(BEYAZ) # Arkaplan beyaza boyanıyor.
    tumkarakterler.draw(ekran) # Bütün karakterler render edilip ekrana çizdiriliyor.
    pygame.display.flip() # Ekran güncelleniyor.





    # class screenDawText (pygame.sprite.Sprite):
#     def screenDrawText(message,screenX,screenY,punto=12,textColor=SIYAH,textBGColor=SIYAH):
#         font=pygame.font.SysFont("arial",punto)
#         text=font.render(u''+message,True,textColor,textBGColor)
#         textrect= text.get_rect()
#     # textrect.left= ekranGenisligi -50
#     # textrect.top= ekranYuksekligi -80
#         def __init__(self):
#             self.rect = self.image.get_rect()
#             self.rect.centerx = ekranGenisligi - 160 # Karakterin başlangıç koordinatları atanıyor.
#             self.rect.bottom = ekranYuksekligi - 200
#     ekran.blit(text,textrect)
#     ekran.blit(-160,-200)

    # screenDrawText("merhaba",ekranGenisligi - 160,ekranYuksekligi - 200,50)
    # ekran.blit(screenDrawText)




# def screenDrawText(message,screenX,screenY,punto=12,textColor=SIYAH,textBGColor=SIYAH):
#     font=pygame.font.SysFont("arial",punto)
#     text=font.render(u''+message,True,textColor,textBGColor)
#     text=font.render("merhaba",ekranGenisligi - 160,ekranYuksekligi - 200,50)
#     textrect= text.get_rect()
#     textrect.left= ekranGenisligi -50
#     textrect.top= ekranYuksekligi -80
    # def __init__(self):
        # self.rect = self.image.get_rect()
        # self.rect.centerx = ekranGenisligi - 160 # Karakterin başlangıç koordinatları atanıyor.
        # self.rect.bottom = ekranYuksekligi - 200
    # ekran.blit(text,textrect)
    # ekran.blit(screenDrawText,-160,-200)
    # text=font.render("merhaba",- 160,e - 200,50)

    # screenDrawText("merhaba",ekranGenisligi - 160,ekranYuksekligi - 200,50)
    # ekran.blit(screenDrawText)