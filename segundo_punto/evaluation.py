import time
import matplotlib.pyplot as plt
from scheduler import Process, fcfs, sjf, priority_scheduling, round_robin


def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


def evaluate_algorithms(processes):
    algorithms = {
        "FCFS": fcfs,
        "SJF": sjf,
        "Priority Scheduling": priority_scheduling,
        "Round Robin": lambda x: round_robin(x, 2),
    }

    results = {}
    for name, algorithm in algorithms.items():
        duration = measure_time(algorithm, processes)
        print(f"La duracion de {name} es: {duration}")
        results[name] = duration
        print(f"{name} took {duration:.4f} seconds")

    return results


def plot_results(results):
    names = list(results.keys())
    values = list(results.values())
    colors = ["blue", "green", "red", "purple"]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(names, values, color=colors)
    plt.xlabel("Scheduling Algorithm")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance of Scheduling Algorithms")

    # Añadir etiquetas a las barras
    for bar, value, color in zip(bars, values, colors):
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 0.01,
            f"{value:.4f} sec",
            ha="center",
            va="bottom",
            color=color,
            fontweight="bold",
        )

    plt.show()


# Example usage
processes = [
    Process(1, 10, 3),  # PID 1, burst time 10, priority 3
    Process(2, 1, 1),  # PID 2, burst time 1, priority 1
    Process(3, 7, 2),  # PID 3, burst time 7, priority 2
    Process(4, 5, 5),  # PID 4, burst time 5, priority 5
    Process(5, 3, 4),  # PID 5, burst time 3, priority 4
    Process(6, 12, 1),  # PID 6, burst time 12, priority 1
    Process(7, 4, 2),  # PID 7, burst time 4, priority 2
    Process(8, 6, 3),  # PID 8, burst time 6, priority 3
    Process(9, 9, 2),  # PID 9, burst time 9, priority 2
    Process(10, 2, 4),  # PID 10, burst time 2, priority 4
    Process(11, 8, 3),  # PID 11, burst time 8, priority 3
    Process(12, 11, 1),  # PID 12, burst time 11, priority 1
    Process(13, 3, 2),  # PID 13, burst time 3, priority 2
    Process(14, 7, 4),  # PID 14, burst time 7, priority 4
    Process(15, 5, 5),  # PID 15, burst time 5, priority 5
    Process(16, 10, 3),  # PID 16, burst time 10, priority 3
    Process(17, 4, 1),  # PID 17, burst time 4, priority 1
    Process(18, 6, 2),  # PID 18, burst time 6, priority 2
    Process(19, 2, 4),  # PID 19, burst time 2, priority 4
    Process(20, 9, 3),  # PID 20, burst time 9, priority 3
    Process(21, 5, 2),  # PID 21, burst time 5, priority 2
    Process(22, 7, 5),  # PID 22, burst time 7, priority 5
    Process(23, 3, 1),  # PID 23, burst time 3, priority 1
    Process(24, 8, 3),  # PID 24, burst time 8, priority 3
    Process(25, 6, 4),  # PID 25, burst time 6, priority 4
    Process(26, 1, 5),  # PID 26, burst time 1, priority 5
    Process(27, 12, 2),  # PID 27, burst time 12, priority 2
    Process(28, 4, 4),  # PID 28, burst time 4, priority 4
    Process(29, 3, 3),  # PID 29, burst time 3, priority 3
]

results = evaluate_algorithms(processes)
plot_results(results)
