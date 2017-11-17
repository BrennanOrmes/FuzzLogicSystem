import sys
import re

def main():

    txt = input("Please input a file name (include extensions): ")

    data = dictionaryInit(txt)

    print(data['ruleBaseName']) 
    print(data['curves'])
    print(data['crisp'])
    print(data['rules']) 

def dictionaryInit(txt):
    data = (txt.replace("\n",""))
    ruleBaseList = []

    read_in = open(txt, "r")
    read_in = (re.split(r'\n\n',read_in.read()))

    memberClasses = {}
    #ruleBaseList = read_in[1]
    crispValues = read_in[len(read_in)-1]

    # Open data file with name given by user input
    with open(txt, 'r') as datafile:
        #For each line in the txt file
        for line in datafile.readlines():
            #If a  line starts with the string Rule
            if line.startswith('Rule'):
                #Use regular expression to remove ("Rule followed by any int 0-9") on the current line
                line = re.sub("^Rule(.+)?[0-9]", "", line)
                #Remove white space
                line = line.strip()
                #Add that rule to the list Rules
                ruleBaseList.append(line)
            #If a line containing Rule base as part of a word is detected
            if ("Rulebase" or "rulebase") in line:
                ruleBaseName = line


    #Initiate Dictionary
    data = {}

    for i in range(2, len(read_in)-1, 2):

        memberShips = []
        groups = read_in[i+1].split("\n")

        for z in range(0,len(groups)):
            x = groups[z].split(" ")
            #print(x)

            #0 = Name, 1 = a, 2 = b, 3 = alpha, 4 = beta
            y = {x[0],x[1],x[2],x[3],x[4]}


            memberShips.append(y)

        memberClasses[read_in[i].strip()] = memberShips
        #print(memberClasses)
        
   
    crispValues = crispValues.split("\n")
    crisp = []
    for i in range(0,len(crispValues)):
        x = crispValues[i].split(" = ")
        if x is not None:
            crisp.append(dict({"name" : x[0], "value":x[1]}))



    data['ruleBaseName'] = ruleBaseName
    data['curves'] = memberClasses
    data['crisp'] = crisp
    data['rules'] = ruleBaseList
    
    return data

if __name__ == '__main__':
    main()