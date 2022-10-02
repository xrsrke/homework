import os.path
import types
import sys

module_name = 'module1'
module_file = 'module1_source.py'
module_path = 'example3a/.'

module_relative_file_path = os.path.join(module_path, module_file)
module_absolute_file_path = os.path.abspath(module_relative_file_path)

with open(module_relative_file_path, 'r') as code_file:
    source_code = code_file.read()

# create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_absolute_file_path

# set a reference in sys.modules
sys.modules[module_name] = mod

# compile the source course
code = compile(source_code, filename=module_absolute_file_path, mode='exec')

# execute compiled source code
exec(code)

# print(mod.__dict__)

mod.hello()

import module1
# module1.hello()
