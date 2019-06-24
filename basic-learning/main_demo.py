print("before import")
import math

print("before functionA")
def functionA():
    print("FunctionA")

print("before functionB")
def functionB():
    print("FunctionB {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == "__main__":
    functionA()
    functionB()
print("after __name__ guard")

