class Circle():
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius

    def area(self):
        area_a = (self.radius ** 2) * self.pi
        return area_a

    def perimeter(self):
        perimeter_a = (self.radius * 2) * self.pi
        return perimeter_a


def main():
    # 半径1の円
    circle1 = Circle(radius=1)
    print(circle1.area())
    print(circle1.perimeter())
    # 半径3の円
    circle3 = Circle(radius=3)
    print(circle3.area())
    print(circle3.perimeter())


if __name__ == "__main__":
    main()
