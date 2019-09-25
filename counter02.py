class MyCounterv2():
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step
        return self.value


def main():
    counter1 = MyCounterv2(value=0, step=1)
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter2 = MyCounterv2(value=0, step=3)
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)


if __name__ == "__main__":
    main()
