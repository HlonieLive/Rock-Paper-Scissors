import pygame
import random

pygame.init()

# Window:
window_height = 600
window_width = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rock Paper Scissor")

# Window Colours:
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 100, 0)
blue = (0, 128, 255)
grey = (128, 128, 128)
indigo = (75, 0, 130)


# Fonts to be used:
font1 = pygame.font.SysFont("Comic Sans MS", 45)
small_font = pygame.font.SysFont("Times New Roman", 25)

# Game choices:
game_choices = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]


class Button:
    def __init__(self, text, position, font, bg_colour, text_colour):
        self.text = text
        self.position = position
        self.font = font
        self.bg_colour = bg_colour
        self.text_colour = text_colour
        self.rectangle = pygame.Rect(position[0], position[1], 150, 50)

    def draw(self, screen):
        # Button:
        pygame.draw.rect(screen, self.bg_colour, self.rectangle)

        # Text surface:
        text_surface = self.font.render(self.text, True, self.text_colour)
        text_rect = text_surface.get_rect(center=self.rectangle.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_position):
        return self.rectangle.collidepoint(mouse_position)


# Buttons for choices:
rock_button = Button("Rock", (5, 450), small_font, green, white)
paper_button = Button("Paper", (204, 450), small_font, blue, white)
scissors_button = Button("Scissor", (403, 450), small_font, grey, white)
lizard_button = Button("Lizard", (602, 450), small_font, indigo, white)
spock_button = Button("Spock", (801, 450), small_font, black, white)


# Game Logic:
options = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]

computer_choice = random.choice(options)

# scores:
cpu_score = 0
player_score = 0


# Computer's Choice
def rps(player_choice, computer_choice):
    cpu_score = 0
    player_score = 0
    if computer_choice == player_choice:
        return "It's a Tie!"
    elif (
        (computer_choice == options[0] and player_choice == options[1])
        or (computer_choice == options[2] and player_choice == options[0])
        or (computer_choice == options[1] and player_choice == options[2])
        or (computer_choice == options[2] and player_choice == options[3])
        or (computer_choice == options[4] and player_choice == options[3])
        or (computer_choice == options[3] and player_choice == options[0])
        or (computer_choice == options[0] and player_choice == options[4])
        or (computer_choice == options[1] and player_choice == options[3])
        or (computer_choice == options[2] and player_choice == options[4])
        or (computer_choice == options[4] and player_choice == options[1])
    ):
        player_score += 1
        return "You Win!"
    else:
        cpu_score += 1
        return "You Lose!"


# 1. Player Images
# Insert Images:
player_rock = pygame.image.load("icons/rock2.png")
player_paper = pygame.image.load("icons/paper2.jpg")
player_scissor = pygame.image.load("icons/scissor2.jpg")
player_lizard = pygame.image.load("icons/lizard2.jpg")
player_spock = pygame.image.load("icons/spock2.jpg")
# Resize image:
player_rock = pygame.transform.scale(player_rock, (200, 200))
player_paper = pygame.transform.scale(player_paper, (200, 200))
player_scissor = pygame.transform.scale(player_scissor, (200, 200))
player_lizard = pygame.transform.scale(player_lizard, (200, 200))
player_spock = pygame.transform.scale(player_spock, (200, 200))

# Rotate:
player_paper = pygame.transform.rotate(player_paper, 90)
player_spock = pygame.transform.rotate(player_spock, 90)

# 2. Computer Images:
# Insert Images:
computer_rock = pygame.image.load("icons/rock1.jpg")
computer_paper = pygame.image.load("icons/paper1.png")
computer_scissor = pygame.image.load("icons/scissor1.jpg")
computer_lizard = pygame.image.load("icons/lizard1.png")
computer_spock = pygame.image.load("icons/spock1.jfif")

# Resize image:
computer_rock = pygame.transform.scale(computer_rock, (200, 200))
computer_paper = pygame.transform.scale(computer_paper, (200, 200))
computer_scissor = pygame.transform.scale(computer_scissor, (200, 200))
computer_lizard = pygame.transform.scale(computer_lizard, (200, 200))
computer_spock = pygame.transform.scale(player_spock, (200, 200))
computer_spock = pygame.transform.flip(player_spock, True, False)


running = True
player_choice = None
computer_choice = None
results = None

