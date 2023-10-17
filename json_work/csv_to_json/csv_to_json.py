import csv
import pygal
from pygal.style import RotateStyle as RS
from country_codes import get_country_code

filename = 'API_SE.ADT.LITR.MA.ZS_DS2_en_csv_v2_4903406.csv'
with open(filename) as f:
    grow_data = csv.reader(f)
    
    title_row = next(grow_data)
    empty_row = next(grow_data)
    update_row = next(grow_data)
    empty_row_1 = next(grow_data)
    header_row = next(grow_data)

    country_literacy = {}
    for row in grow_data:
        country_name = row[0]
        literacy = row[65]
        if literacy == '':
            literacy = row[64]
        if literacy == '':
            literacy = row[63]
        if literacy == '':
            literacy = row[62]
        if literacy == '':
            literacy = row[61]
        if literacy == '':
            literacy = row[60]
        if literacy == '':
            literacy = row[59]
        if literacy == '':
            literacy = row[58]
        if literacy == '':
            literacy = row[57]
        if literacy == '':
            literacy = row[56]
        if literacy == '':
            literacy = row[55]
        if literacy == '':
            literacy = row[54]
        if literacy == '':
            literacy = row[53]
        if literacy == '':
            literacy = row[52]
        if literacy == '':
            literacy = row[51]
        if literacy == '':
            literacy = row[50]
        if literacy == '':
            literacy = row[49]
        if literacy == '':
            literacy = row[48]
        if literacy == '':
            literacy = row[47]
        if literacy == '':
            literacy = row[46]
        if literacy == '':
            literacy = row[45]
        else:
            country_code = get_country_code(country_name)
            country_literacy[country_code] = float(literacy)
            
# Группировка стран по 6 уровням грамотности населения
cc_literacy_1, cc_literacy_2, cc_literacy_3 = {}, {}, {}
cc_literacy_4, cc_literacy_5, cc_literacy_6 = {}, {}, {}
for cc, literacy  in country_literacy.items():
    if literacy > 95:
        cc_literacy_1[cc] = literacy
    elif literacy > 90:
        cc_literacy_2[cc] = literacy
    elif literacy > 85:
        cc_literacy_3[cc] = literacy
    elif literacy > 80:
        cc_literacy_4[cc] = literacy
    elif literacy > 75:
        cc_literacy_5[cc] = literacy
    else:
        cc_literacy_6[cc] = literacy
        
wm_style = RS('#FFFF00')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Literacy rate, adult male /n(% of males ages 15 and above, 2001-2021)'
wm.add('95-100%', cc_literacy_1)
wm.add('90-95%', cc_literacy_2)
wm.add('85-90%', cc_literacy_3)
wm.add('80-85%', cc_literacy_4)
wm.add('75-80%', cc_literacy_5)
wm.add('<75%', cc_literacy_6)

wm.render_to_file('literacy.svg')

