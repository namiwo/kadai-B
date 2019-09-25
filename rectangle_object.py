class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area_a = self.height * self.width
        return area_a

    def diagonal(self):
        diagonal_a = (self.height ** 2 + self.width ** 2) ** 0.5
        return diagonal_a


def main():
    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())
    print(rectangle1.diagonal())

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())
    print(rectangle2.diagonal())


if __name__ == "__main__":
    main()
