
from robolink import *    # API to communicate with robodk
from robodk import *      # robodk robotics toolboxThe program starts here:



# Any interaction with RoboDK must be done through RDK:
RDK = Robolink()

# Turn off automatic rendering (faster)
RDK.Render(False)

#RDK.Set_Simulation_Speed(500); # set the simulation speed

# Gather required items from the station tree
robot = RDK.Item('Fanuc M-2000iC/210R') # establish a link with the simulator
a1 = RDK.Item(' Approach1 ')
a2 = RDK.Item(' Approach2 ')
a3 = RDK.Item(' Approach3 ')
t1 = RDK.Item(' target1 ')     # retrieve the Target item
t2 = RDK.Item(' Target 2 ')
t3 = RDK.Item('Target')
frame1 = RDK.Item('Frame4')
frame2 = RDK.Item('Frame7')
frame3 = RDK.Item('Frame5')
###################


while(1)  :
 import csv
 ##posecart2=[  2541.445716,  -975.059946,   788.330000,   -14.928000,     0.000000,  -135.000000 ]
 
 task = []
 chartxy = []   
 prod = mbox ('Enter the name of csvfile in directory for input Table' , entry =True) 
 prod = str(prod)  
 with open(prod) as f:
 #with open('Book1.csv') as f:    
    reader = csv.reader(f)
    for row in reader:
       # task.append(row[0])
     task = row[0]
     print(task)
     
    
    
     '''
     [  1939.999780,  -373.614010,
     788.330000,   0,     0.000000,  -40.000000 ]
     '''
    
     # Read the 4x4 pose matrix as [X,Y,Z , A,B,C] Euler representation (mm and deg): same representation
     RDK.Render(False)
     cart1=frame1.Pose()
     conv=frame3.Pose() 

     XYZABC=Pose_2_Fanuc(cart1)
     convpose1=Pose_2_Fanuc(conv)
     print("Current cart Pose",XYZABC)
     print("Current conveyor Pose",convpose1)
     #Chart 
     XYZABC2 = XYZABC 
     # Pose values for the Cart
     XYZABC2[0] = float (row[1])
     XYZABC2[1] = float (row[2])
     XYZABC2 [2] = float (row[3])
     XYZABC2 [3] = float (row[4])
     XYZABC2 [4] = float (row[5])
     XYZABC2 [5] = float (row[6])
     

     convpose=convpose1
     # Pose values for the Conveyor
     convpose[0] = float (row[7])
     convpose[1] = float (row[8])
     convpose[2] = float (row[9])
     convpose[3] = float (row[10])
     convpose[4] = float (row[11])
     convpose[5] = float (row[12])

     print ('conv pose 0 ',convpose[0])
     print ('conv pose 1 ',convpose[1])
     print ('conv pose 2 ',convpose[2])
     print ('conv pose 3 ',convpose[3])
     print ('conv pose 4 ',convpose[4])
     print ('conv pose 5 ',convpose[5])
     
     print("new cart Pose",XYZABC2)
     print ("new conveyor Pose",convpose)
     posemat=TxyzRxyz_2_Pose(XYZABC2) #Returns the pose (4*4 matrix)given the position (mm) and Euler angles (rad) as an array [x,y,z,rx,ry,rz]
     print('convpose',convpose)
     posemat2=TxyzRxyz_2_Pose(convpose)

     print('posemat2',posemat2)


     #set frame Locations
     frame1.setPoseAbs(posemat) # with respect to the station reference frame
     frame3.setPoseAbs(posemat2)
     


     RDK.Render(True)

     tasknum = int(task)
     print(tasknum)
     for x in range(0,tasknum) :
             robot.setPoseFrame(frame1)
             robot.MoveJ(a1) # move the robot to the approach position 
             robot.MoveL(t1) # linear move to the target
             robot.MoveL(a1)
             robot.setPoseFrame(frame3)
             robot.MoveJ(a3)
             robot.MoveL(t3)
             robot.MoveL(a3)
             

              
              
        
