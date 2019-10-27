# coding: utf-8

from requests import get as geturl

print("""Chipy installer - By Fred913""")
print("""Move this file to your work dir.""")
print("""Select: """)
print("""1. Install""")
sel = int(input("SELECT - "))
if sel == 1:
    with open("chipy.py", "wb") as f:
        f.write(geturl("https://raw.githubusercontent.com/fred913/chipy/master/chipy.py").content)
        f.close()
        print("Okay! ")
else:
    raise ValueError
