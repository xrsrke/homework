import sys
import importer

print("Running main.py")

module1 = importer.import_('module1', 'example3b/module1_source.py', '.')

# print(module1.__dict__)

# module1.hello()

# Printing the dictionary of the module1 object.
print("sys say: ", sys.modules.get('module1', 'module1 not found'))

