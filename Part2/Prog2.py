from robolink import *    # API to communicate with robodk
from robodk import *      # robodk robotics toolboxThe program starts here:


# Any interaction with RoboDK must be done through RDK:
RDK = Robolink()

# Turn off automatic rendering (faster)
RDK.Render(True)

#RDK.Set_Simulation_Speed(500); # set the simulation speed

# Gather required items from the station 
robot = RDK.Item('Fanuc M-2000iC/210R')
a1 = RDK.Item(' Approach1 ')
a2 = RDK.Item(' Approach2 ')
a3 = RDK.Item(' Approach3 ')
t1 = RDK.Item(' target1 ')
t2 = RDK.Item(' Target 2 ')
t3 = RDK.Item('Target')
frame1 = RDK.Item('Frame4')
frame2 = RDK.Item('Frame7')
frame3 = RDK.Item('Frame5')

#Prompts the user to input(type the name)a CSV file in proper directory  
while(1)  :
 import csv
 task = []
 chartxy = []   
 prod = mbox ('Enter the name of csvfile in directory for input Table' , entry =True)
 prod = str(prod)  
 with open(prod) as f:
 #e.g with open('Book1.csv') as f:    
    reader = csv.reader(f)
    for row in reader:
     #Reads number of tasks(objects in each cart) from 1st column of Excel Table   
     task = row[0]
     #reads from 2nd column the corres   
     chartxy = row[1]
     #Picks from cart and places to the conveyor according to excel table data     
     tasknum = int(task)
     if tasknum == 1 :
         print('',tasknum)
         print (chartxy,charty,chartx)
         if chartxy == charty:
             print('chartxy=charty')   
             robot.setPoseFrame(frame2)
             robot.MoveJ(a2)
             robot.MoveL(t2)
             robot.MoveL(a2)
             robot.setPoseFrame(frame3)
             robot.MoveJ(a3)
             robot.MoveL(t3)
             robot.MoveL(a3)
             
         elif chartxy == chartx:
             print('chartxy==chartx')   
             robot.setPoseFrame(frame1)
             robot.MoveJ(a1)
             robot.MoveL(t1)
             robot.MoveL(a1)
             robot.setPoseFrame(frame3)
             robot.MoveJ(a3)
             robot.MoveL(t3)
             robot.MoveL(a3)
             
             
         else:
            print('error loop')
         
         
     else :
            
        chartx = "chartx"
        charty = "charty"
        if chartxy == chartx :
         print('if loopchartx')  
         for x in range(tasknum) :
          print('for loop chart x task',tasknum )   
          robot.setPoseFrame(frame1)
          robot.MoveJ(a1)
          robot.MoveL(t1)
          robot.MoveL(a1)
          robot.setPoseFrame(frame3)
          robot.MoveJ(a3)
          robot.MoveL(t3)
          robot.MoveL(a3)
        elif chartxy == charty :
         print('else loop chart y')    
         for y in range(tasknum) :
          print('for loop chart y task',tasknum )   
          robot.setPoseFrame(frame2)
          robot.MoveJ(a2)
          robot.MoveL(t2)
          robot.MoveL(a2)
          robot.setPoseFrame(frame3)
          robot.MoveJ(a3)
          robot.MoveL(t3)
          robot.MoveL(a3)

        else :
          print('else loop2',chartxy)
          
          if chartxy == chartx :
              print('movementchartx')
              
              robot.setPoseFrame(frame1)
              robot.MoveJ(a1)
              robot.MoveL(t1)
              robot.MoveL(a1)
              robot.setPoseFrame(frame3)
              robot.MoveJ(a3)
              robot.MoveL(t3)
              robot.MoveL(a3)
              
          elif chartxy == charty :
              print ('movementcharty')
              
              robot.setPoseFrame(frame2)
              robot.MoveJ(a2)
              robot.MoveL(t2)
              robot.MoveL(a2)
              robot.setPoseFrame(frame3)
              robot.MoveJ(a3)
              robot.MoveL(t3)
              robot.MoveL(a3)
          else :
              print('no chart match')
              robot.setPoseFrame(frame1)
              robot.MoveJ(a1)
              robot.MoveL(t1)
              robot.MoveL(a1)
              robot.setPoseFrame(frame3)
              robot.MoveJ(a3)
              robot.MoveL(t3)
              robot.MoveL(a3)
              
        
