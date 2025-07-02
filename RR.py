# Round Robin (RR) Algorithm

def round_robin(processes, quantum):
    current_time = 0
    completed_processes = 0
    n = len(processes)
    queue = []
    total_waiting_time = 0
    total_turnaround_time = 0
    total_completion_time = 0
    index = 0  # To track which processes have been added to the queue

    # Initialize remaining_time for each process
    for p in processes:
        p['remaining_time'] = p['burst_time']

    while completed_processes < n:
        # Add newly arrived processes to the queue
        while index < n and processes[index]['arrival_time'] <= current_time:
            queue.append(processes[index])
            index += 1

        if queue:
            # Get the first process from the queue
            current_process = queue.pop(0)
            
            # Execute the process for the time quantum or its remaining time, whichever is smaller
            time_slice = min(quantum, current_process['remaining_time'])
            current_process['remaining_time'] -= time_slice
            current_time += time_slice

            # Print execution step
            print(f"step: {current_time}, process: {current_process['process_id']}, remaining time: {current_process['remaining_time']}")

            # If the process is completed
            if current_process['remaining_time'] == 0:
                completed_processes += 1
                current_process['completion_time'] = current_time
                current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
                current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
                total_waiting_time += current_process['waiting_time']
                total_turnaround_time += current_process['turnaround_time']
                total_completion_time += current_process['completion_time']
                print(f"Process {current_process['process_id']} completed at time {current_time}.")
            else:
                # Add any newly arrived processes before re-queueing the current process
                while index < n and processes[index]['arrival_time'] <= current_time:
                    queue.append(processes[index])
                    index += 1
                # Re-queue the current process
                queue.append(current_process)
        else:
            # If no process is ready, increment time
            current_time += 1

    # Calculate average times
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    avg_completion_time = total_completion_time / n

    return avg_waiting_time, avg_turnaround_time, avg_completion_time

print("Round Robin (RR) Scheduling Algorithm")
quantum = int(input("Enter the time quantum: "))

print("Do you want to enter the process details manually or from a text file?")
a = input("Enter 'm' for manual or 't' for text file: ")
processes = []


if a == 'm':
    # Input the number of processes
    n = int(input("Enter the number of processes: "))
   

    # Input process details manually
    for i in range(n):
        process_id = input(f"Enter process ID for process {i + 1}: ")
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append({
            'process_id': process_id,
            'arrival_time': arrival_time,
            'burst_time': burst_time,
            'remaining_time': burst_time,
            'completion_time': 0,
            'turnaround_time': 0,
            'waiting_time': 0
        })
elif a == 't':
    # Input the file name
    filename = input("Enter the file name (with .txt extension): ")
    
    # Read process details from the file
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Skip the header line if it exists
            for line in lines:
                # Skip empty lines or header
                if line.strip() and not line.strip().startswith('process_id'):
                    try:
                        process_id, arrival_time, burst_time = line.strip().split()
                        print(f"Process ID: {process_id}, Arrival Time: {arrival_time}, Burst Time: {burst_time}")
                        processes.append({
                            'process_id': process_id,
                            'arrival_time': int(arrival_time),
                            'burst_time': int(burst_time),
                            'remaining_time': int(burst_time),
                            'completion_time': 0,
                            'turnaround_time': 0,
                            'waiting_time': 0
                        })
                    except ValueError:
                        print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)

# Call the Round Robin function to calculate the scheduling details
if processes:  # Only run if processes were successfully loaded
    avg_waiting_time, avg_turnaround_time, avg_completion_time = round_robin(processes, quantum)

    # Print the process details after the Round Robin function has been executed
    print("\nProcess ID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in processes:
        print(f"{process['process_id']}\t\t{process['arrival_time']}\t\t{process['burst_time']}\t\t{process['completion_time']}\t\t{process['turnaround_time']}\t\t{process['waiting_time']}")

    # Print the average times
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Completion Time: {avg_completion_time:.2f}")
else:
    print("No processes to schedule.")