def main( room ): # room - номер комнаты, которую ищем

    assert room <= 2_000_000_000, 'номер команты слишком большой'

    floor = 0 # номер этажа, на котором находится комната
    order = 0 # порядковый номер комнаты на этаже

    cur_room = 0 # номер последней просмотренной комнаты

    side = 0 # содержит сторону текущего квадрата 1*1, 2*2, 3*3 и так далее

    while True:
        side += 1

        if cur_room + side**2 < room:
            cur_room += side**2
            floor += side
            continue

        for i in range(0, side):
            floor += 1
            order = 0

            if cur_room + side < room:
                cur_room += side
                continue

            order += room - cur_room

            return floor, order

if __name__ == "__main__":
    while True:
        try:
            room = int(input("какую комнату будем искать: "))
        except ValueError: # чтобы выйти, достаточно ввести любое не_число
            exit()
        floor, order = main(room)
        print( "комната с номером {0} находится на этаже {1}, порядковый номер комнаты на этаже {2}".format(room, floor, order) )