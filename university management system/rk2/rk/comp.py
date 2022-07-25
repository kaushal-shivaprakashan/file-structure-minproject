import zlib, base64
import os
os.chdir(r'''c:\Users\kaush\OneDrive\Desktop\fsss finale\rk2\rk''')
file1=open ('data.csv','r')
text=file1.read()
file1.close()
code=base64.b64encode(zlib.compress(text.encode('utf-8'),9))
code=code.decode('utf-8')
f=open('compressd.txt', 'w')
f.write(code)
f.close()