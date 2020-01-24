#Bradleigh Kottke

#######################Problem###################################
def countCountries(country):
    infile = open('transactions.csv')
    content=infile.read()
    infile.close()

    count=0
    content=content.upper()
    country=country.upper()

    for i in content:
        count=content.count(country)

    return count


#######################Problem 2##################################

def findCapitalLetters(file):
    infile=open(file)
    content=infile.read()
    infile.close()

    lstContent=content.split()

    splitLst=[]

    capitalLetters=''

    for i in lstContent:
        i=i.split(',')
        splitLst.append(i)

    for row in range(len(splitLst)):
        for column in range(len(splitLst[row])):
            if splitLst[row][column][0].isupper():
               capitalLetters+=splitLst[row][column][0]

    return capitalLetters

#######################Problem 3###################################

def enterNames():
    import datetime
    timestamp=datetime.datetime.now()
    timestamp=str(timestamp)
    infile=open('studentNames.txt', 'w')

    while True:
        print('press <enter> when finished entering names')
        student=input('please enter student name')
        if student=='':
            infile.close()
            return
        else:
            infile.write(student+', '+timestamp+'\n')
