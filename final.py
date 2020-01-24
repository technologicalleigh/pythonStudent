###########problem A#################
class Rectangle(object):
    '''creates a class that will contain the dimensions of a rectangle
    as instance variables, then eventually calculate the area of the rectangle
    based off these dimensions'''
    def __init__(self, l=0, w=0):
        'constructor'
        self.length=l
        self.width=w
        self.calculateArea()

    def __str__(self):
        '''returning a string that relays the length, width,
        and area of the rectangle'''
        return 'Length:{}\n\
Width:{}\n\
Area:{}'.format(self.length, self.width,self.calculateArea())


    def calculateArea(self):
        'calculates the area of the rectangle'
        area=int(self.length*self.width)
        return area


    def __eq__(self, other):
        '''if two rectangles are equal to each other, returns true
        else, returns false'''
        return self.length==other.length and self.width==other.width and self.calculateArea()==other.calculateArea()


###########problem C#################
def createCountriesDict():
    '''creates a dictionary based off the document 'cities_by_continent.csv
    the keys of the dictionary are the continents, while the values in the
    dictionary are the cities
    '''

    content=open('cities_by_continent.csv','r')
    readIt=content.readlines()

    dct={}

    for line in readIt:
        items=[]
        line=line.split(',')
        key=line[0]
        line[3]=line[3].replace('\n','')
        items.append(line[1])
        items.append(line[2])
        items.append(line[3])
        dct[key]=items

    return dct
