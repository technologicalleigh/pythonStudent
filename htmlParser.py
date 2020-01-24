from html.parser import HTMLParser
from urllib.request import urlopen



def searchPage(url,searchTerm):
        '''searches the web page for a word, then counts how many times
        this word appears on the page'''

        searchTerm=searchTerm.lower()
        content=urlopen(url).read().decode('Latin_1')
        parser = myHTMLParser(searchTerm)
        parser.feed(content)
        print(parser)


class myHTMLParser(HTMLParser):

    def __init__(self, word):
        HTMLParser.__init__(self)
        self.searchTerm=word
        self.count=0


    def handle_data(self, data):
        data=data.lower()
        self.count=self.count+data.count(self.searchTerm)

    def __str__(self):
        return 'The term {} appears {} times'.format(self.searchTerm,self.count)

#url='http://condor.depaul.edu/ymendels/130/mozart.htm'
searchPage('https://en.wikipedia.org/wiki/Ludwig_van_Beethoven','Mozart')
