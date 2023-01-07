def create_address(first_name, last_name, street, number, city, zipcode):
    ret = f'Sz. P. {first_name} {last_name}\n' \
          f'ul. {street} {number}\n' \
          f'{zipcode} {city}'
    return ret

print(create_address('Jan', 'Kowalski', 'Lipowa', 4, 'Warszawa', '00-123'))
