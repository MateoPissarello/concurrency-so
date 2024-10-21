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


# Example usage with more diverse processes
processes = [
    Process(1, 10, 3),  # PID 1, burst time 10, priority 3
    Process(2, 1, 1),  # PID 2, burst time 1, priority 1
    Process(3, 7, 2),  # PID 3, burst time 7, priority 2
    Process(4, 5, 5),  # PID 4, burst time 5, priority 5
    Process(5, 3, 4),  # PID 5, burst time 3, priority 4
    Process(6, 12, 1),  # PID 6, burst time 12, priority 1
    Process(7, 4, 2),  # PID 7, burst time 4, priority 2
    Process(8, 6, 3),  # PID 8, burst time 6, priority 3
]

print("First Come First Serve (FCFS):")
fcfs(processes)  # First Come First Serve

print("\nShortest Job First (SJF):")
sjf(processes)  # Shortest Job First

print("\nPriority Scheduling:")
priority_scheduling(processes)  # Priority Scheduling

print("\nRound Robin with quantum 3:")
round_robin(processes, 3)  # Round Robin with quantum 3
