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
        "Round Robin": lambda x: round_robin(x, 2)
    }

    results = {}
    for name, algorithm in algorithms.items():
        duration = measure_time(algorithm, processes)
        results[name] = duration
        print(f"{name} took {duration:.4f} seconds")
    
    return results

def plot_results(results):
    names = list(results.keys())
    values = list(results.values())
    colors = ['blue', 'green', 'red', 'purple']
    
    plt.figure(figsize=(10, 5))
    bars = plt.bar(names, values, color=colors)
    plt.xlabel('Scheduling Algorithm')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance of Scheduling Algorithms')

    # Añadir etiquetas a las barras
    for bar, value, color in zip(bars, values, colors):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{value:.4f} sec', ha='center', va='bottom', color=color, fontweight='bold')

    plt.show()

# Example usage
processes = [Process(1, 5), Process(2, 3), Process(3, 8), Process(4, 6)]
results = evaluate_algorithms(processes)
plot_results(results)
