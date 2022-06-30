from classes.class_a import Class_A

class Class_B(Class_A):
    b = "b"

if __name__ == "__main__":
    test = Class_B()
    print (test.a, test.b)