from random import randint, choice


class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.boost = 0

    def apply_boost(self):
        self.boost += 5
        print(f"Підсилення активовано! +5 до наступної атаки")


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 15)

    def attack(self):
        damage = self.attack_power + randint(1, 10) + self.boost
        self.boost = 0
        return damage


class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe", 20)

    def attack(self):
        damage = self.attack_power + randint(3, 12) + self.boost
        self.boost = 0
        return damage


class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", 10)
        self.range_power = 5

    def attack(self):
        damage = (
            self.attack_power
            + randint(5, 15)
            + self.range_power
            + self.boost
        )
        self.boost = 0
        return damage

    def reload(self):
        self.range_power += 1
        print(f"Дальність збільшена! range_power = {self.range_power}")


weapons = [Sword(), Axe(), Bow()]
player_weapon = choice(weapons)

enemy_hp = 100

print("=== GAME START ===")
print(f"Ваша зброя: {player_weapon.name}")

while enemy_hp > 0:
    print("\n-------------------")
    print(f"HP ворога: {enemy_hp}")

    print("\nОберіть дію:")
    print("1 - Атакувати")
    print("2 - Підсилити зброю")

    if isinstance(player_weapon, Bow):
        print("3 - Reload лука")

    action = input("Ваш вибір: ")

    if action == "1":
        damage = player_weapon.attack()
        enemy_hp -= damage

        print(f"\nВи нанесли {damage} шкоди!")

    elif action == "2":
        player_weapon.apply_boost()

    elif action == "3" and isinstance(player_weapon, Bow):
        player_weapon.reload()

    else:
        print("Невірна дія!")

    if enemy_hp <= 0:
        print("\nВорог переможений!")
        break