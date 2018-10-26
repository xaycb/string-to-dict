def string_to_dict(value=None):
    result = {}

    if isinstance(value, str):
        temp_list = value.split(':')
    else:
        return 'Incorrect input: {} is not a string!'.format(value)

    try:
        for i in range(0, len(temp_list), 2):
            if result.get(temp_list[i]):
                result[temp_list[i]].append(temp_list[i+1])
            else:
                result[temp_list[i]] = [temp_list[i+1]]
    except IndexError:
        return 'Incorrect input'

    return result


if __name__ == '__main__':

    print(string_to_dict('key1:val1:key2:val2'))
