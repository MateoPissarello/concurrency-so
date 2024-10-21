import threading
import time
import random


class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            print(f"{self.name} está pensando.")
            time.sleep(random.uniform(1, 3))
            print(f"{self.name} tiene hambre.")
            self.dine()

    def dine(self):
        fork1, fork2 = self.left_fork, self.right_fork

        while True:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print(f"{self.name} cambia de tenedor.")
            fork1, fork2 = fork2, fork1
            time.sleep(random.uniform(1, 3))

        print(f"{self.name} está comiendo.")
        time.sleep(random.uniform(1, 3))
        print(f"{self.name} ha terminado de comer.")
        fork1.release()
        fork2.release()


def main():
    forks = [threading.Lock() for _ in range(5)]
    names = ["Filósofo 1", "Filósofo 2", "Filósofo 3", "Filósofo 4", "Filósofo 5"]
    philosophers = [
        Philosopher(names[i], forks[i], forks[(i + 1) % 5]) for i in range(5)
    ]

    for philosopher in philosophers:
        philosopher.start()


if __name__ == "__main__":
    main()
