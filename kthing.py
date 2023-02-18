import random
import math
def read_file():
    fileName = "kmeans 2 input1.txt" # find k size
    print(fileName)
    
    for i in fileName.split():
        if i.isdigit():
            k = i
            print(k)
    print(k)
    count = 0;
    with open("C:/Users/djfox/OneDrive/kmeans 2 input1.txt") as f_n:# read in int
        line = [line.strip().split() for line in f_n]
    for i in line:
        kgroup =random.randrange(1,int(k)+1)
        line[count].insert(2,kgroup) 
        count = count + 1   
    
    cluster = [[0 for x in range(3)] for y in range(int(k))] # array for cluster centroid
    
    for i in range(int(k)): # loop to find intial x and y for cluster centroid
        for j in range(2):
          clust= random.randrange(0,1000)
          cluster[i][j] = clust
    print(cluster)
    mean = 0
    
    
    for i in range(count-1):
        newMin = 1000;
        for j in range(int(k)):
            x2 = cluster[j][0] # x axis for cluster centroid
            x1 = line[i][0] # x axis for data
            y2 = cluster[j][1] # y axis for cluster centroid
            y1 = line[i][1] # y axis for cluster centroid
            
            cluster[int(j)][2] = math.sqrt(pow((x2 - int(x1)),2) + pow((y2 - int(y1)),2)) #Euclidean Distance Formula
            
            min = cluster[int(j)][2]
            print ("min total " + str(min)) 
            if(min < newMin ): # for loop to put small value into right cluster
                newMin = min
                line[i][2] = j + 1
    
    for i in range(int(k)): # loop to find to reset for cluster centroid
        for j in range(3):
          cluster[i][j] = 0
    print(cluster)
    temp = int(k)
    while temp !=0:
        for i in range(count):
        
            print(i)
            if(line[i][2] == temp ):
                print(temp)
                cluster[temp-1][0] = int(line[i][0]) + cluster[temp-1][0] 
                cluster[temp-1][1] = int(line[i][1]) + cluster[temp-1][1] 
                cluster[temp-1][2] = 1 + cluster[temp-1][2] 
        temp = temp - 1
    print (cluster)
    for i in range(int(k)): # loop to find to reset for cluster centroid
        for j in range(3):
          cluster[i][j] = cluster[i][j] / cluster[i][2] 
        
    print (cluster)        
    print(line)
                
            
   
                
    
read_file()