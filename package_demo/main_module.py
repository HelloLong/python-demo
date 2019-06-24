import sub_module
from package_module1 import package1_sub1
from directory_module1 import directory_submodule1
from package_module1 import package1_driver

print(sub_module.name)
print(package1_sub1.name)
print(directory_submodule1.name)
package1_driver.say()