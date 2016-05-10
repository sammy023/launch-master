import os
"""
This module is to translate load from moses to sacs
"""
f = open(r"D:\wenchang92-93\jisuan\Launch and Floatation Analysis Input Files\006-Launch-Motion-HYSY229-0.78dep-4.25_Base\006_launch.ans\ppo01.txt")
line = f.readline()
load = line.split()
print load

"""
check line foramt
"""



def jointLoad(load):
    """
    This is too format Joint Load from moses to jointLoad
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
