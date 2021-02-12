class MainClass:
    def __init__(self, resolution):
        main_loop()

    def initialize_pygame(self):
        pygame.init()
        self.screen = pygame.video.set_mode()

    def initialize_bricks(self):

    def main_loop(self):
        self.initialize_pygame()
        self.initialize_bricks()
        while True:
            self.check_collision()

class SubMain(MainClass):
    def __init__(self):
        self.name = "Underklasse"
        super().__init__((600,600))

