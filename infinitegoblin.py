#
# Infinite Goblin

from random import *
import json
import statistics
import buildtreasure as treasure
import printhtmlfile as printhtml


with open('lairs.json') as json_file:
    dataLairs = json.load(json_file)
with open('rooms.json') as json_file:
    dataRooms = json.load(json_file)
with open('monsters.json') as json_file:
    dataMonsters = json.load(json_file)


xpBudget = [200, 400, 600, 800, 1200, 1600, 2400, 3200, 4800]
crLevels = [50, 65, 100, 135, 200, 400, 600, 800, 1200, 1600, 2400, 3200, 4800, 6400]
goblinName1 = ["Black", "Green", "Raging", "Filthy", "Noxious", "Dread"]
goblinName2 = ["Moon", "Tongue", "Eye", "Rotter", "Snot", "Fury"]
goblinName3 = ["Gang", "Mob", "Tribe", "Rabble", "Pack", "Crew"]
goblinNames = ["Mosshorn", "Roughchopper", "Woldrip", "Steelmark", "Stumpfall", "Snowpunch", "Hardwad", "Crystalrage",
               "Deadmaw", "Highwatcher", "Marshchopper", "Manpart", "Rainscar", "Strongscar", "Pokebinder", "Heavyrip",
               "Goldbrace", "Crowpunch", "Woodcrest", "Deweye", "Hillblazer", "Shadowroar", "Steelstalker", "Crowshot",
               "Stumpcut", "Cragbinder", "Grasslasher", "Earsnarl", "Stardancer", "Gloomspear"]
goblinGods = ["Hadregash", "Lamashtu", "Venkelvore", "Zarongel", "Zogmugot", "Water Elemental", "Earth Elemental",
              "Fire Elemental", "Evil Sorcerer", "Something Really Weird"]

lairOrigin = {"Dwarf Ruins", "Abandoned Gnome Burrowtown", "Ruins of a Black Dragon lair", "Cliffside fortress",
              "Sewers", "Garbage Pits", "Limestone caves", "Ravine", "Abandoned Ore Mine",
              "Abandoned Drow Surface Outpost"}
adventureHooks = {"Punitive Raid", "Retrieve Item", "Free Prisoners"}

'''
Goblin lair creation notes:

Hadregash : Goblin god of Goblin supremacy, salvery, and territory
Lamashtu : Mother of monsters.  Madness, monsters, nightmares
Venkelvore: Famine, Graves, Torture, undead
Zargongel: Dog killing, fire, mounted combat
Zogmugot: Drowning, Flotsam, Scavenging, Traps
Earth Elemental : Found it and worship it.  It basically tolerates the goblins because it enjoys the worship from lesser beings.
Fire Elemental : Barely notices the Goblins.  They just really like fire.
Evil Sorcerer : Both god and king for the Goblins
Something Weird : Build a sub table here.  Might have the evil sorcerer on it, could also see Ogre, Bugbear, Hill Giant.

Why is there a goblin lair here?  Need to answer that question for every lair generated.  In general, goblins are 
going to florish in areas where there is enough food to allow them to live.  Think in general terms, like a pest around
human cities today.  If it's too much trouble to root it out, it likely thrives.  When it's big enough to be a pest,
an group of people organize to root it out.

In general then, the lairs should be places that are out of ordinary reach, either because of the general geography, or
the conditions (garbage, disease ridden)  Think swamps, sewers, cliffs, deep forests, rugged terrain that is hard to get
in and out of.

Goblins are lazy, so most of their lairs would be naturally constructed or in the ruins of a more industrial race.  
Place these as per terrain selected initially.  (Settlement, Plains, Forest, Hills, Mountain, Swamp)  
TODO: Think about above ground goblin lairs, probably smaller and open.

- Dwarf ruins in a remote hillside or underground
    - Corridors are generally finished stone, less change of cave-ins
    - Doors ripped off hinges, especially discovered secret doors
    - Better chance of a secret hidden room that the goblins haven't discovered yet.
- Swampy ruins of a long dead black dragon
    - Lots of disease chances
    - Increase rate of vermin in the lair
    - Decrease treasure chance of things that Black Dragon acid might have destroyed, but increase treasure amounts
    - Small chance of young black dragon trying to take the lair.
- Cliffs where access is only possible at low tide
    - Useful around settlements.  Gives the goblins a fighting chance of not being discovered
    - Lots of trade goods in the treasures
    - Rooms un-even and prone to cave-ins and floors falling.
    - Many small passageways
- Sewers under a human settlement
    - Lots of disease
    - Many small passageways
    - Goblins have lots of vermin
    - Increased chance of prisoners.  Use for cold open hooks.
- Within the garbage pits where a settlement dumps garbage
    - Lots of disease
    - Goblins have lots of vermin
    - Many improvised traps
    - Increased chance of prisoners.  Use for cold open hooks.
- Natural limestone caves
    - Many small passageways
    - Increased chance of cave-ins, difficult terrain.
    - Think bats, and other creatures that live in caves
- Natural ravine
    - Hidden, sentries posted.
    - Chance to flood in rain
    - Deep passageways possible
- Abandoned drow surface outpost
    - Goblins reverence for Drow.  (Maybe a weird goblin god here?)
    - Lair should feel creepy and sinister for flavor
- Abandoned mine (copper, tin, silver, iron, other ores...)
    - Answer the why was the mine abandoned question.
    - Abandoned tools, mix of mine and passageways that the goblins have carved.
- Abandoned gnome burrow town
    - Goblins took residence.  Passageways should be small, potential for a hidden room

Possible light sources in a lair
- Fire beetle glands
- torches
- pitch dark!
- illuminate fungus

Beyond the theme

Think about things that can be held across the lair.  What happens if the goblins are alerted to the presence of the 
heroes?  How long do they stay alerted?  Does light that the characters carry matter?  Do the goblins extinguish the 
fires they have, or use that as a weapon?  How does a day/night cycle affect the denizens of the dungeon?

Thinking about rooms.  Think about placing objects randomly in each.  Sleeping cots, crates, piles of debris, broken
equipment, etc.  Then have some randomness about what might be in the items, and what sorts of noises, traps, diseases, 
etc there might be in each.  

Wandering monsters in a lair by theme.


'''


