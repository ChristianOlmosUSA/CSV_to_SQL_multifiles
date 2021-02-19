



def Screen_Tickers():
    Dirfile = open("FileDirectory.txt", "r")
    myline = Dirfile.readline()
    while myline:
        print("MyLine: ", myline)
        myline = Dirfile.readline()
    # split the line into dates
        x = myline.split('\\')
        print("x: ",x[4:5], x[6:7])
    # compare date to file
        import csv
        with open('Tickers_vs_Dates.csv', newline='') as csvfile:
            datereader = csv.reader(csvfile, delimiter=' ')
            for row in datereader:
                print(', '.join(row))
        

    # if cool, write new file to new Directory

    # use new directory to import only the desired files

    # Close files

    Dirfile.close()




Screen_Tickers()