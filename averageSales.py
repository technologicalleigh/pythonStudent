
######################Problem 1##################################
def getAvgSales(name):
    infile=open('widget_sales_with_id.csv')
    content=infile.readlines()
    infile.close()
    counter=0
    sales=[]
    salesAgent=[]
    salesTotal=0
    salesAvg=0
    for line in content:
        saleList=line.split(',')
        for line in range((len(saleList))):
            saleList[line]=saleList[line]
        sales.append(saleList)

    for row in range(len(sales)):
        for column in range(1,len(sales[row])):
            sales[row][column]=int(sales[row][column])

    for row in range(len(sales)):
        if sales[row][0]==name:
            salesAgent.append(sales[row])

    for row in range(len(salesAgent)):
        for column in range(1,len(salesAgent[row])):
            counter+=1
            salesTotal+=salesAgent[row][column]

    salesAvg=salesTotal/(counter)

    salesAvg='{:.1f}'.format(salesAvg)

    return salesAvg

######################Problem 2##################################
def getMothlyAverage():
    def getMonthlyAverage(month):
    infile=open('widget_sales_with_id.csv')
    content=infile.readlines()
    infile.close()
    counter=0
    sales=[]
    salesAgent=[]
    salesTotal=0
    salesAvg=0
    for line in content:
        saleList=line.split(',')
        for line in range((len(saleList))):
            saleList[line]=saleList[line]
            counter+=1
        sales.append(saleList)

    for row in range(len(sales)):
        for column in range(1,len(sales[row])):
            sales[row][column]=int(sales[row][column])

    for row in range(len(sales)):
        for column in range(len(sales[row])):
            if column==month-1:
                salesTotal+=sales[row][column+1]

    salesAvg=salesTotal/len(sales)
    return (salesAvg)
