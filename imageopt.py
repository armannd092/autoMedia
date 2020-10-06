
import os
import time
global now
now = time.time()

def readMas(dir):
    """
    read all the files in the image directory of the web site and return their address
    """
    n=0
    fs = []
    for (dirpath, dirnames, filenames) in os.walk(dir):
        if len(filenames)>0:
            for f in filenames:
                pth = os.path.join(dirpath,f)
                fs.append(pth)
            pass
    return fs

def imgConv(paths, remove= True, sizeLimit=100):
    """
    Call magicimage from cmd and convert the png files to jpg. It will remove the old one
    """
    cmd_main = "magick convert -resize 1080x720 -sampling-factor 4:2:0 -strip -quality 65 -interlace JPEG -colorspace sRGB"
    for path in paths:
        #print(path)
        split=path.split(".")
        size=CheckSize(path)
        addCapNumber(path)
        print(size)
        if size > sizeLimit:
            #print("its big!")
            if split[-1].lower() == "png":
                cmd = cmd_main+" "+path+" "+split[0]+".jpg"
                os.system(cmd)
                if remove:
                    os.remove(path)
                    pass
            elif split[-1].lower() == "jpg":
                #print("nice!")
                #if check the file size > thershholder:
                    cmd = cmd_main+" "+path+" "+split[0]+".jpg"
                    os.system(cmd)
    return None


# check the time of creation and add the counter to the file name
def addCapNumber(path):
    n = 0
    #now = time.time()
    time = float(os.stat(path).st_ctime)
    print(now-time)
    pass

    #print(paths)
def CheckSize(path):
    #print(files)
    size = float("{0:.2f}".format(os.stat(path).st_size/1024))
    return size
    pass

def main():
    p =  input("where is the files?")
    if not os.path.exists(p): 
      print ("Dest directory does not exist")
      return
    else:
        img_path = os.path.normpath(os.path.join(os.getcwd(), p))
        print(img_path)
        f = readMas(img_path)
        #addCapNumber(f)
        #CheckSize(f)
        imgConv(f)
        return None

if __name__ == '__main__':
    main()
