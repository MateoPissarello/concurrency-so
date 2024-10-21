import heapq

class Process:
    def __init__(self, pid, burst_time, priority=0):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority

def fcfs(processes):
    processes.sort(key=lambda x: x.pid)
    current_time = 0
    for process in processes:
        current_time += process.burst_time
        print(f"Process {process.pid} finished at {current_time}")

def sjf(processes):
    processes.sort(key=lambda x: x.burst_time)
    current_time = 0
    for process in processes:
        current_time += process.burst_time
        print(f"Process {process.pid} finished at {current_time}")

def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority)
    current_time = 0
    for process in processes:
        current_time += process.burst_time
        print(f"Process {process.pid} finished at {current_time}")

def round_robin(processes, quantum):
    current_time = 0
    queue = processes[:]
    while queue:
        process = queue.pop(0)
        if process.burst_time > quantum:
            process.burst_time -= quantum
            current_time += quantum
            queue.append(process)
        else:
            current_time += process.burst_time
            process.burst_time = 0
            print(f"Process {process.pid} finished at {current_time}")

# Example usage
processes = [Process(1, 5), Process(2, 3), Process(3, 8), Process(4, 6)]
fcfs(processes)           # First Come First Serve
sjf(processes)            # Shortest Job First
priority_scheduling(processes)  # Priority Scheduling
round_robin(processes, 2) # Round Robin with quantum 2
