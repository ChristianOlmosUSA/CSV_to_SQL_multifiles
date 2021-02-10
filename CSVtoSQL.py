# This program takes a single CME options print out, of 57 columns and converts it to SQL. 
# see CSVtoSQL_LOOP.py if you have tons of folders of these files to convert

import sqlite3          # to set up: pip install db-sqlite3
# from sqlite3 import Error
import csv              # to set up: pip install python-csv
conn= sqlite3.connect('example.db')    # This is the Database, the database then has a table

# To execute SQLite statements in Python, you need a cursor object. You can create it using the cursor() method
c = conn.cursor()            

# STEP 2 is to CREATE the TABLE called MarketDataX, a subset of the file called example:
c.execute('DROP TABLE IF EXISTS MarketDataX')     # if this file has already been run then this table exists - consider renaming it and run again
c.execute('''CREATE TABLE MarketDataX(Ticker text,
    UTCDate text,
    CallPut text,
    Strike text,
    Month text,
    ExpirationYear text,
    UTCTimeBarStart text,
    LocalDate text,
    LocalTimeBarStart text,
    OpenBidTime text,
    OpenBidPrice text,
    OpenBidSize text,
    OpenAskTime text,
    OpenAskPrice text,
    OpenAskSize text,
    OpenTradeTime text,
    OpenTradePrice text,
    OpenTradeSize text,
    HighBidTime text,
    HighBidPrice text,
    HighBidSize text,
    HighAskTime text,
    HighAskPrice text,
    HighAskSize text,
    HighTradeTime text,
    HighTradePrice text,
    HighTradeSize text,
    LowBidTime text,
    LowBidPrice text,
    LowBidSize text,
    LowAskTime text,
    LowAskPrice text,
    LowAskSize text,
    LowTradeTime text,
    LowTradePrice text,
    LowTradeSize text,
    CloseBidTime text,
    CloseBidPrice text,
    CloseBidSize text,
    CloseAskTime text,
    CloseAskPrice text,
    CloseAskSize text,
    CloseTradeTime text,
    CloseTradePrice text,
    CloseTradeSize text,
    MinSpread text,
    MaxSpread text,
    VolumeWeightPrice text,
    TotalRegularQuotes text,
    BuyAggressorTrades text,
    SellAggressorTrades text,
    NoAggressorTrades text,
    BuyAggressorQuantity text,
    SellAggressorQuantity text,
    NoAggressorQuantity text,
    Volume text,
    TotalTrades text
) 
''')                # Create an SQL table

#def get_file_name():
#    fname=input(Enter name of CSV file to convert: )
#    return fname

filename = "E1AF1-C1800-test.csv"
#if len(fname) < 1 : print(dont skip this beat, specify a file to convert          # if you just press enter it looks for this default file name

