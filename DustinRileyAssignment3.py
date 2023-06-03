# INF360 - Programming in Python
# Dustin Riley
# Assignment 3

# import pprint #not sure if pprint is allowed
# (5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above.
v1 = {'Name':"Ka", 'Year Introduced':"1996", 'Production of the Current Model':"2014", 'Generation':"3rd", 'Vehicle Information':"Developed by Ford Brazil as a super mini car"}
v2 = {'Name':"Fiesta", 'Year Introduced':"1976", 'Production of the Current Model':"2017", 'Generation':"7th", 'Vehicle Information':"Ford's long running subcompact line based on global B-car Platform"}
v3 = {'Name':"Focus", 'Year Introduced':"1998", 'Production of the Current Model':"2018", 'Generation':"3rd", 'Vehicle Information':"Ford's Compact car based on global C-car platform"}
v4 = {'Name':"Mondeo", 'Year Introduced':"1992", 'Production of the Current Model':"2012", 'Generation':"2nd", 'Vehicle Information':"Mid sized passenger sedan with \"One-Ford\" design based on CD4 platform"}
v5 = {'Name':"Fusion", 'Year Introduced':"2005", 'Production of the Current Model':"2014", 'Generation':"5th", 'Vehicle Information':"Similar to Mondero"}
v6 = {'Name':"Taurus", 'Year Introduced':"1986", 'Production of the Current Model':"2009", 'Generation':"6th", 'Vehicle Information':"Full sized car based on D3 platform"}
v7 = {'Name':"Fiesta ST", 'Year Introduced':"2013", 'Production of the Current Model':"2013", 'Generation':"1st", 'Vehicle Information':"Fiesta's high performance factory tune"}
v8 = {'Name':"Focus RS", 'Year Introduced':"2015", 'Production of the Current Model':"2015", 'Generation':"1st", 'Vehicle Information':"Special high performance Focus developed by SVT"}
v9 = {'Name':"Mustang", 'Year Introduced':"1964", 'Production of the Current Model':"2014", 'Generation':"6th", 'Vehicle Information':"Ford's long running pony/muscle car"}
v10 = {'Name':"GT", 'Year Introduced':"2004", 'Production of the Current Model':"2016", 'Generation':"2nd", 'Vehicle Information':"Ford's limited production super car inspired by the legendary race car GT40"}

def createDict(dictList):               # (5/5 points) Write a function that will take a list of these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
    newDict = {}
    for i in range(len(dictList)):      # new dictionaries key = the name key's value from list item i
        newDict[dictList[i].get('Name')] = dictList[i]
    return newDict

def sortList(newDict):                  # (5/5 points) Write a function that will go through the newly created dictionary and return a list of all the car's names, sorted alphabetically.
    newList = list(newDict.keys())      # creates a list out of the dictionary's keys
    newList.sort()                      # sorts the list
    return newList


def nameAndYear(newDict):               # (5/5 points) Write a function that will go through the newly created dictionary return a dictionary of all the cars names and year introduced.
    nameAndYearDict = {}
    for k, v in newDict.items():
        nameAndYearDict[k] = {v['Year Introduced']} #v is a dictionary the ['Year Introduced'] key gets the value from inside the dictionary
    return nameAndYearDict

dictList = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10] # assigning the dictionaries into the list
newDict = createDict(dictList)
sortedList = sortList(newDict)
nameAndYearDict = nameAndYear(newDict)

for i in range(len(sortedList)):
    print(sortedList[i])                # (5/5 points) Use a print statement to show the results of the function from step 3, each on their own line.

tempDict = {}
for k, v in nameAndYearDict.items():    # filling new dictionary with nameAndYearDict year:name
    tempDict[str(v)] = {k}
# pprint.pprint(tempDict)   # not sure if pprint is allowed
temp = sorted(tempDict.items())         # sorted sorts by key (which is why i made a new year:name dictionary)
for k, v in temp:                           # [2:-2] gets rid of {''}
    print(k[2:-2] + " : " + str(v)[2:-2])   # (5/5 points) Use a print statement to show the results of the function from step 4 to display in the format: year : name. Sort by year introduced.

#getting .sort() and sorted() to work correctly was a pain
#they both work diffrently
#.sort() works on lists and modifies the list itself also cannot do (return list.sort())
#sorted() sorts dictionaries by their keys but does not modify the dictionary itself gotta save the result to a variable