class Lair:
    class Encounter:

        def __init__(self, lair, room_type, xp_budget, room_number):
            self.type = room_type
            self.room_number = room_number
            self.encounterXP = xp_budget
            if room_type == "King":
                self.seedMonster = {lair.goblinKing: 1}
            # TODO: Build a memory here to take out rooms that we've already put into the lair.
            select_rooms = ([x for x in dataRooms["rooms"] if (x["type"] == self.type and x["minXP"] <= self.encounterXP)])
            room = choice(select_rooms)
            if len(room) > 0:
                self.titleText = room["titleText"]
                self.subHead = room["subHead"]
                self.flavor = room["flavor"]
                self.minX = room["minX"]
                self.maxX = room["maxX"]
                self.minY = room["minY"]
                self.maxY = room["maxY"]
                self.chanceToStartAlive = room["chanceToStartAlive"]
            else:
                self.titleText = "This is an error"
                self.subHead = ""
                self.flavor = ""
                self.minX = 0
                self.maxX = 0
                self.minY = 0
                self.maxY = 0
                self.chanceToStartAlive = 1
            w = int(self.minX + random() * (self.maxX - self.minX + 1))
            h = int(self.minY + random() * (self.maxY - self.minY + 1))
            success = 0
            while success == 0:
                collide = 0
                x = int(randrange(10 * self.room_number, 10 * self.room_number + 10))
                y = int(randrange(10, 60))
                if x < 1:
                    x = 1
                if y < 1:
                    y = 1
                self.x1 = x
                self.y1 = y
                preset_map = 0
                try:
                    self.map = room["map"]
                    preset_map = 1
                    w = len(self.map[0])
                    h = len(self.map)
                except KeyError:
                    self.map = []
                self.x2 = x + w
                self.y2 = y + h
                self.cy = int(statistics.mean([self.y1, self.y2]))
                self.cx = int(statistics.mean([self.x1, self.x2]))

                # check if we are out of bounds.
                if self.x2 + 1 > lair.MAP_WIDTH:
                    print(self.x2, lair.MAP_WIDTH, "x2")
                    lair.MAP_WIDTH = self.x2 + 5
                if self.x1 - 1 < 0:
                    print(self.x1, lair.MAP_WIDTH, "x1")
                if self.y2 + 1 > lair.MAP_HEIGHT:
                    print(self.y2, lair.MAP_HEIGHT, "y2")
                    lair.MAP_HEIGHT = self.y2 + 5
                if self.y1 - 1 < 0:
                    print(self.y1, lair.MAP_HEIGHT, "y1")

                # Room collusion code
                for i in range(self.x1 - 1, self.x2 + 1):
                    for j in range(self.y1 - 1, self.y2 + 1):
                        if j < lair.MAP_WIDTH and i < lair.MAP_HEIGHT:
                            if lair.map[j][i] > 0:
                                collide += 1
                if collide < 1:
                    success = 1

            for j in range(self.y1, self.y2):
                for i in range(self.x1, self.x2):
                    if preset_map == 1:
                        lair.map[j][i] = self.map[j - self.y1][i - self.x1]
                    else:
                        if abs(self.cy - i) > (self.cy - self.y1) / 4 and abs(self.cx - j) > (self.cx - self.x1) / 4:
                            if random() < self.chanceToStartAlive:
                                lair.map[j][i] = 99
                            else:
                                if i % 2 == 0:
                                    if j % 2 == 0:
                                        lair.map[j][i] = -1
                                    else:
                                        lair.map[j][i] = 0
                                else:
                                    if y % 2 == 0:
                                        lair.map[j][i] = 0
                                    else:
                                        lair.map[j][i] = -1
                        else:
                            lair.map[j][i] = 99
                    if (i == int(self.cx)) and (j == int(self.cy)):
                        lair.map[j][i] = self.room_number

            try:
                self.treasureType = dict(room["treasureRoll"])
            except KeyError:
                self.treasureType = []
            try:
                if self.type == "King":
                    if len(self.seedMonster) > 0:
                        self.seedMonster = {**self.seedMonster, **dict(room["seedMonster"])}
                    else:
                        self.seedMonster = dict(room["seedMonster"])
                else:
                    self.seedMonster = dict(room["seedMonster"])
            except KeyError:
                self.seedMonster = []
            except AttributeError:
                self.seedMonster = []
            self.minXP = room["minXP"]
            self.notes = room["notes"]
            self.encounterType = room["monsters"]
            self.seedName = ''
            self.seedNumber = 0
            self.monster_list = []
            try:
                self.maxXP = room["maxXP"]
            except KeyError:
                self.maxXP = 9999
            if self.maxXP < self.encounterXP:
                self.encounterXP = self.maxXP
            # Build the monsters in the encounter.  Maybe this gets it's own def
            encounter_xp = self.encounterXP
            if len(self.seedMonster) > 0:
                for i, j in self.seedMonster.items():
                    select_monsters = ([x for x in dataMonsters["monsters"] if (str(x['monsterName']) == str(i))])
                    if len(select_monsters) > 0:
                        m = int(random() * (len(select_monsters)))
                        for k in range(j):
                            self.monster_list.append(select_monsters[m])
                            encounter_xp = encounter_xp - int(select_monsters[m]['xp'])
                            # TODO: This is where you should add monster individual treasure
                            # TODO: This is where you should give each individual monster a name
                            # TODO: This could also be an interesting place to make "elite" mobs by x2 HP and treasure.
            while encounter_xp > 0:
                select_monsters = ([x for x in dataMonsters["monsters"] if
                                    (x['xp'] <= self.encounterXP) and x['monsterType'] == self.encounterType])
                if len(select_monsters) > 0:
                    m = int(random() * (len(select_monsters)))
                    self.monster_list.append(select_monsters[m])
                    encounter_xp = encounter_xp - int(select_monsters[m]['xp'])
                else:
                    encounter_xp = 0
            # Build the treasure for the encounter
            if len(self.treasureType) > 0:
                for i, j in self.treasureType.items():
                    self.notes += treasure.build_horde(i, j)
            self.monster_list = sorted(self.monster_list, key=lambda t: (t['xp'],t['monsterName']))
            self.origin = ""

        def describe_encounter(self):
            print(self.titleText)
            print(self.subHead)
            print(self.type)
            print("xp budget is " + str(self.encounterXP))
            for monsters in self.monster_list:
                print(monsters["monsterName"])
            print(self.notes)

    def __init__(self):

        def build_corridors(lair):
            r = 1
            while r < len(self.encounter):
                y1 = int(self.encounter[r].cy)
                y2 = int(self.encounter[r - 1].cy)
                x1 = int(self.encounter[r].cx)
                x2 = int(self.encounter[r - 1].cx)
                check = 0
                xtarget = x1
                ytarget = y2
                lair.map[y2][x1] = 99
                if y1 <= y2:
                    for i in range(y1, y2):
                        if check > 3:
                            if random() > .6:
                                if lair.map[i][xtarget] < 1:
                                    lair.map[i][xtarget] = 99
                                check = 0
                                if random() > .5:
                                    xtarget += 1
                                else:
                                    xtarget -= 1
                        if lair.map[i][xtarget] < 1:
                            lair.map[i][xtarget] = 99
                        check += 1
                else:
                    for i in range(y2, y1):
                        if check > 3:
                            if random() > .6:
                                if lair.map[i][xtarget] < 1:
                                    lair.map[i][xtarget] = 99
                                check = 0
                                if random() > .5:
                                    xtarget += 1
                                else:
                                    xtarget -= 1
                        if lair.map[i][xtarget] < 1:
                            lair.map[i][xtarget] = 99
                        check += 1
                check = 0
                if x1 <= x2:
                    for j in range(x1, x2):
                        if check > 3:
                            if random() > .6:
                                if lair.map[ytarget][j] < 1:
                                    lair.map[ytarget][j] = 99
                                check = 0
                                if random() > .5:
                                    ytarget += 1
                                else:
                                    ytarget -= 1
                        if lair.map[ytarget][j] < 1:
                            lair.map[ytarget][j] = 99
                        check += 1
                else:
                    for j in range(x2, x1):
                        if check > 3:
                            if random() > .6:
                                if lair.map[ytarget][j] < 1:
                                    lair.map[ytarget][j] = 99
                                check = 0
                                if random() > .5:
                                    ytarget += 1
                                else:
                                    ytarget -= 1
                        if lair.map[ytarget][j] < 1:
                            lair.map[ytarget][j] = 99
                        check += 1

                if xtarget > x1:
                    for j in range(x1, xtarget + 1):
                        if lair.map[y2][j] < 1:
                            lair.map[y2][j] = 99
                elif xtarget < x1:
                    for j in range(xtarget - 1, x1):
                        if lair.map[y2][j] < 1:
                            lair.map[y2][j] = 99
                if ytarget > y2:
                    for i in range(y2, ytarget + 1):
                        if lair.map[i][x1] < 1:
                            lair.map[i][x1] = 99
                elif ytarget < y2:
                    for i in range(ytarget - 1, y2):
                        if lair.map[i][x1] < 1:
                            lair.map[i][x1] = 99
                r += 1
        select_lairs = ([x for x in dataLairs["lairs"]])
        this_lair = choice(select_lairs)
        self.resourceAbundance = 6
        self.distanceToSea = 4
        self.temperature = 4
        self.numberOfPlayers = 5
        self.totalLevels = 6
        self.apl = int(self.totalLevels/self.numberOfPlayers)
        if self.numberOfPlayers > 5:
            self.apl += 1
        if self.numberOfPlayers < 4:
            self.apl -= 1
        if self.apl < 1:
            self.apl = 1
        self.goblinTribeName = choice(goblinName1) + " " + choice(goblinName2) + " " + choice(goblinName3)
        self.goblinGod = this_lair['goblingod']
        self.goblinKing = this_lair['goblinking']
        self.origin = this_lair['origin']
        self.notes = this_lair['notes']
        self.maxRooms = int((random()*3)+4)
        if self.maxRooms < 3:
            self.maxRooms = 3
        mapMod = (self.maxRooms - 6) * 20
        if mapMod < 0:
            mapMod = 0
        self.MAP_WIDTH = 200 + mapMod
        self.MAP_HEIGHT = 200 + mapMod
        xmax = 0
        ymax = 0
        # this tweaks how much it will look like a "cave"
        self.map = [[0 for x in range(self.MAP_WIDTH)] for y in range(self.MAP_HEIGHT)]
        for map_x in range(self.MAP_WIDTH):
            for map_y in range(self.MAP_HEIGHT):
                if map_x % 2 == 0:
                    if map_y % 2 == 0:
                        self.map[map_x][map_y] = -1
                    else:
                        self.map[map_x][map_y] = 0
                else:
                    if map_y % 2 == 0:
                        self.map[map_x][map_y] = 0
                    else:
                        self.map[map_x][map_y] = -1
        room_budget = int(self.apl)
        self.encounter = []
        for x in range(self.maxRooms):

            room_type = "Basic"
            if x == 0:
                room_type = "Entry"
                room_budget += 1
            elif x == self.maxRooms-1:
                room_type = "King"
                room_budget += 2
            else:
                if random()*100 > 80:
                    room_type = "Setback"
                    room_budget += 1
            self.encounter.append(self.Encounter(self, room_type,  xpBudget[room_budget], x + 1))
            if self.encounter[x].x2 > xmax:
                xmax = self.encounter[x].x2
            if self.encounter[x].y2 > ymax:
                ymax = self.encounter[x].y2
        build_corridors(self)
        self.MAP_WIDTH = 5 + xmax
        self.MAP_HEIGHT = 5 + ymax

    def describe_lair(self):
        print(self.goblinTribeName)
        print(self.goblinGod)
        print(self.notes)
        print("build the html")
        printhtml.build_html_page(self)
        print("finished the html")


if __name__=='__main__':
    print("\n\n\n")
    myLair = Lair()
    print("I'm a lair! rawr!")
    myLair.describe_lair()
