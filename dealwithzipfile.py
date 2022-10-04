import zipfile

zipfilename = zipfile.ZipFile('filename')
files = zipfilename.filelist()
print(zipfilename.namelist())
print(zipfilename.getinfo('filename'))
zipfilename.extract()
zipfilename.extractall()
newzip = zipfile.ZipFile('filename','w')
newzip.write('file',compress_type=zipfile.ZIP_DEFLATED)
newzip.close()