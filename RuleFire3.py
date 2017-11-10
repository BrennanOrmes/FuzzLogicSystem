import re 
import sys
import math

#IF AND - take min value
#IF OR - take max value
#If the driving is good and the journey_time is short then the tip will be big
def main(): 
# Open data file with name given by user input
	data = parseRules()
	rList = data["ruleBaseList"]
	#rWorldValues = data["crisp"]

	rNames = []
	rValues = []

	# for j in rWorldValues:
	# 	Name = 
	# 	rName.append

	
	for y in rList:
		#if 
		splitRule = y.split(" ")
		#ruleConditions = {splitRule[2]: splitRule[4], "conjunctive": splitRule[5],  splitRule[7]: splitRule[9]}

		#if ("and" or "or") in splitRule[5]:
		ruleConditions = {splitRule[2]: splitRule[4], "conjunctive": splitRule[5],  splitRule[7]: splitRule[9], splitRule[12]: splitRule[15]}
		print(ruleConditions)
		# else:
		# 	print("This rule does not compute, it has not been added to the system")
		# 	#For some reason thinks the last rule does not compute?
		# 	break


		# for x in rList:
		# 	if splitRule[5] == "and":





def parseRules():
	data = {}
	ruleBaseList = []

	txt = input("Please input file name: ")

	with open(txt, 'r') as datafile:
		#For each line in the text file
		for line in datafile.readlines():
			#If a line starts with the string "Rule"
			if line.startswith('Rule'):
				#Use re to remove ("Rule followed by any int 0-9") on the current 
				line = re.sub("^Rule(.+)?[0-9]", "", line)
				#Remove white space
				line = line.strip()
				#Add that rule to the rule list
				ruleBaseList.append(line)

	# crispValues = crispValues.split("\n")
	# crisp = []
	# for i in range(0,len(crispValues)):
	# 	x = crispValues[i].split(" = ")
	# 	if x is not None:
	# 		crisp.append(dict({"name" : x[0], "value":x[1]}))


	data["ruleBaseList"] = ruleBaseList
	# data["crisp"] = crisp

	#print(data["ruleBaseList"])
	return data


def ruleFire():
	pass

class membershipCurves:

    name = "";

    def __init__(self, name, a, b, alpha, beta):
        self.a = int(a)
        self.b = int(b)
        self.alpha = int(alpha)
        self.beta = int(beta)
        self.name = name

    def __str__(self):
        return str(self.membership)

    def name(self):
        return self.name

    def membership(self, value):

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
