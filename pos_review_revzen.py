from moteus_fdcan_adapter import Controller
from moteus_fdcan_adapter import MoteusReg
import numpy
import time
import math

def home():
    controller_1 = Controller(controller_ID = 1)
    response_data_c1=controller_1.get_data()
    pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
    if (pos_deg_c1>0):      
        while(1):
            response_data_c1=controller_1.get_data()
            pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
            print(pos_deg_c1)
            if (pos_deg_c1<=0):
                break
            controller_1.set_velocity(velocity=-0.5)
    else: 
        while(1):
            response_data_c1=controller_1.get_data()
            pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
            print(pos_deg_c1)
            if (pos_deg_c1>=0):
                break
            if abs(pos_deg_c1-0)<0.05:
                vel=0.5
            controller_1.set_velocity(velocity=0.5)

def setpos(pos,L):       #homming needed, coz if the move command starts from position motor is not now, it jumps and falls into safe mode
        if pos>1: pos=0.98    # encoder never reaches 1 or -1 so limit needs to lesser than that to be able to jump out of the while loop
        if pos<-1: pos=-0.98
        controller_1 = Controller(controller_ID = 1)
        response_data_c1=controller_1.get_data()
        pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
        
        if pos_deg_c1==pos:
            pass
        elif pos_deg_c1>pos:  #pos_deg_c1 current position
            print("in -ve looping")
            r=pos_deg_c1
            
            while pos_deg_c1>=pos:
                time.sleep(0.015)
                controller_1.set_position(position=r, max_torque=0.2, kd_scale=0.4, get_data=True, print_data=False)
                response_data_c1=controller_1.get_data()
                pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
                L.append([time.time(),r,pos_deg_c1])
                r=r-0.02
                print(pos_deg_c1)
                if(pos_deg_c1>1 or pos_deg_c1<-1):
                    break

        elif pos_deg_c1<pos:
            print("in -ve looping")
            r=pos_deg_c1

            while pos_deg_c1<=pos:
                time.sleep(0.015)
                controller_1.set_position(position=r, max_torque=0.2, kd_scale=0.4, get_data=True, print_data=False)           
                response_data_c1=controller_1.get_data()
                pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
                L.append([time.time(),r,pos_deg_c1])
                r=r+0.02                
                print(pos_deg_c1)
                if(pos_deg_c1>1 or pos_deg_c1<-1):
                    break

def main():
    home()
    controller_1 = Controller(controller_ID = 1)
    global L
    L=[]
   

    t = time.localtime()
    first_full_timei = time.strftime("%H:%M:%S", t)
    setpos(-0.88,L)   #-180
    t = time.localtime()
    first_full_timef = time.strftime("%H:%M:%S", t)
    
    return L 
    

if __name__ == '__main__':
    L=main()
    L=numpy.asarray(L).T

    