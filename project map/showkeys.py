from glob import glob
from json import load
def showHtmlInstructions(data,name):
    print("Showing data for file"+name)
def openfiles(x):
    for file in x:
        f=open(file,'r')
        showHtmlInstructions(load(f),file)
        f.close()
if __name__=="__main__":
    keys=[]
    openfiles(glob("data*.txt"))
    
    