# Starter:
while running:
    window.fill(white)
    user = small_font.render("Player 1", True, black)
    window.blit(user, (800, 110))
    cpu = small_font.render("The CPU", True, black)
    window.blit(cpu, (130, 110))
    window.blit(player_rock, (750, 150))
    window.blit(computer_rock, (80, 150))
    # The Title:
    title = font1.render("Rock Paper Scissor", True, black)
    window.blit(title, (window_width // 2 - title.get_width() // 2, 50))
    # cpu_score = small_font.render(f"{cpu_score}", True, black)
    # window.blit(cpu_score, (300, 300))
    # player_score = small_font.render(f"{player_score}", True, black)
    # window.blit(cpu_score, (600, 300))
    # Draw Buttons:
    rock_button.draw(window)
    paper_button.draw(window)
    scissors_button.draw(window)
    lizard_button.draw(window)
    spock_button.draw(window)

    # Player and Computer Choices Display:
    user = small_font.render("Player 1", True, black)
    window.blit(user, (800, 110))
    cpu = small_font.render("The CPU", True, black)
    window.blit(cpu, (130, 110))
    if player_choice:
        if player_choice == "Rock":
            window.blit(player_rock, (750, 150))
            player_text = small_font.render(f"You Chose: {player_choice}", True, black)
            window.blit(player_text, (770, 360))

        elif player_choice == "Paper":
            window.blit(player_paper, (750, 150))
            player_text = small_font.render(f"You Chose: {player_choice}", True, black)
            window.blit(player_text, (770, 360))

        elif player_choice == "Scissor":
            window.blit(player_scissor, (750, 150))
            player_text = small_font.render(f"You Chose: {player_choice}", True, black)
            window.blit(player_text, (770, 360))

        elif player_choice == "Lizard":
            window.blit(player_lizard, (750, 150))
            player_text = small_font.render(f"You Chose: {player_choice}", True, black)
            window.blit(player_text, (770, 360))

        elif player_choice == "Spock":
            window.blit(player_spock, (750, 150))
            player_text = small_font.render(f"You Chose: {player_choice}", True, black)
            window.blit(player_text, (770, 360))

    if computer_choice:
        if computer_choice == "Rock":
            window.blit(computer_rock, (80, 150))
            computer_text = small_font.render(
                f"The CPU Chose: {computer_choice}", True, black
            )
            window.blit(computer_text, (60, 360))
        elif computer_choice == "Paper":
            window.blit(computer_paper, (80, 150))
            computer_text = small_font.render(
                f"The CPU Chose: {computer_choice}", True, black
            )
            window.blit(computer_text, (60, 360))
        elif computer_choice == "Scissor":
            window.blit(computer_scissor, (80, 150))
            computer_text = small_font.render(
                f"The CPU Chose: {computer_choice}", True, black
            )
            window.blit(computer_text, (60, 360))
        elif computer_choice == "Lizard":
            window.blit(computer_lizard, (80, 150))
            computer_text = small_font.render(
                f"The CPU Chose: {computer_choice}", True, black
            )
            window.blit(computer_text, (60, 360))
        elif computer_choice == "Spock":
            window.blit(computer_spock, (80, 150))
            computer_text = small_font.render(
                f"The CPU Chose: {computer_choice}", True, black
            )
            window.blit(computer_text, (60, 360))

    # Display Results:
    if results:
        results_text = small_font.render(results, True, black)
        window.blit(results_text, (450, 250))

    # Event Handling:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos

            # Handling Button click:
            if rock_button.is_clicked(mouse_position):
                player_choice = "Rock"
                computer_choice = random.choice(options)
                results = rps(player_choice, computer_choice)
            elif paper_button.is_clicked(mouse_position):
                player_choice = "Paper"
                computer_choice = random.choice(options)
                results = rps(player_choice, computer_choice)
            elif scissors_button.is_clicked(mouse_position):
                player_choice = "Scissor"
                computer_choice = random.choice(options)
                results = rps(player_choice, computer_choice)
            elif lizard_button.is_clicked(mouse_position):
                player_choice = "Lizard"
                computer_choice = random.choice(options)
                results = rps(player_choice, computer_choice)
            elif spock_button.is_clicked(mouse_position):
                player_choice = "Spock"
                computer_choice = random.choice(options)
                results = rps(player_choice, computer_choice)
    pygame.display.update()
pygame.quit()
