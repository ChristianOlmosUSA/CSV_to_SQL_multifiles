# This file prints all the file paths to the terminal so you can see it running, and then it saves them to a file called FileDirectory.txt
import os
rootdir = 'TESTINGS'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        csvName = (os.path.join(subdir, file)+"\n")
        print(csvName)
        file1 = open("FileDirectory.txt","a")    # Here you can rename the output file if you like. Currently it is setting 'a' for "append"
        # it will add to prior data, manually delete the data from "FileDirectory.txt" if you dont want repitition, this avoids us accidentally deleting data, rather have double than zero!
        file1.write(csvName)
        file1.close()
     

# Count the number of lines in the text file, dont forget using a so you may have duplicates
filename = 'FileDirectory.txt'
nFILECOUNT = len(open(filename).readlines())
print('\n\n * * * * * * * * * * * * * * * * * ')
print('This many files listed in the file called ',filename,": ", nFILECOUNT)
print(' * * * * * * * * * * * * * * * * * \n')
file2 = open("FileCount.txt","w")    # save the number of files into this blank file. each time it overwrites the old number (hence 'w')
file2.write(str(nFILECOUNT))
file2.close()


f = open('FileCount.txt', 'r')
nFILECOUNT = f.readline()
print (nFILECOUNT," files to be processed")
f.close()