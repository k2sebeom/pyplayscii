from playscii.input import Input
from playscii import GameObject, GameManager


class MoveAManager(GameManager):
    def __init__(self):
        super().__init__((80, 20))
        self.a_object = GameObject(pos=(40, 10), render='A')

    def setup(self):
        self.add_object(self.a_object)

    def update(self):
        if Input.get_key('left'):
            self.a_object.x -= 10 * self.delta_time
        if Input.get_key('right'):
            self.a_object.x += 10 * self.delta_time
        if Input.get_key('up'):
            self.a_object.y += 10 * self.delta_time
        if Input.get_key('down'):
            self.a_object.y -= 10 * self.delta_time
        if Input.get_key('q'):
            self.quit()


if __name__ == '__main__':
    manage = MoveAManager()
    manage.start()
