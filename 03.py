def anonymize(email):
    ret = ""
    if len(email) < 10:
        ret = "***" + email[-5:]
    else:
        ret = email[0:3] + "***" + email[-5:]

    return ret

print(anonymize('j.kowalski@gmail.com'))
print(anonymize('jko@o2.pl'))
