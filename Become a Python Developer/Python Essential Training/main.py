from unicodedata import name
from termcolor import colored 

# print colored text using termcolor package
text = colored("Hello World", "red" )
print(text)

#Lists
#print(dir(list))
animals = ['dog', 'cat', 'ox', 'lion']
print(animals)

#Sets
#print(dir(set))
animal_set = {1,1}
print(f'length of animal_set : {len(animal_set)}')

#Tuples
#print(dir(tuple))
animal_tuple = (animals)
print(animal_tuple)

#Dictonaries
print(dir(dict))
animals_dict = {'dog': 'animal', 'cat': 'animal', 'parrot':'bird'}
print(animals_dict)

#class
class Dog:
    def __init__(self,name):
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(f'{self.name} says: bark!')

my_dog = Dog('Rover')
dog = Dog('fluffy')

my_dog.speak()
dog.speak()