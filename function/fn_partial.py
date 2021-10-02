from functools import partial


def check_connection(key):
    print('True')
    if key == 123:
        return True


def get_map_data(key: str, start, end):
    check_connection(key)
    print(start)
    print(end)


get_map_data_check_connection = partial(get_map_data, 123)
get_map_data_check_connection_start = get_map_data_check_connection('abc', 'xyz')
print(get_map_data_check_connection_start())