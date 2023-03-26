import pygame
import random

fereastra_latime = 1000
fereastra_inaltime = 800

pygame.init()
screen = pygame.display.set_mode((fereastra_latime, fereastra_inaltime))
pygame.display.set_caption("Breakout")

blue = (0, 0, 190)
green = (0, 190, 0)
orange = (190, 95, 0)
culoare_platforma = (204,0,204)

#variabilele jocului
linii = 6
coloane = 5
clock = pygame.time.Clock()
fps = 60
miscare = 0
game_active = 1
start_time = 0
scor_final = 0
scor_maxim = 0

try:
    f = open("Proiect_breakout/scor.txt", 'r')
    scor_maxim = int(f.read())
    f.close()
except:
    scor_maxim = 0


class caramizi():
    def __init__(self):
        self.latime = int((fereastra_latime - 20) / coloane)
        self.inaltime = 55

    def creare_zid(self):
        self.caramida = []
        for linie in range(linii):
            caramizi_in_linie = []
            zidul = []
            for coloana in range(coloane):
                caramida_x = self.latime * coloana + 10
                caramida_y = self.inaltime * linie + 10
                if coloana == 4:
                    rect = pygame.Rect(caramida_x, caramida_y, self.latime , self.inaltime - 10)
                else:
                    rect = pygame.Rect(caramida_x, caramida_y, self.latime - 10 , self.inaltime - 10)
                zidul = [rect, linie]
                caramizi_in_linie.append(zidul)
        
            self.caramida.append(caramizi_in_linie)
    
    def afisare_zid(self):
        for linie in self.caramida:
            for coloana in linie:
                if coloana[1] < 2:
                    culoare_caramida = blue
                elif coloana[1] < 4:
                    culoare_caramida = orange
                elif coloana[1] < 6:
                    culoare_caramida = green
            
                pygame.draw.rect(screen, culoare_caramida, coloana[0])



