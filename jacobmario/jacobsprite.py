import pygame

# Initialize Pygame
pygame.init()
BLACK = (0, 0, 0)

# Constants for window size, frames per second, and sprite scaling
SCREEN_WIDTH = 860
SCREEN_HEIGHT = 580
GROUND_HEIGHT = 500
FPS = 60
SCALE_FACTOR = 0.12

# Constants for player physics
GRAVITY = 1
JUMP_STRENGTH = -22

# Defining the block for collisions
BLOCK_WIDTH = 200
BLOCK_HEIGHT = 50
block_x = 645
block_y = 345

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Sheet Animation')
background_image = pygame.image.load("mariobg.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


def extract_sprites():
    sprites = []
    for i in range(8):
        sprite = scaled_spritesheet_image.subsurface((i * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
        sprites.append(sprite)
    return sprites


# Load and scale the jacob spritesheet image
spritesheet_image = pygame.image.load('jacobspritesheet.png').convert_alpha()
scaled_spritesheet_image = pygame.transform.scale(
    spritesheet_image,
    (int(spritesheet_image.get_width() * SCALE_FACTOR), int(spritesheet_image.get_height() * SCALE_FACTOR)))
SPRITE_WIDTH = scaled_spritesheet_image.get_width() // 8
SPRITE_HEIGHT = scaled_spritesheet_image.get_height()
jacobsprites = extract_sprites()

# goomba
spritesheet_image = pygame.image.load('goombasprite.png').convert_alpha()
scaled_spritesheet_image = pygame.transform.scale(
    spritesheet_image,
    (int(spritesheet_image.get_width() * 1), int(spritesheet_image.get_height() *1)))
SPRITE_WIDTH = scaled_spritesheet_image.get_width() // 8
SPRITE_HEIGHT = scaled_spritesheet_image.get_height()
goombasprites = extract_sprites()
# Load mushroom image
mushroom = pygame.image.load("mush.png")
pygame.transform.scale(
    mushroom,
    (int(mushroom.get_width() * 1), int(mushroom.get_height() * 1)))

# Import music and sound effects
pygame.mixer.music.load("Ground Theme.mp3")
pygame.mixer.music.play(-1)
jump_sound = pygame.mixer.Sound('maro-jump-sound-effect_1.mp3')
jump_sound.set_volume(0.1)
# welcome = pygame.mixer.Sound("sm64_mario_here_we_go.wav")
# pygame.mixer.music.play(welcome)
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprites, pos, *groups):
        super().__init__(*groups)
        self.sprites = sprites
        self.current_frame = 0
        self.image = self.sprites[self.current_frame]
        self.rect = self.image.get_rect(midbottom=pos)
        self.velocity_y = 0
        self.on_ground = True
        self.direction = "right"
        self.is_jumping = False
        self.onblock = False

    def idle(self):
        self.image = pygame.transform.flip(self.sprites[0], self.direction == "left", False)
        pygame.time.wait(10)

    def run(self):
        frame_index = 2 + (self.current_frame % 4)
        self.image = pygame.transform.flip(self.sprites[frame_index], self.direction == "left", False)
        self.current_frame = (self.current_frame + 1) % 4  # Loop through running frames
        pygame.time.wait(75)  # Run animation speed


class PlayableCharacter(AnimatedSprite):
    def __init__(self, sprites, pos, *groups):
        super().__init__(sprites, pos, *groups)

    def update(self):
        keys = pygame.key.get_pressed()
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Check if on the ground
        if self.rect.bottom >= GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.on_ground = True
            self.velocity_y = 0
            self.is_jumping = False
        if self.rect.bottom == GROUND_HEIGHT:
            self.onblock = False
        if keys[pygame.K_LEFT]:
            self.rect.x -= 25
            self.direction = "left"
            if not self.is_jumping:
                self.run()
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 25
            self.direction = "right"
            if not self.is_jumping:
                self.run()
        elif keys[pygame.K_SPACE] and self.on_ground or keys[pygame.K_SPACE] and self.onblock == True:
            self.jump()

        if self.is_jumping:
            self.image = pygame.transform.flip(self.sprites[5], self.direction == "left", False)

        if not self.is_jumping and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] or not keys[
            pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.onblock == True:
            self.idle()

        if self.rect.y + self.rect.height >= block_y and self.rect.x + self.rect.width >= block_x and self.rect.x <= block_x + BLOCK_WIDTH:
            if self.velocity_y >= 0 and self.rect.y < block_y:
                self.rect.y = block_y - self.rect.height
                self.velocity_y = 0
                self.onblock = True

        # Prevent the player from going out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def idle(self):
        self.image = pygame.transform.flip(self.sprites[0], self.direction == "left", False)
        pygame.time.wait(10)

    def run(self):
        frame_index = 2 + (self.current_frame % 4)
        self.image = pygame.transform.flip(self.sprites[frame_index], self.direction == "left", False)
        self.current_frame = (self.current_frame + 1) % 4  # Loop through running frames
        pygame.time.wait(75)  # Run animation speed

    def jump(self):
        self.velocity_y = JUMP_STRENGTH
        self.on_ground = False
        self.is_jumping = True
        jump_sound.play()


class NPC(AnimatedSprite):
    def __init__(self, sprites, pos, *groups):
        super().__init__(sprites, pos, *groups)
        self.direction = "left"
        self.velocity_x = 2

    def update(self):
        self.rect.x += self.velocity_x

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.velocity_x = -self.velocity_x
            if self.direction == "right":
                self.direction = "left"
            else:
                self.direction = "right"
            self.image = pygame.transform.flip(self.image, True, False)


# Game loop
def game_loop():
    running = True
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    jacob = PlayableCharacter(jacobsprites, (SCREEN_WIDTH // 2, SCREEN_HEIGHT), all_sprites)
    goomba = NPC(goombasprites, (SCREEN_WIDTH // 4, GROUND_HEIGHT), all_sprites)

    all_sprites.add(jacob, goomba)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        collisions = pygame.sprite.spritecollide(jacob, all_sprites, False)
        for sprite in collisions:
            if isinstance(sprite, NPC):
                jump_sound.play()
        screen.blit(background_image, (0, 0))  # Fill the screen with white background
        all_sprites.draw(screen)
        screen.blit(mushroom,(645,345))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
