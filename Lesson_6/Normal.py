# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Character:
    def __init__(self, name, health=100, damage=10, armor=2, lvl=1):
        self._health = health
        self._damage = damage
        self._armor = armor
        self._name = name
        self._lvl = lvl

    def get_health(self):
        return self._health

    def get_damage(self):
        return self._damage

    def get_armor(self):
        return self._armor

    def get_level(self):
        return self._lvl

    def _calc_damage(self, enemy):
        return self._damage / enemy.get_armor()

    def attack(self, enemy):
        damage = self._calc_damage(enemy)
        enemy.hit(damage)

    def hit(self, damage):
        self._set_health(self._health - damage)

    def _set_health(self, value):
        self._health = value


class Player(Character):

    def __init__(self, name, health, armor, damage):
        super().__init__(name, health, armor, damage)
        self._exp = 0
        self._exp_to_levelup = 100

    def get_experience(self):
        return self._exp

    def _is_next_lvl(self):
        if self._exp >= self._exp_to_levelup:
            self._lvl += 1
            self._exp = 0
            self._exp_to_levelup *= 2

    def increase_exp(self, value):
        if value > 0:
            self._exp = self._exp + value
            self._is_next_lvl()


class Enemy(Character):
    def __init__(self, name, lvl=1):
        super().__init__(name)
        self.lvl = lvl
        self._health = self._health * lvl
        self._armor = self._armor * lvl
        self._damage = self._damage * lvl


class Game:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last_attacker = self._player
        while self._player.get_health() > 0 and self._enemy.get_health() > 0:
            if last_attacker == self._player:
                self._enemy.attack(self._player)
                last_attacker = self._enemy
            else:
                self._player.attack(self._enemy)
                last_attacker = self._player

        if self._player.get_health() > 0:
            print('Вы победили')
        else:
            print('Вы проиграли')



player = Player('Roland', 100, 20, 1)
enemy = Enemy('NPC')
game = Game(player, enemy)
game.start()

