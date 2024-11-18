import sys
import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 300, 550
GRID_SIZE = 25
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
COLORS = [RED, BLUE, GREEN, YELLOW, PURPLE, CYAN]

# Tetromino shapes
PREDEFINED_SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['..O..',
         '..O..',
         '..O..',
         '..O..',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['..O..',
         '.OO..',
         '..O..',
         '.....',
         '.....'],
        ['..O..',
         '.OOO.',
         '.....',
         '.....',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '.OO..',
         '.OO..',
         '.....']
    ]
]

# Dynamic Shape Generator
def generate_connected_shape():
    grid_size = 5
    shape = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    blocks = 4

    x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
    shape[y][x] = 'O'

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(blocks - 1):
        while True:
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < grid_size and 0 <= new_y < grid_size and shape[new_y][new_x] == '.':
                shape[new_y][new_x] = 'O'
                x, y = new_x, new_y
                break

    rotations = [shape]
    for _ in range(3):
        rotated = list(zip(*rotations[-1][::-1]))
        rotations.append([''.join(row) for row in rotated])
    return rotations

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)
        self.rotation = 0

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = None
        self.bag = []
        self.refill_bag()
        self.new_piece()
        self.game_over = False
        self.score = 0
        self.fall_speed = 800
        self.last_fall_time = pygame.time.get_ticks()

    def refill_bag(self):
        self.bag = PREDEFINED_SHAPES + [generate_connected_shape() for _ in range(2)]
        random.shuffle(self.bag)

    def new_piece(self):
        if not self.bag:
            self.refill_bag()
        self.current_piece = Tetromino(WIDTH // 2 // GRID_SIZE, -2, self.bag.pop(0))

    def valid_move(self, piece, dx, dy, rotation):
        for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    new_x = piece.x + j + dx
                    new_y = piece.y + i + dy
                    if new_x < 0 or new_x >= self.width or new_y >= self.height or (new_y >= 0 and self.grid[new_y][new_x]):
                        return False
        return True

    def lock_piece(self):
        for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    grid_x = self.current_piece.x + j
                    grid_y = self.current_piece.y + i
                    if grid_y >= 0:
                        self.grid[grid_y][grid_x] = self.current_piece.color
        self.clear_lines()
        self.new_piece()
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in lines_to_clear:
            del self.grid[i]
            self.grid.insert(0, [0 for _ in range(self.width)])
        self.score += len(lines_to_clear) * 100

    def rotate_piece(self):
        new_rotation = (self.current_piece.rotation + 1) % len(self.current_piece.shape)
        if self.valid_move(self.current_piece, 0, 0, 1):
            self.current_piece.rotation = new_rotation

    def update(self, current_time):
        if current_time - self.last_fall_time > self.fall_speed:
            if self.valid_move(self.current_piece, 0, 1, 0):
                self.current_piece.y += 1
                self.last_fall_time = current_time
            else:
                self.lock_piece()

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]:
                    pygame.draw.rect(screen, self.grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))
        for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O' and self.current_piece.y + i >= 0:
                    pygame.draw.rect(screen, self.current_piece.color, ((self.current_piece.x + j) * GRID_SIZE, (self.current_piece.y + i) * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def draw_game_over(screen):
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 4, HEIGHT // 2))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubbles The Dev - Tetris")
    game = Tetris(GRID_WIDTH, GRID_HEIGHT)
    clock = pygame.time.Clock()
    running = True

    while running:
        current_time = pygame.time.get_ticks()
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not game.game_over:
                if event.key == pygame.K_LEFT:
                    if game.valid_move(game.current_piece, -1, 0, 0):
                        game.current_piece.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0, 0):
                        game.current_piece.x += 1
                elif event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1
                        game.last_fall_time = current_time
                elif event.key == pygame.K_UP:
                    game.rotate_piece()

        if not game.game_over:
            game.update(current_time)
            game.draw(screen)
            draw_score(screen, game.score)
        else:
            draw_game_over(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
