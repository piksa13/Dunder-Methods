class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Changing representation of the vector, you get repr rather than object
    # In Java you will use to_str
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        print("I was called!")


v1 = Vector(10, 20)
v2 = Vector(50, 60)

# +  initialize __add__ defined in class above (equal print(v3.x, v3.y))
v3 = v1 + v2

# v3 initialize __repr__
print(v3)

# v3() initialize __call__ magic method
v3()
