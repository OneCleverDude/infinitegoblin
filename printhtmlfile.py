from string import Template
from PIL import Image, ImageFilter
from pathlib import Path
import buildtreasure as treasure
import buildmapimages as buildmap


def build_html_page(lair):
    print("starting large map")
    buildmap.print_map(lair)
    print("finish large map")
    path = 'demo.html'
    d = open(path, 'w')
    print("start writing rooms")
    d.write(print_rooms(lair))
    print("finish writing rooms")
    print("start writing all monsters")
    d.write(print_all_monsters(lair))
    print("finish writing all monsters")
    d.close()


def print_rooms(lair):
    # Prints the rooms to HTML
    data_folder = Path("htmltemplates/")
    path = 'skeletonheader.html'
    with open(data_folder / path) as h:
        header = h.read()
    path = 'template-monster-new.html'
    with open(data_folder / path) as mb:
        monsterbody = mb.read()
    path = 'template-encounterfooter.html'
    with open(data_folder / path) as ef:
        encounterfooter = ef.read()
    path = 'template.html'
    with open(data_folder / path) as b:
        body = b.read()
    ht = Template(header)
    header = ht.substitute(mapfile='map.png', goblinTribeName=lair.goblinTribeName, goblinGod=lair.goblinGod,
                           playerNum=lair.numberOfPlayers, APL=lair.apl, totalLevels=lair.totalLevels,
                           notes=lair.notes, origin=lair.origin)
    output_string = header
    data_folder = Path("mapassets/")
    im = Image.open(data_folder / 'transparent.png')
    db = Image.open(data_folder / 'floor_debug2.png')
    data_folder = Path("mapassets/")
    ch1 = Image.open(data_folder / 'map-crosshatch0.png')
    ch2 = Image.open(data_folder / 'map-crosshatch1.png')

    for i in range(len(lair.encounter)):
        print("working on room "+str(i))
        r = Template(body)
        room_text = r.substitute(titleText=lair.encounter[i].titleText, number=str(lair.encounter[i].room_number),
                                 subHead=lair.encounter[i].subHead,
                                 flavor=lair.encounter[i].flavor, notes=lair.encounter[i].notes,
                                 roommap=str(i) + '.png')
        output_string = output_string + room_text
        room_map_width = ((abs(lair.encounter[i].x2 - lair.encounter[i].x1) + 6) * 40)
        room_map_height = ((abs(lair.encounter[i].y2 - lair.encounter[i].y1) + 6) * 40)
        room_image = im.resize((room_map_width, room_map_height))
        image_y = 0
        for y in range((lair.encounter[i].y1 - 2), (lair.encounter[i].y2 + 3)):
            image_y = image_y + 1
            image_x = 0
            for x in range((lair.encounter[i].x1 - 2), (lair.encounter[i].x2 + 3)):
                image_x = image_x + 1
                position = (image_x * 40, image_y * 40)
                if y < 0 or y > lair.MAP_HEIGHT - 1 or x < 0 or x > lair.MAP_WIDTH - 1:
                    room_image.paste(db, position)
                else:
                    if lair.map[y][x] > 0:
                        p1 = p2 = p3 = p4 = 0
                        if lair.map[y][x-1] < 1:
                            p1 = 1
                        if lair.map[y][x+1] < 1:
                            p3 = 1
                        if lair.map[y-1][x] < 1:
                            p2 = 1
                        if lair.map[y+1][x] < 1:
                            p4 = 1
                        fl = Image.open(data_folder / ("map-genericfloor-"+str(p1)+str(p2)+str(p3)+str(p4)+".png"))
                        room_image.paste(fl, position)
                        if lair.map[y][x] > 99:
                            fl = Image.open(data_folder / ("map-"+str(lair.map[y][x])+".png"))
                            extra_position = ((image_x * 40) + 4, (image_y * 40) + 4)
                            room_image.paste(fl, extra_position)
                        if int(lair.map[y][x]) < 99:
                            num_position = ((image_x * 40)+5, (image_y * 40)+5)
                            n1 = Image.open(data_folder / ("map-"+str(lair.map[y][x])+".png"))
                            room_image.paste(n1, num_position)

                    else:
                        if lair.map[y][x] == 0:
                            room_image.paste(ch1, position)
                        else:
                            room_image.paste(ch2, position)
        room_image.save(str(i) + '.png')
        counter = 0
        mr = Template(monsterbody)
        for j in range(len(lair.encounter[i].monster_list)):
            counter += 1
            treasure_roll = ""
            for r, s in lair.encounter[i].monster_list[j]['treasureRoll'].items():
                treasure_roll += treasure.build_horde(r, s)  # TODO: This needs to be in the generation, not the print.
            mbtext = mr.substitute(monsterName=lair.encounter[i].monster_list[j]['monsterName'],
                                   image=lair.encounter[i].monster_list[j]['imageCard'],
                                   HP=lair.encounter[i].monster_list[j]['HP'],
                                   AC=lair.encounter[i].monster_list[j]['AC']['normal'],
                                   fort=lair.encounter[i].monster_list[j]['saves']['FORT'],
                                   reflex=lair.encounter[i].monster_list[j]['saves']['REF'],
                                   will=lair.encounter[i].monster_list[j]['saves']['WILL'],
                                   attackicon=lair.encounter[i].monster_list[j]['attacks'][0][1],
                                   attackwpn=lair.encounter[i].monster_list[j]['attacks'][0][2],
                                   attackbonus=lair.encounter[i].monster_list[j]['attacks'][0][3],
                                   damage=lair.encounter[i].monster_list[j]['attacks'][0][4],
                                   init=lair.encounter[i].monster_list[j]['init'],
                                   treasure=treasure_roll, tactics=lair.encounter[i].monster_list[j]['tactics'])
            output_string = output_string + mbtext
            if counter > 4:
                output_string = output_string + '</div><div class="row align-items-start">'
                counter = 0
        while counter < 5:
            counter = counter + 1
            output_string = output_string + ' <div class="col-md"></div>'
        output_string = output_string + encounterfooter

    return output_string


