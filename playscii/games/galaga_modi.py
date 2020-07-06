from playscii import GameManager, GameObject
from threading import Timer
from random import randint

JET_RENDER = "  /\\\n" \
             "  []\n" \
             "< () >\n" \
             "  <>"

ENEMY_RENDER = " __\n" \
               "<oo>"

WIDTH, HEIGHT, SPEED, ENEMY_SPEED = 50, 25, 30, 5


class GalagaManager(GameManager):
    def __init__(self, gyro, button, led):
        super().__init__((WIDTH, HEIGHT))
        self.gyro = gyro
        self.button = button
        self.led = led
        self.time = 0
        self.jet = Jet(pos=(WIDTH // 2, 3))
        self.cooling = False
        self.enemies = []
        self.bullets = []
        self.spawn_time = 3
        self.score = 0
        self.scoreboard = GameObject((WIDTH // 2, HEIGHT - 2), str(self.score))

    def setup(self):
        self.time = 0
        self.add_object(self.jet)
        self.set_title("Galaga with PyMODI")
        self.led.green = 255
        self.add_object(self.scoreboard)

    def update(self):
        self.time += self.delta_time

        if self.time > self.spawn_time:
            self.time = 0
            self.spawn_enemy()
        self.scoreboard.render = str(self.score)
        pitch = self.gyro.pitch
        if pitch < 5 and self.jet.x < self.width - self.jet.width:
            self.jet.x += SPEED * self.delta_time
        elif pitch > 5 and self.jet.x > 0:
            self.jet.x -= SPEED * self.delta_time
        if self.button.pressed:
            if not self.cooling:
                self.cooling = True
                self.jet.shoot(self)
                Timer(0.2, self.cool_off).start()
        if self.jet.check_death(self.enemies):
            self.set_title("GAME OVER")
            self.led.rgb = 255, 0, 0
            self.quit()
            return
        self.clean_enemies()
        self.clean_bullets()

    def cool_off(self):
        self.cooling = False

    def spawn_enemy(self):
        enemy = Enemy((randint(0, WIDTH - 6), HEIGHT))
        self.add_object(enemy)
        self.enemies.append(enemy)

    def clean_enemies(self):
        i = 0
        while i < len(self.enemies):
            enemy = self.enemies[i]
            if enemy.dead or enemy.check_death(self.bullets):
                self.enemies.pop(i)
                self.score += 1
                if self.spawn_time > 0.7:
                    self.spawn_time -= 0.1
                self.game_objects.remove(enemy)
            else:
                i -= -1

    def clean_bullets(self):
        i = 0
        while i < len(self.bullets):
            bullet = self.bullets[i]
            if bullet.hit:
                self.bullets.pop(i)
                self.game_objects.remove(bullet)
            else:
                i -= -1


class Bullet(GameObject):
    def __init__(self, pos, render):
        super().__init__(pos, render, (2, 2))
        self.hit = False

    def update(self):
        if self.y < HEIGHT:
            self.y += 20 * self.delta_time
        else:
            self.hit = True


class Jet(GameObject):
    def __init__(self, pos):
        super().__init__(pos, JET_RENDER, (4, 2))

    def update(self):
        pass

    def shoot(self, manager):
        bullet = Bullet((self.x, self.y), '   |')
        manager.add_object(bullet)
        manager.bullets.append(bullet)

    def check_death(self, enemies):
        for enemy in enemies:
            if self.on_collision(enemy):
                return True
        return False


class Enemy(GameObject):
    def __init__(self, pos):
        super().__init__(pos, ENEMY_RENDER, (4, 2))
        self.dead = False

    def update(self):
        if self.y >= -5:
            self.y -= ENEMY_SPEED * self.delta_time
        else:
            self.dead = True

    def check_death(self, bullets):
        for bullet in bullets:
            if bullet.on_collision(self):
                bullet.hit = True
                return True
        return False
