import string

NROWS = 103 #7
NCOLS = 101 #11
MAX_STEPS = 100

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
    robot.evolve()
    robots.append(robot)

robots_per_quadrant = {'top left': 0, 'top right': 0, 'bottom left': 0, 'bottom right': 0}
for robot in robots:
    quadrant = robot.check_quandrant()
    # print(robot.x, robot.y, quadrant)
    if quadrant == 'middle':
        continue
    robots_per_quadrant[quadrant] += 1

safety_factor = 1
for quadrant in robots_per_quadrant:
    safety_factor *= robots_per_quadrant[quadrant]

print(safety_factor)