with open(filename) as csv_file:                # So the SQL is inside the '''  ''' part, whereas the pythonic can be a list like here without a , each time
     csv_reader = csv.reader(csv_file, delimiter=',')        # ensure the , is your delimiter else change this
     for row in csv_reader:
        print(row)              # this does a row a time on your csv and prints to SQL
        Ticker=str(row[0])
        UTCDate=str(row[1])
        CallPut=str(row[2])
        Strike=str(row[3])
        Month=str(row[4])
        ExpirationYear=str(row[5])
        UTCTimeBarStart=str(row[6])
        LocalDate=str(row[7])
        LocalTimeBarStart=str(row[8])
        OpenBidTime=str(row[9])
        OpenBidPrice=str(row[10])
        OpenBidSize=str(row[11])
        OpenAskTime=str(row[12])
        OpenAskPrice=str(row[13])
        OpenAskSize=str(row[14])
        OpenTradeTime=str(row[15])
        OpenTradePrice=str(row[16])
        OpenTradeSize=str(row[17])
        HighBidTime=str(row[18])
        HighBidPrice=str(row[19])
        HighBidSize=str(row[20])
        HighAskTime=str(row[21])
        HighAskPrice=str(row[22])
        HighAskSize=str(row[23])
        HighTradeTime=str(row[24])
        HighTradePrice=str(row[25])
        HighTradeSize=str(row[26])
        LowBidTime=str(row[27])
        LowBidPrice=str(row[28])
        LowBidSize=str(row[29])
        LowAskTime=str(row[30])
        LowAskPrice=str(row[31])
        LowAskSize=str(row[32])
        LowTradeTime=str(row[33])
        LowTradePrice=str(row[34])
        LowTradeSize=str(row[35])
        CloseBidTime=str(row[36])
        CloseBidPrice=str(row[37])
        CloseBidSize=str(row[38])
        CloseAskTime=str(row[39])
        CloseAskPrice=str(row[40])
        CloseAskSize=str(row[41])
        CloseTradeTime=str(row[42])
        CloseTradePrice=str(row[43])
        CloseTradeSize=str(row[44])
        MinSpread=str(row[45])
        MaxSpread=str(row[46])
        VolumeWeightPrice=str(row[47])
        TotalRegularQuotes=str(row[48])
        BuyAggressorTrades=str(row[49])
        SellAggressorTrades=str(row[50])
        NoAggressorTrades=str(row[51])
        BuyAggressorQuantity=str(row[52])
        SellAggressorQuantity=str(row[53])
        NoAggressorQuantity=str(row[54])
        Volume=str(row[55])
        TotalTrades=str(row[56])
        c.execute('''INSERT INTO MarketDataX(Ticker,UTCDate,CallPut,Strike,Month,ExpirationYear,UTCTimeBarStart,LocalDate,LocalTimeBarStart,OpenBidTime,OpenBidPrice,OpenBidSize,OpenAskTime,OpenAskPrice,OpenAskSize,OpenTradeTime,OpenTradePrice,OpenTradeSize,HighBidTime,HighBidPrice,HighBidSize,HighAskTime,HighAskPrice,HighAskSize,HighTradeTime,HighTradePrice,HighTradeSize,LowBidTime,LowBidPrice,LowBidSize,LowAskTime,LowAskPrice,LowAskSize,LowTradeTime,LowTradePrice,LowTradeSize,CloseBidTime,CloseBidPrice,CloseBidSize,CloseAskTime,CloseAskPrice,CloseAskSize,CloseTradeTime,CloseTradePrice,CloseTradeSize,MinSpread,MaxSpread,VolumeWeightPrice,TotalRegularQuotes,BuyAggressorTrades,SellAggressorTrades,NoAggressorTrades,BuyAggressorQuantity,SellAggressorQuantity,NoAggressorQuantity,Volume,TotalTrades
) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(Ticker,UTCDate,CallPut,Strike,Month,ExpirationYear,UTCTimeBarStart,LocalDate,LocalTimeBarStart,OpenBidTime,OpenBidPrice,OpenBidSize,OpenAskTime,OpenAskPrice,OpenAskSize,OpenTradeTime,OpenTradePrice,OpenTradeSize,HighBidTime,HighBidPrice,HighBidSize,HighAskTime,HighAskPrice,HighAskSize,HighTradeTime,HighTradePrice,HighTradeSize,LowBidTime,LowBidPrice,LowBidSize,LowAskTime,LowAskPrice,LowAskSize,LowTradeTime,LowTradePrice,LowTradeSize,CloseBidTime,CloseBidPrice,CloseBidSize,CloseAskTime,CloseAskPrice,CloseAskSize,CloseTradeTime,CloseTradePrice,CloseTradeSize,MinSpread,MaxSpread,VolumeWeightPrice,TotalRegularQuotes,BuyAggressorTrades,SellAggressorTrades,NoAggressorTrades,BuyAggressorQuantity,SellAggressorQuantity,NoAggressorQuantity,Volume,TotalTrades
))
        conn.commit()