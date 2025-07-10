################################################
# Without Generics
################################################

#Example Without Generics

# def first_element(items):
#     return items[0]

# nums = [1,2,3]
# strings = ['a','b','c']

# num_result = first_element(nums)
# string_result = first_element(strings)

# print(num_result)       # output: 1
# print(string_result)    # output: a

# Issue: No type checking. We can't restrict or inform about expected data types explicitly.


################################################
# With Generics
# T = TypeVar('T')
################################################

# from typing import TypeVar

# #Type Variable for generic typing
# T = TypeVar('T')

# def generic_first_element(items: list[T])-> T:
#     return items[0]


# nums = [1,2,3]
# strings = ['a', 'b', 'c']

# num_result = generic_first_element(nums)
# string_result = generic_first_element(strings)

# print(num_result)
# print(string_result)


################################################
# Generic Classes
################################################


from typing import Generic, TypeVar, ClassVar
from dataclasses import dataclass, field

T = TypeVar('T')

@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)
    limit: ClassVar[int] = 30

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self)-> T :
        return self.items.pop()
    
stack_of_ints = Stack[int]()

print(stack_of_ints)
print(stack_of_ints.limit)
stack_of_ints.push(10)
stack_of_ints.push(20)
print(stack_of_ints)
print(stack_of_ints.pop())

stack_of_strings = Stack[str]()

print(stack_of_strings)
stack_of_strings.push("hello")
stack_of_strings.push("world")
print(stack_of_strings)

print(stack_of_strings.pop())