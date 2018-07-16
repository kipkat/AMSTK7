from algorithm7 import nature


def amstk9(s: str, chars: int = 64, seed2: int = 0, charmap: int = 26, charstart: int = 65, replacedict: dict = {}):
    seed = len(s)
    leg = len(s)
    e = ''
    for x in s:
        asc = ord(x)
        seed += asc
        e += chr(asc * leg * len(str(asc)) % charmap + charstart)
        e += str(((asc * 9 * leg + 42 * len(str(asc))) % 10 + len(e)) % 10)
        e += str(len(e))
    for x in e:
        asc = ord(x)
        e += chr(asc * leg * seed % 10 * len(str(asc)) % charmap + charstart)
        e += str(((asc * 8 * leg + 53 * len(str(asc))) % 10 + len(e) + seed) % 10)
        e += chr(len(e) % charmap + charstart)
        e += str(len(e))
    seed *= int.from_bytes(e.encode(), 'big')
    seed += int.from_bytes(s.encode(), 'big')
    nature.seed(seed + seed2)
    str_var = list(e)
    nature.shuffle(str_var)
    e = ''.join(str_var)
    for x in range(1, 8):
        str_var = list(e)
        nature.shuffle(str_var)
        e += ''.join(str_var)
    rpl = ''
    for x in e[-chars:]:
        if x in replacedict:
            rpl += replacedict[x]
        else:
            rpl += x
    return rpl


def repeat_amstk9(s: str, repeats: int = 0, chars: int = 64, seed2: int = 0, charmap: int = 26, charstart: int = 65,
                  replacedict: dict = {}):
    for x in range(repeats):
        s = amstk9(s, chars, seed2, charmap, charstart, replacedict)
    return s
