from playscii import GameObject, GameManager
from playscii.input import Input


BALL = "    **    \n" \
       "   ****\n" \
       "    **"


class Ball(GameObject):
    def __init__(self):
        super().__init__(pos=(40, 10), render=BALL)
        self.vel = (10, 10)

    def update(self):
        self.x += self.vel[0] * self.delta_time
        self.y += self.vel[1] * self.delta_time


class BounceManager(GameManager):
    def __init__(self):
        super().__init__((80, 20))
        self.ball = Ball()

    def setup(self):
        self.add_object(self.ball)

    def update(self):
        if self.ball.x < 0 or self.ball.x > 74:
            self.ball.vel = (-self.ball.vel[0], self.ball.vel[1])
        if self.ball.y < 2 or self.ball.y > 20:
            self.ball.vel = (self.ball.vel[0], -self.ball.vel[1])

        if Input.get_key_down('q'):
            self.quit()


if __name__ == "__main__":
    manager = BounceManager()
    manager.start()
