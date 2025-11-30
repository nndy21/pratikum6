import math # [cite: 376]

# def a(x): return x**2
a_lambda = lambda x: x**2 # [cite: 377, 378]

# def b(x,y): return math.sqrt(x**2+y**2)
b_lambda = lambda x, y: math.sqrt(x**2 + y**2) # [cite: 379, 380]

# def c(*args): return sum(args)/len(args)
c_lambda = lambda *args: sum(args) / len(args) # [cite: 381, 382]

# def d(s): return "".join(set(s))
d_lambda = lambda s: "".join(set(s)) # [cite: 384, 385]

# Test the functions
print("a_lambda(5):", a_lambda(5))
print("b_lambda(3, 4):", b_lambda(3, 4))
print("c_lambda(1, 2, 3):", c_lambda(1, 2, 3))
print("d_lambda('Mississippi'):", d_lambda('Mississippi'))