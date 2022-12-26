import json

def to_json(func):
    def wrapper():
        result = func()

        with open('func_to_json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        if func.__name__  in json_data:
            json_data[func.__name__].append(result)
        else:
            json_data[func.__name__ ] = []
            json_data[func.__name__ ].append(result)

        with open('func_to_json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=3)

        with open('func_to_json', 'r', encoding = 'utf-8') as file:
            json_data  = json.load(file)
            search_value = json_data.get(func.__name__)
            print(*search_value, sep='\n')

        return result
    return wrapper

@to_json
def crow_time():
    from datetime import datetime
    rooster = "Yout crow time is " + str(datetime.now())
    return(rooster)

@to_json
def rand_mts_num():
    MTS = ["915", "910", "911", "912", "913", "914", "987"]
    from string import digits
    from random import choice, sample
    tel = {}
    s7 = sample(digits, 7)
    s_str = ""

    for ind, val in enumerate(s7):
        s_str += s7[ind]

    tel["MTS"] = "+7" + choice(MTS) + s_str

    return tel

crow_time()