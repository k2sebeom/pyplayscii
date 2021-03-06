import unittest
from playscii.playscii import GameManager


class TestGameObject(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
