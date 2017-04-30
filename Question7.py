#code for FCFS


process_queue = []
total_wating_time = 0
no_of_process = int(input('Enter the total no of processes: '))
for i in range(no_of_process):
    process_queue.append([])             #append a list object to the list
    process_queue[i].append(input('Enter process name: '))
    process_queue[i].append(int(input('Enter process arrival time: ')))
    total_wating_time += process_queue[i][1]
    process_queue[i].append(int(input('Enter process burst time: ')))
    print (' ')

process_queue.sort(key = lambda process_queue:process_queue[1])

print ('ProcessName\tArrivalTime\tBurstTime')
for i in range(no_of_process):
    print (process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2])
    
print ('Total waiting time: ',total_wating_time)
print ('Average waiting time: ',(total_wating_time/no_of_process))