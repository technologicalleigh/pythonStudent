class Song(object):
    '''requires the instance variables title, singer, and yearReleased
    '''

    def __init__(self, theTitle='unknown', theSinger='unknown', theYearReleased=-1):
        self.title=theTitle
        self.singer=theSinger
        self.yearReleased=theYearReleased



    def __str__(self):

        s='Song Title:\t{}\n\
Singer:\t{}\n\
Year Released:\t{}\n'.format(self.title,self.singer,self.yearReleased)
        return s

    def __eq__(self, other):
        if(self.title==other.title):
            if(self.singer==other.singer):
                if(self.yearReleased==other.yearReleased):
                    return True




############Problem 2#################################################

class Employee(object):

    def __init__(self, employeeName='uknown', idNum=-1, y=-1, employeeSalary=30000, isSenior='uknown'):
        self.name=employeeName
        self.idNum=idNum
        self.yearHired=y
        self.salary=employeeSalary
        self.isSenior=isSenior
        if self.yearHired<=2005:
            self.isSenior='{} is a senior!'.format(self.name)
        else:
            self.isSenior='{} is not a senior!'.format(self.name)





    companyName='BradsWorld'
    number_of_emplyees=0

    def __str__(self):

        s='Employee Name:\t{}\n\
Employee ID:\t{}\n\
Employee Hire Date:\t{}\n\
Salary:\t{}\n\
{}\n'.format(self.name,self.idNum,self.yearHired,self.salary,self.isSenior)
        return s

    def addBonus(self, bonus=8):
        self.salary=self.salary+(self.salary*(bonus/100))

    def __eq__(self, other):
        if(self.name==other.name):
            if(self.idNum==other.idNum):
                if(self.yearHired==other.yearHired):
                    if(self.salary==other.salary):
                        if(self.isSenior==other.isSenior):
                            return True
