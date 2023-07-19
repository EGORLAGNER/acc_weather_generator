import random


def random_value(a, b):
    value = random.randint(a, b)
    return value


def random_value_from_tuple(item):
    first_value = item[0]
    second_value = item[1]
    final_value = random_value(first_value, second_value)
    return final_value


def get_game_parameter(data_set: tuple | list):
    if type(data_set) == tuple:
        item = data_set
        return random_value_from_tuple(item)

    if type(data_set) == list:
        value = random_value(0, len(data_set) - 1)
        item = data_set[value]
        return random_value_from_tuple(item)


def generate_type_weather(data_set):
    value = random_value(0, len(data_set) - 1)
    weather_type = data_set[value]
    return weather_type
