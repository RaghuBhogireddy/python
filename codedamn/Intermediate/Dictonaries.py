

def main():
    """ We can create dictonaries in 4 standard ways"""
    d_1 = {'A' : 1, 'B' : 2, 'C' : 3}
    d_2 = dict(A=1, B=2, C=3)
    d_3 = dict([('A',1),('B',2),('C',3)])

    """ We can create dictonaries 
        using two Lists """
    x = ['x', 'y', 'z']
    y = ['1','2','3']
    d_4 = dict(zip(x,y))

    """ we can create using dict.fromkeys(itrable, value) class method"""
    d_5 = dict.fromkeys(x,0) # The value '0' is default will get assigned to all keys
    print(d_1, d_2, d_3, d_4, d_5)

    """ we can retrive keys from dictonaries using d_5.keys() method"""
    print(type(d_5.keys()), d_5.keys())

    """ we can retrive values from dictonaries using d_5.values() method"""
    print(type(d_5.values()), d_5.values())

    """ we can retrive values from dictonaries using two modes ( d_3.get(key) || d_3[] method"""
    print(d_4.get('z'), d_4['z'])

    """ we can retrive items from dictonaries using d_3.items() """
    print(type(d_3.items()), d_3.items())

    """ we can check the membership in dictonary using " v in d_1" Note: it checks for keys alone"""
    print("A" in d_1)


    """ we can also loop through individual items like key or values"""

    for keys in d_1.keys():
        print(keys)

    for values in d_1.values():
        print(values)

    """ we can loop through items using d_1.items() methods """
    for keys, values in d_1.items():
        print(keys, values)

    """ we can pop items from dictonaries using d_1.pop(key)"""
    print(d_1.pop("A"))

    """ we can pop last pair from dictonaries using d_1.popitem() acts a LIFO"""
    print(d_1.popitem())

    """ setdefault(self, key, default=None, /)
    Insert key with a value of default if key is not in the dictionary.
    Return the value for key if key is in the dictionary, else default."""

    print(d_1.setdefault("C"))
    print(d_1)
    print(d_1.setdefault("B"))
    print(d_1.setdefault("C",3))


    """update(...)
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]"""
    d_1.update(A=4)
    print(d_1)

    """copy(...)
    D.copy() -> a shallow copy of D"""
    d_6 = d_1.copy()
    print(d_6)

    """clear(...)
    D.clear() -> None.  Remove all items from D."""

    d_6.clear()
    print(d_6)

    """we can add key/values using square brackets as well d_4[key] = value"""

    d_7 = dict()
    d_7["name"] = "raghu"
    d_7["surname"] = "b"
    print(d_7)

    values = [4, 8, 15, 1]

    d_1 = {'fish': 0, 'dog': 1, 'cat': 2, 'wolf': 3}

    # Iterate through d_1 adding contents of list to
    # coresponding value in list

    index = 0
    for key in d_1.keys():
        d_1[key] += values[index]
        index += 1
        print(d_1.values())
















if __name__ == "__main__":
    main()