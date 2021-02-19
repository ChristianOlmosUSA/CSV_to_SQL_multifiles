def Screen_Tickers():
    import csv
    from csv import reader
    # compare date to file of expiry dates from Ivan
    with open('Tickers_vs_Dates.csv', 'r') as read_obj:
        # read csv file as a list of lists, # Pass reader object to list() to get a list of lists
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        #print(list_of_rows)
    Dirfile = open("FileDirectory.txt", "r")
    DirLine = Dirfile.readline()
    while DirLine:
        # print("MyLine: ", DirLine)
        DirLine = Dirfile.readline()
    # split the line into dates
        x = DirLine.split('\\')
        # print("x: ",x[4:5], x[6:7])
        ticker = x[6:7]                     # This is our file ticker
        date = x[4:5]                          # This is our file date if its older than the reference it will be struck out                     
        print("Ticker: ",ticker, "  Date: ", date)
        #print("Date: ", date)
            
           
                            
              
"""  if (row[1] == ticker) & (date > row[0]):
    CleanData = open("InDateTickers.csv","a")
    CleanData.write(datereader)
"""          
Screen_Tickers()