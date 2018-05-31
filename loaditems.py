import json

data = {}  
data['Weapons'] = []  
data['Weapons'].append({ 
    'wpnName': 'Bastard sword'
})
data['Weapons'].append({ 
    'wpnName': 'Battleaxe'
})
data['Weapons'].append({ 
    'wpnName': 'Composite Longbow'
})
data['Weapons'].append({ 
    'wpnName': 'Composite Shortbow'
})
data['Weapons'].append({ 
    'wpnName': 'Dagger'
})
data['Weapons'].append({ 
    'wpnName': 'Greataxe'
})
data['Weapons'].append({ 
    'wpnName': 'Greatsword'
})
data['Weapons'].append({ 
    'wpnName': 'Halberd'
})
data['Weapons'].append({ 
    'wpnName': 'Handaxe'
})
data['Weapons'].append({ 
    'wpnName': 'Heavy Crossbow'
})
data['Weapons'].append({ 
    'wpnName': 'Heavy Flail'
})
data['Weapons'].append({ 
    'wpnName': 'Heavy Mace'
})
data['Weapons'].append({ 
    'wpnName': 'Light Crossbow'
})
data['Weapons'].append({ 
    'wpnName': 'Light Flail'
})
data['Weapons'].append({ 
    'wpnName': 'Light Hammer'
})
data['Weapons'].append({ 
    'wpnName': 'Longbow'
})
data['Weapons'].append({ 
    'wpnName': 'Longsword'
})
data['Weapons'].append({ 
    'wpnName': 'Morningstar'
})
data['Weapons'].append({ 
    'wpnName': 'Quarterstaff'
})
data['Weapons'].append({ 
    'wpnName': 'Rapier'
})
data['Weapons'].append({ 
    'wpnName': 'Spear'
})
data['Weapons'].append({ 
    'wpnName': 'Trident'
})
data['Weapons'].append({ 
    'wpnName': 'Warhammer'
})
data['commonPotion0'] = []  
data['commonPotion0'].append({ 
    'potionName': 'Arcane Mark'
})
data['commonPotion0'].append({ 
    'potionName':'Guidance'
})
data['commonPotion0'].append({ 
    'potionName':'Light'
})
data['commonPotion0'].append({ 
    'potionName':'Purify food and drink'
})
data['commonPotion0'].append({ 
    'potionName':'Resistance'
})
data['commonPotion0'].append({ 
    'potionName':'Stabilize'
})
data['commonPotion0'].append({ 
    'potionName':'Virtue'
})
data['commonPotion1'] = []  
data['commonPotion1'].append({ 
    'potionName':'Bless Weapon'
})
data['commonPotion1'].append({ 
    'potionName':'Cure Light Wounds'
})
data['commonPotion1'].append({ 
    'potionName':'Endure elements'
})
data['commonPotion1'].append({ 
    'potionName':'Enlarge Person'
})
data['commonPotion1'].append({ 
    'potionName':'Jump'
})
data['commonPotion1'].append({ 
    'potionName':'Mage Armor'
})
data['commonPotion1'].append({ 
    'potionName':'Magic Fang'
})
data['commonPotion1'].append({ 
    'potionName':'Magic Weapon'
})
data['commonPotion1'].append({ 
    'potionName':'Pass without trace'
})
data['commonPotion1'].append({ 
    'potionName':'Protection from chaos'
})
data['commonPotion1'].append({ 
    'potionName':'Protection from evil'
})
data['commonPotion1'].append({ 
    'potionName':'Protection from good'
})
data['commonPotion1'].append({ 
    'potionName':'Protection from law'
})
data['commonPotion1'].append({ 
    'potionName':'Reduce person'
})
data['commonPotion1'].append({ 
    'potionName':'Remove fear'
})
data['commonPotion1'].append({ 
    'potionName':'Sanctuary'
})
data['commonPotion1'].append({ 
    'potionName':'Shield of faith'
})
data['uncommonPotion1'] = []  
data['uncommonPotion1'].append({ 
    'potionName':'Animate Rope'
})
data['uncommonPotion1'].append({ 
    'potionName':'Ant haul'
})
data['uncommonPotion1'].append({ 
    'potionName':'Cloak of the shade'
})
data['uncommonPotion1'].append({ 
    'potionName':'Erase'
})
data['uncommonPotion1'].append({ 
    'potionName':'Feather step'
})
data['uncommonPotion1'].append({ 
    'potionName':'Goodberry'
})
data['uncommonPotion1'].append({ 
    'potionName':'Grease'
})
data['uncommonPotion1'].append({ 
    'potionName':'Hided from animals'
})
data['uncommonPotion1'].append({ 
    'potionName':'Hide from undead'
})
data['uncommonPotion1'].append({ 
    'potionName':'Hold portal'
})
data['uncommonPotion1'].append({ 
    'potionName':'Invigorate'
})
data['uncommonPotion1'].append({ 
    'potionName':'Keen senses'
})
data['uncommonPotion1'].append({ 
    'potionName':'Magic stone'
})
data['uncommonPotion1'].append({ 
    'potionName':'Remove Sickness'
})
data['uncommonPotion1'].append({ 
    'potionName':'Sanctify corpse'
})
data['uncommonPotion1'].append({ 
    'potionName':'Shillelagh'
})
data['uncommonPotion1'].append({ 
    'potionName':'Touch of the sea'
})
data['uncommonPotion1'].append({ 
    'potionName':'Vanish'
})	
data['commonPotion2'] = []  
data['commonPotion2'].append({ 
    'potionName':'Aid'
})
data['commonPotion2'].append({ 
    'potionName':'Align weapon'
})
data['commonPotion2'].append({ 
    'potionName':'Barkskin'
})
data['commonPotion2'].append({ 
    'potionName':'Bears Endurance'
})
data['commonPotion2'].append({ 
    'potionName':'Blur'
})
data['commonPotion2'].append({ 
    'potionName':'Bulls Strength'
})
data['commonPotion2'].append({ 
    'potionName':'Cats Grace'
})
data['commonPotion2'].append({ 
    'potionName':'Cure moderate wounds'
})
data['commonPotion2'].append({ 
    'potionName':'Darkvision'
})
data['commonPotion2'].append({ 
    'potionName':'Delay Poison'
})
data['commonPotion2'].append({ 
    'potionName':'Eagles splendor'
})
data['commonPotion2'].append({ 
    'potionName':'Foxs cunning'
})
data['commonPotion2'].append({ 
    'potionName':'Invisibility'
})
data['commonPotion2'].append({ 
    'potionName':'Levitate'
})
data['commonPotion2'].append({ 
    'potionName':'Owls wisdom'
})
data['commonPotion2'].append({ 
    'potionName':'Protection from arrows'
})
data['commonPotion2'].append({ 
    'potionName':'Remove Paralysis'
})
data['commonPotion2'].append({ 
    'potionName':'Resist engergy, Acid'
})
data['commonPotion2'].append({ 
    'potionName':'Resist engergy, cold'
})
data['commonPotion2'].append({ 
    'potionName':'Resist engergy, electricity'
})
data['commonPotion2'].append({ 
    'potionName':'Resist engergy, fire'
})
data['commonPotion2'].append({ 
    'potionName':'Resist engergy, sonic'
})
data['commonPotion2'].append({ 
    'potionName':'Spider climb'
})
data['commonPotion2'].append({ 
    'potionName':'undetectable alignment'
})
data['commonArcane0'] = []  
data['commonArcane0'].append({ 
    'spellName':'Acid Splash'
})
data['commonArcane0'].append({ 
    'spellName':'Daze'
})
data['commonArcane0'].append({ 
    'spellName':'Detect Magic'
})
data['commonArcane0'].append({ 
    'spellName':'Flare'
})
data['commonArcane0'].append({ 
    'spellName':'Light'
})
data['commonArcane0'].append({ 
    'spellName':'MageHand'
})
data['commonArcane0'].append({ 
    'spellName':'Mending'
})
data['commonArcane0'].append({ 
    'spellName':'Prestidigitation'
})
data['commonArcane0'].append({ 
    'spellName':'Ray of Frost'
})
data['commonArcane0'].append({ 
    'spellName':'Read Magic'
})
data['commonArcane0'].append({ 
    'spellName':'Touch of Fatigue'
})
data['uncommonArcane0'] = []  
data['uncommonArcane0'].append({ 
    'spellName':'Arcane Mark'
})
data['uncommonArcane0'].append({ 
    'spellName':'Bleed'
})
data['uncommonArcane0'].append({ 
    'spellName':'Dancing Lights'
})
data['uncommonArcane0'].append({ 
    'spellName':'Detect Poison'
})
data['uncommonArcane0'].append({ 
    'spellName':'Disrupt Undead'
})
data['uncommonArcane0'].append({ 
    'spellName':'Ghost Sound'
})
data['uncommonArcane0'].append({ 
    'spellName':'Message'
})
data['uncommonArcane0'].append({ 
    'spellName':'Open/Close'
})
data['uncommonArcane0'].append({ 
    'spellName':'Resistance'
})
data['uncommonArcane0'].append({ 
    'spellName':'Sift'
})
data['uncommonArcane0'].append({ 
    'spellName':'Spark'
})
data['uncommonArcane0'].append({ 
    'spellName':'Unwitting Ally'
})
data['commonArcane1'] = []  
data['commonArcane1'].append({ 
    'spellName':'Burning Hands'
})
data['commonArcane1'].append({ 
    'spellName':'Cause Fear'
})
data['commonArcane1'].append({ 
    'spellName':'Charm Person'
})
data['commonArcane1'].append({ 
    'spellName':'Chill Touch'
})
data['commonArcane1'].append({ 
    'spellName':'Disguise Self'
})
data['commonArcane1'].append({ 
    'spellName':'Endure Elements'
})
data['commonArcane1'].append({ 
    'spellName':'Enlarge Person'
})
data['commonArcane1'].append({ 
    'spellName':'Expeditious Retreat'
})
data['commonArcane1'].append({ 
    'spellName':'Grease'
})
data['commonArcane1'].append({ 
    'spellName':'Hypnotism'
})
data['commonArcane1'].append({ 
    'spellName':'Identify'
})
data['commonArcane1'].append({ 
    'spellName':'Mage Armor'
})
data['commonArcane1'].append({ 
    'spellName':'Magic Missle'
})
data['commonArcane1'].append({ 
    'spellName':'Magic Weapon'
})
data['commonArcane1'].append({ 
    'spellName':'Obscuring Mist'
})
data['commonArcane1'].append({ 
    'spellName':'Protection from Chaos'
})
data['commonArcane1'].append({ 
    'spellName':'Protection from Evil'
})
data['commonArcane1'].append({ 
    'spellName':'Protection from Good'
})
data['commonArcane1'].append({ 
    'spellName':'Protection from Law'
})
data['commonArcane1'].append({ 
    'spellName':'Ray of Enfeeblement'
})
data['commonArcane1'].append({ 
    'spellName':'Shield'
})
data['commonArcane1'].append({ 
    'spellName':'Shocking Grasp'
})
data['commonArcane1'].append({ 
    'spellName':'Silent Image'
})
data['commonArcane1'].append({ 
    'spellName':'Sleep'
})
data['commonArcane1'].append({ 
    'spellName':'Summon Monster I'
})
data['commonArcane1'].append({ 
    'spellName':'True Strike'
})
data['uncommonArcane1'] = []  
data['uncommonArcane1'].append({ 
    'spellName':'Air Bubble'
})
data['uncommonArcane1'].append({ 
    'spellName':'Alarm'
})
data['uncommonArcane1'].append({ 
    'spellName':'Animate Rope'
})
data['uncommonArcane1'].append({ 
    'spellName':'Ant Haul'
})
data['uncommonArcane1'].append({ 
    'spellName':'Blend'
})
data['uncommonArcane1'].append({ 
    'spellName':'Break'
})
data['uncommonArcane1'].append({ 
    'spellName':'Color Spray'
})
data['uncommonArcane1'].append({ 
    'spellName':'Comprehend Languages'
})
data['uncommonArcane1'].append({ 
    'spellName':'Corrosive Touch'
})
data['uncommonArcane1'].append({ 
    'spellName':'Detect Secret Doors'
})
data['uncommonArcane1'].append({ 
    'spellName':'Detect Undead'
})
data['uncommonArcane1'].append({ 
    'spellName':'Erase'
})
data['uncommonArcane1'].append({ 
    'spellName':'Flare Burst'
})
data['uncommonArcane1'].append({ 
    'spellName':'Floating Disk'
})
data['uncommonArcane1'].append({ 
    'spellName':'Hold Portal'
})
data['uncommonArcane1'].append({ 
    'spellName':'Hydraulic Push'
})
data['uncommonArcane1'].append({ 
    'spellName':'Icicle Dagger'
})
data['uncommonArcane1'].append({ 
    'spellName':'Illusion of Calm'
})
data['uncommonArcane1'].append({ 
    'spellName':'Jump'
})
data['uncommonArcane1'].append({ 
    'spellName':'Magic Aura'
})
data['uncommonArcane1'].append({ 
    'spellName':'Mirror Strike'
})
data['uncommonArcane1'].append({ 
    'spellName':'Mount'
})
data['uncommonArcane1'].append({ 
    'spellName':'Ray of Sickening'
})
data['uncommonArcane1'].append({ 
    'spellName':'Reduce Person'
})
data['uncommonArcane1'].append({ 
    'spellName':'Shadow Weapon'
})
data['uncommonArcane1'].append({ 
    'spellName':'Shock Shield'
})
data['uncommonArcane1'].append({ 
    'spellName':'Stone Fist'
})
data['uncommonArcane1'].append({ 
    'spellName':'Touch of the Sea'
})
data['uncommonArcane1'].append({ 
    'spellName':'Unseen Servant'
})
data['uncommonArcane1'].append({ 
    'spellName':'Urban Grace'
})
data['uncommonArcane1'].append({ 
    'spellName':'Vanish'
})
data['uncommonArcane1'].append({ 
    'spellName':'Ventriloquism'
})
data['uncommonArcane1'].append({ 
    'spellName':'Voice Alteration'
})
data['commonArcane2'] = []  
data['commonArcane2'].append({ 
    'spellName':'Acid Arrow'
})
data['commonArcane2'].append({ 
    'spellName':'Alter Self'
})
data['commonArcane2'].append({ 
    'spellName':'Bears Endurance'
})
data['commonArcane2'].append({ 
    'spellName':'Blur'
})
data['commonArcane2'].append({ 
    'spellName':'Bulls Strength'
})
data['commonArcane2'].append({ 
    'spellName':'Cats Grace'
})
data['commonArcane2'].append({ 
    'spellName':'Darkness'
})
data['commonArcane2'].append({ 
    'spellName':'Darkvision'
})
data['commonArcane2'].append({ 
    'spellName':'Eagles Splendor'
})
data['commonArcane2'].append({ 
    'spellName':'False Life'
})
data['commonArcane2'].append({ 
    'spellName':'Flaming Sphere'
})
data['commonArcane2'].append({ 
    'spellName':'Foxs Cunning'
})
data['commonArcane2'].append({ 
    'spellName':'Glitterdust'
})
data['commonArcane2'].append({ 
    'spellName':'Invisibility'
})
data['commonArcane2'].append({ 
    'spellName':'Knock'
})
data['commonArcane2'].append({ 
    'spellName':'Levitate'
})
data['commonArcane2'].append({ 
    'spellName':'Minor Image'
})
data['commonArcane2'].append({ 
    'spellName':'Mirror Image'
})
data['commonArcane2'].append({ 
    'spellName':'Owls Wisdom'
})
data['commonArcane2'].append({ 
    'spellName':'Resist Energy'
})
data['commonArcane2'].append({ 
    'spellName':'Rope Trick'
})
data['commonArcane2'].append({ 
    'spellName':'Scorching Ray'
})
data['commonArcane2'].append({ 
    'spellName':'See Invisibility'
})
data['commonArcane2'].append({ 
    'spellName':'Shatter'
})
data['commonArcane2'].append({ 
    'spellName':'Spider Climb'
})
data['commonArcane2'].append({ 
    'spellName':'Summon Monster II'
})
data['commonArcane2'].append({ 
    'spellName':'Summon Swarm'
})
data['commonArcane2'].append({ 
    'spellName':'Web'
})
data['commonArcane2'].append({ 
    'spellName':'Whispering Wind'
})
data['uncommonArcane2'] = []  
data['uncommonArcane2'].append({ 
    'spellName':'Bestow Weapon Proficiency'
})
data['uncommonArcane2'].append({ 
    'spellName':'Blindness/Deafness'
})
data['uncommonArcane2'].append({ 
    'spellName':'Burning Gaze'
})
data['uncommonArcane2'].append({ 
    'spellName':'Certain Grip'
})
data['uncommonArcane2'].append({ 
    'spellName':'Command Undead'
})
data['uncommonArcane2'].append({ 
    'spellName':'Create Pit'
})
data['uncommonArcane2'].append({ 
    'spellName':'Daze Monster'
})
data['uncommonArcane2'].append({ 
    'spellName':'Detect Thoughts'
})
data['uncommonArcane2'].append({ 
    'spellName':'Disguise Other'
})
data['uncommonArcane2'].append({ 
    'spellName':'Elemental Touch'
})
data['uncommonArcane2'].append({ 
    'spellName':'Fire Breath'
})
data['uncommonArcane2'].append({ 
    'spellName':'Fog Cloud'
})
data['uncommonArcane2'].append({ 
    'spellName':'Ghoul Touch'
})
data['uncommonArcane2'].append({ 
    'spellName':'Glide'
})
data['uncommonArcane2'].append({ 
    'spellName':'Gust of Wind'
})
data['uncommonArcane2'].append({ 
    'spellName':'Haunting Mists'
})
data['uncommonArcane2'].append({ 
    'spellName':'Hideous Laughter'
})
data['uncommonArcane2'].append({ 
    'spellName':'Hypnotic Pattern'
})
data['uncommonArcane2'].append({ 
    'spellName':'Locate Object'
})
data['uncommonArcane2'].append({ 
    'spellName':'Make Whole'
})
data['uncommonArcane2'].append({ 
    'spellName':'Misdirection'
})
data['uncommonArcane2'].append({ 
    'spellName':'Obscure Object'
})
data['uncommonArcane2'].append({ 
    'spellName':'Pernicious Poison'
})
data['uncommonArcane2'].append({ 
    'spellName':'Protection from Arrows'
})
data['uncommonArcane2'].append({ 
    'spellName':'Pyrotechnics'
})
data['uncommonArcane2'].append({ 
    'spellName':'Returning Weapon'
})
data['uncommonArcane2'].append({ 
    'spellName':'Scare'
})
data['uncommonArcane2'].append({ 
    'spellName':'Shadow Anchor'
})
data['uncommonArcane2'].append({ 
    'spellName':'Share Memory'
})
data['uncommonArcane2'].append({ 
    'spellName':'Slipstream'
})
data['uncommonArcane2'].append({ 
    'spellName':'Spectral Hand'
})
data['uncommonArcane2'].append({ 
    'spellName':'Spontaneous Immolation'
})
data['uncommonArcane2'].append({ 
    'spellName':'Touch of Idiocy'
})
data['uncommonArcane2'].append({ 
    'spellName':'Unshakable Chill'
})
data['uncommonArcane2'].append({ 
    'spellName':'Magic Mouth'
})
data['uncommonArcane2'].append({ 
    'spellName':'Arcane Lock'
})
data['uncommonArcane2'].append({ 
    'spellName':'Continual Flame'
})
data['uncommonArcane2'].append({ 
    'spellName':'Phantom Trap'
})
data['commonDivine0'] = []  
data['commonDivine0'].append({ 
    'spellName':'Bleed'
})
data['commonDivine0'].append({ 
    'spellName':'Create Water'
})
data['commonDivine0'].append({ 
    'spellName':'Detect Magic'
})
data['commonDivine0'].append({ 
    'spellName':'Know Direction'
})
data['commonDivine0'].append({ 
    'spellName':'Light'
})
data['commonDivine0'].append({ 
    'spellName':'Mending'
})
data['commonDivine0'].append({ 
    'spellName':'Purify Food and Drink'
})
data['commonDivine0'].append({ 
    'spellName':'Read Magic'
})
data['commonDivine0'].append({ 
    'spellName':'Stabilize'
})
data['uncommonDivine0'] = []  
data['uncommonDivine0'].append({ 
    'spellName':'Detect Poison'
})
data['uncommonDivine0'].append({ 
    'spellName':'Flare'
})
data['uncommonDivine0'].append({ 
    'spellName':'Guidance'
})
data['uncommonDivine0'].append({ 
    'spellName':'Resistance'
})
data['uncommonDivine0'].append({ 
    'spellName':'Spark'
})
data['uncommonDivine0'].append({ 
    'spellName':'Virtue'
})
data['commonDivine1'] = []  
data['commonDivine1'].append({ 
    'spellName':'Bane'
})
data['commonDivine1'].append({ 
    'spellName':'Bless'
})
data['commonDivine1'].append({ 
    'spellName':'Cause Fear'
})
data['commonDivine1'].append({ 
    'spellName':'Command'
})
data['commonDivine1'].append({ 
    'spellName':'Comprehend Languages'
})
data['commonDivine1'].append({ 
    'spellName':'Cure Light Wounds'
})
data['commonDivine1'].append({ 
    'spellName':'Detect Chaos'
})
data['commonDivine1'].append({ 
    'spellName':'Detect Detect Evil'
})
data['commonDivine1'].append({ 
    'spellName':'Detect Detect Good'
})
data['commonDivine1'].append({ 
    'spellName':'Detect Law'
})
data['commonDivine1'].append({ 
    'spellName':'Detect Undead'
})
data['commonDivine1'].append({ 
    'spellName':'Divine Favor'
})
data['commonDivine1'].append({ 
    'spellName':'Doom'
})
data['commonDivine1'].append({ 
    'spellName':'Entagle'
})
data['commonDivine1'].append({ 
    'spellName':'Inflict Light Wounds'
})
data['commonDivine1'].append({ 
    'spellName':'Magic Fang'
})
data['commonDivine1'].append({ 
    'spellName':'Obscuring Mist'
})
data['commonDivine1'].append({ 
    'spellName':'Produce Flame'
})
data['commonDivine1'].append({ 
    'spellName':'Protection from Chaos'
})
data['commonDivine1'].append({ 
    'spellName':'Protection from Evil'
})
data['commonDivine1'].append({ 
    'spellName':'Protection from Good'
})
data['commonDivine1'].append({ 
    'spellName':'Protection from Law'
})
data['commonDivine1'].append({ 
    'spellName':'Remove Fear'
})
data['commonDivine1'].append({ 
    'spellName':'Sanctuary'
})
data['commonDivine1'].append({ 
    'spellName':'Shield of Faith'
})
data['commonDivine1'].append({ 
    'spellName':'Summon Monster I'
})
data['commonDivine1'].append({ 
    'spellName':'Summon Natures Ally I'
})
data['uncommonDivine1'] = []  
data['uncommonDivine1'].append({ 
    'spellName':'Ant Haul'
})
data['uncommonDivine1'].append({ 
    'spellName':'Aspect of the Falcon'
})
data['uncommonDivine1'].append({ 
    'spellName':'Calm Animals'
})
data['uncommonDivine1'].append({ 
    'spellName':'Charm Animal'
})
data['uncommonDivine1'].append({ 
    'spellName':'Compel Hostility'
})
data['uncommonDivine1'].append({ 
    'spellName':'Deathwatch'
})
data['uncommonDivine1'].append({ 
    'spellName':'Detect Animals or Plants'
})
data['uncommonDivine1'].append({ 
    'spellName':'Detect Snares and Pits'
})
data['uncommonDivine1'].append({ 
    'spellName':'Diagnose Disease'
})
data['uncommonDivine1'].append({ 
    'spellName':'Endure Elements'
})
data['uncommonDivine1'].append({ 
    'spellName':'Entropic Shield'
})
data['uncommonDivine1'].append({ 
    'spellName':'Faerie Fire'
})
data['uncommonDivine1'].append({ 
    'spellName':'Feather Step'
})
data['uncommonDivine1'].append({ 
    'spellName':'Forbid Action'
})
data['uncommonDivine1'].append({ 
    'spellName':'Frostbite'
})
data['uncommonDivine1'].append({ 
    'spellName':'Goodberry'
})
data['uncommonDivine1'].append({ 
    'spellName':'Hide from Animals'
})
data['uncommonDivine1'].append({ 
    'spellName':'Hide from Undead'
})
data['uncommonDivine1'].append({ 
    'spellName':'Hydraulic Push'
})
data['uncommonDivine1'].append({ 
    'spellName':'Jump'
})
data['uncommonDivine1'].append({ 
    'spellName':'Keen Senses'
})
data['uncommonDivine1'].append({ 
    'spellName':'Liberating Command'
})
data['uncommonDivine1'].append({ 
    'spellName':'Longstrider'
})
data['uncommonDivine1'].append({ 
    'spellName':'Magic Stone'
})
data['uncommonDivine1'].append({ 
    'spellName':'Pass without Trace'
})
data['uncommonDivine1'].append({ 
    'spellName':'Remove Sickness'
})
data['uncommonDivine1'].append({ 
    'spellName':'Sanctify Corpse'
})
data['uncommonDivine1'].append({ 
    'spellName':'Shillelagh'
})
data['uncommonDivine1'].append({ 
    'spellName':'Speak with Animals'
})
data['uncommonDivine1'].append({ 
    'spellName':'Stone Fist'
})
data['uncommonDivine1'].append({ 
    'spellName':'Stone Shield'
})
data['uncommonDivine1'].append({ 
    'spellName':'Sun Metal'
})
data['uncommonDivine1'].append({ 
    'spellName':'Touch of the Sea'
})
data['uncommonDivine1'].append({ 
    'spellName':'Bless Water'
})
data['uncommonDivine1'].append({ 
    'spellName':'Curse Water'
})
data['commonDivine2'] = []  
data['commonDivine2'].append({ 
    'spellName':'Aid'
})
data['commonDivine2'].append({ 
    'spellName':'Align Weapon'
})
data['commonDivine2'].append({ 
    'spellName':'Animal Messenger'
})
data['commonDivine2'].append({ 
    'spellName':'Barkskin'
})
data['commonDivine2'].append({ 
    'spellName':'Bears Endurance'
})
data['commonDivine2'].append({ 
    'spellName':'Bulls Strength'
})
data['commonDivine2'].append({ 
    'spellName':'Cats Grace'
})
data['commonDivine2'].append({ 
    'spellName':'Chill Metal'
})
data['commonDivine2'].append({ 
    'spellName':'Cure Moderate Wounds'
})
data['commonDivine2'].append({ 
    'spellName':'Darkness'
})
data['commonDivine2'].append({ 
    'spellName':'Delay Poison'
})
data['commonDivine2'].append({ 
    'spellName':'Eagles Splendor'
})
data['commonDivine2'].append({ 
    'spellName':'Find Traps'
})
data['commonDivine2'].append({ 
    'spellName':'Flame Blade'
})
data['commonDivine2'].append({ 
    'spellName':'Fog Cloud'
})
data['commonDivine2'].append({ 
    'spellName':'Heat Metal'
})
data['commonDivine2'].append({ 
    'spellName':'Hold Animal'
})
data['commonDivine2'].append({ 
    'spellName':'Hold Person'
})
data['commonDivine2'].append({ 
    'spellName':'Inflict Moderate Wounds'
})
data['commonDivine2'].append({ 
    'spellName':'Owls Wisdom'
})
data['commonDivine2'].append({ 
    'spellName':'Remove Paralysis'
})
data['commonDivine2'].append({ 
    'spellName':'Reist Energy'
})
data['commonDivine2'].append({ 
    'spellName':'Restoration Lesser'
})
data['commonDivine2'].append({ 
    'spellName':'Shield Other'
})
data['commonDivine2'].append({ 
    'spellName':'Silence'
})
data['commonDivine2'].append({ 
    'spellName':'Sound Burst'
})
data['commonDivine2'].append({ 
    'spellName':'Spirital Weapon'
})
data['commonDivine2'].append({ 
    'spellName':'Summon Monster II'
})
data['commonDivine2'].append({ 
    'spellName':'Summon Natures Ally II'
})
data['commonDivine2'].append({ 
    'spellName':'Summon Swarm'
})
data['commonDivine2'].append({ 
    'spellName':'Zone of Truth'
})
data['commonDivine2'].append({ 
    'spellName':'Augury'
})
data['uncommonDivine2'] = []  
data['uncommonDivine2'].append({ 
    'spellName':'Uncommon 2'
})

