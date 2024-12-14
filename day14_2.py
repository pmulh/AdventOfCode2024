import string
import numpy as np
from matplotlib import pyplot as plt

NROWS = 103 #7
NCOLS = 101 #11
MAX_STEPS = 1

# with open('day14_test_input.txt') as f:
with open('day14_input.txt') as f:
    data = f.read()

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


    def evolve(self):
        # print(self.x, self.y, self.vx, self.vy, NROWS, NCOLS)
        step = 0
        while step < MAX_STEPS:
            self.x = self.x + self.vx
            if self.x < 0:
                self.x = NCOLS + self.x
            elif self.x >= NCOLS:
                self.x = self.x - NCOLS

            self.y = self.y + self.vy
            if self.y < 0:
                self.y = NROWS + self.y
            elif self.y >= NROWS:
                self.y = self.y - NROWS
            step += 1


    def check_quandrant(self):
        if self.x < NCOLS // 2:
            if self.y < NROWS // 2:
                return 'top left'
            if self.y > NROWS / 2:
                return 'bottom left'

        if self.x > NCOLS / 2:
            if self.y < NROWS // 2:
                return 'top right'
            if self.y > NROWS / 2:
                return 'bottom right'
        return 'middle'


lines = data.strip('\n').split('\n')
robots = []
for line in lines:
    x, y = ''.join([i for i in line if i in set(string.digits + ',- ')]).split(' ')[0].split(',')
    vx, vy = ''.join([i for i in line if i in set(string.digits + ',- ')]).split(' ')[1].split(',')
    robot = Robot(int(x), int(y), int(vx), int(vy))
    # robot.evolve()
    robots.append(robot)

for step in range(0, 10000):
    for robot in robots:
        robot.evolve()

    grid = np.empty(shape=(NCOLS, NROWS))
    grid.fill(int(0))
    for robot in robots:
        grid[(robot.x, robot.y)] = int(1)

    fig = plt.imshow(grid, interpolation='nearest')
    step_str = str(step)
    fig.write_png(f'/Users/peter/Downloads/test_{step_str.zfill(5)}.png')
