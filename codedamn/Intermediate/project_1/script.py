
from raven import text


def last(x):
    return x[-1]



def main():
   """sdf"""
   file = text.split()
   book = {}
   for i in file:
       if i in book:
           book[i] += 1
       else:
           book[i] = 1

   print(book.items())
   sort_book = sorted(book, key=last, reverse=True)

   return sort_book[:5]




def alpha_order_7(poem):
    """alpha order string"""
    file = poem.split()

    book = {}

    for i in file:
        if i in book:
            book[i] += 1
        else:
            book[i] = 1

    def last(x):
        return x[-1]

    book = book.items()

    sort_book = sorted(book, key=last, reverse=True)

    new = []

    for i in book:
        if i[1] == 7:
            new.append(i[0])
    new = ''.join(new)
    newer = list(new)
    newer.sort()
    newest = ''.join(newer)
    return newest


"""
def math_or_dicipher(d):
    Values int or str
    new = {}
    for i in d:
        if type(d[i]) ==  str:
            s = ""
            for letter in d[i]:
                s += chr(ord(letter) + i)
            new[i] = s
        else:
            l = d[i]
            m1 = l.pop(l.index(max(l)))
            m2 = l.pop(l.index(min(l)))
            ttl = sum(l)
            new[i] = [m1,m2,ttl]
    return new"""


if __name__ == "__main__":
    print(alpha_order_7(text))