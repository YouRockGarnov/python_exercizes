import json
import functools
import sys


class Hero:
    max_values = {'Sorceress': {'max_health': 50, 'max_defence_power': 42,
                                'max_attack_power': 90, 'max_mana': 200},
                  'Knight': {'max_health': 100, 'max_defence_power': 170,
                             'max_attack_power': 150},
                  'Barbarian': {'max_health': 120, 'max_defence_power': 150,
                                'max_attack_power': 180},
                  'Warlock': {'max_health': 70, 'max_defence_power': 50,
                              'max_attack_power': 100, 'max_mana': 180}}

    experience_after_kill = 4

    def __init__(self, json_str, hero_id):
        data = json.loads(json_str)

        hero = data['armies'][hero_id]
        self.race = hero['race']
        self.lord = hero['lord']
        self.name = hero_id

        self.health = min(Hero.max_values[self.race]['max_health'],
                          hero['health'])
        self._attack_power = min(Hero.max_values[self.race]
                                 ['max_attack_power'], hero['attack'])

        self._defence_power = min(Hero.max_values[self.race]
                                  ['max_defence_power'], hero['defence'])
        self.experience = hero['experience']

        if 'max_mana' in Hero.max_values[self.race].keys():
            self.mana = min(Hero.max_values[self.race]['max_mana'],
                            hero['mana'])
        else:
            self.mana = 0

    def load_from_json(self):
        json.loads()

    def dead_check(self):
        def wrapped(func):
            def wrapper(*args, **kwargs):
                pass

            if self.is_dead():
                return wrapper
            else:
                return func

        return wrapped

    def attack_somebody(self, power):
        if power > self._attack_power or self.is_dead():
            return 0
        else:
            self.experience += 1
            self._attack_power -= power
            return power

    def cast_spell(self, power):  # TODO warrier can't cast spells!!!
        if self.race != 'Knight' and self.race != 'Barbarian'\
                and not self.is_dead():
            self.experience += 1

            if power > self.mana or self.is_dead():
                return 0
            else:
                self.mana -= power
                return power

    def defend_myself(self, damage):
        if not self.is_dead():
            self.experience += 1

            old_defence_power = self._defence_power
            self._defence_power = max(0, self._defence_power - damage)

            damage -= old_defence_power

            if self._defence_power == 0:
                self.health -= damage

    def heal_myself(self, heal):
        if not self.is_dead():
            self.health = min(self.health + heal,
                              self.max_values[self.race]['max_health'])

    def is_dead(self):
        return self.health <= 0

    def calculate_score(self):
        # print(self.lord, self.health, self._defence_power,
        # self.mana, self.experience)

        if self.is_dead():
            return 0
        else:
            return self.experience + 2*self._defence_power + \
                   3*self._attack_power + 10*self.mana


class Game:
    def __init__(self, json_str):
        self.data = json.loads(json_str)
        self.heroes = dict()
        self.battle_steps = self.data["battle_steps"]

        for id in self.data['armies']:
            # if self.heroes.get(hero.lord) != None:
            #     self.heroes[hero.lord].append(hero)
            # else:
            #     self.heroes[hero.lord] = [hero]

            self.heroes[id] = Hero(json_str, id)

    def fight(self):
        for step in self.battle_steps:
            # self.print_all()

            if step['action'] == 'attack':
                attack_power = self.heroes[step['id_from']]\
                    .attack_somebody(step['power'])
                self.heroes[step['id_to']].defend_myself(attack_power)

                if self.heroes[step['id_to']].is_dead():
                    self.heroes[step['id_from']].experience\
                        += Hero.experience_after_kill

            elif step['action'] == 'cast_damage_spell':
                attack_power = self.heroes[step['id_from']]\
                    .cast_spell(step['power'])
                self.heroes[step['id_to']].defend_myself(attack_power)

                if self.heroes[step['id_to']].is_dead():
                    self.heroes[step['id_from']].experience\
                        += Hero.experience_after_kill

            else:
                heal_power = self.heroes[step['id_from']]\
                    .cast_spell(step['power'])
                self.heroes[step['id_to']].heal_myself(heal_power)

    def print_all(self):
        for hero_id in self.heroes.keys():
            print(self.heroes[hero_id].lord, self.heroes[hero_id].health,
                  self.heroes[hero_id]._defence_power,
                  self.heroes[hero_id].mana, self.heroes[hero_id].experience)
            sys.stdout.flush()

        print()

    def play(self):
        self.fight()
        self.winner = self.find_winner()

    def find_winner(self):
        scores = dict()
        for hero in self.heroes.values():
            if hero.lord in scores.keys():
                scores[hero.lord] += hero.calculate_score()
            else:
                scores[hero.lord] = hero.calculate_score()

        # for item in scores.items():
        #     print(item[0], item[1])

        winner = None
        if len(scores) == 0:
            winner = 'unknown'
        else:
            winner = max(scores, key=scores.get)
            win_score = scores[winner]

            if list(scores.values()).count(win_score) > 1:
                winner = 'unknown'

        return winner


inp = input()
game = Game(inp)
game.play()
print(game.winner)
