from db import *
from views import *
from functions import *

RAIN = 0     # принудительно включить дождь

if __name__ == '__main__':
    view_time(get_game_parameter(TIME))
    view_sky(get_game_parameter(SKY))
    view_temp((get_game_parameter(TEMPERATURE)))
    weather = generate_type_weather(DRY_OR_RAIN)
    if weather == 'дождь' or RAIN is True:
        view_weather(weather)
        view_wet(get_game_parameter(WET_VALUE))
        view_water(get_game_parameter(WATER_ON_THE_TRACK))
    else:
        view_weather(weather)
