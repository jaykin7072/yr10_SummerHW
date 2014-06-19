def gettimestable():
    moveon=False #defining a variable for later use
    while moveon==False: #It will keep asking until correct
        times=int(input("What number would you like to see the times table for? > ")) #grab the number
        if times<101: #something reasonable
            moveon=True #allow it to continue
    return times #return outside of function

def dotimestable(times):
    moveon=False
    while moveon==False:
        howmanytimes=int(input("How many times of that number would you like to see? > ")) #self-explanatory
        if howmanytimes<21: #something reasonable
            moveon=True
    for x in range(howmanytimes): #Do it as many times as specified
        print("{0} x {1} = {2}".format((x+1),times,(x+1)*times)) #print in the format 1 x 2 = 2

def main():
    repeat=True
    while repeat==True:
        times=gettimestable() #gettimestable's return is stored in times
        dotimestable(times) #doesn't return anything, no need for storage
        dorepeat=str(input("Would you like to do it again? (y/n) > ").upper())
        if dorepeat=="Y":
            continue #actually does nothing
        else:
            repeat=False #if you enter anything other than a Y, you quit.
    
main() #Just call the main program so you don't have to manually.
