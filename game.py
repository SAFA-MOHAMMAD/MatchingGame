import pygame
import sys
import random


pygame.init()
class Card:
    def __init__(self, image):
        self.image = image
        self.is_face_up = False

# Set up window
width, height = 800, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Memory Matching Game")
font=pygame.font.SysFont(None,60,italic=True)
clock = pygame.time.Clock()
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
    def Update_to_rec(self,rec):
        self=rec
    def Update(self,image):
        self.image=image
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
Welcome=font.render('Welcome',True,'Black')
Welcome_rec=Welcome.get_rect(center=(400,200))
level_st=font.render('choose a level to start playing',True,'Black')
level_st_rec=level_st.get_rect(center=(400,250))
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

# Load images
# card_images = []
# for i in range(1, 9):
#     img = pygame.image.load(f"image_{i}.png")  # Replace with your image filenames
#     card_images.extend([img, img])
# random.shuffle(card_images)
# cards = [Card(image) for image in card_images]
card_images_hard = []
for i in range(1, 9):
    img = pygame.image.load(f"image_{i}.png")
    card_images_hard.extend([img, img])
random.shuffle(card_images_hard)
cards_hard = [Card(image) for image in card_images_hard]
def hard_level():
    finish=0
    selected_cards = []
    run =True
    while run and finish!=8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // 180
                row = y // 150
                index = row * 4 + col
                selected_cards.append(cards_hard[index])
                cards_hard[index].is_face_up = True

                if len(selected_cards) == 2:
                    pygame.time.wait(500)  # Pause for a moment to show the second card
                    if selected_cards[0].image == selected_cards[1].image:
                    # Cards match, keep them face up
                        selected_cards = []
                        finish+=1
                    else:
                    # Cards do not match, flip them back face down
                        for card in selected_cards:
                            card.is_face_up = False
                        selected_cards = []

        screen.fill((202,228,241))  # Fill the screen with a white background
        display_cards(cards_hard)
        pygame.display.flip()
        clock.tick(60)
card_images_med = []
for i in range(1, 7):
    img = pygame.image.load(f"image_{i}.png")
    card_images_med.extend([img, img])
random.shuffle(card_images_med)
cards_med = [Card(image) for image in card_images_med]
def med_level():
    finish=0
    selected_cards = []
    run=True
    while run and finish!=6:
        screen.fill((202,228,241))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // 180
                row = y // 150
                index = row * 4 + col
                selected_cards.append(cards_med[index])
                cards_med[index].is_face_up = True

                if len(selected_cards) == 2:
                    pygame.time.wait(500)  # Pause for a moment to show the second card
                    if selected_cards[0].image == selected_cards[1].image:
                    # Cards match, keep them face up
                        selected_cards = []
                        finish+=1
                    else:
                    # Cards do not match, flip them back face down
                        for card in selected_cards:
                            card.is_face_up = False
                        selected_cards = []

          # Fill the screen with a white background
        display_cards(cards_med)
        pygame.display.flip()
        clock.tick(60)
card_images_easy = []
for i in range(1, 5):
    img = pygame.image.load(f"image_{i}.png")
    card_images_easy.extend([img, img])
random.shuffle(card_images_easy)
cards_easy = [Card(image) for image in card_images_easy]
def esay_level():
    finish=0
    selected_cards = []
    run=True
    while run and finish!=4:
        screen.fill((202,228,241))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if Exit_button.draw(screen):
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // 180
                row = y // 150
                index = row * 4 + col
                selected_cards.append(cards_easy[index])
                cards_easy[index].is_face_up = True

                if len(selected_cards) == 2:
                    pygame.time.wait(500)  # Pause for a moment to show the second card
                    if selected_cards[0].image == selected_cards[1].image:
                    # Cards match, keep them face up
                        selected_cards = []
                        finish+=1
                    else:
                    # Cards do not match, flip them back face down
                        for card in selected_cards:
                            card.is_face_up = False
                        selected_cards = []

          # Fill the screen with a white background
        display_cards(cards_easy)
        Exit_button.is_face_up=True
        Exit_button.draw(screen)
        pygame.display.flip()
        clock.tick(60)
Exit=pygame.image.load('Exit.png').convert_alpha()
Hard=pygame.image.load('Hard.png').convert_alpha()
Med=pygame.image.load('Med.png').convert_alpha()
Easy=pygame.image.load('Esay.png').convert_alpha()
Easy_button=Button(150,400,Easy,1)
Med_button=Button(400,400,Med,1)
Hard_button=Button(650,400,Hard,1)
Exit_button=Button(400,550,Exit,0.6)
run=True
while run:
    screen.fill((202,228,241))
    screen.blit(Welcome,Welcome_rec)
    screen.blit(level_st,level_st_rec)
    for button in [Easy_button,Med_button,Hard_button,Exit_button]:
        button.is_face_up=True
        button.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if Exit_button.draw(screen):
            run=False
        if Easy_button.draw(screen):
            esay_level()
        if Med_button.draw(screen):
            med_level()
        if Hard_button.draw(screen):
            hard_level()
            
    pygame.display.update()
    clock.tick(60) 

