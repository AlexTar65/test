import zipfile
with zipfile.ZipFile('rogaikopyta.zip', 'r') as zip_ref:
    zip_ref.extractall('C:\Users\taranenko\Desktop\new project')
zip = zipfile.ZipFile('rogaikopyta.zip')

# extract a specific file from the zip container
#f = zip.open("file_inside_zip.txt")

# save the extraced file 
#content = f.read()
#f = open('file_inside_zip.extracted.txt', 'wb')
#f.write(content)
#f.close()    
import urllib.request
url = 'https:\\stepik.org\media\attachments\lesson\245299\rogaikopyta.zip'
resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html') # скачиваем файл
#response = urllib.request.urlopen(url)
#response = requests.get(url, stream=True)
#html = response.read()


import xlrd
import wget

url = 'https:\\stepik.org\media\attachments\lesson\245299\rogaikopyta.zip'
wget.download(url)



wb = xlrd.open_workbook('tab.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]
for rownum in range(7, 27):
    temp = sh.row_values(rownum)
    nmin = min(nmin, temp[2])
print(nmin)

import zipfile as z
import os
a=z.ZipFile("rogaikopyta.zip")
a.extractall('./$$$/')
os.chdir('$$$')
opened=[]
for i in range(1000):
    opened+=open('%d.xlsx'%i+1)
#TODO: обработка массива opened
