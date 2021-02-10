import os
rootdir = 'test'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))


# This file just prints all the file paths to the terminal, it doesnt save them
# this was just used for testing, but I dont like to throw out neat code


# count the number of lines in the file, this is equal to the number of files! 
filename = 'FileDirectory.txt'
n = len(open(filename).readlines())
print('\n\n * * * * * * * * * * * * * * * * * ')
print('This many files in the file called ',filename,": ", n)
print(' * * * * * * * * * * * * * * * * * \n')
