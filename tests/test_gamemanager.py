import unittest
from playscii.playscii import GameManager, GameObject


class TestGameManager(unittest.TestCase):

    class TestManager(GameManager):
        def __init__(self, size):
            super().__init__(size)

        def setup(self):
            pass

        def update(self):
            pass

    def setUp(self) -> None:
        self.game_manager = self.TestManager((10, 10))

    def tearDown(self) -> None:
        del self.game_manager

    def test_add_object(self):
        obj = GameObject(pos=(1, 1))
        self.game_manager.add_object(obj)
        self.assertEqual(obj.x, self.game_manager.game_objects[0].x)
        self.assertEqual(obj.y, self.game_manager.game_objects[0].y)


if __name__ == '__main__':
    unittest.main()
