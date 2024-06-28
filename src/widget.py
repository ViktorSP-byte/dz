import masks

def get_data(data):
    """Функция, меняющая формат даты"""
    result = data[8:10] + "." + data[5:7] + "." + data[:4]
    return result


data = "2018-07-11T02:26:18.671407"
print(get_data(data))