data['gem1'] = []  
data['gem1'].append({ 
    'gemName':'Agate (10gp)'
})
data['gem1'].append({ 
    'gemName':'Alabaster (10gp)'
})
data['gem1'].append({ 
    'gemName':'Azurite (10gp)'
})
data['gem1'].append({ 
    'gemName':'Hematite (10gp)'
})
data['gem1'].append({ 
    'gemName':'Lapis Lazuli (10gp)'
})
data['gem1'].append({ 
    'gemName':'Malachite (10gp)'
})
data['gem1'].append({ 
    'gemName':'Obsidian (10gp)'
})
data['gem1'].append({ 
    'gemName':'Pearl (10gp)'
})
data['gem1'].append({ 
    'gemName':'Pyrite (10gp)'
})
data['gem1'].append({ 
    'gemName':'Rhodochrosite (10gp)'
})
data['gem1'].append({ 
    'gemName':'Quartz (10gp)'
})
data['gem1'].append({ 
    'gemName':'Shell (10gp)'
})
data['gem1'].append({ 
    'gemName':'Tigereye (10gp)'
})
data['gem1'].append({ 
    'gemName':'Turquoise (10gp)'
})
data['gem2'] = []  
data['gem2'].append({ 
    'gemName':'Bloodstone (50gp)'
})
data['gem2'].append({ 
    'gemName':'Carnelian (50gp)'
})
data['gem2'].append({ 
    'gemName':'Chrysoprase (50gp)'
})
data['gem2'].append({ 
    'gemName':'Citrine (50gp)'
})
data['gem2'].append({ 
    'gemName':'Ivory (50gp)'
})
data['gem2'].append({ 
    'gemName':'Jasper (50gp)'
})
data['gem2'].append({ 
    'gemName':'Moonstone (50gp)'
})
data['gem2'].append({ 
    'gemName':'Onyx (50gp)'
})
data['gem2'].append({ 
    'gemName':'Peridot (50gp)'
})
data['gem2'].append({ 
    'gemName':'Quartz (50gp)'
})
data['gem2'].append({ 
    'gemName':'Sard (50gp)'
})
data['gem2'].append({ 
    'gemName':'Sardonyx (50gp)'
})
data['gem2'].append({ 
    'gemName':'Spinel (50gp)'
})
data['gem2'].append({ 
    'gemName':'Zircon (50gp)'
})

with open('items.json', 'w') as outfile:  
    json.dump(data, outfile)
















