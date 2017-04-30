# Code For Round Robin

#declaring variables

no_of_process=8
count=0
time=0
remain=0
flag=0
time_quantum=0
wait_time=0
turn_around_time=0
arrival_time=[None] * 8 
burst_time=[None] * 8
reamining_time=[None] * 8 
  
  #initializing burst time to every process

remain=5

#arrival times

arrival_time[0]=0
arrival_time[1]=1
arrival_time[2]=4
arrival_time[3]=5
arrival_time[4]=7
arrival_time[4]=10
arrival_time[4]=12
arrival_time[4]=14

#burst times

burst_time[0]=4
burst_time[1]=3
burst_time[2]=11
burst_time[3]=9
burst_time[4]=6
burst_time[5]=10
burst_time[6]=7
burst_time[7]=5


time_quantum= 4

#calculating waiting & turn Around  time for processes
  
print (str("process")+'     '+str("Turnaround Time")+'     '+str("Waiting Time"))

while remain!=0 :
  if reamining_time[count]<=time_quantum and reamining_time[count]>0 :
    time+=reamining_time[count]
    reamining_time[count]=0
    flag=1
    
    if reamining_time[count]>0:
      reamining_time[count]=time_quantum
      time+=time_quantum
      
      if reamining_time[count]==0 and flag==1:
        remain=remain-1
        print(str("process")+str(count+1)+'    '+str(time-arrival_time[count])+'     '+str(time-arrival_time[count]-burst_time[count]))
        wait_time+=time-arrival_time[count]-burst_time[count]
        turn_around_time=time-arrival_time[count]
        flag=0
        
        if count==no_of_process-1 :
          count=0
          
          if arrival_time[count+1]<=time :
            count=count+1
             else:
              count=0
			  
              
              
              
              
          
          
    
    
    
  

  

  
  

  