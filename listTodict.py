## THIS READS THE LIST OF EVERY FILE WE HAVE MADE, 
## ADN CONVERTS IT PURELY INTO FILE/DATE , so next it can be read  

# Define our variables as a list
itemName = []
itemDate=[]
itemIndexNo=[]  # The index number will reference which line to delete

def Screen_Tickers():
    Dirfile = open("FileDirectory.txt", "r")
    myline = Dirfile.readline()
    a = 0
    while myline:
        # print("MyLine: ", myline)   # print the name of the file
        myline = Dirfile.readline()
    # split the line into dates
        x = myline.split('\\')
        y = x[4:5]      # 4:5 is the location chunk of the Date, 6:7 is the location of the name like E1F1
        z = x[6:7]
        a = a + 1
        itemDate.append(y)  # Create a Python List with all dates
        itemName.append(z)  # Create a Python List with all Names
        itemIndexNo.append(a) # index the line numbers for removal later on<
  
    
    # print (itemName, itemDate)  # Print to termainal to show they are not grouped

    OurFiles = (list(zip(itemName,itemDate, itemIndexNo))) # combine 3 lists into 1

    print (OurFiles)

    return itemDate, itemName, itemIndexNo, OurFiles


if __name__ == "__main__":      # this runs the function above only if run from listTodict directly
    Screen_Tickers()

