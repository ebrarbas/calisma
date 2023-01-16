import pygame, sys
# Pygame'in açılması için gerekli fonksiyonlar açılıyor.


class Player(pygame.sprite.Sprite):
	# Projeyi oluşturmak için class açılmalı ve buna bir isim verilmeli
	def _init_(self, pos_x, pos_y):
		# Oluşturulan class için konum ayarlanır.
		global ters
		super()._init_()
		self.yay_hareketi = False
		# İlk başta hareketin olmamasını sağlar.
		self.yay = []
		
		# Görseller ekleniyor
		self.yay.append(pygame.image.load('-1.5.png'))
		self.yay.append(pygame.image.load('-1.png'))
		self.yay.append(pygame.image.load('-0.5.png'))
		self.yay.append(pygame.image.load('0.png'))
		self.yay.append(pygame.image.load('0.5.png'))
		self.yay.append(pygame.image.load('1.png'))
		self.yay.append(pygame.image.load('1.5.png'))
		self.yay.append(pygame.image.load('2.png'))
		self.yay_durum = 0
		self.image = self.yay[self.yay_durum]  # Görseller image'in içine ekleniyor
		self.rect = self.image.get_rect()  # İmage ekrana aktarılıyor
		self.rect.topleft = [pos_x,pos_y]  # Görsellerin konumu belirleniyor.

	def calıs(self):
		# Hareket başlatıyor.
		self.yay_hareketi = True

	def update(self,speed):
		# 
		if self.yay_hareketi == True:
			self.yay_durum += speed
			self.image = self.yay[int(self.yay_durum)]
			if int(self.yay_durum) == (round(X/10)):
					self.yay_hareketi = False
			

				
class Button():
	# Buton için class oluşturulur.
	def _init_(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		# scale koyulan görselin boyutunu ayarlar.
		self.rect = self.image.get_rect()
		# Görsel image eklenir.
		self.rect.topleft = (x, y)
		# Görselin konumları tanımlanır.
		self.clicked = False

	def draw(self, surface):
		action = False
		#Mouse pozisyonu alınır.
		pos = pygame.mouse.get_pos()

		#Mouse'un üzerinde bulunma ve tıklanma koşullarını kontrol eder.
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				# Mouse'un 1 kere tıklamasını kontrol eder
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			# Mouse'un kontrolünü sonlandırır.
			self.clicked = False

		#Ekranda çizim düğmesi
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action 	

# Genel kurulum
pygame.init()
clock = pygame.time.Clock()

# Oyun ekranı
screen_width = 1000  # Ekran genişliğini ayarlar.
screen_height = 800  # Ekran yüksekliğini ayarlar.
screen = pygame.display.set_mode((screen_width,screen_height))  # Ekran girdilerini açar
pygame.display.set_caption("YAY ANİMASYONU")  # İsim tanımlanır.


# Yay ve grupları oluşturma
moving_yay = pygame.sprite.Group()
player = Player(50,0)
moving_yay.add(player)

# Görsellere isim tanımlama
cetvel = pygame.image.load("cetvel.png")
buton = pygame.image.load("8kg.png")
buton1 = pygame.image.load("6kg.png")
buton2 = pygame.image.load("4kg.png")
buton3 = pygame.image.load("Demir.png")
buton4 = pygame.image.load("Çelik.png")
buton5 = pygame.image.load("Bakır.png")
buton6 = pygame.image.load("button_resume.png")

# Cetvele konum tanımlama
width = cetvel.get_width()
height = cetvel.get_height()
scale = 0.7
cetvel = pygame.transform.scale(cetvel, (int(width * scale), int(height * scale)))
# Butonlara konum ayarlama
tip1 = Button(350,300,buton5,0.8)
tip2 = Button(350,400,buton3,0.8)
tip3 = Button(350,500,buton4,0.8)
kilo1 = Button(500,300,buton,0.8)
kilo2 = Button(500,400,buton1,0.8)
kilo3 = Button(500,500,buton2,0.8)
Basla = Button(400,600,buton6,1)

State = "seçenek"
font = pygame.font.SysFont("Arial", 25)
# Yazı fontu ve büyüklüğünü belirleme
Color = ((0,0,0))
Demir = 2
Bakır = 1.5
Celik = 2.5
İsim = "Demir"
# İlk açıldığında gösterilecek seçenekleri tanımlama
Tip = 2		
kilo = 4
speed = 0.15
def draw_text(text, font, text_col, x, y):
	# Yazının    fontunu, rengini , konumunu tanımlama
  img = font.render(text, True, text_col)
# Yazıyı image aktarma
  screen.blit(img, (x, y))
# İmage'ı ekrana aktarma.
def yay_hesap(K,m):
	# Yay hesaplama fonksiyonu tanımlama ve yazma
	global X
	# Uzama miktarı hesaplama fonksiyonu yazılır.
	# F = K*X  BURDAN DA X = F/K eşitliği bulunur.
	F = m * (9.81)
	X = F/K
	
	print(round(X/10))
	

# Döngü oluşturulur
run = True
while run:
	screen.fill((255, 255, 255))
	# Ekran rengi belirlenir.

	
	
	if State == "seçenek":
		if tip1.draw(screen):
			Tip = Bakır
			İsim = "Bakır"
		if tip2.draw(screen):
			Tip = Demir
			İsim = "Demir"
		if tip3.draw(screen):
			Tip = Celik
			İsim = "Celik"
		if kilo1.draw(screen):
			kilo = 8
		if kilo2.draw(screen):
			kilo = 6
		if kilo3.draw(screen):
			kilo = 4
		if Basla.draw(screen):
			State= "devam"
	if State == "devam":
		screen.blit(cetvel,(500,40))
		# Cetvel ekrana yansıtılır.
		moving_yay.draw(screen)
		# Yay ekrana yansıtılır
		moving_yay.update(speed)
	if State != any:
		draw_text("Kilo: {} KG ".format(kilo), font,Color,40,250)
		# Ekrana kilo bilgileri yazdırılır
		draw_text("Tip: {} ".format(İsim), font,Color,40,300)
		# Ekrana tip bilgileri yazdırılır.

	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.calıs()
			print(kilo)
			print(Tip)
			yay_hesap(Tip,kilo)

			
 
	# Pygame'in kapatılması için belirli kodlar yazılır.	
	pygame.display.flip()
	clock.tick(60)
