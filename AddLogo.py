import os

directory = input()
filename = "./" + directory + "/Build/" + "UnityLoader.js"

try:
    f = open(filename, 'r')
    contents = f.read()
    f.close()
    sidx = contents.find('progressLogoUrl:"data:image/png;base64,') + len('progressLogoUrl:"data:image/png;base64,')
    fidx = contents.find('",progressEmptyUrl:"data:image/png;base64,')

    logo = open("logo.txt", 'r')
    logoStr = logo.read()
    logo.close()

    f = open(filename, 'w')
    f.write(contents[0:sidx] + logoStr + contents[fidx:len(contents)])
    f.close()
    
except IOError:
    print("ERROR")