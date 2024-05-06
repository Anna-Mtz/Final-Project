import pygame
import os
import random

pygame.init()

Screen_Height = 600
Screen_Width = 1100
screen = pygame.display.set_mode((Screen_Width, Screen_Height))

running = [pygame.image.load(os.path.join("assests/egg", "eggwalk1.png")),
        pygame.image.load(os.path.join("assests/egg", "eggwalk2.png"))]

jumping = [pygame.image.load(os.path.join("assests/egg", "jumpegg.png"))]

small_obsticales = [pygame.image.load(os.path.join("assests/obsticles", "smallduck.png")),
                pygame.image.load(os.path.join("assests/obsticles", "smallgegg.png")),
                pygame.image.load(os.path.join("assests/obsticles", "smallgrave.png"))]

big_obsticales = [pygame.image.load(os.path.join("assests/obsticles", "bigduck.png")),
                pygame.image.load(os.path.join("assests/obsticles", "biggegg.png")),
                pygame.image.load(os.path.join("assests/obsticles", "biggrave.png"))]

track = [pygame.image.load(os.path.join("assests/other", "Track.png"))]



class Egg:
    x_pos = 80
    y_pos = 310
    JUMP_Vel = 8.5

    def __init__(self):
        self.run_img = running
        self.jump_img = jumping

        self.egg_run = True
        self.egg_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_Vel
        self.image = self.run_img[0]
        self.egg_rect = self.image.get_rect()
        self.egg_rect.x = self.x_pos
        self.egg_rect.y = self.y_pos
        
        

    def update(self, userInput):
        if self.egg_run:
            self.run()
        if self.egg_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.egg_jump:
            self.egg_jump = True
            self.egg_run = False
        else:
            self.egg_jump = False
            self.egg_run = True

    def run (self):
        self.image = self.run_img[self.step_index // 5]
        self.egg_rect = self.image.get_rect()
        self.egg_rect.x = self.x_pos
        self.egg_rect.y = self.y_pos
        self.step_index += 1

    def jump (self):
        self.image = self.jump_img
        if self.egg_jump:
            self.egg_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_Vel:
            self.egg_jump = False
            self.jump_vel = self.JUMP_Vel

    def draw(self, screen):
        screen.blit(self.image, (self.egg_rect.x, self.egg_rect.y))

def main():
    global game_speed, x_pos_bg, y_pos_bg, points
    run = True
    clock = pygame.time.Clock()
    player = Egg()
    game_speed = 1.4
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)

    def score ():
        global points, game_speed
        points =+ 1
        if points % 100 ==0:
            game_speed += 1
        text = font.render("Points:" + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        screen.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = track.get_width()
        screen.blit(track, (x_pos_bg, y_pos_bg))
        screen.blit(track, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(track, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)

        background()
        score()

        clock.tick(30)
        pygame.display.update()


main()