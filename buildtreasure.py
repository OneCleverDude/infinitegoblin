
from random import *
import json

with open('items.json') as json_file:
    dataItems = json.load(json_file)


def build_horde(treasure_type, treasure_level):

    def build_coins(mod):
        coin_treasure = str(int(mod[6] * (random() * mod[7] + 1)) * mod[8]) + "gp, " \
                        + str(int(mod[3] * (random() * mod[4] + 1)) * mod[5]) + "sp, " \
                        + str(int(mod[0] * (random() * mod[1] + 1)) * mod[2]) + "cp, "
        return coin_treasure

    def build_gems(mod):
        eligible_gems = ([x for x in dataItems[mod]])
        gem_treasure = eligible_gems[int(random() * len(eligible_gems))]['gemName'] + ', '
        return gem_treasure

    def build_potions(mod):
        potion_treasure = ""
        how_many_potions = int(mod[0])
        while how_many_potions > 0:
            if (random() * 100) < 41:
                eligible_pots = ([x for x in dataItems["commonPotion0"]])
                select_pot = random()*100
                if select_pot < 15:
                    pot_index = 0
                elif select_pot < 29:
                    pot_index = 1
                elif select_pot < 45:
                    pot_index = 2
                elif select_pot < 59:
                    pot_index = 3
                elif select_pot < 73:
                    pot_index = 4
                elif select_pot < 87:
                    pot_index = 5
                else:
                    pot_index = 6
            else:
                if (random() * 100) < 76:
                    eligible_pots = ([x for x in dataItems["commonPotion1"]])
                    select_pot = random() * 100
                    if select_pot < 5:
                        pot_index = 0
                    elif select_pot < 15:
                        pot_index = 1
                    elif select_pot < 20:
                        pot_index = 2
                    elif select_pot < 28:
                        pot_index = 3
                    elif select_pot < 34:
                        pot_index = 4
                    elif select_pot < 42:
                        pot_index = 5
                    elif select_pot < 48:
                        pot_index = 6
                    elif select_pot < 56:
                        pot_index = 7
                    elif select_pot < 61:
                        pot_index = 8
                    elif select_pot < 65:
                        pot_index = 9
                    elif select_pot < 69:
                        pot_index = 10
                    elif select_pot < 73:
                        pot_index = 11
                    elif select_pot < 77:
                        pot_index = 12
                    elif select_pot < 82:
                        pot_index = 13
                    elif select_pot < 88:
                        pot_index = 14
                    elif select_pot < 93:
                        pot_index = 15
                    else:
                        pot_index = 16
                else:
                    eligible_pots = ([x for x in dataItems["uncommonPotion1"]])
                    select_pot = random() * 100
                    if select_pot < 5:
                        pot_index = 0
                    elif select_pot < 12:
                        pot_index = 1
                    elif select_pot < 17:
                        pot_index = 2
                    elif select_pot < 21:
                        pot_index = 3
                    elif select_pot < 27:
                        pot_index = 4
                    elif select_pot < 31:
                        pot_index = 5
                    elif select_pot < 42:
                        pot_index = 6
                    elif select_pot < 50:
                        pot_index = 7
                    elif select_pot < 54:
                        pot_index = 8
                    elif select_pot < 59:
                        pot_index = 9
                    elif select_pot < 65:
                        pot_index = 10
                    elif select_pot < 69:
                        pot_index = 11
                    elif select_pot < 76:
                        pot_index = 12
                    elif select_pot < 81:
                        pot_index = 13
                    elif select_pot < 85:
                        pot_index = 14
                    elif select_pot < 93:
                        pot_index = 15
                    else:
                        pot_index = 16
            potion_treasure += "<b>" + eligible_pots[pot_index]['potionName'] + ' potion</b>, '
            how_many_potions -= 1
        return potion_treasure

    def build_scrolls(mod):
        # TODO: Make the scroll chance equal to the charts here:
        # http://paizo.com/pathfinderRPG/prd/ultimateEquipment/appendix.html#treasure-values-per-encounter-table
        scroll_treasure = ""
        how_many_scrolls = int(mod[0])
        while how_many_scrolls > 0:
            scroll_roll = random() * 100
            scroll_type_roll = random() * 100
            scroll_type = 'uncommonDivine'
            if scroll_type_roll < 46:
                # Arcane Common
                scroll_type = 'commonArcane'
                scroll_treasure += '<b>Arcane scroll of '
            elif scroll_type_roll < 61:
                # Arcane Uncommon
                scroll_type = 'uncommonArcane'
                scroll_treasure += '<b>Arcane scroll of '
            elif scroll_type_roll < 91:
                # Divine Common
                scroll_type = 'commonDivine'
                scroll_treasure += '<b>Divine scroll of '
            else:
                # Divine Uncommon  (also the default value)
                scroll_treasure += '<b>Divine scroll of '
            if scroll_roll < 16:
                # Spell level 0
                scroll_type += '0'
            elif scroll_roll < 61:
                # Spell level 1
                scroll_type += '1'
            else:
                # Spell level 2
                scroll_type += '2'
            eligible_scrolls = [x for x in dataItems[scroll_type]]
            scroll_treasure += eligible_scrolls[int(random() * len(eligible_scrolls))]['spellName'] + '</b>, '
            how_many_scrolls -= 1
        return scroll_treasure

    eligible_wpns = ([x for x in dataItems["Weapons"]])
    treasure_horde = ""
    if treasure_type == 'A':
        treasure_horde = "Pouch with "
        coin_mod = 1, 1, 0, 1, 1, 0, 1, 1, 0
        if treasure_level == 1:
            coin_mod = 5, 10, 1, 3, 4, 1, 1, 1, 0
        if treasure_level == 2:  # 2d6*10cp, 4d8sp, 1d4gp
            coin_mod = 2, 6, 10, 4, 8, 1, 1, 4, 1
        if treasure_level == 3:  # 5d10*10cp, 5d10sp, 1d8gp
            coin_mod = 5, 10, 10, 5, 10, 1, 1, 8, 1
        treasure_horde += build_coins(coin_mod)

    if treasure_type == 'B':
        gem_mod = "gem1"
        treasure_horde = "Sack of "
        treasure_horde += build_gems(gem_mod)
        if treasure_level == 2:  # 2d6*10cp, 4d8sp, 1d4gp
            coin_mod = 2, 6, 10, 4, 8, 1, 1, 4, 1
            treasure_horde += build_coins(coin_mod)
        if treasure_level == 3:  # 1d1*0cp, 5d10sp, 1d4gp
            coin_mod = 1, 1, 0, 5, 10, 1, 1, 4, 1
            treasure_horde += build_gems(gem_mod)
            treasure_horde += build_coins(coin_mod)

    if treasure_type == 'C':
        treasure_horde = "Grade 1 Art Object, "
        if treasure_level == 2:
            treasure_horde = "Grade 2 Art Object, "
        if treasure_level == 3:
            treasure_horde = "Grade 1 Art Object, Grade 1 Art Object, "

    if treasure_type == 'D':
        coin_mod = 1, 1, 0, 3, 6, 10, 4, 4, 1
        scroll_mod = 1, 0
        potion_mod = 0, 0
        if treasure_level == 2:  # 1d1*0 cp, 2d4*10sp, 2d4gp
            coin_mod = 1, 1, 0, 2, 4, 10, 2, 4, 1
            scroll_mod = 0, 0
            potion_mod = 1, 0
        if treasure_level == 3:  # 1d1*0 cp, 4d6*10sp, 3d10gp
            coin_mod = 1, 1, 0, 4, 6, 10, 3, 10, 1
            scroll_mod = 1, 0
            potion_mod = 1, 0
        treasure_horde = "Sack of "
        treasure_horde += build_coins(coin_mod)
        treasure_horde += build_potions(potion_mod)
        treasure_horde += build_scrolls(scroll_mod)

    if treasure_type == 'H':
        coin_mod = 4, 4, 100, 3, 6, 10, 2, 4, 10
        gem_mod = "gem2"
        potion_mod = 1, 0, 0
        scroll_mod = 1, 0
        treasure_horde = "Sack of "
        treasure_horde += build_coins(coin_mod)
        treasure_horde += " masterwork " + eligible_wpns[int(random() * len(eligible_wpns))][
            'wpnName'] + ', '
        treasure_horde += build_potions(potion_mod)
        treasure_horde += build_scrolls(scroll_mod)
        treasure_horde += build_gems(gem_mod)

    return treasure_horde
