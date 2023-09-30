from db import NAME
from functions import main_script


def run(flag=False):
    if flag:
        print('========  Сессия  ========')
        main_script(RAIN)
    else:
        for _ in NAME:
            print(_)
            main_script(RAIN)


""""""
RAIN = False  # принудительно включить дождь
ONE_SESSION = False  # сгенерировать погоду для одной сессии

if __name__ == '__main__':
    run(ONE_SESSION)
