class Mycounterv3():
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step
        return self.value

    def count_down(self):
        self.value -= self.step
        return self.value


def main():
    counter1 = Mycounterv3(value=1, step=2)
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_up()
    print(counter1.value)

    counter1.count_down()
    print(counter1.value)

    counter2 = Mycounterv3(value=3, step=4)
    print(counter2.value)

    counter2.count_down()
    print(counter2.value)

    counter2.count_down()
    print(counter2.value)


if __name__ == "__main__":
    main()
