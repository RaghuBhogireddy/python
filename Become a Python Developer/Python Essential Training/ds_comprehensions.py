
class list_compre:
    def __init__(self):
        self.list = list(range(100))
        self.string = "Hello everyone. This has been coded to help with List comprehensions."

    def list_multiply(self, key):
        print([key * value for value in self.list])

    def list_filter(self, key):
        print([value for value in self.list if value % key == 0])

    def list_split(self, key=None):
        print(self.string.split(key))

    def nested_list(self):
        print([word for word in self.string.split()] for self.string in self.string.split('.'))

print("++++++++++ List Comprehension ++++++++++++++++++++")
my_list = list_compre()
my_list.list_multiply(2)
my_list.list_filter(2)
my_list.list_split('.')
my_list.nested_list()


class dict_compre:
    def __init__(self):
        self.animals = [('a', 'antelope'),('b', 'bull'),('c','cat'),('d','dog')]

    def create_dict(self):
        print({key : value for key, value in self.animals})

    def create_individual_dict(self):
        dict = {key : value for key, value in self.animals}
        print([{'letter': key, 'name': value} for key,value in dict.items()])

    def create_dict_by_initial_value(self):
        values = [[1, 'i', 'a'], ['2', 'we', 'be', 'it'], [3, 'are', 'few', 'too']]
        print({item[0]: item[1:] for item in values})

print("++++++++++ dictionary Comprehension ++++++++++++++++++++")
my_dict = dict_compre()
my_dict.create_dict()
my_dict.create_individual_dict()
my_dict.create_dict_by_initial_value()
