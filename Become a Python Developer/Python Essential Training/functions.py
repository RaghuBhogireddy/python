
import math

class function:
    def __init__(self) -> None:
        pass
    def operation(self,*args):
        print(sum(args))

    def operation_kwargs(self, *args):
        print(sum(args))

    ''' *args are used for passing multiple positional arguments
        **kwargs are used for passing multiple keyword arguments'''


fun = function()
fun.operation(2,3,45,123,23434)
#fun.operation_kwargs(name='raghu', initial='B')

fun_list = [fun.operation, fun.operation_kwargs]

for item in fun_list:
    item(23,234,45,2343)

print("=== Lambda functions ===")
print((lambda x: x+3)(5))

my_list = [{'num':3}, {'num':2}, {'num':1}]
print(sorted(my_list, key=lambda x:x['num']))