class platform():
    def __init__(self):
        self.latime = int(fereastra_latime / 10)
        self.inaltime = 20
        self.x = int((fereastra_latime / 2) - (self.latime / 2))
        self.y = int(fereastra_inaltime - self.inaltime) - 10
        self.viteza = 10
        self.rect = pygame.Rect(self.x, self.y, self.latime, self.inaltime)
        self.directie = 0
    
    def directie_platforma(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.viteza
            self.directie = -1
            
        elif key[pygame.K_RIGHT] and self.rect.right <= fereastra_latime:
            self.rect.x += self.viteza
            self.directie = 1
            
        
    def afisare_platforma(self):
        pygame.draw.rect(screen, culoare_platforma, self.rect)



class bila():
    def __init__(self, x, y):
        self.diametru_bila = 20
        self.x = x - self.diametru_bila
        self.y = y 
        self.rect = pygame.Rect(self.x, self.y, self.diametru_bila, self.diametru_bila)
        self.viteza_x = random.choice([1,-1]) * random.choice([1, 2, 3, 4])
        self.viteza_y = -1 * random.choice([3, 4, 5, 6])
        

    def miscare_bila(self):
        game_active2 = 2
        stergere = 0
        nr_caramizi_sterse = 0

        self.rect.y += self.viteza_y


        for linie in zid.caramida:
            for coloana in linie:
                if self.rect.colliderect(coloana[0]):
                    impact_sound.play()
                    if (self.rect.top <= coloana[0].bottom) and self.viteza_y < 0: 
                        self.rect.top = coloana[0].bottom + 1
                        self.viteza_y = self.viteza_y * (-1) + 0.5
                        if self.viteza_x > 0:
                            self.viteza_x += 0.5
                        else:
                            self.viteza_x -= 0.5
                        stergere = 1

                    elif (self.rect.bottom >= coloana[0].top)  and self.viteza_y > 0:
                        self.rect.bottom = coloana[0].top - 1
                        self.viteza_y = self.viteza_y * (-1) + 0.5
                        if self.viteza_x > 0:
                            self.viteza_x += 0.5
                        else:
                            self.viteza_x -= 0.5
                        stergere = 1
                    
                    if stergere == 1:
                        coloana[0] = (0,0,0,0)

        self.rect.x += self.viteza_x

        for linie in zid.caramida:
            for coloana in linie:
                if self.rect.colliderect(coloana[0]):        
                    impact_sound.play()
                    if (self.rect.left <= coloana[0].right) and self.viteza_x < 0:  
                        self.rect.left = coloana[0].right + 1
                        self.viteza_x = self.viteza_x * (-1) + 0.5
                        if self.viteza_y > 0:
                            self.viteza_y += 0.5
                        else:
                            self.viteza_y -= 0.5
                        stergere = 1

                    elif (self.rect.right >= coloana[0].left) and self.viteza_x > 0: 
                        self.rect.right = coloana[0].left - 1
                        self.viteza_x = self.viteza_x * (-1) + 0.5
                        if self.viteza_y > 0:
                            self.viteza_y += 0.5
                        else:
                            self.viteza_y -= 0.5
                        stergere = 1


                    if stergere == 1:
                        coloana[0] = (0,0,0,0)

        for linie in zid.caramida:
            for coloana in linie:
                if coloana[0] == (0,0,0,0):
                    nr_caramizi_sterse += 1
                
        if nr_caramizi_sterse == linii * coloane:
            game_active2 = 3

        if self.rect.left <= 0:
            self.rect.left = 0
            self.viteza_x *= -1
        elif self.rect.right >= fereastra_latime:
            self.rect.right = fereastra_latime
            self.viteza_x *= -1
        elif self.rect.bottom >= fereastra_inaltime:
            game_active2 = 0
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.viteza_y *= -1

        if self.rect.colliderect(platforma):
            impact_sound.play()
            if self.rect.bottom >= platforma.rect.top and self.viteza_y > 0:
                self.viteza_y *= -1
                self.viteza_x += platforma.directie
            elif self.rect.right >= platforma.rect.left and self.viteza_x > 0:
                self.viteza_x *= -1
            elif self.rect.left <= platforma.rect.right and self.viteza_x < 0:
                self.viteza_x *= -1

        return game_active2
    
    def afisare_bila(self):
        pygame.draw.circle(screen, (192, 192, 192), (self.rect.x + self.diametru_bila / 2, self.rect.y + self.diametru_bila / 2), self.diametru_bila / 2)


def scor():
    timp = str(int(pygame.time.get_ticks() / 1000) - start_time)
    text_scor_surface = text_font3.render('Score: %s' %timp, True, 'Gray')
    text_scor_dreptunghi = text_scor_surface.get_rect(topleft = (0, 0))
    screen.blit(text_scor_surface, text_scor_dreptunghi)
    return int(timp)

background_sound_game = pygame.mixer.Sound('Proiect_breakout/Sunete/Sunet2.wav')
background_sound_game.play(loops = -1)
background_sound_game.set_volume(0.2)

impact_sound = pygame.mixer.Sound('Proiect_breakout/Sunete/Sunet1.wav')
impact_sound.set_volume(0.2)

text_font = pygame.font.Font('Proiect_breakout/Font/Pixeltype.ttf', 100)
text_font2 = pygame.font.Font('Proiect_breakout/Font/Pixeltype.ttf', 250)
text_font3 = pygame.font.Font('Proiect_breakout/Font/Pixeltype.ttf', 50)
text_font4 = pygame.font.Font('Proiect_breakout/Font/Pixeltype.ttf', 150)

background_surface = pygame.image.load('Proiect_breakout/Imagini/Background4.jpg').convert()
scaled_background = pygame.transform.scale(background_surface, (fereastra_latime, fereastra_inaltime))

background2_surface = pygame.image.load('Proiect_breakout/Imagini/Background9.jpg').convert()
scaled_background2 = pygame.transform.scale(background2_surface, (fereastra_latime, fereastra_inaltime))

background3_surface = pygame.image.load('Proiect_breakout/Imagini/Background12.jpg').convert()
scaled_background3 = pygame.transform.scale(background3_surface, (fereastra_latime, fereastra_inaltime))

background4_surface = pygame.image.load('Proiect_breakout/Imagini/Background3.jpg').convert()
scaled_background4 = pygame.transform.scale(background4_surface, (fereastra_latime, fereastra_inaltime))

text_surface = text_font2.render('Game Over', False, 'Gray')
text_dreptunghi = text_surface.get_rect(center = (500, 200))

text2_surface = text_font.render('Press Space to enter menu', False, 'Gray')
text2_dreptunghi = text2_surface.get_rect(center = (500, 600))

text_joc_surface = text_font.render('Press SPACE to start', True, 'Gray')
text_joc_dreptunghi = text_joc_surface.get_rect(center = (500,400))

text_meniu_surface = text_font.render('Click here to play', True, 'Gray')
text_meniu_dreptunghi = text_meniu_surface.get_rect(center = (500, 400))

text2_meniu_surface = text_font.render('Click here to exit', True, 'Gray')
text2_meniu_dreptunghi = text2_meniu_surface.get_rect(center = (500, 700))

text3_meniu_surface = text_font2.render("Breakout", True, 'Gray')
text3_meniu_dreptunghi = text3_meniu_surface.get_rect(center = (500, 200))

text4_meniu_surface = text_font.render('Click here to see highest score', True, 'Gray')
text4_meniu_dreptunghi = text4_meniu_surface.get_rect(center = (500, 550))

text_joc_castigat_surface = text_font.render('Congratulations', False, 'Gray')
text2_joc_castigat_surface = text_font.render('You beat the game!', False, 'Gray')
text_joc_castigat_dreptunghi = text_joc_castigat_surface.get_rect(center = (500,200))
text2_joc_castigat_dreptunghi = text2_joc_castigat_surface.get_rect(center = (500,260))

platforma = platform()
zid = caramizi()
zid.creare_zid()
biluta = bila(fereastra_latime / 2 + 10 , platforma.y - platforma.inaltime)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                f = open("Proiect_breakout/scor.txt",'w')
                f.write(str(scor_maxim))
                f.close()
            except:
                print("Error")
            pygame.quit()
            exit()
    
    if game_active == 1:  #fereastra meniu
        clock.tick(fps)
        screen.blit(scaled_background, (0, 0))
        mouse_poz = pygame.mouse.get_pos()
        butoane_mouse = pygame.mouse.get_pressed()

        if text_meniu_dreptunghi.collidepoint(mouse_poz):  
            if butoane_mouse[0] :
                game_active = 2
        if text_meniu_dreptunghi.left <= mouse_poz[0] <= text_meniu_dreptunghi.right and text_meniu_dreptunghi.top <=  mouse_poz[1] <= text_meniu_dreptunghi.bottom:
            pygame.draw.rect(screen, "Purple", text_meniu_dreptunghi,  border_radius= 10)

        if text2_meniu_dreptunghi.collidepoint(mouse_poz):
            if butoane_mouse[0]:
                try:
                    f = open("Proiect_breakout/scor.txt",'w')
                    f.write(str(scor_maxim))
                    f.close()
                except:
                    print("Error")
                pygame.quit()
                exit()
        if text2_meniu_dreptunghi.left <= mouse_poz[0] <= text2_meniu_dreptunghi.right and text2_meniu_dreptunghi.top <=  mouse_poz[1] <= text2_meniu_dreptunghi.bottom:
            pygame.draw.rect(screen, "Purple", text2_meniu_dreptunghi, border_radius= 10)

        if text4_meniu_dreptunghi.collidepoint(mouse_poz):
            if butoane_mouse[0]:
                game_active = 4
        if text4_meniu_dreptunghi.left <= mouse_poz[0] <= text4_meniu_dreptunghi.right and text4_meniu_dreptunghi.top <=  mouse_poz[1] <= text4_meniu_dreptunghi.bottom:
            pygame.draw.rect(screen, "Purple", text4_meniu_dreptunghi, border_radius= 10)

        screen.blit(text3_meniu_surface, text3_meniu_dreptunghi)
        screen.blit(text_meniu_surface,text_meniu_dreptunghi)
        screen.blit(text2_meniu_surface,text2_meniu_dreptunghi)
        screen.blit(text4_meniu_surface, text4_meniu_dreptunghi)

    if game_active == 2:  #fereastra joc
        clock.tick(fps)
        screen.blit(scaled_background2, (0,0))
        zid.afisare_zid()
        platforma.afisare_platforma()
        biluta.afisare_bila()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            miscare = 1

        if miscare:
            platforma.directie_platforma()
            game_active = biluta.miscare_bila()
            scor_final = scor()
        else:
            screen.blit(text_joc_surface, text_joc_dreptunghi)
            start_time = int(pygame.time.get_ticks() / 1000)
            
    if game_active == 0:      #fereastra game over si resetare
        screen.blit(scaled_background3, (0,0))
        screen.blit(text_surface, text_dreptunghi)
        screen.blit(text2_surface,text2_dreptunghi)

        if scor_final > scor_maxim:
            text_scor_final_surface = text_font.render('Highest score: %s' %scor_final, False, 'Gray')
        else:
            text_scor_final_surface = text_font.render('Your score: %s' %scor_final, False, 'Gray')
    
        text_scor_final_dreptunghi = text_scor_final_surface.get_rect(center = (500, 500))
        screen.blit(text_scor_final_surface, text_scor_final_dreptunghi)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if scor_final > scor_maxim:
                scor_maxim = scor_final               
            game_active = 1
            platforma = platform()
            zid = caramizi()
            zid.creare_zid()
            biluta = bila(fereastra_latime / 2 + 10 , platforma.y - platforma.inaltime)
            miscare = 0

    if game_active == 3:  #fereastra de joc castigat si resetare
        screen.blit(scaled_background3, (0,0))
        screen.blit(text_joc_castigat_surface, text_joc_castigat_dreptunghi)
        screen.blit(text2_joc_castigat_surface, text2_joc_castigat_dreptunghi)
        screen.blit(text2_surface,text2_dreptunghi)

        if scor_final > scor_maxim:
            text_scor_final_surface = text_font.render('Highest score: %s' %scor_final, False, 'Gray')
        else:
            text_scor_final_surface = text_font.render('Your score: %s' %scor_final, False, 'Gray')

        text_scor_final_dreptunghi = text_scor_final_surface.get_rect(center = (500, 500))
        screen.blit(text_scor_final_surface, text_scor_final_dreptunghi)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if scor_final > scor_maxim:
                scor_maxim = scor_final    
            game_active = 1
            platforma = platform()
            zid = caramizi()
            zid.creare_zid()
            biluta = bila(fereastra_latime / 2 + 10 , platforma.y - platforma.inaltime)
            miscare = 0
    
    if game_active == 4: #fereastra scor maxim
        screen.blit(scaled_background4, (0,0))
        text_scor_maxim_surface = text_font4.render('Highest score: %d' %scor_maxim, True, 'Gray')
        text_scor_maxim_dreptunghi = text_scor_maxim_surface.get_rect(center = (500, 300))
        screen.blit(text_scor_maxim_surface, text_scor_maxim_dreptunghi)
        screen.blit(text2_surface, text2_dreptunghi)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_active = 1
    pygame.display.update()
    
