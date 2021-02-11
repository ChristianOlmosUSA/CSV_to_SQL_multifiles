# Convert Zip to CSV to SQL: Iterates through all files in the folder 'test'

a) If you wish to convert zip files first, then move unzipNested.py to the same folder as the zip files, this will iterate through every single zip file and unzip it into a CSV, you then need to rename the folder to TESTINGS
> python unzipNested.py

b)
1) run 
> python iterate_to_txt.py      
This looks for and runs on a folder called TESTINGS and creates a list of every csv file it can find. This will count the files in TESTINGS folder and save the name of each to a text file called FileDirectory.txt

2) run 
> python CSVtoSQL_LOOP.py 
this will read all the files from FileDirectory.txt and write them into an SQL table in example.db


I have left some of the dev tools and test files in here.
smallTestFolder contains some examples to run this on
but the 2GB file I ran this on is in gitignore
