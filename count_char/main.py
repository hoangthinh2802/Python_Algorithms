import operator


from typing import Counter, Tuple




def count_chars_ve(strings: str) -> Tuple[str, int]:
    strings = strings.lower()

    l = [(c, strings.count(c)) for c in strings if not c.isspace()]
    return max(l, key=operator.itemgetter(1))

def count_chars_v2(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]

def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter() 
    for char in strings:
        if not char.isspace():
            d[char] += 1
    max_key = max(d, key = d.get)
    return max_key, d[max_key]


if __name__=='__main__':
    s = 'This is a pen. This is an apple. Applenpen.'
    print(count_chars_v3(s))
   
