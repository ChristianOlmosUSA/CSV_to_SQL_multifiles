from zipfile import ZipFile

with ZipFile('zipFiles.zip', 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall('unzippedFiles')
   print('Filea all in unzippedFiles folder') 