#this is file operations
from msilib.schema import File

f=open("D://Test112.jpg","w+",1)
f.write("Hello this is lankesh")
print(f.tell())
f.seek(0,0)
print(f.read(30))

