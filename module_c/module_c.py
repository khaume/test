import test.module_a as module_a
from .utils import SOME_STR, VAR_1

print('in module_c')

module_a.my_fun(1, VAR_1)

print('just executed module_a')
print('string is: ', SOME_STR)

