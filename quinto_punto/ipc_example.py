import multiprocessing
import time

def producer(shared_memory, semaphore):
    for i in range(10):
        time.sleep(1)  # Simula la producción de un recurso
        with semaphore:
            shared_memory[i] = i * 2
            print(f"Produced: {shared_memory[i]}")

def consumer(shared_memory, semaphore):
    for i in range(10):
        time.sleep(1.5)  # Simula el consumo de un recurso
        with semaphore:
            print(f"Consumed: {shared_memory[i]}")
            shared_memory[i] = -1  # Marca el recurso como consumido

def main():
    shared_memory = multiprocessing.Array('i', 10)  # Memoria compartida
    semaphore = multiprocessing.Semaphore()  # Semáforo para sincronización

    producer_process = multiprocessing.Process(target=producer, args=(shared_memory, semaphore))
    consumer_process = multiprocessing.Process(target=consumer, args=(shared_memory, semaphore))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("All processes finished.")

if __name__ == "__main__":
    main()
