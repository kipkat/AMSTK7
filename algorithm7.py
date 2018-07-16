import random as nature
import newalg7

def amstk7(s: str, chars: int = 64):
    seed = len(s)
    leg = len(s)
    e = ''
    for x in s:
        asc = ord(x)
        seed += asc
        e += chr(asc * leg * len(str(asc)) % 26 + 65)
        e += str((asc * 3 * leg + 42 * len(str(asc))) % 10 + len(e))
    for x in e:
        asc = ord(x)
        e += chr(asc * leg * seed % 10 * len(str(asc)) % 26 + 65)
        e += str((asc * 3 * leg + 42 * len(str(asc))) % 10 + len(e) + seed % 10)
        e += chr(len(e) % 26 + 65)
    seed *= int.from_bytes(e.encode(), 'big')
    seed += int.from_bytes(s.encode(), 'big')
    nature.seed(seed)
    str_var = list(e)
    nature.shuffle(str_var)
    e = ''.join(str_var)
    for x in range(1, 6):
        str_var = list(e)
        nature.shuffle(str_var)
        e += ''.join(str_var)
    return e[-chars:]


def seed_amstk7(s: str, seed2: int, chars: int = 64):
    seed = len(s)
    leg = len(s)
    e = ''
    for x in s:
        asc = ord(x)
        seed += ord(x)
        e += chr(asc * leg * len(str(asc)) % 26 + 65)
        e += str((asc * 3 * leg + 42 * len(str(asc))) % 10 + len(e))
    for x in e:
        asc = ord(x)
        e += chr(asc * leg * seed % 10 * len(str(asc)) % 26 + 65)
        e += str((asc * 3 * leg + 42 * len(str(asc))) % 10 + len(e) + seed % 10)
        e += chr(len(e) % 26 + 65)
    seed *= int.from_bytes(e.encode(), 'big')
    seed += int.from_bytes(s.encode(), 'big')
    nature.seed(seed + seed2)
    str_var = list(e)
    nature.shuffle(str_var)
    e = ''.join(str_var)
    for x in range(1, 6):
        str_var = list(e)
        nature.shuffle(str_var)
        e += ''.join(str_var)
    return e[-chars:]


def repeat_amstk7(s: str, repeats: int, chars: int = 64):
    for x in range(repeats):
        s = amstk7(s, chars)
    return s
