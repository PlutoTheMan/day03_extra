def user_data(first_name, last_name):
    if type(first_name) != str or type(last_name) != str:
        raise TypeError

    ret = {
        "first name": first_name,
        "last name": last_name,
        "full_name": first_name + " " + last_name,
        "initials": first_name[0] + ". " + last_name[0] + "."
    }

    return ret


print(user_data('Jan', 'Kowalski'))
