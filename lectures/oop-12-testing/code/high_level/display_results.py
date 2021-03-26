#!/usr/bin/env python3
'''
Reads a two-column space-seperated input on STDIN
With the first column as HHMMSS, and the 2nd as
a value
Plots the values as a function of time
Saves the data to temperatures.bmp
'''

import sys

import pygame

class DisplayResult:
    '''
    Class for plotting data using pygame, scaled to fit to the
    data
    '''
    def __init__(self):
        pygame.init()
        self._screen_size = 800
        self._screen = pygame.display.set_mode((self._screen_size,
                                                self._screen_size))
        self._point = pygame.Surface((3,3))
        self._point.fill((255,0,0))
        self.points = []
        self.minmax_x = [999999, -999999]
        self.minmax_y = [999999, -999999]

    def _update_minmax_points(self, new_point):
        x, y = new_point
        self.minmax_x[0] = min(x, self.minmax_x[0])
        self.minmax_x[1] = max(x, self.minmax_x[1])
        self.minmax_y[0] = min(y, self.minmax_y[0])
        self.minmax_y[1] = max(y, self.minmax_y[1])

    def _get_seconds(self, time):
        hour = int(time[:2])
        minute = int(time[2:4])
        second = int(time[4:])
        return second + (minute * 60) + (hour * 60 * 60)

    def _get_datapoint(self, line):
        timestamp, y = line.split()
        y = float(y)
        x = self._get_seconds(timestamp)
        return (x, y)

    def _update_scaling_factors(self):
        try:
            self.x_factor = self._screen_size / (self.minmax_x[1] - self.minmax_x[0])
        except ZeroDivisionError:
            self.x_factor = 1
        self.x_constant = self.minmax_x[0]

        try:
            self.y_factor = self._screen_size / (self.minmax_y[1] - self.minmax_y[0])
        except ZeroDivisionError:
            self.y_factor = 1
        self.y_constant = self.minmax_y[0]

    def _draw_screen(self):
        self._screen.fill((0,0,0))
        for p in self.points:
            real_x = int((p[0] - self.x_constant) * self.x_factor)
            real_y = int((p[1] - self.y_constant) * self.y_factor)
            self._screen.blit(self._point, (real_x, real_y))
        pygame.display.flip()

    def save_image(self, filename):
        '''
        Save the current graph to file.
        '''
        pygame.image.save(self._screen, filename)

    def new_data(self, line):
        '''
        Add a new data point to the graph.
        '''
        self.points.append(self._get_datapoint(line))
        self._update_minmax_points(self.points[-1])
        self._update_scaling_factors()
        self._draw_screen()


def mainloop():
    A = DisplayResult()
    for line in sys.stdin:
        A.new_data(line)
    A.save_image("temperatures.bmp")


if __name__ == "__main__":
    mainloop()

