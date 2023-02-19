import random
import math
import numpy

def read_file():
    fileName = "kmeans 4 input3.txt" # find k size
    
    for i in fileName.split():
        if i.isdigit():
            k = i
            
    count = 0;
    with open("C:/Users/djfox/OneDrive/Desktop/assignment/kmeans 4 input4.txt") as f_n:# read in int
        line = [line.strip().split() for line in f_n]
    for i in line:
        kgroup =random.randrange(1,int(k)+1)
        line[count].insert(2,kgroup) 
        count = count + 1   
    
    cluster = [[0 for x in range(3)] for y in range(int(k))] # array for cluster centroid
    
    for i in range(int(k)): # loop to find intial x and y for cluster centroid
        clust= random.randrange(0,count)
        cluster[i][0] = int(line[clust][0])
        cluster[i][1] = int(line[clust][1])
    print("oringanl cluster point")
    print(cluster)
    mean = 0
    
    checker = [[0 for x in range(3)] for y in range(int(k))]
    for i in range(int(k)): # loop to find intial x and y for cluster centroid
        for j in range(2):
          
          checker[i][j] = 0

    t = 0
    while(t != int(k)):
        t = 0
        for i in range(int(k)): # loop to find intial x and y for cluster centroid
            for j in range(2):
          
              checker[i][j] = cluster[i][j]
    
        
        for i in range(count):
            newMin = 1000;
            for j in range(int(k)):
                x2 = cluster[j][0] # x axis for cluster centroid
                x1 = line[i][0] # x axis for data
                y2 = cluster[j][1] # y axis for cluster centroid
                y1 = line[i][1] # y axis for cluster centroid
                
                cluster[int(j)][2] = math.sqrt(pow((x2 - int(x1)),2) + pow((y2 - int(y1)),2)) #Euclidean Distance Formula
                
                min = cluster[int(j)][2]
 
                if(min < newMin ): # for loop to put small value into right cluster
                    newMin = min
                    line[i][2] = j + 1
        
        for i in range(int(k)): # loop to find to reset for cluster centroid
            for j in range(3):
                cluster[i][j] = 0
        temp = int(k) 
        while temp !=0:
            for i in range(count):
               
        
                if(line[i][2] == temp ):
                    cluster[temp-1][0] = int(line[i][0]) + cluster[temp-1][0] 
                    cluster[temp-1][1] = int(line[i][1]) + cluster[temp-1][1] 
                    cluster[temp-1][2] = 1 + cluster[temp-1][2] 
                    
            
            temp = temp - 1
            
        for i in range(int(k)): # loop to find to reset for cluster centroid
            for j in range(2):
                if(cluster[i][2] != 0):
                    cluster[i][j] = cluster[i][j] / cluster[i][2]
                else:
                    cluster[i][j] = cluster[i][j] / 1   
        
        
        for i in range(int(k)): # loop to find to reset for cluster centroid
                if(cluster[i][0] == checker[i][0] and cluster[i][1] == checker[i][1]):
                    t = t + 1
    nextLine = 0              
    outputFile = open("C:/Users/djfox\OneDrive/kmeans 2 output1.txt","w")                
    for r in line:
        for c in r:
            outputFile.write(str(c) + " ")
            nextLine = nextLine + 1
            if(nextLine == 3):
                nextLine = 0
                outputFile.write("\n")
                
        print()         
        
                    
                    
          
    
read_file()