import json
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# Список заполняется данными
filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)
    
# Построение словаря с данными ВВП
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = gdp_dict['Value']
        country_code = get_country_code(country_name)
        if country_code:
            cc_gdp[country_code] = gdp
        else:
            print('ERROR - ' + country_name)

wm_style = RS('#00FF00', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Regional and World GDP (Gross Domestic Product), by Country'
wm.add('2016', cc_gdp)

wm.render_to_file('world_gdp_2016.svg')

