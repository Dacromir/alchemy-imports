from classes.class_b import Class_B
from classes.class_c import Class_C

def print_attributes():
    b = Class_B()
    c = Class_C()
    print("Class B attributes: ", b.a, b.b)
    print("Class C attributes: ", c.a, c.c)

if __name__ == "__main__":
    print_attributes()