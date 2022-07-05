
class list_ds:
    def __init__(self):
        self.list = ['1',"two", "3", 'four']
        
    def reutrn_list(self):
        return print(self.list)

    def append(self, param):
        self.list.append(param)
        return self.reutrn_list()

    def insert(self, pos, param):
        self.list.insert(pos, param)
        return self.reutrn_list()

    def remove(self, param):
        self.list.remove(param)
        return self.reutrn_list()

    def pop(self):
        self.list.pop()
        return self.reutrn_list()

    def slice_list(self, start = None, end = None):
        slice = self.list[start:end]
        return slice

print("+++++++++++++ Lists +++++++++++++++++")

# list is data structure more similar like an string but with ordered sequence of objects. 
# list is subscriptable -> meaning we can access an element inside a list with an index 
my_list = list_ds()
my_list.append("raghu") # add element at end
my_list.insert(1, "ramu") # add element at position, if pos, given at non existing index, it will add at end
my_list.remove("ramu") # removed specified element
my_list.pop() # always remove element at end
print(my_list.slice_list(2,3)) # can slice a list based on start and end. also can use step to skip elemets 

print("+++++++++++ Sets +++++++++++++++++++")

class set_ds:
    def __init__(self):
        self.set = {'1',"two", "3", 'four'}
        
    def reutrn_set(self):
        return print(self.set)

    def add(self, param):
        self.set.add(param)
        return self.reutrn_set()

    def discard(self, param):
        self.set.discard(param)
        return self.reutrn_set()

    def remove(self, param):
        self.set.remove(param)
        return self.reutrn_set()

# set is mostly a list but store only unique values and it is unordered.
# sets are not subscriptable
my_set = set_ds() # set is mostly a list but store only unique values 
my_set.add("raghu") # to add element
my_set.discard("raghu") # to remove an element. If element not exist it won't throw an error
my_set.remove("four") # to remove an element. If element not exist, it will throw an error

print("+++++++++++ Tuple +++++++++++++++++++")

class tuple_ds:
    def __init__(self):
        self.list = ['1',"two", "3", 'four']
        self.tuple = ('1',"two", "3", 'four',self.list)

    def return_tuple(self):
        return print(self.tuple)

    def modify(self, param):
        # can access an elements using it's index
        self.tuple[4].append(param)
        return self.return_tuple()
    
# tuple are different from list, as these are immutable.But we can modify the contents of a list inside a tuple  
my_tuple = tuple_ds()
my_tuple.return_tuple()
my_tuple.modify("raghu")

print("++++++++++ dictionary ++++++++++++++++++++")


class dict_ds:
    def __init__(self):
        self.dict = {
            '0' : 'raghu',
            '1' : 'ram',
            '2' : 'bhogireddy'
        }

    def return_dict(self, ret=None):
        if not ret:
            return print(self.dict)
        else:
            return print(f'returned : {ret} and dict is {self.dict}')

    def update(self,key, value):
        self.dict.update(key=value)
        return self.return_dict()

    def get(self,param):
        return print(self.dict.get(param))
    
    def values(self):
        return print(self.dict.values())
        

    def keys(self):
        return print(self.dict.keys())

    def pop(self, param):
        ret = self.dict.pop(param)
        return self.return_dict(ret)

    def pop_item(self):
        ret = self.dict.popitem()
        return self.return_dict(ret)

    def items(self):
        return print(self.dict.items())


# dictornary is a ds which conists of key value pairs.
my_dict = dict_ds()
my_dict.update(2,'b') # can update a key value pair by using as mentioned in method
my_dict.get('key') # can get value by passing key
my_dict.values() # can get values
my_dict.keys() # can get keys
my_dict.pop('key') # can pop a value by passing key and value get back
my_dict.pop_item() # can pop a key value pair and return it in tuple
my_dict.items() # can get dict items 

