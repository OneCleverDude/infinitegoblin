import json

data = {}  
data['monsters'] = []  
data['monsters'].append({  
    'monsterName': 'Goblin Archer',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 133,
    'cr': '1/3',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Humanoid (goblinoid)',
    'size': 'Small',
    'HD': '(1d10+2)',
    'HP': '6',
    'image': 'goblin_archer_small.png',
    'imageCard': 'goblin_archer.png',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6',
    'speed': '30ft',
    'tactics': 'Likes to fight from range;  Will flee if it can when forced to melee.',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, \
                ungainly head.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': -1},
    'attacks': [
        ['basic ranged', 'weapons_bow-128.png', 'bow', '+4', '1d4', '20 x3', '60ft'],
        ['basic melee', 'weapons_club-128.png', 'club', '+2', '1d4', '19-20 x3', '5ft']
    ],
    'crunch': 'Melee Attack: Short Sword +2 attack, 1d4(19-20/x2) Damage<br />Ranged Attack: Shortbow +4 attack, \
                range 60 ft, 1d4(20/x3) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Warrior',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 133,
    'cr': '1/3',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_mace_small.png',
    'imageCard': 'goblin_mace.png',
    'size': 'Small',
    'HD': '(1d10+2)',
    'HP': '8',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee;',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, \
                ungainly head.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': -1},
    'attacks': [
        ['basic melee', 'weapons_sledgehammer-128.png', 'mace', '+2', '1d6', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'bow', '+4', '1d4', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Mace +2 attack, 1d6(20/x2) Damage<br />Ranged Attack: Shortbow +4 attack, range \
                60 ft, 1d4(20/x3) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Warrior',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 133,
    'cr': '1/3',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_warrior2_small.png',
    'imageCard': 'goblin_warrior2.png',
    'size': 'Small',
    'HD': '(1d10+2)',
    'HP': '8',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee;',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': -1},
    'attacks': [
        ['basic melee', 'weapons_spear-128.png', 'spear', '+2', '1d6', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'bow', '+4', '1d4', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Spear +2 attack, 1d6(20/x2) Damage<br />Ranged Attack: Shortbow +4 attack, range 60 ft, \
                1d4(20/x3) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Warrior',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 133,
    'cr': '1/3',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_warrior3_small.png',
    'imageCard': 'goblin_warrior3.png',
    'size': 'Small',
    'HD': '(1d10+2)',
    'HP': '8',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee;',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': -1},
    'attacks': [
        ['basic melee', 'weapons_medieval_sword-128.png', 'dagger', '+2', '1d4', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'bow', '+4', '1d4', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Dagger +2 attack, 1d4(20/x2) Damage<br />Ranged Attack: Dagger +4 attack, range 10 ft, \
                1d4(20/x2) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Javelin',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 133,
    'cr': '1/3',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_javelin_small.png',
    'imageCard': 'goblin_javelin.png',
    'size': 'Small',
    'HD': '(1d10+2)',
    'HP': '8',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from range;',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': -1},
    'attacks': [
        ['basic ranged', 'weapons_spear-128.png', 'javelin', '+4', '1d6', '20 x3', '15ft'],
        ['basic melee', 'weapons_club-128.png', 'club', '+2', '1d4', '19-20 x3', '5ft']
    ],
    'crunch': 'Melee Attack: Dagger +2 attack, 1d4(20/x2) Damage<br />Ranged Attack: Javelin +4 attack, range 15 ft, \
                1d6(20/x3) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Slave',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 65,
    'cr': '1/6',
    'job': 'commoner 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 0},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_slave_small.png',
    'imageCard': 'goblin_slave.png',
    'size': 'Small',
    'HD': '(1d4+2)',
    'HP': '3',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+2',
    'speed': '30ft',
    'tactics': 'Only fights if there are other goblins there;',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': -1},
    'attacks': [
        ['basic melee', 'weapons_club-128.png', 'club', '+0', '1d4', '19-20 x3', '5ft']
    ],
    'crunch': 'Melee Attack: Claw +2/+2 attack, 1d2(x2) Damage'
})
data['monsters'].append({
    'monsterName': 'Human Commoner',
    'reference': '',
    'xp': 200,
    'cr': '1/2',
    'job': 'commoner 2',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 0},
    'monsterType': 'Humanoid',
    'image': 'commoner_small.png',
    'imageCard': 'commoner.png',
    'size': 'Medium',
    'HD': '(1d6+1)',
    'HP': '4',
    'AC': {'normal': 9, 'flatfooted': 9, 'touch': 9, 'cmd': 9},
    'init': '-1 (DEX -1)',
    'speed': '30ft',
    'tactics': 'The commoner threatens aggressors with her scythe, but switches to her club if she actually \
                has to attack.',
    'senses': 'standard',
    'alignment': 'Neutral',
    'languages': 'Common',
    'scores': {'STR': 13, 'DEX': 9, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 8},
    'favor': 'Human commoner',
    'saves': {'FORT': 1, 'REF': -1, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_club-128.png', 'club', '+1', '1d4+1', '19-20 x3', '5ft']
    ],
    'crunch': 'Melee Attack: Club +2 attack, 1d6+1(x2) Damage'
})
data['monsters'].append({
    'monsterName': 'Goblin Commoner',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 65,
    'cr': '1/6',
    'job': 'commoner 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_civ_small.png',
    'imageCard': 'goblin_civ.png',
    'size': 'Small',
    'HD': '(1d4+2)',
    'HP': '2',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+2',
    'speed': '30ft',
    'tactics': 'Only fights if there is no way to run away.',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': -1},
    'attacks': [
        ['basic melee', 'weapons_club-128.png', 'club', '+0', '1d4', '19-20 x3', '5ft']
    ],
    'crunch': 'Melee Attack: Claw +2/+2 attack, 1d2(x2) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Lieutenant',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 200,
    'cr': '1',
    'job': 'fighter 2',
    'roomtype': 'Normal',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_lieutenant_small.png',
    'imageCard': 'goblin_lieutenant.png',
    'size': 'Small',
    'HD': '(3d10+4)',
    'HP': '26',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; will use potions',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 16, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 3, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_medieval_sword-128.png', 'ShortSword', '+7', '1d6+3', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+6', '1d4', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Short Sword +7 attack, 1d4+3(20/x2) Damage<br />Ranged Attack: Shortbow +6 attack, range \
                60 ft, 1d4(20/x3) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Captain',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 400,
    'cr': '2',
    'job': 'fighter 3',
    'roomtype': 'Normal',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_fighter_small.png',
    'imageCard': 'goblin_fighter.png',
    'size': 'Small',
    'HD': '(4d10+6)',
    'HP': '32',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; will use potions',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 17, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 3, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_medieval_sword-128.png', 'ShortSword', '+8', '1d6+4', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+7', '1d6', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Short Sword +8 attack, 1d6+4(20/x2) Damage<br />Ranged Attack: Shortbow +7 attack, range \
                60 ft, 1d6(20/x3) Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Rogue',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 200,
    'cr': '1',
    'job': 'rogue 2',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 3},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_rogue2_small.png',
    'imageCard': 'goblin_rogue2.png',
    'size': 'Small',
    'HD': '(2d8+2)',
    'HP': '13',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; with flanking for sneak attack',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 4, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_medieval_sword-128.png', 'ShortSword', '+7', '1d4+3', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+6', '1d4', '20 x3', '60ft'],
        ['sneak attack', 'powerups_electric_bolt-128.png', '', '', '+1d6', '', '']
    ],
    'crunch': 'Melee Attack: Short Sword +7 attack, 1d4+3(20/x2) Damage<br />Ranged Attack: Shortbow +6 attack, range \
                60 ft, 1d4(20/x3) Damage<br />Sneak Attack +1d6 Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Rogue',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 400,
    'cr': '2',
    'job': 'rogue 3',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 3},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_rogue_small.png',
    'imageCard': 'goblin_rogue.png',
    'size': 'Small',
    'HD': '(3d8+3)',
    'HP': '19',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; with flanking for sneak attack',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 4, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_medieval_sword-128.png', 'ShortSword', '+7', '1d4+3', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+6', '1d4', '20 x3', '60ft'],
        ['sneak attack', 'powerups_electric_bolt-128.png', '', '', '+2d6', '', '']
    ],
    'crunch': 'Melee Attack: Short Sword +7 attack, 1d4+3(20/x2) Damage<br />Ranged Attack: Shortbow +6 attack, range \
                60 ft, 1d4(20/x3) Damage<br />Sneak Attack +2d6 Damage'
})
data['monsters'].append({  
    'monsterName': 'Goblin Barbarian',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 400,
    'cr': '2',
    'job': 'barbarian 3',
    'roomtype': 'Normal',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_barbarian_small.png',
    'imageCard': 'goblin_barbarian.png',
    'size': 'Small',
    'HD': '(3d12+3)',
    'HP': '33',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; with flanking for sneak attack',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 17, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 4, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_battle_axe-128.png', 'Battle Axe', '+7', '1d8+6', '19-20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+6', '1d6', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Battle Axe +7 attack, 1d8+6(19-20/x2) Damage<br />Ranged Attack: Shortbow +6 attack, \
                range 60 ft, 1d6(20/x3) Damage<br />Rage Feat'
})
data['monsters'].append({  
    'monsterName': 'Goblin King',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 1200,
    'cr': '4',
    'job': 'fighter 5',
    'roomtype': 'King',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)(king)',
    'image': 'goblin_king_small.png',
    'imageCard': 'goblin_king.png',
    'size': 'Small',
    'HD': '(5d10+8)',
    'HP': '41',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; with flanking for sneak attack',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 17, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 4, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_flail-128.png', 'Mace', '+7', '1d8+6', '19-20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+6', '1d6', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Mace +7 attack, 1d8+6(19-20/x2) Damage<br />Ranged Attack: Shortbow +6 attack, range 60 \
                ft, 1d6(20/x3) Damage<br />Kingly thing'
})
data['monsters'].append({  
    'monsterName': 'Goblin King',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 800,
    'cr': '3',
    'job': 'fighter 4',
    'roomtype': 'King',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)(king)',
    'image': 'goblin_king_small.png',
    'imageCard': 'goblin_king.png',
    'size': 'Small',
    'HD': '(4d10+7)',
    'HP': '34',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; with flanking for sneak attack',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 17, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 4, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_flail-128.png', 'Mace', '+6', '1d8+6', '19-20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+5', '1d6', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Mace +6 attack, 1d8+6(19-20/x2) Damage<br />Ranged Attack: Shortbow +5 attack, range 60 \
                ft, 1d6(20/x3) Damage<br />Kingly thing'
})
data['monsters'].append({  
    'monsterName': 'Goblin King',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 600,
    'cr': '2',
    'job': 'fighter 3',
    'roomtype': 'King',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)(king)',
    'image': 'goblin_king_small.png',
    'imageCard': 'goblin_king.png',
    'size': 'Small',
    'HD': '(3d10+6)',
    'HP': '25',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; with flanking for sneak attack',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 17, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 4, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_flail-128.png', 'Mace', '+5', '1d8+6', '19-20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+4', '1d6', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Mace +5 attack, 1d8+6(19-20/x2) Damage<br />Ranged Attack: Shortbow +4 attack, range \
                60 ft, 1d6(20/x3) Damage<br />Kingly thing'
})
data['monsters'].append({  
    'monsterName': 'Ogre',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/ogre.html',
    'xp': 800,
    'cr': '3',
    'job': 'warrior 1',
    'roomtype': 'Feature',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (giant)',
    'image': 'ogre_small.png',
    'imageCard': 'ogre.png',
    'size': 'Large',
    'HD': '(4d8+12)',
    'HP': '30',
    'AC': {'normal': 17, 'flatfooted': 17, 'touch': 8, 'cmd': 17},
    'init': '-1',
    'speed': '30ft (40ft base)',
    'tactics': 'Likes to fight from melee',
    'senses': 'darkvision (60ft); low-light vision; Perception +5',
    'alignment': 'Chaotic Evil',
    'languages': 'Giant',
    'scores': {'STR': 21, 'DEX': 8, 'CON': 15, 'INT': 6, 'WIS': 10, 'CHA': 7},
    'favor': 'A typical adult ogre stands 10 feet tall and weighs roughly 650 pounds.',
    'saves': {'FORT': 6, 'REF': 0, 'WILL': 3},
    'attacks': [
        ['basic melee', 'weapons_club-128.png', 'greatclub', '+7', '2d8+7', '20 x2', '10ft'],
        ['basic ranged', 'weapons_spear-128.png', 'javelin', '+1', '1d8+5', '20 x3', '60ft']
    ],
    'crunch': 'Melee Attack: Greatclub +7 attack, 2d8+7(x2) Damage<br />Ranged Attack:Javelin +1 attack, range 30 ft, \
                1d8+5(20/x3) Damage<br />Reach 10'
})
data['monsters'].append({  
    'monsterName': 'Goblin Cleric',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 400,
    'cr': '2',
    'job': 'Cleric 3',
    'roomtype': 'Feature',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_cleric_small.png',
    'imageCard': 'goblin_cleric.png',
    'size': 'Small',
    'HD': '(4d8+4)',
    'HP': '28',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from melee; will use potions',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 14, 'DEX': 14, 'CON': 12, 'INT': 10, 'WIS': 15, 'CHA': 6},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 2, 'WILL': 5},
    'attacks': [
        ['basic melee', 'weapons_flail-128.png', 'Mace', '+5', '1d6+2', '20 x2', '5ft'],
        ['basic ranged', 'weapons_bow-128.png', 'Short bow', '+6', '1d4', '20 x3', '60ft'],
        ['spell', 'magic_spell_book-128.png', 'Bless', '+1', '', '', '']
    ],
    'crunch': 'Melee Attack: Mace +5 attack, 1d6+2(20/x2) Damage<br />Ranged Attack: Shortbow +6 attack, range 60 ft, \
                1d4(20/x3) Damage<br />Spells:Bless, Cure Light Wounds, Silence 15ft radius'
})
data['monsters'].append({  
    'monsterName': 'Goblin Sorcerer',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/goblin.html',
    'xp': 400,
    'cr': '2',
    'job': 'Sorcerer 3',
    'roomtype': 'Feature',
    'treasureRoll': {'D': 2},
    'monsterType': 'Humanoid (goblinoid)',
    'image': 'goblin_hexer_small.png',
    'imageCard': 'goblin_hexer.png',
    'size': 'Small',
    'HD': '(2d6+2)',
    'HP': '11',
    'AC': {'normal': 15, 'flatfooted': 13, 'touch': 13, 'cmd': 11},
    'init': '+6 ',
    'speed': '30ft',
    'tactics': 'Likes to fight from range; will use potions',
    'senses': 'darkvision (60ft)',
    'alignment': 'Neutral Evil',
    'languages': 'Goblin',
    'scores': {'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 9, 'CHA': 13},
    'favor': 'This creature stands barely three feet tall, its scrawny, humanoid body dwarfed by its wide, ungainly \
                head.',
    'saves': {'FORT': 4, 'REF': 2, 'WILL': 5},
    'attacks': [
        ['basic melee', 'weapons_medieval_sword-128.png', 'dagger', '+0', '1d4', '20 x2', '5ft'],
        ['basic ranged', 'magic_spell_book-128.png', 'Ray of Frost', '+2', '1d4', '20', '30ft']
    ],
    'crunch': 'Melee Attack: Dagger +0 attack, 1d4(20/x2) Damage<br />Ranged Attack: Ray of Frost +2 (v.Touc), range \
                30 ft, 1d4(20) Damage<br />Spells:Acid Splash, Daze, Obscuring Mist, Burning Hands (DC 12)'
})
data['monsters'].append({  
    'monsterName': 'Common Bat',
    'reference': '',
    'xp': 50,
    'cr': '1/8',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 0},
    'monsterType': 'Animal',
    'image': 'bat_small.png',
    'imageCard': 'bat.png',
    'size': 'Diminutive',
    'HD': '(1d8-2)',
    'HP': '2',
    'AC': {'normal': 16, 'flatfooted': 14, 'touch': 16, 'cmd': 16},
    'init': '+2',
    'speed': '5ft, fly 40ft. (good)',
    'tactics': 'Likes to fight from melee;',
    'senses': 'blindsense (20ft), low-light vision, perception+6',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 1, 'DEX': 15, 'CON': 6, 'INT': 2, 'WIS': 14, 'CHA': 5},
    'favor': 'It is a bat',
    'saves': {'FORT': 0, 'REF': 4, 'WILL': 2},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'bite', '+6', '1d3-4', '', '5ft']
    ],
    'crunch': 'Melee Attack: bite+6 attack, 1d3-4 Damage'
})
data['monsters'].append({  
    'monsterName': 'Grizzly Bear',
    'reference': '',
    'xp': 1200,
    'cr': '4',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 0},
    'monsterType': 'Animal',
    'image': 'bear_small.png',
    'imageCard': 'bear.png',
    'size': 'Large',
    'HD': '(5d8+20)',
    'HP': '42',
    'AC': {'normal': 16, 'flatfooted': 15, 'touch': 10, 'cmd': 16},
    'init': '+1',
    'speed': '40ft',
    'tactics': 'When faced with a foe or small group of threats, the grizzly attempts to subdue or kill with its \
                claws. When it can, the bear tries to grab a single target to deal continual damage until that target \
                is dead, unconscious, or escapes.',
    'senses': 'low-light vision, scent; perception+6',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 21, 'DEX': 13, 'CON': 19, 'INT': 2, 'WIS': 12, 'CHA': 6},
    'favor': 'Broad, powerful muscles move beneath this massive bears brown fur, promising both speed and lethal \
                force.',
    'saves': {'FORT': 8, 'REF': 5, 'WILL': 2},
    'attacks': [
        ['basic melee', 'weapons_claw-128.png', 'claws', '+7/+7', '1d6+5 (grab)', '', '5ft'],
        ['basic melee', 'weapons_bite-128.png', 'bite', '+7', '1d6+5', '', '5ft']
    ],
    'crunch': 'Melee Attack: 2 claws +7 (1d6+5 plus grab), bite +7 attack, (1d6+5) Damage'
})
data['monsters'].append({  
    'monsterName': 'Giant Centipede',
    'reference': '',
    'xp': 200,
    'cr': '1/2',
    'job': '',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 0},
    'monsterType': 'Vermin',
    'image': 'centipedeM_small.png',
    'imageCard': 'centipedeM.png',
    'size': 'Medium',
    'HD': '(1d8+1)',
    'HP': '5',
    'AC': {'normal': 14, 'flatfooted': 12, 'touch': 12, 'cmd': 14},
    'init': '+2',
    'speed': '40ft; Climb 40ft',
    'tactics': 'Giant centipedes attack nearly any living creatures with their poisonous jaws.',
    'senses': 'darkvision 60ft; perception+4',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 9, 'DEX': 15, 'CON': 12, 'INT': 0, 'WIS': 10, 'CHA': 2},
    'favor': 'This lengthy, segmented horror writhes and twists, pulsing its venomous mandibles in search of prey.',
    'saves': {'FORT': 3, 'REF': 2, 'WILL': 0},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'bite', '+2', '1d6-1 (poison)', '', '5ft']
    ],
    'crunch': 'Melee Attack: bite +2 (1d6-1 plus poison) Damage <br/>Poison (EX) Bite—injury; save Fort DC 13; \
                frequency 1/round for 6 rounds; effect 1d3 Dex damage; cure 1 save. The save DC is Constitution-based \
                and includes a +2 racial bonus.'
})
data['monsters'].append({  
    'monsterName': 'Rust Monster',
    'reference': '',
    'xp': 800,
    'cr': '3',
    'job': '',
    'roomtype': 'Normal',
    'treasureRoll': {'C': 1},
    'monsterType': 'Aberration',
    'image': 'rustmonster_small.png',
    'imageCard': 'rustmonster.png',
    'size': 'Medium',
    'HD': '(5d8+5)',
    'HP': '27',
    'AC': {'normal': 18, 'flatfooted': 15, 'touch': 13, 'cmd': 18},
    'init': '+3',
    'speed': '40ft; Climb 10ft',
    'tactics': 'Though rust monsters have no innate tendency toward violence, their insatiable hunger leads them to \
                charge anything they come across that bears even trace amounts of metal, and any resistance is met \
                with unthinking savagery.',
    'senses': 'darkvision 60ft; Scent Metals 90ft; perception+12',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 10, 'DEX': 17, 'CON': 13, 'INT': 2, 'WIS': 13, 'CHA': 8},
    'favor': 'This insectile monster has four legs, a strange propeller-shaped protrusion at the end of its tail, and \
                two long, feathery antennae.',
    'saves': {'FORT': 2, 'REF': 4, 'WILL': 5},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'bite', '+6', '1d3', '', '5ft'],
        ['basic melee', 'weapons_bite-128.png', 'atennae', '+6 touch', 'Rust', '', '5ft']
    ],
    'crunch': 'Melee Attack: bite +6 (1d3) Damage, antennae +6 touch (rust) <br/>Rust: The object touched takes half \
                its maximum hp in damage and gains the broken condition—a second hit destroys the item.'
})
data['monsters'].append({  
    'monsterName': 'Giant Spider',
    'reference': '',
    'xp': 400,
    'cr': '1',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 3},
    'monsterType': 'Vermin',
    'image': 'giant_spiderM_small.png',
    'imageCard': 'giant_spiderM.png',
    'size': 'Medium',
    'HD': '(3d8+3)',
    'HP': '16',
    'AC': {'normal': 14, 'flatfooted': 11, 'touch': 13, 'cmd': 14},
    'init': '+3',
    'speed': '30ft; climb 30ft',
    'tactics': 'Likes to fight from webs;',
    'senses': 'darkvision (60ft); termorsense (60ft); perception+4',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 11, 'DEX': 17, 'CON': 12, 'INT': 0, 'WIS': 10, 'CHA': 2},
    'favor': 'A spider the size of a man crawls silently from the depths of its funnel-shaped web.',
    'saves': {'FORT': 4, 'REF': 4, 'WILL': 1},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'bite', '+2', '1d6 (poison)', '', '5ft']
    ],
    'crunch': 'Melee Attack: bite+2 attack, 1d6 Damage + poison <br/>Special Attack Web +5 ranged, DC12 hp 2<br/>\
                Poison (Ex) Bite—injury; save Fort DC 14; frequency 1/round for 4 rounds; effect 1d2 Strength \
                damage; cure 1 save.'
})
data['monsters'].append({  
    'monsterName': 'Dire Rat',
    'reference': '',
    'xp': 133,
    'cr': '1/3',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Animal',
    'image': 'rat_dire_small.png',
    'imageCard': 'rat_dire.png',
    'size': 'Small',
    'HD': '(1d8+1)',
    'HP': '7',
    'AC': {'normal': 14, 'flatfooted': 11, 'touch': 14, 'cmd': 14},
    'init': '+3',
    'speed': '40ft, Climb 20ft, Swim 20ft',
    'tactics': 'Likes to fight from melee;',
    'senses': 'low-light vision, scent perception+4',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 10, 'DEX': 17, 'CON': 13, 'INT': 2, 'WIS': 13, 'CHA': 4},
    'favor': 'This filthy rat is the size of a small dog. It has a coat of coarse fur, a long and scabby tail, and \
                two glittering eyes.',
    'saves': {'FORT': 3, 'REF': 5, 'WILL': 1},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'bite', '+1', '1d4 (disease)', '', '5ft']
    ],
    'crunch': 'Melee Attack: bite+1 attack, 1d4+disease Damage<br/>Disease (Ex) Filth fever: Bite—injury; save Fort \
                DC 11; onset 1d3 days; frequency 1/day; effect 1d3 Dex damage and 1d3 Con damage; cure 2 consecutive \
                saves. The save DC is Constitution-based.'
})
data['monsters'].append({  
    'monsterName': 'Rat Swarm',
    'reference': '',
    'xp': 600,
    'cr': '2',
    'job': 'warrior 1',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 0},
    'monsterType': 'Animal',
    'image': 'rat_small.png',
    'imageCard': 'rat.png',
    'size': 'Tiny (swarm)',
    'HD': '(3d8+3)',
    'HP': '16',
    'AC': {'normal': 14, 'flatfooted': 12, 'touch': 14, 'cmd': 14},
    'init': '+6',
    'speed': '15ft, Climb 15ft, Swim 15ft',
    'tactics': 'Rat swarms surround and attack any warm-blooded prey in their path.',
    'senses': 'low-light vision, scent perception+8',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 2, 'DEX': 15, 'CON': 13, 'INT': 2, 'WIS': 13, 'CHA': 2},
    'favor': 'A rat swarm typically consists of a biting, roiling mass of hundreds of disease-ridden rats driven to \
                uncharacteristic heights of aggression by fantastic and overwhelming hunger. In such numbers, they \
                become voracious hunters, capable of killing a full-grown human with hundreds of bites. Rat swarms are \
                often found in the sewers of large human settlements.',
    'saves': {'FORT': 4, 'REF': 5, 'WILL': 2},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'bite', 'swarm', '1d6 (disease)', '', '0ft']
    ],
    'crunch': 'Melee swarm 1d6+disease Damage<br/>Swarm Defenses<br/>Disease (Ex) Filth fever: Bite—injury; save Fort \
                DC 12; onset 1d3 days; frequency 1/day; effect 1d3 Dex damage and 1d3 Con damage; cure 2 consecutive \
                saves. The save DC is Constitution-based.'
})
data['monsters'].append({
    'monsterName': 'Fire Elemental',
    'reference': '',
    'xp': 800,
    'cr': '3',
    'job': '',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 3},
    'monsterType': 'Outsider',
    'image': 'fire_elemental_small.png',
    'imageCard': 'fire_elemental.png',
    'size': 'Medium',
    'HD': '(4d10+8)',
    'HP': '30',
    'AC': {'normal': 17, 'flatfooted': 13, 'touch': 14, 'cmd': 17},
    'init': '+7',
    'speed': '50ft',
    'tactics': 'Moves to burn whatever if can close with.',
    'senses': 'Darkvision 60ft; perception+7',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 12, 'DEX': 17, 'CON': 14, 'INT': 4, 'WIS': 11, 'CHA': 11},
    'favor': 'This creature looks like a living, mobile bonfire, tongues of flame reaching out in search of things to \
                burn.',
    'saves': {'FORT': 6, 'REF': 7, 'WILL': 1},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'slam', '+7', '1d6 (burn)', '', '5ft']
    ],
    'crunch': 'Melee: Slam +7 (1d6+1 plus burn)<br/>Special Attacks: Burn (1d6 DC14)<br/>Immune Fire; Elemental \
                traits<br/>Vulnerable to Cold'
})
data['monsters'].append({
    'monsterName': 'Water Elemental',
    'reference': '',
    'xp': 800,
    'cr': '3',
    'job': '',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 3},
    'monsterType': 'Outsider',
    'image': 'water_elemental_small.png',
    'imageCard': 'water_elemental.png',
    'size': 'Medium',
    'HD': '(4d10+8)',
    'HP': '30',
    'AC': {'normal': 17, 'flatfooted': 16, 'touch': 11, 'cmd': 17},
    'init': '+7',
    'speed': '20ft; swim 90ft',
    'tactics': 'Moves to slam whatever if can close with.',
    'senses': 'Darkvision 60ft; perception+7',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 16, 'DEX': 12, 'CON': 15, 'INT': 4, 'WIS': 11, 'CHA': 11},
    'favor': 'This translucent creatures shape shifts between a spinning column of water and a crashing wave.',
    'saves': {'FORT': 6, 'REF': 7, 'WILL': 1},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'slam', '+7', '1d8+4', '', '5ft']
    ],
    'crunch': 'Melee: Slam +7 (1d8+4)<br/>Special Attacks: drench, vortex (DC15), water mastery <br/>Immune Elemental \
                traits<br/>Feats: Power Attack, Cleave'
})
data['monsters'].append({
    'monsterName': 'Earth Elemental',
    'reference': '',
    'xp': 800,
    'cr': '3',
    'job': '',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 3},
    'monsterType': 'Outsider',
    'image': 'earth_elemental_small.png',
    'imageCard': 'earth_elemental.png',
    'size': 'Medium',
    'HD': '(4d10+8)',
    'HP': '34',
    'AC': {'normal': 18, 'flatfooted': 18, 'touch': 9, 'cmd': 18},
    'init': '-1',
    'speed': '20ft; burrow 20ft, earth glide',
    'tactics': 'Moves to slam whatever if can close with.',
    'senses': 'Darkvision 60ft; tremorsense 60ft; perception+7',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 20, 'DEX': 8, 'CON': 17, 'INT': 4, 'WIS': 11, 'CHA': 11},
    'favor': 'This hulking, roughly humanoid creature of dirt and stone explodes up from the earth, faceless save for \
                two glowing gemstone eyes.',
    'saves': {'FORT': 6, 'REF': 7, 'WILL': 1},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'slam', '+9', '1d8+7', '', '5ft']
    ],
    'crunch': 'Melee: Slam +9 (1d8+7)<br/>Special Attacks: earth mastery <br/>Immune Elemental \
                traits<br/>Feats: Power Attack, Cleave, Improved Bull Rush'
})
data['monsters'].append({
    'monsterName': 'Gelatinous Cube',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/gelatinousCube.html',
    'xp': 800,
    'cr': '3',
    'job': '',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 3},
    'monsterType': 'Ooze',
    'image': 'gelatinous_cube_small.png',
    'imageCard': 'gelatinous_cube.png',
    'size': 'Large',
    'HD': '(4d8+32)',
    'HP': '50',
    'AC': {'normal': 4, 'flatfooted': 4, 'touch': 4, 'cmd': 4},
    'init': '-5',
    'speed': '15ft;',
    'tactics': 'Moves to slam whatever if can close with.',
    'senses': 'blindsight 60ft; perception-5',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 10, 'DEX': 1, 'CON': 26, 'INT': 0, 'WIS': 1, 'CHA': 1},
    'favor': 'Bits of broken weapons, coins, and a partially digested skeleton are visible inside this quivering \
                cube of slime.',
    'saves': {'FORT': 9, 'REF': -4, 'WILL': -4},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'slam', '+2', '1d6 (1d6 Acid)', '', '5ft']
    ],
    'crunch': 'Melee: Slam +2 (1d6+1d6 Acid)<br/>Special Attacks: engulf, paralysis <br/>Immune electricity, ooze  \
                traits'
})
data['monsters'].append({
    'monsterName': 'Stirge',
    'reference': 'http://paizo.com/pathfinderRPG/prd/bestiary/stirge.html',
    'xp': 200,
    'cr': '1/2',
    'job': '',
    'roomtype': 'Normal',
    'treasureRoll': {'A': 1},
    'monsterType': 'Magical Beast',
    'image': 'stirge_small.png',
    'imageCard': 'stirge.png',
    'size': 'Tiny',
    'HD': '(1d10)',
    'HP': '5',
    'AC': {'normal': 16, 'flatfooted': 12, 'touch': 16, 'cmd': 16},
    'init': '+4',
    'speed': '10ft; Fly 40ft (average)',
    'tactics': 'Swoop down to attach and drink blood.',
    'senses': 'darkvision 60ft; low light vision; perception+1',
    'alignment': 'Neutral',
    'languages': 'none',
    'scores': {'STR': 3, 'DEX': 19, 'CON': 10, 'INT': 1, 'WIS': 12, 'CHA': 6},
    'favor': 'This insectoid creature has two pairs of bat wings, a tangle of thin legs, and a needle-sharp proboscis.',
    'saves': {'FORT': 2, 'REF': 6, 'WILL': 1},
    'attacks': [
        ['basic melee', 'weapons_bite-128.png', 'attach', '+7 touch', 'blood drain', '', '5ft']
    ],
    'crunch': 'Melee: touch +7 (attach)<br/>Special Attacks: blood drain<br/>Diseased(Ex)'
})
with open('monsters.json', 'w') as outfile:  
    json.dump(data, outfile)