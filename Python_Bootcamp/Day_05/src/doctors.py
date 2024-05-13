from threading import Thread, RLock
from time import sleep


class Screwdriver:
    def __init__(self, index: int) -> None:
        self.index: int = index
        self.locker: RLock = RLock()

    def pick_up(self) -> None:
        sleep(0.2)
        self.locker.acquire()

    def put_down(self) -> None:
        sleep(0.2)
        self.locker.release()


class Doctor(Thread):
    def __init__(
        self, index: int, l_screwdriver: Screwdriver, r_screwdriver: Screwdriver
    ) -> None:
        super().__init__()
        self.index: int = index
        self.l_screwdriver: Screwdriver = l_screwdriver
        self.r_screwdriver: Screwdriver = r_screwdriver

    def run(self) -> None:
        if self.index % 2 == 0:
            sleep(0.2)
        first: Screwdriver
        second: Screwdriver
        first, second = sorted(
            [self.l_screwdriver, self.r_screwdriver],
            key=lambda x: x.index,
        )
        first.pick_up()
        second.pick_up()
        sleep(0.2)
        print(f"Doctor {self.index}: BLAST!")
        second.put_down()
        first.put_down()


def run_doctors_rounds(num_rounds):
    for round_num in range(num_rounds):
        print(f"Round {round_num + 1}")

        screwdrivers = [Screwdriver(i) for i in range(5)]
        doctors = [
            Doctor(
                index=i + 9,
                l_screwdriver=screwdrivers[i],
                r_screwdriver=screwdrivers[(i + 1) % 5],
            )
            for i in range(5)
        ]

        for doctor in doctors:
            doctor.start()

        for doctor in doctors:
            doctor.join()


if __name__ == "__main__":
    print("Enter number of rounds:")
    run_doctors_rounds(int(input()))
