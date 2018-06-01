import json

data = {}
data['lairs'] = []
data['lairs'].append({
    'origin': 'Abandoned Dwarf Outpost',
    'floor': 'Smooth Stone',
    'structuremod': 0.85,
    'goblingod': 'Hadregash',
    'goblinking': 'Goblin King',
    'wanderingMonsters': {"goblin warrior": 1, "goblin archer": 1},
    'notes': '<p>This is a warrior tribe, goblins found here will be more likely to fight to the death than in other \
    goblin tribes.  Play the goblins as bloodthirsty and more courageous than normal at full health.  They will shout \
    insults at opponents to try to build up their own courage.  Play it up.</p><p>The ancient dwarf outpost has long \
    ago passed from the dwarfs.  It\'s fallen into ruin.  Since the dwarves who built it were such good craftsman, \
    most of the passageways, while worn, are actually in good shape.  Except where the goblins have deliberately \
    destroyed the work</p>'
})
data['lairs'].append({
    'origin': 'Natural Limestone Cave System',
    'floor': 'Natural Stone',
    'structuremod': 0.85,
    'goblingod': 'Resident Ogre',
    'goblinking': 'Ogre',
    'wanderingMonsters': {"goblin warrior": 1, "goblin archer": 1},
    'notes': '<p>This is a tribe that has found itself taken over by an ogre.  The goblins have begun to exhibit ogre \
    like behaviors.  Goblins should have a better than average chance to be using clubs instead of other weapons \
    because they have seen how awesome those weapons are when employed by the ogre.</p>'
})
data['lairs'].append({
    'origin': 'Natural Limestone Cave System',
    'floor': 'Natural Stone',
    'structuremod': 0.85,
    'goblingod': 'Fire Elemental',
    'goblinking': 'Fire Elemental',
    'wanderingMonsters': {"goblin warrior": 1, "goblin archer": 1},
    'notes': '<p>This is a tribe has decided to worship a resident fire elemental.  When the elemental gets hot, they \
    rush to small hide holes.</p>'
})
data['lairs'].append({
    'origin': 'Natural Limestone Cave System',
    'floor': 'Natural Stone',
    'structuremod': 0.85,
    'goblingod': 'Earth Elemental',
    'goblinking': 'Earth Elemental',
    'wanderingMonsters': {"goblin warrior": 1, "goblin archer": 1},
    'notes': '<p>This is a tribe has decided to worship a resident earth elemental.</p>'
})

with open('lairs.json', 'w') as outfile:
    json.dump(data, outfile)
