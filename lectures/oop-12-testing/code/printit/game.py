import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BALL_RADIUS = 10

class DebugPrint:
    def __init__(self, screen):
        self.font = pygame.font.SysFont("", 16)
        self.messages = {}
        self.screen = screen

    def print(self):
        current_y_pos = self.font.get_linesize()
        for key in self.messages:
            text = f"{key}: {self.messages[key]}"
            text_image = self.font.render(text, True, (0,255,0))
            self.screen.blit(text_image, (10, current_y_pos))
            current_y_pos += self.font.get_linesize()

    def value(self, description, value):
        self.messages[description] = value


def mainloop(screen):
    ball_pos = [10,10]
    d = DebugPrint(screen)
    clock = pygame.time.Clock()
    debug = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    debug = not debug
        time_taken = clock.tick(60)
        screen.fill((0,0,0))
        ball_pos[0] += 1
        ball_pos[1] += 1
        ball_pos[0] %= SCREEN_WIDTH
        ball_pos[1] %= SCREEN_HEIGHT
        pygame.draw.circle(screen, (255,0,0), ball_pos, BALL_RADIUS)

        if debug:
            # Debug info
            d.value("Ball position", ball_pos)
            d.value("Keys pressed", pygame.mouse.get_pressed())
            d.value("Mouse position", pygame.mouse.get_pos())
            d.print()

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    mainloop(surf)
