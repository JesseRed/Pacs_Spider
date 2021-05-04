import os
from os.path import dirname, realpath
print(dirname(realpath(__file__)))
print(os.path.join(dirname(dirname(dirname(realpath(__file__)))),"imported"))