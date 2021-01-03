#this program produces the file which is used to populate the grid initially
import random
import re

def playboy(N) :
    iterations = N * N
    fhandle = open('data.txt', 'w')
    grid_length = N * N
    fhandle.write('LENGTH: ' + str(N) + '\n')
    for i in range(0, iterations) :
        number = random.randint(0, grid_length)
        fhandle.write(str(number) + '\n')
    fhandle.close()
    
def user() :
    file_name = input("Enter the file name pls: ")
    fhandle1 = open(file_name, 'r')
    fhandle2 = open('data.txt', 'w')
    for line in fhandle1:
        fhandle2.write(line)
        llist = re.findall('^LENGTH: (\S+)', line)
        if len(llist) > 0 :
            N = int(llist[0])
        grid_length = N * N
    fhandle1.close()
    fhandle2.close()
    return N