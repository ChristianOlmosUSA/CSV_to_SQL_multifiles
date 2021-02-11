from zipfile import ZipFile

inputFolder = input("What is the folder name you wish to unzip?  ")
outputFolder = input("What is the folder name you wish to save the files to?  ")

with ZipFile(inputFolder, 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall(outputFolder)
   print('Files all in ',outputFolder,' folder') 