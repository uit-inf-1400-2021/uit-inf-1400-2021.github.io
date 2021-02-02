''' Module for Particles, used for making fountains '''

import random
import pygame
import pympler.tracker

SCREEN_X = 800
SCREEN_Y = 800
PARTICLE_IMAGE = "particle.png"
PARTICLES_PER_SECOND = 20
GRAVITY = 5000

class Particle:
    ''' Representing a single particle '''
    def __init__(self, position, direction):
        self.position = pygame.math.Vector2(position)
        self.direction = pygame.math.Vector2(direction)
        self.image = load_image(PARTICLE_IMAGE)

    def draw(self, surface):
        ''' Draw the particle onto the given surface '''
        surface.blit(self.image, self.position)

    def move(self, time_delta):
        ''' Update the position, speed and direction based on time_delta '''
        self.position += self.direction * time_delta
        self.direction.y += (GRAVITY  * time_delta)

def load_image(image_filename):
    ''' Reads image from image_filename and returns converted pygame surface '''
    return pygame.image.load(image_filename).convert_alpha()

def mainloop():
    ''' Run the particle fountain in a window '''
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    particles = []
    clock = pygame.time.Clock()
    frame_counter = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    mem = pympler.tracker.SummaryTracker()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                mem.print_diff()
                exit()
            elif event.type == pygame.USEREVENT:
                text = "{} frames last second, with {} particles active"
                text = text.format(frame_counter, len(particles))
                print(text)
                frame_counter = 0
            elif event.type == pygame.KEYDOWN:
                import pdb
                pdb.set_trace()
        frame_counter += 1
        time_passed = clock.tick(200) / 1000.0

        for _ in range(int(2000 * time_passed)):
            particles.append(Particle(
                (SCREEN_X / 2, SCREEN_Y / 2),
                (random.randint(-500, 500), -(500 + random.random()*1000))))

        screen.fill((0, 0, 0))
        for particle in particles:
            particle.move(time_passed)
            particle.draw(screen)
            if particle.position.y > SCREEN_Y:
                particles.remove(particle)
        pygame.display.update()


if __name__ == "__main__":
    mainloop()
