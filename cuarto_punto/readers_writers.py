import threading
import time
import random


class SharedData:
    def __init__(self):
        self.value = 0
        self.read_count = 0
        self.mutex = threading.Semaphore(1)  # Mutex para read_count
        self.wrt = threading.Semaphore(1)  # Semaphore para acceso al recurso compartido


class Reader(threading.Thread):
    def __init__(self, name, shared_data):
        threading.Thread.__init__(self)
        self.name = name
        self.shared_data = shared_data

    def run(self):
        while True:
            time.sleep(random.uniform(1, 3))  # Simula tiempo de lectura
            self.shared_data.mutex.acquire()
            self.shared_data.read_count += 1
            if self.shared_data.read_count == 1:
                self.shared_data.wrt.acquire()  # Primer lector bloquea a los escritores
            self.shared_data.mutex.release()

            print(f"{self.name} está leyendo. Valor: {self.shared_data.value}")
            time.sleep(random.uniform(1, 3))  # Simula tiempo de lectura

            self.shared_data.mutex.acquire()
            self.shared_data.read_count -= 1
            if self.shared_data.read_count == 0:
                self.shared_data.wrt.release()  # Último lector libera el bloqueo
            self.shared_data.mutex.release()


class Writer(threading.Thread):
    def __init__(self, name, shared_data):
        threading.Thread.__init__(self)
        self.name = name
        self.shared_data = shared_data

    def run(self):
        while True:
            time.sleep(random.uniform(1, 3))  # Simula tiempo de escritura
            self.shared_data.wrt.acquire()

            self.shared_data.value += 1
            print(
                f"{self.name} está escribiendo. Nuevo valor: {self.shared_data.value}"
            )
            time.sleep(random.uniform(1, 3))  # Simula tiempo de escritura

            self.shared_data.wrt.release()


def main():
    shared_data = SharedData()
    readers = [Reader(f"Lector {i+1}", shared_data) for i in range(3)]
    writers = [Writer(f"Escritor {i+1}", shared_data) for i in range(2)]

    for reader in readers:
        reader.start()
    for writer in writers:
        writer.start()

    for reader in readers:
        reader.join()
    for writer in writers:
        writer.join()


if __name__ == "__main__":
    main()
