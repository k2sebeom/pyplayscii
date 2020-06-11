import keyboard


class Input:
    pressed_keys = dict()

    @classmethod
    def get_key(cls, key):
        if keyboard.is_pressed(key):
            cls.pressed_keys[key] = True
            return True
        else:
            cls.pressed_keys[key] = False
            return False

    @classmethod
    def get_key_down(cls, key):
        if not keyboard.is_pressed(key):
            cls.pressed_keys[key] = False
            return False
        elif not cls.pressed_keys.get(key):
            cls.pressed_keys[key] = True
            return True
        else:
            return False
