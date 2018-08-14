import cv2.cv2 as cv
import os

def View():
    for i in os.listdir("./"):
        if endwith(i,".jpg"):
            print(i)
            img=cv.imread(i)
            cv.imshow("PView",img)
            keycode = cv.waitKey(0)
            print(keycode)
            if 32==keycode:
                os.system("rm -f {0}".format(i))
                print("rm done")    

def endwith(s,*endstring):
   resultArray = map(s.endswith,endstring)
   if True in resultArray:
       return True
   else:
       return False

if __name__ == "__main__":
    View()