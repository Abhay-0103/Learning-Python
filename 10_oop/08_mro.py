class A:
    lable = "A : Base Class"

class B(A):
    lable = "B : Ek Mera"

class C(A):
    lable = "C : Ek Tera"

class D(B, C):
    pass

cup = D()
print(cup.lable)