def amstk7(s: str, chars: int = 64):
    seed = len(s)
    l = len(s)
    e = ''
    for x in s:
        ascii = ord(x)
        seed += ord(x)
        e += chr(ascii * l * len(ascii.__str__()) % 26 + 65)
        e += str((ascii * 3 * l + 42 * len(ascii.__str__())) % 10 + len(e))
    for x in e:
        ascii = ord(x)
        e += chr(ascii * l * seed % 10 * len(ascii.__str__()) % 26 + 65)
        e += str((ascii * 3 * l + 42 * len(ascii.__str__())) % 10 + len(e) + seed % 10)
    seed *= int.from_bytes(e.encode(), 'big')
    seed += int.from_bytes(s.encode(), 'big')
    random.seed(seed)
    str_var = list(e)
    random.shuffle(str_var)
    e = ''.join(str_var)
    for x in range(1, 6):
        str_var = list(e)
        random.shuffle(str_var)
        e += ''.join(str_var)
    return (e[-chars:])


def seed_amstk7(s: str, seed2: int, chars: int = 64):
    seed = len(s)
    l = len(s)
    e = ''
    for x in s:
        ascii = ord(x)
        seed += ord(x)
        e += chr(ascii * l * len(ascii.__str__()) % 26 + 65)
        e += str((ascii * 3 * l + 42 * len(ascii.__str__())) % 10 + len(e))
    for x in e:
        ascii = ord(x)
        e += chr(ascii * l * seed % 10 * len(ascii.__str__()) % 26 + 65)
        e += str((ascii * 3 * l + 42 * len(ascii.__str__())) % 10 + len(e) + seed % 10)
    seed *= int.from_bytes(e.encode(), 'big');
    seed += int.from_bytes(s.encode(), 'big')
    random.seed(seed + seed2)
    str_var = list(e)
    random.shuffle(str_var)
    e = ''.join(str_var)
    for x in range(1, 6):
        str_var = list(e)
        random.shuffle(str_var)
        e += ''.join(str_var)
    return (e[-chars:])


def repeat_amstk7(s: str, repeats: int, chars: int = 64):
    for x in range(repeats): s = amstk7(s, chars)
    return s
