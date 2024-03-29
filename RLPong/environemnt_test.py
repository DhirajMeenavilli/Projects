import pygame
from agent import Player
import torch
# User-defined functions
score = 0
score2 = 0

def interact(paddle,ball):
    if ball.center[0] > paddle.pos[0] and ball.center[0] < (paddle.pos[0] + paddle.length):
        if ball.center[1] > paddle.pos[1] - 30 and ball.center[1] < paddle.pos[1] + paddle.width + 20:
            return True

def main():
    RLagent = Player()
    pygame.init()
    pygame.display.set_mode((500, 400))
    pygame.display.set_caption('Pong')
    w_surface = pygame.display.get_surface()
    for i in range(10):
        game = Game(w_surface)
        game.play(score,score2,RLagent)
    pygame.quit()
    torch.save(RLagent.policy_network.state_dict(), "model_weights.pt")

# User-defined classes

class Game:
    # An object in this class represents a complete game.
    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object
        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True
        # === game specific objects
        self.small_dot = Ball('white', 8, [150, 80], [5,5], self.surface)
        self.left_paddle = Paddle('white',50,150,20,80,self.surface)
        self.right_paddle = Paddle('white',420,150,20,80,self.surface)
        self.contact_paddle_left = Paddle('white', 65, 150, 10, 80, self.surface)
        self.contact_paddle_right = Paddle('white', 420, 150, 10, 80, self.surface)
        #self.max_frames = 150
        #self.frame_counter = 0

    def play(self,score,score2,RLagent,cumReward=0):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            pressedKeys = pygame.key.get_pressed()
            agent_hit = False
            if interact(self.contact_paddle_right,self.small_dot):
                if self.small_dot.velocity[0] > 0:
                    agent_hit = True
                    self.small_dot.hit()
            
            if interact(self.contact_paddle_left,self.small_dot):
                if self.small_dot.velocity[0] < 0:
                    self.small_dot.hit()

            score,score2 = self.small_dot.ScoreUp(score,score2)

            if score == 11 or score2 == 11:
                print(score, score2, cumReward)
                self.close_clicked = True

            self.draw(score,score2)

            if self.continue_game:
                
                state = torch.Tensor([self.right_paddle.y, self.small_dot.center[0], self.small_dot.center[1],self.small_dot.velocity[0], self.small_dot.velocity[1]])
                action = RLagent.choose_action(state)
                
                self.update(pressedKeys, action)

                new_state = torch.tensor([self.right_paddle.y, self.small_dot.center[0], self.small_dot.center[1],self.small_dot.velocity[0], self.small_dot.center[1]])
                
                if agent_hit == False:
                    reward = abs((self.left_paddle.pos[1] + self.left_paddle.dim[0])//2 - self.small_dot.center[1]) * -1
                else:
                    reward = 10
                
                # print(reward)
                cumReward += reward
                RLagent.store_transition(state, new_state, action, reward)
                #self.decide_continue()
                RLagent.learn()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self,score,score2):
        # Draw all game objects.
        # - self is the Game to draw
        self.surface.fill(self.bg_color)  # clear the display surface first
        font = pygame.font.SysFont("arial", 25, True)
        text = font.render('Score:' + str(score2), 1, (245, 56, 78))
        self.surface.blit(text, (390, 10))
        font = pygame.font.SysFont("arial", 25, True)
        text = font.render('Score:' + str(score), 1, (245, 56, 78))
        self.surface.blit(text, (50, 10))
        self.small_dot.draw()
        self.left_paddle.draw()
        self.right_paddle.draw()
        self.contact_paddle_left.draw()
        self.contact_paddle_right.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self,pressedKeys, RLaction):
        # Update the game objects for the next frame.
        # - self is the Game to update
        if pressedKeys[pygame.K_w]:
            self.left_paddle.moveUp()
            self.contact_paddle_left.moveUp()

        if pressedKeys[pygame.K_s]:
            self.left_paddle.moveDown()
            self.contact_paddle_left.moveDown()

        if RLaction == 1:
            self.right_paddle.moveUp()
            self.contact_paddle_right.moveUp()

        if RLaction == 0:
            self.right_paddle.moveDown()
            self.contact_paddle_right.moveDown()


        self.small_dot.move()
        self.small_dot.change_vel()
        #self.frame_counter = self.frame_counter + 1

    #def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

     #   if self.frame_counter > self.max_frames:
      #      self.continue_game = False


class Ball:
    # An object in this class represents a Dot that moves

    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
        self.color = pygame.Color(dot_color)
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.surface = surface

    def move(self):
        for i in range(0, 2):
            self.center[i] = (self.center[i] + self.velocity[i])

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def change_vel(self):
        if self.center[0] > 490 or self.center[0] < 0:
            self.velocity[0] = self.velocity[0] * -1

        if self.center[1] > 390 or self.center[1] < 0:
            self.velocity[1] = self.velocity[1] * -1

    def hit(self):
        self.velocity[0] = self.velocity[0] * -1

    def ScoreUp(self,score,score2):
        if self.center[0] > 490:
            score = score+1

        if self.center[0] < 0:
            score2 = score2+1

        return score,score2
class Paddle:
    def __init__(self,colour,x,y,length,width,surface):
        self.color = pygame.Color(colour)
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.pos = [x,y]
        self.dim = [length,width]
        self.surface = surface
        self.Rect = [self.surface,self.color,(self.pos,self.dim)]
        self.vel = 5

    def draw(self):
        pygame.draw.rect(self.surface,self.color,(self.pos,self.dim))

    def moveUp(self):
        if self.pos[1] > 0:
            self.pos[1] = self.pos[1] - self.vel

    def moveDown(self):
        if self.pos[1] < 400 - self.width:
            self.pos[1] = self.pos[1] + self.vel

main()
