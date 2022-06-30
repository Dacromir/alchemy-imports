from classes.class_a import Class_A

class Class_C(Class_A):
    c = "c"

if __name__ == "__main__":
    test = Class_C()
    print (test.a, test.c)