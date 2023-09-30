import random
from db import *
from views import *


def _random_value(a, b):
    value = random.randint(a, b)
    return value


def _random_value_from_tuple(item):
    first_value = item[0]
    second_value = item[1]
    final_value = _random_value(first_value, second_value)
    return final_value


def _get_game_parameter(data_set: tuple | list):
    if type(data_set) == tuple:
        item = data_set
        return _random_value_from_tuple(item)

    if type(data_set) == list:
        value = _random_value(0, len(data_set) - 1)
        item = data_set[value]
        return _random_value_from_tuple(item)


def _generate_type_weather(data_set):
    value = _random_value(0, len(data_set) - 1)
    weather_type = data_set[value]
    return weather_type


def main_script(rain_flag=False):
    view_time(_get_game_parameter(TIME))
    view_sky(_get_game_parameter(SKY))
    view_temp((_get_game_parameter(TEMPERATURE)))
    weather = _generate_type_weather(DRY_OR_RAIN)
    if weather == 'дождь' or rain_flag is True:
        view_weather(weather)
        view_wet(_get_game_parameter(WET_VALUE))
        view_water(_get_game_parameter(WATER_ON_THE_TRACK))
    else:
        view_weather(weather)
    print()
