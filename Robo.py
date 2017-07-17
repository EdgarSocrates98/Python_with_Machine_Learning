import random

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Reward(Point):

    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name

    def __str__(self):
        return '<%s, %s>: %s' % (self.x, self.y, self.name)

    def __repr__(self):
        return 'Reward %s' % str(self)

class Robot(Point):

    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('ErRoR: Invalid Movement  /\ ')

    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('ErRoR: Invalid Movement  \/')

    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('ErRoR: Invalid Movement  <--')

    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('ErRoR: Invalid Movement  -->')

def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print("The R2-D2 find: %s" % reward.name)
            ok = True
    return ok

r1 = Reward(random.randint(0, 10), random.randint(0, 10), 'coin')
r2 = Reward(random.randint(0, 10), random.randint(0, 10), 'gas')
r3 = Reward(random.randint(0, 10), random.randint(0, 10), 'metal')
r4 = Reward(random.randint(0, 10), random.randint(0, 10), 'tools')

rewards = [r1, r2, r3, r4]
