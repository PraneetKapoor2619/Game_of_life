#max grid size is chosen to be 50 x 50
import os
from populator import *
import re
import time

#producer function
def producer(GRID, N) :
    #initialize an empty list which will be returned
    xerox = list()
    
    #initialize a position counter
    i = 0
    
    #main generation producer loop
    for cell in GRID :
        #sigma: a variable which is incremented by one if the cell adjacent to the current cell is alive
        sigma = 0
        
        #>>1. check i - N<<
        #check if the ith cell is at upper boundary, i.e., i - N < 0
        if (i - N) > 0 :
            if GRID[i - N] == 'o' :
                sigma = sigma + 1
                
        #>>2. check i - 1<<
        #check if the ith cell is at the left margin of the grid, i.e., i % N == 0
        if (i % N) != 0 : 
            if GRID[i - 1] == 'o' :
                sigma = sigma + 1
        
        #>>3. check i + 1<<
        #check if the ith cell is at the right margin of the grid, i.e., (i + 1) % N == 0
        if ((i + 1) % N) != 0 :
            if GRID[i + 1] == 'o' : 
                sigma = sigma + 1
        
        #>>4. check i + N<<
        #check if the ith cell is at the lower boundary, i.e., i + N > N * N
        if (i + N) < (N * N) :
            if GRID[i + N] == 'o' :
                sigma = sigma + 1

        #>>1. Any live cell with two or three live neighbours survives<<
        #sigma should either be equal to 2 or be equal to 3
        if (GRID[i] == 'o') and ((sigma == 2) or (sigma == 3)) :
            xerox.insert(i, 'o')
            
        #>>2. Any dead cell with 3 live neighbours becomes a live cell<<
        #GRID cell dead and sigma == 3
        elif (GRID[i] == ' ') and (sigma == 3) :
            xerox.insert(i, 'o')
        
        #>>3. All other cells die in the next generation
        #else dead
        else :
            xerox.insert(i, ' ')
        
        #increment index counter
        i = i + 1
    
    #return xerox
    return xerox
    
#grid_print function
def grid_print(GRID, N, gen) :
    count = 0
    for cell in GRID :
        if ((count + 1) % N) != 0 :
            print(cell, end = '')
        else :
            print(cell)
        count = count + 1
    print("Generation:", gen)

#main body
#choice of file
command = input("Do you wish to upload some other data file?(Y/N)")
if (command == 'y') or (command == 'Y') :
    file_name = input("Enter the file name pls: ")
    fhandle1 = open(file_name)
    fhandle2 = open('data.txt', 'w')
    for line in fhandle1:
        fhandle2.write(line, '\n')
    fhandle1.close()
    fhandle2.close()
else :
    #set up grid length 
    N = int(input('Enter the grid size: ')
    grid_length = N * N
    playboy(grid_length, N)

os.system('CLS')
#opening the file and extracting postions for initial living cells
fhandle = open('data.txt', 'r')
string = fhandle.read()
initial_life = re.findall('(\S+)', string)
fhandle.close()

#setting up STATE1 and STATE2 lists
STATE1 = list()
STATE2 = list()

#putting up initial data in STATE1
flag = False
for i in range(0, grid_length) :
    for j in initial_life :
        if int(j) == i :
            flag = True
            break
    if flag == True :
        STATE1.insert(i, 'o')
        flag = False
    else :
        STATE1.insert(i, ' ')

#print initial state of the grid
grid_print(STATE1, N, 1)
time.sleep(1)

#the main loop. I call it the life-cycle
flag = False
gen = 2
while True :
    os.system('CLS')
    if flag == False :
        STATE2 = producer(STATE1, N)
        grid_print(STATE2, N, gen)
    elif flag == True :
        STATE1 = producer(STATE2, N)
        grid_print(STATE1, N, gen)
    #time.sleep(1)
    flag = not(flag)
    gen = gen + 1