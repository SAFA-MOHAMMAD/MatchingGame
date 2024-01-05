import pygame
import sys
import random
import time
from pygame import mixer
pygame.init()
class Card:
    def __init__(self, image):
        self.image = image
        self.is_face_up = False
# Set up window
width, height = 800, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sugar Rush")
font=pygame.font.SysFont(None,85)
clock = pygame.time.Clock()
mixer.music.load('BackgroundMusic.wav')
mixer.music.play(-1)
lifeHeart=pygame.image.load('lifeHeart.png')
def display_life(x,y,Num_of_hearts):
    for num in range(Num_of_hearts):
        lifeHeart_rec=lifeHeart.get_rect(center=(x,y))
        screen.blit(lifeHeart,lifeHeart_rec)
        x+=70
class Button():
    def __init__(self,x,y,image,scale):
        self.x=x
        self.y=y
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rec=self.image.get_rect(center=(x,y))
        self.clicked=False
        self.is_face_up=False
    def draw(self, surface):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rec.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
        if pygame.mouse.get_pressed()[0]==0 :
            self.clicked=False
        if self.is_face_up:
            screen.blit(self.image,self.rec) 
        else:
            card_back = pygame.image.load("Rectangle.png")
            screen.blit(card_back, self.rec) 
        return action
def display_cards(cards):
    for i, card in enumerate(cards):
        row, col = divmod(i, 4)
        x, y = col * 200, row * 150
        if card.is_face_up:
            screen.blit(card.image, (x, y))
        else:
            # Display a card back image when the card is face down
            card_back = pygame.image.load("Rectangle.png")  # Replace with your card back image filename
            screen.blit(card_back, (x, y))
card_images_hard = []
for i in range(1, 9):
    img = pygame.image.load(f"image_{i}.png")
    card_images_hard.extend([img, img])
def hard_level():
    life=7
    finish=0
    selected_cards = []
    run =True
    win=True
    random.shuffle(card_images_hard)
    cards_hard = [Card(image) for image in card_images_hard]
    while run and finish!=8:
        screen.fill((202,228,241))
        screen.blit(Background,Background_rec)
        display_cards(cards_hard)
        if life==7:
            display_life(340,650,7)
        elif life==6:
            display_life(340,650,6)
        elif life==5:
            display_life(340,650,5)
        elif life==4:
            display_life(340,650,4)
        elif life==3 :
            display_life(340,650,3)
        elif life==2:
            display_life(340,650,2)
        elif life==1:
            display_life(340,650,1)          
        elif life==0:
            win=False
            return win
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win=False
                return win
                run=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound=mixer.Sound('BubbleBell.wav')
                click_sound.play()
                x, y = pygame.mouse.get_pos()
                col = x // 190
                row = y // 150
                index = row * 4 + col
                selected_card = cards_hard[index]
                if selected_card not in selected_cards:
                    selected_cards.append(selected_card)
                    selected_card.is_face_up = True
                if len(selected_cards) == 2:
                    run_inside=True
                    while run_inside:
                        display_cards(cards_hard)
                        pygame.display.update()
                        if pygame.time.delay(500):
                           run_inside=False
                    if selected_cards[0].image == selected_cards[1].image:
                    # Cards match, keep them face up
                        selected_cards = []
                        finish+=1
                        if finish==8 and not all(card.is_face_up for card in cards_hard):
                            finish-=1
                    else:
                        life-=1
                        losing_sound=mixer.Sound('losing.wav')
                        losing_sound.play()
                    # Cards do not match, flip them back face down
                        for card in selected_cards:
                            card.is_face_up = False
                        selected_cards = []


        pygame.display.update()
        clock.tick(60)
    win=pygame.image.load('WIN.png')
    win_rec=win.get_rect(center=(400,350))
    click_sound=mixer.Sound('VICTORY.wav')
    click_sound.play()
    run_inside=True
    while run_inside:
        screen.blit(win,win_rec)
        pygame.display.update()
        if pygame.time.delay(4000):
            run_inside=False
    for card in cards_hard:
        card.is_face_up=False
    return win
card_images_med = []
for i in range(1, 7):
    img = pygame.image.load(f"image_{i}.png")
    card_images_med.extend([img, img])
def med_level():
    life=6
    finish=0
    selected_cards = []
    win=True
    run=True
    random.shuffle(card_images_med)
    cards_med = [Card(image) for image in card_images_med]
    while run and finish!=6:
        screen.fill((202,228,241))
        screen.blit(Background,Background_rec)
        display_cards(cards_med)
        if life==6:
            display_life(410,650,6)
        elif life==5:
            display_life(410,650,5)
        elif life==4:
            display_life(410,650,4)
        elif life==3 :
            display_life(410,650,3)
        elif life==2:
            display_life(410,650,2)
        elif life==1:
            display_life(410,650,1)           
        elif life==0:
            win=False
            return win
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win=False
                return win
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound=mixer.Sound('BubbleBell.wav')
                click_sound.play()
                x, y = pygame.mouse.get_pos()
                col = x // 190
                row = y // 150
                index = row * 4 + col
                # selected_cards.append(cards_med[index])
                # cards_med[index].is_face_up = True
                selected_card = cards_med[index]
                if selected_card not in selected_cards:
                    selected_cards.append(selected_card)
                    selected_card.is_face_up = True
                    # pygame.time.wait(500)  # Pause for a moment to show the second card
                if len(selected_cards) == 2:
                    run_inside=True
                    while run_inside:
                        display_cards(cards_med)
                        pygame.display.update()
                        if pygame.time.delay(500):
                           run_inside=False
                    if selected_cards[0].image == selected_cards[1].image:
                    # Cards match, keep them face up
                        selected_cards = []
                        finish+=1
                        if finish==6 and not all(card.is_face_up for card in cards_med):
                            finish-=1
                    else:
                        life-=1
                        losing_sound=mixer.Sound('losing.wav')
                        losing_sound.play()
                    # Cards do not match, flip them back face down
                        for card in selected_cards:
                            card.is_face_up = False
                        selected_cards = []
        # display_cards(cards_med)
        pygame.display.update()
        clock.tick(60)
    win=pygame.image.load('WIN.png')
    win_rec=win.get_rect(center=(400,350))
    click_sound=mixer.Sound('VICTORY.wav')
    click_sound.play()
    run_inside=True
    while run_inside:
        screen.blit(win,win_rec)
        pygame.display.update()
        if pygame.time.delay(4000):
            run_inside=False
    for card in cards_med:
        card.is_face_up=False
    return win
