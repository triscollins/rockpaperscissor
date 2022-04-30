import random
import pygame
import sys
from pygame.locals import *
from enum import IntEnum

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Setup a display with caption
display_width = 600
display_height = 600
DISPLAYSURF = pygame.display.set_mode((display_width,display_height))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")

sprite_width = 150

rockImg = pygame.transform.scale(pygame.image.load('images/rock.png'), (sprite_width,sprite_width))
rockImg_position = Rect(50, 50, sprite_width, sprite_width) # Width/height of 100 pixels.

paperImg = pygame.transform.scale(pygame.image.load('images/paper.png'), (sprite_width,sprite_width))
paperImg_position = Rect(50, 200, sprite_width, sprite_width) # Width/height of 100 pixels.

scissorImg = pygame.transform.scale(pygame.image.load('images/scissor.png'), (sprite_width,sprite_width))
scissorImg_position = Rect(50, 350, sprite_width, sprite_width) # Width/height of 100 pixels.

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


actions = [Action.Rock, Action.Paper, Action.Scissors]


def start_game():
    pygame.init()
    user_action = None
    computer_action = None
    while True:
        # set up out player options
        DISPLAYSURF.blit(rockImg, (50, 50))
        DISPLAYSURF.blit(paperImg, (50, 200))
        DISPLAYSURF.blit(scissorImg, (50, 350))

        pygame.display.update()

        # now we start watching for events to happen on the screen.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # grab the coordinates where the user clicked.
                x, y = event.pos

                # now match these to the image on the screen
                user_action = get_user_action(x, y)

                # now grab a random choice for the computers action
                computer_action = get_computer_action()


                # now determine who the winner is!
                if user_action is not None and computer_action is not None:
                    print(f"\nYou chose {user_action.name}, computer chose {computer_action.name}\n")
                    winner = determine_winner(user_action, computer_action)

                    winner_text = pygame.font.SysFont("comicsansms", 20)
                    text_surf = text_objects(f"And the winner is... {winner}!", winner_text)
                    text_rect = Rect(display_width - (display_width / 2), display_height-(display_height / 3), display_width / 3, (display_height / 3))
                    DISPLAYSURF.fill(WHITE)
                    DISPLAYSURF.blit(text_surf, text_rect)

                    # paint the corresponding sprite to the screen based on what computer selected.
                    computer_action_image = get_image_for_choice(computer_action)
                    comp_action_rect = Rect(400, 200, sprite_width, sprite_width)
                    DISPLAYSURF.fill(WHITE, comp_action_rect)
                    DISPLAYSURF.blit(computer_action_image, comp_action_rect)

                    print(f"And the winner is..... {winner}!")


def text_objects(text, font):
    text_surface = font.render(text, True, GREEN)
    return text_surface


def get_user_action(x,y):
    if rockImg_position.collidepoint(x, y):
        print('clicked on rock')
        return Action.Rock
    if paperImg_position.collidepoint(x, y):
        print('clicked on paper')
        return Action.Paper
    if scissorImg_position.collidepoint(x, y):
        print('clicked on scissor')
        return Action.Scissors


def get_computer_action():
    # derive a random action for the computers choice.
    # randint chooses a random integer between arg_a and arg_b
    choice = random.randint(0, len(Action)-1)
    return Action(choice)


def determine_winner(user_action, computer_action):
    winner = None

    winner_actions = {
        Action.Rock: [Action.Scissors],
        Action.Paper: [Action.Rock],
        Action.Scissors: [Action.Paper]
    }

    defeat = winner_actions[user_action]

    if user_action == computer_action:
        winner = "A Draw"
    elif computer_action in defeat:
        winner = "You"
    else:
        winner = "Computer"

    return winner


def get_image_for_choice(action):
    if action == Action.Rock:
        return rockImg
    if action == Action.Paper:
        return paperImg
    if action == Action.Scissors:
        return scissorImg


if __name__ == '__main__':
    start_game()
