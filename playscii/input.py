import keyboard


class Input:
    "A class to handle pyplayscii key presses."
    pressed_keys = dict()

    @classmethod
    def get_key(cls, key) -> bool:
        "Returns True if the given key is pressed. Can be a keycode or a key name."
        if keyboard.is_pressed(key):
            cls.pressed_keys[key] = True
            return True
        else:
            cls.pressed_keys[key] = False
            return False

    @classmethod
    def get_key_down(cls, key) -> bool:
        if not keyboard.is_pressed(key):
            cls.pressed_keys[key] = False
            return False
        elif not cls.pressed_keys.get(key):
            cls.pressed_keys[key] = True
            return True
        else:
            return False