card_images_easy = []
for i in range(1, 5):
    img = pygame.image.load(f"image_{i}.png")
    card_images_easy.extend([img, img])
def esay_level():
    life=5
    win=True
    finish=0
    selected_cards = []
    run=True
    random.shuffle(card_images_easy)
    cards_easy = [Card(image) for image in card_images_easy]
    while run and finish!=4:
        screen.fill((202,228,241))
        screen.blit(Background,Background_rec)
        display_cards(cards_easy)
        if life==5:
            display_life(480,650,5)
        elif life==4:
            display_life(480,650,4)
        elif life==3 :
            display_life(480,650,3)
        elif life==2:
            display_life(480,650,2)
        elif life==1:
            display_life(480,650,1)          
        elif life==0:
            win=False
            
            return win
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win=False
                return win
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound=mixer.Sound('BubbleBell.wav')
                click_sound.play()
                x, y = pygame.mouse.get_pos()
                col = x // 190
                row = y // 150
                index = row * 4 + col
                selected_card = cards_easy[index]
                if selected_card not in selected_cards:
                    selected_cards.append(selected_card)
                    selected_card.is_face_up = True
                if len(selected_cards) == 2:
                    run_inside=True
                    while run_inside:
                        display_cards(cards_easy)
                        pygame.display.update()
                        if pygame.time.delay(500):
                           run_inside=False
                    if selected_cards[0].image == selected_cards[1].image:
                    # Cards match, keep them face up
                        selected_cards = []
                        finish+=1
                        if finish==4 and not all(card.is_face_up for card in cards_easy):
                            finish-=1
                    else:
                        life-=1
                        losing_sound=mixer.Sound('losing.wav')
                        losing_sound.play()
                        if life==0:
                            Lose=pygame.image.load('LOSE.png')
                            Lose_rec=Lose.get_rect(center=(400,350))
                            run_inside=True
                            while run_inside:
                                screen.blit(Lose,Lose_rec)
                                pygame.display.update()
                                if pygame.time.delay(1500):
                                    run_inside=False
                    # Cards do not match, flip them back face down
                        for card in selected_cards:
                            card.is_face_up = False
                        selected_cards = []
        pygame.display.flip()
        clock.tick(60)
    win=pygame.image.load('WIN.png')
    win_rec=win.get_rect(center=(400,350))
    click_sound=mixer.Sound('VICTORY.wav')
    click_sound.play()
    run_inside=True
    while run_inside:
        screen.blit(win,win_rec)
        pygame.display.update()
        if pygame.time.delay(4000):
            run_inside=False
    for card in cards_easy:
        card.is_face_up=False
    return win
Exit=pygame.image.load('Exit.png').convert_alpha()
Hard=pygame.image.load('Hard.png').convert_alpha()
Med=pygame.image.load('Med.png').convert_alpha()
Easy=pygame.image.load('easy.png').convert_alpha()
Easy_button=Button(150,500,Easy,1)
Med_button=Button(400,500,Med,1)
Hard_button=Button(650,500,Hard,1)
Exit_button=Button(410,650,Exit,0.7)
Background=pygame.image.load('Background.png').convert_alpha()
Background_rec=Background.get_rect(center=(400,350))
Welcome=pygame.image.load('Welcome.png')
Welcome_rec=Welcome.get_rect(center=(400,250))
level_st=pygame.image.load('Level.png')
level_st_rec=level_st.get_rect(center=(400,370))
Score=0
run=True
while run:
    screen.fill((202,228,241))
    screen.blit(Background,Background_rec)
    screen.blit(Welcome,Welcome_rec)
    screen.blit(level_st,level_st_rec)
    Score_st=pygame.image.load('TotalScore.png')
    Score_st_rec=Score_st.get_rect(bottomleft=(10,670))
    screen.blit(Score_st,Score_st_rec)
    Score_pr=font.render(f"{Score}",True,'white')
    Score_pr_rec=Score_pr.get_rect(bottomright=(278,675))
    screen.blit(Score_pr,Score_pr_rec)
    for button in [Easy_button,Med_button,Hard_button,Exit_button]:
        button.is_face_up=True
        button.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if Exit_button.draw(screen):
            click_sound=mixer.Sound('clickSound.wav')
            click_sound.play()
            run=False
        if Easy_button.draw(screen):
            click_sound=mixer.Sound('clickSound.wav')
            click_sound.play()
            if esay_level():
                Score+=1
        if Med_button.draw(screen):
            click_sound=mixer.Sound('clickSound.wav')
            click_sound.play()
            if med_level():
                Score+=1
        if Hard_button.draw(screen):
            click_sound=mixer.Sound('clickSound.wav')
            click_sound.play()
            if hard_level():
                Score+=1
    pygame.display.update()
    clock.tick(60) 

