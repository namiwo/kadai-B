class Mycounterv1():
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value = self.value + 1
        return self.value


def main():
    counter1 = Mycounterv1(value=0)
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter2 = Mycounterv1(value=7)
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)


if __name__ == "__main__":
    main()
