import re
import math

def main():
    print("Please input a file name ( for example data.txt)")
    txt = input(">: ")
    data = dictionaryInit(txt)

    rName = data["ruleBaseName"]
    rList = data["rules"]
    rWorldValues = data["crisp"]
    mCurves = data["curves"]

    print("Here is our rules:")
    for x in rList:
        print(x)
    print("Here is our crisp values:")
    for x in rWorldValues:
        print(x)

    fuzzyWorldValues = fuzzifyValues(rWorldValues, mCurves)

    print("Here is our curves:")
    for k, v in mCurves.items():
        print(k)

    answer = ruleProcess(rList, fuzzyWorldValues, mCurves)
    
    print("\nAnd the answer is " + str(answer))


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
        #print(groups)
        for z in range(0,len(groups)):
            x = groups[z].split(" ")
            #print(groups)
            #0 = Name, 1 = a, 2 = b, 3 = alpha, 4 = beta
            #Enter in tuple
            y = membershipCurves(x[0],x[1],x[2],x[3],x[4])
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

    ### DEBUG ###
    # print(data['ruleBaseName'])
    # print("Curves")
    # for x in data['curves']:
    #     print(x)

    # print("RealWorld values")
    # for x in data['crisp']:
    #     print(x)
    # print("Rules:")
    
    # for x in data['rules']:
    #     print(x)
    ### DEBUG END ###

    return data

def fuzzifyValues(rWorldValues, mCurves):

    allMemberGroups = {}

    for i in range(0,len(rWorldValues)):
        rName = rWorldValues[i]["name"]
        rValue = rWorldValues[i]["value"]

        memberGroup = {}

        for x in range(0, len(mCurves.get(rName))):
            #print(rName)
            memberGroup[mCurves.get(rName)[x].name] = str(mCurves.get(rName)[x].fuzz(rValue))

        allMemberGroups[rName] = memberGroup

    return allMemberGroups

#Defuzzifcation
def ruleProcess(rList, fuzzyWorldValues, mCurves):  
    potentialValueList = []
    andValueList = []
    orValueList = []
    curvesToCheck = []

    #print(fuzzyWorldValues)
    print("Parsed Rules: ")
    for y in rList:
        #print(y)
        splitRule = y.split(" ")
        ruleConditions = {splitRule[2]: splitRule[4], "conjunctive": splitRule[5], splitRule[7]: splitRule[9], splitRule[12]: splitRule[15]}
        
        print(ruleConditions)

        
        if splitRule[5] == "and":
            #print("and")
            for k, v in fuzzyWorldValues.items():
                #print(k)
                if k == splitRule[2]:
                    for key, value in v.items():
                        if key == splitRule[4]:
                            if float(value) > 0:
                                #print(value)
                                andValueList.append(value)
                                curvesToCheck.append(splitRule[15])
                            else:
                                #print("I have passed")
                                pass
                elif k == splitRule[7]:
                    for key, value in v.items():
                        if key == splitRule[9]:
                            if float(value) > 0:
                                #print(value)
                                andValueList.append(value)
                                curvesToCheck.append(splitRule[15])
                            else: 
                                #print("I have passed")
                                pass
                
        elif splitRule[5] == "or":
            #print("or")
            for k, v in fuzzyWorldValues.items():
                if k == splitRule[2]:
                    for key, value in v.items():
                        if key == splitRule[4]:
                            if float(value) > 0:
                                #print(value)
                                orValueList.append(value)
                                curvesToCheck.append(splitRule[15])
                            else:
                                #print("I have passed")
                                pass
                elif k == splitRule[7]:
                    for key, value in v.items():
                        if key == splitRule[9]:
                            if float(value) > 0:
                                #print(value)
                                orValueList.append(value)
                                curvesToCheck.append(splitRule[15])
                            else:
                                #print("I have passed")
                                pass

        
        outputK = splitRule[12]

    orValue = max(orValueList)
    potentialValueList.append(orValue)
    andValue = min(andValueList)
    potentialValueList.append(andValue)

    offset = 0
    for x in range(len(mCurves[outputK])):
        c = mCurves[outputK][x]
        newOffset = (c.a - c.alpha)
        if (offset > newOffset):
            offset = newOffset

    top = []
    bottom = []

    dValues = {}
    centres = {}
    for x in range(len(mCurves[outputK])):
        #print(mCurves[outputK][x].name)
        if (mCurves[outputK][x].name in curvesToCheck):
            #COA, need to make it work with 4 tuple
            curve = mCurves[outputK][x]
            base = abs((curve.b + curve.beta) - (curve.a - curve.alpha))
            total = 0.5 * base * float(potentialValueList[x-1])

            centre = (curve.a - curve.alpha) + base / 2 + offset
            top.append(centre * total)
            bottom.append(total)

            dValues[curve.name] = total
            centres[curve.name] = centre

    answer = sum(top) / sum(bottom)
    return answer

class membershipCurves:

    name = ""

    def __init__(self, name, a, b, alpha, beta):
        self.name = name
        self.a = int(a)
        self.b = int(b)
        self.alpha = int(alpha)
        self.beta = int(beta)

    def getName():
        return self.name

    def fuzz(self, value):

        value = int(value)

        if (value < (self.a - self.alpha)):
            return 0
        elif (value in range (self.a - self.alpha, self.a)):
            return (value - self.a + self.alpha) / self.alpha
        elif (value in range(self.a, self.b)):
            return 1
        elif (value in range(self.b, self.b + self.beta)):
            return (self.b + self.beta - value) / self.beta
        elif (value > (self.b + self.beta)):
            return 0

        return

if __name__ == '__main__':
    main()