def print_all_monsters(lair):
    # Gets all of the monsters so we can make a monster index at the end of the file.
    all_monsters = []
    for i in range(len(lair.encounter)):
        for j in range(len(lair.encounter[i].monster_list)):
            all_monsters.append(lair.encounter[i].monster_list[j])
    all_print_monsters = list({v['monsterName']: v for v in all_monsters}.values())
    print_monsters = sorted(all_print_monsters, key=lambda t: (t['xp'], t['monsterName']))
    data_folder = Path("htmltemplates/")
    path = 'template-monstercards-main.html'
    with open(data_folder / path) as mb:
        monster_body = mb.read()
    path = 'template-monstercards-end.html'
    with open(data_folder / path) as mbe:
        monster_body_each = mbe.read()
    path = 'template-monstercards-attacks.html'
    with open(data_folder / path) as mba:
        monster_body_each_attack = mba.read()
    counter = 0
    output_string = '<h2>Monster Index</h2><hr /><div class="row">'
    for i in range(len(print_monsters)):
        counter += 2
        mc = Template(monster_body)
        mc_text = mc.substitute(monsterName=print_monsters[i]['monsterName'], size=print_monsters[i]['size'],
                                image=print_monsters[i]['imageCard'], HP=print_monsters[i]['HP'],
                                monsterType=print_monsters[i]['monsterType'], xp=print_monsters[i]['xp'],
                                cr=print_monsters[i]['cr'], AC=print_monsters[i]['AC']['normal'],
                                HD=print_monsters[i]['HD'],
                                init=print_monsters[i]['init'], speed=print_monsters[i]['speed'],
                                fort=print_monsters[i]['saves']['FORT'], reflex=print_monsters[i]['saves']['REF'],
                                will=print_monsters[i]['saves']['WILL'], str=print_monsters[i]['scores']['STR'],
                                dex=print_monsters[i]['scores']['DEX'], con=print_monsters[i]['scores']['CON'],
                                int=print_monsters[i]['scores']['INT'], wis=print_monsters[i]['scores']['WIS'],
                                cha=print_monsters[i]['scores']['CHA'],
                                strmod=(print_monsters[i]['scores']['STR']-10)//2,
                                dexmod=(print_monsters[i]['scores']['DEX']-10)//2,
                                conmod=(print_monsters[i]['scores']['CON']-10)//2,
                                intmod=(print_monsters[i]['scores']['INT']-10)//2,
                                wismod=(print_monsters[i]['scores']['WIS']-10)//2,
                                chamod=(print_monsters[i]['scores']['CHA']-10)//2,
                                flatfooted=print_monsters[i]['AC']['flatfooted'],
                                touch=print_monsters[i]['AC']['touch'], cmd=print_monsters[i]['AC']['cmd'],
                                saves=print_monsters[i]['saves'], tactics=print_monsters[i]['tactics'],
                                scores=print_monsters[i]['scores'], senses=print_monsters[i]['senses'],
                                alignment=print_monsters[i]['alignment'], languages=print_monsters[i]['languages'],
                                crunch=print_monsters[i]['crunch'], treasure='10gp',
                                job=print_monsters[i]['job'])
        output_string = output_string + mc_text
        # loop on the number of attacks
        if len(print_monsters[i]['attacks']) > 0:
            for attacks in range(len(print_monsters[i]['attacks'])):
                mca = Template(monster_body_each_attack)
                mca_text = mca.substitute(attacktype=print_monsters[i]['attacks'][attacks][0],
                                          attackicon=print_monsters[i]['attacks'][attacks][1],
                                          attackwpn=print_monsters[i]['attacks'][attacks][2],
                                          attackbonus=print_monsters[i]['attacks'][attacks][3],
                                          damage=print_monsters[i]['attacks'][attacks][4],
                                          crit=print_monsters[i]['attacks'][attacks][5],
                                          range=print_monsters[i]['attacks'][attacks][6])
                output_string = output_string + mca_text
        mce = Template(monster_body_each)
        mce_text = mce.substitute(crunch=print_monsters[i]['crunch'], treasure='10gp')
        output_string = output_string + mce_text
        if counter > 1:
            output_string += '</div><div class="row">'
            counter = 0
    while counter < 2:
        counter = counter + 1
        output_string += ' <div class="col-sm"></div>'
    output_string += '</div>'

    path = 'skeletonfooter.html'
    with open(data_folder / path) as f:
        footer = f.read()
    output_string = output_string + footer
    return output_string
