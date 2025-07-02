🧮 CPU Scheduling Algorithms in Python
This project implements three fundamental CPU scheduling algorithms using Python:

FCFS: First Come First Serve (Non-preemptive)

SJF: Shortest Job First (Non-preemptive)

SRTF: Shortest Remaining Time First (Preemptive SJF)

Each algorithm allows users to enter process details manually or read them from a .txt file, and then calculates:

Completion time

Turnaround time

Waiting time

Averages for all the above

📂 File Structure
bash

cpu_scheduling/
├── FCFS.py        # First Come First Serve algorithm
├── SJF.py         # Shortest Job First (non-preemptive)
├── SRTF.py        # Shortest Remaining Time First (preemptive SJF)
├── README.md      # Project documentation
🛠 Features
Manual or file-based input support

Dynamic simulation with timestamps

Calculation of:

Completion time

Waiting time

Turnaround time

Averages

Preemptive logic for SRTF

Console logging of step-by-step execution

📥 Input Format
For manual input, each script will prompt:

bash

Enter the number of processes:
Enter process ID for process 1:
Enter arrival time for process 1:
Enter burst time for process 1:
🔠 Text File Format Example

P1 0 8
P2 1 4
P3 2 9
P4 3 5
Each line: <Process_ID> <Arrival_Time> <Burst_Time>

▶️ How to Run
Make sure you have Python 3 installed, then run:

bash
python FCFS.py
python SJF.py
python SRTF.py
You will be prompted to enter input mode:
Enter 'm' for manual or 't' for text file:
📊 Sample Output
Process ID  Arrival Time  Burst Time  Completion Time  Turnaround Time  Waiting Time
P1          0             8           8                8                0
P2          1             4           12               11               7
...
Average Waiting Time: 5.75
Average Turnaround Time: 9.25
Average Completion Time: 13.50
📚 Algorithms Explained
1. 🧾 First Come First Serve (FCFS)
Non-preemptive

Processes are scheduled in order of arrival

Fair but may lead to high waiting time

2. ⚡ Shortest Job First (SJF)
Non-preemptive

Selects the job with the shortest burst time

Efficient for batch systems

3. ⏳ Shortest Remaining Time First (SRTF)
Preemptive version of SJF

Always selects the job with the least remaining burst time

May cause starvation

🧠 Use Cases
Teaching CPU scheduling concepts

Simulating process execution behavior

Analyzing scheduling performance

Practicing Python logic and control structures

📄 License
This project is licensed under the MIT License. Free to use and modify.



