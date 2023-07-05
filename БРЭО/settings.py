SETTINGS = {
    # маршрут
    'PATHWAY': {
        # приоритетность маршрута
        'PRIORITY': { 
            'NORMAL': 'normal',
            'HIGH': 'high',
            'URGENT': 'urgent'
        },
        # полетное задание
        'TASK': {
            'FLY': 'fly', # полет с зависанием
            'DELIVERY': 'delivery', # полет с разгрузкой
            'LANDING': 'landing' # полет с посадкой
        }
    },
    # список событий медиатора
    'MEDIATOR_EVENTS': {
        'TEST': 'TEST',
        'MAKE_PATHWAY': 'MAKE_PATHWAY', # задать полетное задание (маршрут)
        'NEW_PATHWAY': 'NEW_PATHWAY', # новое полетное задание создано
        'START_NEXT_PATHWAY': 'START_NEXT_PATHWAY', # начать выполнение следующего полетного задания
        'TERMINATE_PATHWAY': 'TERMINATE_PATHWAY', # прекратить выполнение текущего маршрута
        'GET_NEXT_POINT': 'GET_NEXT_POINT', # запросить следующую точку полетного маршрута
        'FIRST_POINT': 'FIRST_POINT', # первая точка полетного маршрута
        'NEXT_POINT': 'NEXT_POINT', # следующая точка полетного маршрута
        'LAST_POINT': 'LAST_POINT', # последняя точка полетного маршрута

        'SIMPLE_ARM': 'SIMPLE_ARM', # заармится, включить двигатели, подрочить, и выключиться

        'CAMERA_IMAGE_CAPTURE': 'CAMERA_IMAGE_CAPTURE', # захваченный очередной снимок с камеры

        'FIRE_DROP': 'FIRE_DROP', # сбросить подарки, нанести счастье, причинить добро
        'SHUTDOWN': 'SHUTDOWN', # команда на выключение
        'REBOOT': 'REBOOT' # команда на перезапуск
    },
    # список используемых пинов
    'PINS': {
        'DROP': 7, # сбросить подарки
        'GROUND': 9 # земля
    }
}