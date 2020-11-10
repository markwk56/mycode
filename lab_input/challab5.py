#!/usr/bin/env python3


Heros = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}


char_name = input("Which character do you want to know about? (Flash, Batman, Superman) ").lower()

char_stat = input("What statistic do you wnat to know about? (Strength, speed, or intelligence) ").lower()




print(Heros[char_name] [char_stat])






