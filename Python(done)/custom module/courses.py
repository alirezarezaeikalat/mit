import sys, os
from my_module import find_index
courses = ['History', 'math', 'physics', 'comsci']

index = find_index(courses, 'math')
#print(index)

print(os.__file__)