import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# --- Settings ---
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Zombie Shooter")

FPS = 60
PLAYER_SPEED = 5
BULLET_SPEED = 10
ZOMBIE_SPEED = 2
SPAWN_RATE = 30  # frames between spawns

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)a
BLACK = (0, 0, 0)

# --- Classes ---

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_w]: dy -= PLAYER_SPEED
        if keys[pygame.K_s]: dy += PLAYER_SPEED
        if keys[pygame.K_a]: dx -= PLAYER_SPEED
        if keys[pygame.K_d]: dx += PLAYER_SPEED
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(WIN.get_rect())  # Keep inside screen

        # Rotate to face mouse
        mx, my = pygame.mouse.get_pos()
        self.angle = math.degrees(math.atan2(my - self.rect.centery, mx - self.rect.centerx))

    def shoot(self):
        mx, my = pygame.mouse.get_pos()
        angle = math.atan2(my - self.rect.centery, mx - self.rect.centerx)
        bullet = Bullet(self.rect.centerx, self.rect.centery, angle)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 4))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.velx = math.cos(angle) * BULLET_SPEED
        self.vely = math.sin(angle) * BULLET_SPEED

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        if not WIN.get_rect().colliderect(self.rect):
            self.kill()


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), -20))
        elif side == "bottom":
            self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), HEIGHT + 20))
        elif side == "left":
            self.rect = self.image.get_rect(center=(-20, random.randint(0, HEIGHT)))
        else:
            self.rect = self.image.get_rect(center=(WIDTH + 20, random.randint(0, HEIGHT)))

    def update(self):
        # Move toward player
        dx, dy = player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
        self.rect.x += dx * ZOMBIE_SPEED
        self.rect.y += dy * ZOMBIE_SPEED


# --- Setup groups ---
all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(player)

clock = pygame.time.Clock()
frame_count = 0
score = 0
font = pygame.font.Font(None, 36)

# --- Game Loop ---
running = True
while running:
    clock.tick(FPS)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot()

    # Spawn zombies
    if frame_count % SPAWN_RATE == 0:
        z = Zombie()
        all_sprites.add(z)
        zombies.add(z)

    # Update
    all_sprites.update()

    # Collision: bullets hit zombies
    hits = pygame.sprite.groupcollide(zombies, bullets, True, True)
    score += len(hits)

    # Collision: zombies hit player
    if pygame.sprite.spritecollideany(player, zombies):
        running = False

    # Draw
    WIN.fill(BLACK)
    all_sprites.draw(WIN)

    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
