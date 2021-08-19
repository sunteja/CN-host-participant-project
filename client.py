import pygame
from network import Network
import pickle
from questions import Questions
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 100
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

#questions = ["color of cricket ball?\nA)white\nB)black\nC)pink\nD)blue", "cat says?\nA)meow\nB)bow\nC)chrip\nD)none", "Sachin Tendulkar is also known as\nA)Dada\nB)God of Cricket\nC)Captain India\nD)Google Master"]
#answers = ["A","A","B"]
def redrawWindow(win, game, p,quest):
    win.fill((128,128,128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        k = 30
        for line in quest.splitlines():
            text = font.render(line, 1, (0, 255,255))
            win.blit(text, (30, k))
            k = k+50

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        move3 = game.get_player_move(2)
        if game.allWent():
            text1 = font.render(move1+" by 0", 1, (0,0,0))
            text2 = font.render(move2+" by 1", 1, (0, 0, 0))
            text3 = font.render(move3+" by 2", 1, (0,0,0))
        else:
            if game.p1Went:
                text1 = font.render(move1+" by 0", 1, (0,0,0))
            else:
                text1 = font.render("Waiting response from 0", 1, (0, 0, 0))

            if game.p2Went:
                text2 = font.render(move2+" by 1", 1, (0,0,0))
            else:
                text2 = font.render("Waiting response from 1", 1, (0, 0, 0))
            if game.p3Went: 
                text3 = font.render(move3+" by 2", 1, (0,0,0))
            else:
                text3 = font.render("Waiting response from 2", 1, (0, 0, 0))


        
        win.blit(text1, (200, 350))
        win.blit(text2, (200, 450))
        win.blit(text3, (200, 550))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [Button("A", 30, 300, (0,0,0)), Button("B", 30, 400, (255,255,0)), Button("C", 30, 500, (0,255,0)),Button("D", 30, 600, (255,0,0))]
def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    q = Questions()
    player = int(n.getP())
    print("You are player", player)
    k=0
    wp1=0
    wp2=0
    wp3=0

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.allWent():
            redrawWindow(win, game, player,q.quest(k))
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.get_player_move(1) == q.answer(k) and player == 1) or (game.get_player_move(0) == q.answer(k) and player == 0) or (game.get_player_move(2) == q.answer(k) and player == 2):
                text = font.render("Correct Answer", 1, (255,0,0))
                if game.get_player_move(0) == q.answer(k):
                    wp1 = wp1+1
                elif game.get_player_move(1) == q.answer(k):
                    wp2 = wp2+1
                elif game.get_player_move(2) == q.answer(k):
                    wp3 = wp3+1
            else:
                text = font.render("Wrong Answer", 1, (255, 0, 0))
                if game.get_player_move(0) == q.answer(k):
                    wp1 = wp1+1
                elif game.get_player_move(1) == q.answer(k):
                    wp2 = wp2+1
                elif game.get_player_move(2) == q.answer(k):
                    wp3 = wp3+1



            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
            k=k+1
            if wp1 == 5 :
                text = font.render("Player 1 has Won!",1,(255,0,0))
                win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2+100))
                pygame.display.update()
                pygame.time.delay(2000)
                k=q.length

            if wp2 == 5 :
                text = font.render("Player 2 has Won!",1,(255,0,0))
                win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2+100))
                pygame.display.update()
                pygame.time.delay(2000)
                k=q.length

            if wp3 == 5 :
                text = font.render("Player 3 has Won!",1,(255,0,0))
                win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2+100))
                pygame.display.update()
                pygame.time.delay(2000)
                k=q.length


            if(k == q.length):
                text = font.render("Game Over",1,(255,0,0))
                win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2-100))
                pygame.display.update()
                pygame.time.delay(2000)
                run = False
                pygame.quit()


            #pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        elif player == 1:
                            if not game.p2Went:
                                n.send(btn.text)
                        else:
                            if not game.p3Went:
                                n.send(btn.text)

        redrawWindow(win, game, player, q.quest(k))

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True: #always gets executed.
    menu_screen()
