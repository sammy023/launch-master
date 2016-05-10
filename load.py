import os
"""
This module is to translate load from moses to sacs
"""
#f = open(r"D:\wenchang92-93\jisuan\Launch and Floatation Analysis Input Files\006-Launch-Motion-HYSY229-0.78dep-4.25_Base\006_launch.ans\ppo01.txt")
f = open(r"C:\Users\sammy\Desktop\launch-master-master\data\test.txt")
line = f.readline()
load = line.split()
print load

"""
check line foramt
"""



def jointLoad(load):
    """
    This function is to format Joint Load from moses to jointLoad
    sample:
    jointLoad(loadline)
    """
    if '*J' in load[0]: # Check line foramt
        number = ['']
        for i in load[1:]:
            number = [number[0]+format(float(i),'.9f')[0:7]] # load format changed

        """
        conbinate the line
        """
        jointLoad = ['LOAD   '+load[0][2:]+'     '+number[0]+' GLOB JOIN'] #conbinate the line
        return jointLoad
    else:
        pass

def formatNum(num):
    """
    This function is to format load value from moses to Sacs
    sample:
    formatNum(load[x],it must be a number string)
     1.2935E+01 ====> 1.294+1
    -.12395E+03 ====> -1.29-3
    """
    if '00' in num.split('E')[1]:  # Check E+00
        loadNum = num.split('E')[0]
        return loadNum.ljust(7)  # Load value format complited
    elif  float(num) > 0:
        a = float(num[0:6])  #number slice, 1*a
        b = num[8:10] #number slice, 10*b
        i = 4-len(str(int(b)))
        loadNum = str(round(a,i))+num[7:8]+str(int(b)) # Load value format complited
        return loadNum
    elif float(num) < 0:
        a = float(num[0:6])  #number slice, 1*a
        b = num[9:11] #number slice, 10*b
        i = 4-len(str(int(b)))
        loadNum = str(round(a,i))+num[8:9]+str(int(b)) # Load value format complited
        return loadNum
    elif float(num) == 0:
        loadNum = ''
        return loadNum.rjust(7)
    else:
       pass

f.close()
