import curses
from _curses import error as size_error
from abc import ABC, abstractmethod
import time


class GameManager(ABC):
    def __init__(self, screen_size):
        self.__game_objects = []
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.__board = []
        self.__clear_board()
        self.__stdscr = None
        self.__flags = dict()
        self.__flags['quit'] = False
        self.delta_time = 0
        self.__old_time = time.time()
        self.__title = ""

    def find(self, obj_class):
        obj_with_class = []
        for game_object in self.__game_objects:
            if isinstance(game_object, obj_class):
                obj_with_class.append(game_object)
        return obj_with_class

    def add_object(self, obj):
        self.__game_objects.append(obj)

    def set_title(self, title):
        self.__title = title

    def start(self):
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
        if flag_key not in self.__flags:
            raise KeyError
        else:
            self.__flags[flag_key] = flag_value

    def quit(self):
        self.set_flag('quit', True)

    def __clear_board(self):
        self.__board = [[" " for _ in range(self.width)]
                        for _ in range(self.height)]

    def __update_board(self):
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
    def __init__(self, pos=(0, 0), render='', size=(0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.render = render
        self.delta_time = 0
        self.width = size[0]
        self.height = size[1]
        self.__parent = None

    @property
    def parent(self):
        return self.__parent

    def draw(self, board):
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

    def on_collision(self, other):
        return (
                       other.x - other.width <= self.x
                       <= other.x + other.width
               ) and (
                       other.y - other.height <= self.y
                       <= other.y + other.height
               )

    def update(self):
        pass
