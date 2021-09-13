import curses
from _curses import error as size_error
from abc import ABC, abstractmethod
import time
import typing


class GameManager(ABC):
    def __init__(self, screen_size: typing.Tuple[int, int]):
        self.__game_objects = []
        self.width: int = screen_size[0]
        self.height: int = screen_size[1]
        self.__board: list = []
        self.__clear_board()
        self.__stdscr = None
        self.__flags: dict = {'quit': False}
        self.delta_time = 0
        self.__old_time = time.time()
        self.__title: str = ""

    def find(self, obj_class: 'GameObject') -> list['GameObject']:
        return [
            game_object
            for game_object in self.__game_objects
            if isinstance(game_object, obj_class)
        ]

    def add_object(self, obj: 'GameObject'):
        self.__game_objects.append(obj)

    def set_title(self, title: str):
        "Sets the pyplayscii window title."
        self.__title = title

    def start(self):
        "Starts the pyplayscii window and game."
        self.__stdscr = curses.initscr()
        self.setup()
        while True:
            if self.__flags['quit']:
                break
            curr_time = time.time()
            self.delta_time = curr_time - self.__old_time
            self.__old_time = curr_time
            self.update()
            self.__clear_board()
            for game_object in self.__game_objects:
                game_object.delta_time = self.delta_time
                game_object.update()
                game_object.draw(self.__board)
            try:
                self.__update_board()
            except size_error:
                curses.resize_term(self.height + 5, self.width + 10)
                self.__stdscr.refresh()
            time.sleep(0.02)

    def set_flag(self, flag_key, flag_value):
        "Sets a GameManager flag."
        if flag_key not in self.__flags:
            raise KeyError
        else:
            self.__flags[flag_key] = flag_value

    def quit(self):
        "Closes game and exits pyplayscii."
        self.set_flag('quit', True)

    def __clear_board(self):
        "Clears the graphical board."
        self.__board = [[" " for _ in range(self.width)]
                        for _ in range(self.height)]

    def __update_board(self):
        "Updates the graphical board."
        self.__stdscr.clear()
        padding = ' ' * ((curses.COLS - self.width) // 2)
        self.__stdscr.addstr(padding + '-' * (self.width + 2) + '\n')
        self.__stdscr.addstr(padding + f"|{self.__title:^{self.width}}|\n")
        self.__stdscr.addstr(padding + '-' * (self.width + 2) + '\n')
        for row in self.__board:
            self.__stdscr.addstr(padding + '|')
            for curr in row:
                self.__stdscr.addstr(f"{curr:^1}")
            self.__stdscr.addstr('|\n')
        self.__stdscr.addstr(padding + '-' * (self.width + 2))
        self.__stdscr.refresh()

    def get_flag(self, flag_key):
        "Returns the corresponding flag value."
        if flag_key not in self.__flags:
            raise KeyError
        else:
            return self.__flags[flag_key]

    @property
    def game_objects(self):
        return self.__game_objects

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def update(self):
        pass


class GameObject(ABC):
    "An abstract base class for pyplayscii game objects."

    def __init__(self,
                 pos: typing.Tuple[int, int] = (0, 0),
                 render: str = '',
                 size: typing.Tuple[int, int] = (0, 0)):
        self.x: int = pos[0]
        self.y: int = pos[1]
        self.render: str = render
        self.delta_time = 0
        self.width: int = size[0]
        self.height: int = size[1]
        self.__parent = None

    @property
    def parent(self):
        return self.__parent

    def draw(self, board: list):
        "Draws this GameObject on the graphical board."
        render_text = self.render.split('\n')
        x, y = int(self.x), int(self.y)
        if len(render_text) == 1 and render_text[0] == '':
            return
        for i in range(len(render_text)):
            if not (0 <= y - i < len(board)):
                break
            for j in range(len(render_text[i])):
                if not (0 <= x + j < len(board[0])):
                    continue
                board[~(y - i)][x + j] = render_text[i][j]

    def on_collision(self, other: 'GameObject') -> bool:
        "Returns True if the GameObject has collided with another GameObject."
        return (
            other.x - other.width <= self.x
            <= other.x + other.width
        ) and (
            other.y - other.height <= self.y
            <= other.y + other.height
        )

    def update(self):
        pass
