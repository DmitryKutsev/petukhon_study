from petuch import add_petuch


def check_petuch():
    petuch_add_res = add_petuch('Python')
    if type(petuch_add_res) == str:
        return petuch_add_res
    else:
        return "Fuck off! This type isn't str, this is", type(petuch_add_res)