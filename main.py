import pygame
import os


class Board:
    def __init__(self, name_karta, cell_size=50):
        self.karta = load_level(name_karta)
        self.width = len(self.karta)
        self.height = len(self.karta[1])
        self.board = [[0] * width for i in range(height)]
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                a = (i + 1) * self.cell_size
                b = (j + 1) * self.cell_size
                image1 = pygame.transform.scale(pygame.image.load(os.path.join('data', "centre.png")),
                                                (self.cell_size, self.cell_size))
                screen.blit(image1, (a, b))
                pygame.draw.rect(screen, pygame.Color("brown"), (a, b, self.cell_size, self.cell_size), 1)
                if i + 1 == self.width and j == 0:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "rt_edge.png")),
                                                    (self.cell_size, self.cell_size))
                    screen.blit(image2, (a + self.cell_size, b - self.cell_size))
                elif i == 0 and j == 0:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "lt_edge.png")),
                                                    (self.cell_size, self.cell_size))
                    screen.blit(image2, (a - self.cell_size, b - self.cell_size))
                elif i == 0 and j + 1 == self.height:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "ld_edge.png")),
                                                    (self.cell_size, self.cell_size))
                    screen.blit(image2, (a - self.cell_size, b + self.cell_size))
                elif i + 1 == self.width and j + 1 == self.height:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "rd_edge.png")),
                                                    (self.cell_size, self.cell_size))
                    screen.blit(image2, (a + self.cell_size, b + self.cell_size))
                if i == 0:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "left_edge.png")),
                                                    (self.cell_size, self.cell_size + 1))
                    screen.blit(image2, (a - self.cell_size, b))
                if j == 0:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "top_edge.png")),
                                                    (self.cell_size + 1, self.cell_size))
                    screen.blit(image2, (a, b - self.cell_size))
                if j + 1 == self.height:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "down_edge.png")),
                                                    (self.cell_size + 1, self.cell_size))
                    screen.blit(image2, (a, b + self.cell_size))
                if i + 1 == self.width:
                    image2 = pygame.transform.scale(pygame.image.load(os.path.join('data', "right_edge.png")),
                                                    (self.cell_size, self.cell_size + 1))
                    screen.blit(image2, (a + self.cell_size, b))
                if self.karta[j][i] == '*':
                    image0 = pygame.transform.scale(pygame.image.load(os.path.join('data', "sunduk.png")),
                                                    (self.cell_size, self.cell_size))
                    size_sunduk = self.cell_size - self.cell_size // 5
                    image1 = pygame.transform.scale(image0, (size_sunduk, size_sunduk))
                    screen.blit(image1, (a + self.cell_size // 10, b + self.cell_size // 10))

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.cell_size) // self.cell_size
        cell_y = (mouse_pos[1] - self.cell_size) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        pass

def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    board = Board("karta.txt", 100)
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == __main__ :
    main()
