
# -*- coding: utf-8 -*-


import time
import fileinput



varl = 'temp'

def tempupdate() :
        var1 = "26.06"
        with fileinput.FileInput("index-Copy.html", inplace=True, backup='.bak') as file:
                for line in file:
                        print(line.replace('varl', varl), end='')
        with fileinput.FileInput("index-Copy.html", inplace=True, backup='.bak') as file:
                for line in file:
                        print(line.replace('timedate', time.strftime("%H:%M%p on %a, %d %b, %Y")), end='')
                        fileinput.close()

while 1:
        tempupdate()
        time.sleep(5)





