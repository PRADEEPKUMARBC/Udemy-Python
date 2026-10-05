class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala Blend"

class C(A):
    label = "C: Herbel Blend"

class D(B, C):
    pass

cup = D()
print(cup.label())  # Output: B: Masala Blend