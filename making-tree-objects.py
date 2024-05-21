# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()


robot = RDK.Item('Fanuc M-2000iC/210R')
frame4=RDK.AddFrame('frame4')
frame4.setPose(transl(1940,-373.614,788.330)*rotz(-135*pi/180)*roty(0*pi/180)*rotx(-14.928*pi/180))
cart4 = RDK.AddFile(r'C:\Users\fredy\Desktop\carts\cart4.stl',frame4)
cart4.setPose(transl(454.522,205.054,-761.197)*rotz(-90*pi/180)*roty(14.928*pi/180)*rotx(90*pi/180))
Approach1 = RDK.AddTarget('Approach1',frame4)
Approach1=Approach1.setPose(transl(836,275,320)*rotz(-90.112*pi/180)*roty(-3.382*pi/180)*rotx(178.460*pi/180))
target1=RDK.AddTarget('target1',frame4)
target1=target1.setPose(transl(836,275,120)*rotz(-90.112*pi/180)*roty(-3.382*pi/180)*rotx(178.460*pi/180))
##
#
frame7=RDK.AddFrame('frame7')
frame7.setPose(transl(2541.446,-975.060,788.330)*rotz(-135*pi/180)*roty(0*pi/180)*rotx(-14.928*pi/180))
cart7 = RDK.AddFile(r'C:\Users\fredy\Desktop\carts\cart7.stl',frame7)
cart7.setPose(transl(454.522,203.078,-761.724)*rotz(-90*pi/180)*roty(14.928*pi/180)*rotx(90*pi/180))
Approach2 = RDK.AddTarget('Approach2',frame7)
Approach2=Approach2.setPose(transl(836.03,112.647,330)*rotz(-90.112*pi/180)*roty(-3.382*pi/180)*rotx(178.460*pi/180))
target2=RDK.AddTarget('target2',frame7)
target2=target2.setPose(transl(836,112.647,120)*rotz(-90.112*pi/180)*roty(-3.382*pi/180)*rotx(178.460*pi/180))

##
#
frame5=RDK.AddFrame('frame5')
frame5.setPose(transl(-812.638,1005.325,0)*rotz(45*pi/180)*roty(0*pi/180)*rotx(0*pi/180))
convoyer = RDK.AddFile(r'C:\Users\fredy\Desktop\carts\convoyer.stl',frame5)
holder = RDK.AddFile(r'C:\Users\fredy\Desktop\carts\holder.stl',frame5)
convoyer.setPose(transl(596.9,1752.6,0)*rotz(90*pi/180)*roty(0*pi/180)*rotx(0*pi/180))
holder.setPose(transl(-848.180,1326.987,-1076.296)*rotz(90*pi/180)*roty(0*pi/180)*rotx(0*pi/180))
Approach3 = RDK.AddTarget('Approach3',frame5)
Approach3=Approach3.setPose(transl(576.577,814.278,1200)*rotz(-89.591*pi/180)*roty(1.808*pi/180)*rotx(179.622*pi/180))
target3=RDK.AddTarget('target3',frame5)
target3=target3.setPose(transl(576.577,814.278,1050)*rotz(-89.591*pi/180)*roty(1.808*pi/180)*rotx(179.622*pi/180))


