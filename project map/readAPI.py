from base64 import b64decode as bc
def readAPI():
    f=open("API Key.txt",'r')
    s=f.read()
    f.close()
    return bc(s).decode('utf-8')
