from moteus_fdcan_adapter import Controller
from moteus_fdcan_adapter import MoteusReg
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

def setpos(pos):       #homming needed, coz if the move command starts from position motor is not now, it jumps and falls into safe mode
        if pos>1: pos=0.98    # encoder never reaches 1 or -1 so limit needs to lesser than that to be able to jump out of the while loop
        if pos<-1: pos=-0.98
        controller_1 = Controller(controller_ID = 1)
        response_data_c1=controller_1.get_data()
        pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]

        if pos_deg_c1==pos:
            pass
        elif pos_deg_c1>pos:
            print("in -ve looping")
            r=pos_deg_c1
            while pos_deg_c1>=pos:
                time.sleep(0.0025)
                controller_1.set_position(position=r, max_torque=0.2, kd_scale=0.2, get_data=True, print_data=False)
                r=r-0.005
                response_data_c1=controller_1.get_data()
                pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
                print(pos_deg_c1)
                if(pos_deg_c1>1 or pos_deg_c1<-1):
                    break

        elif pos_deg_c1<pos:
            print("in -ve looping")
            r=pos_deg_c1
            while pos_deg_c1<=pos:
                time.sleep(0.0025)
                controller_1.set_position(position=r, max_torque=0.2, kd_scale=0.2, get_data=True, print_data=False)
                r=r+0.005                
                response_data_c1=controller_1.get_data()
                pos_deg_c1 = response_data_c1[MoteusReg.MOTEUS_REG_POSITION]
                print(pos_deg_c1)
                if(pos_deg_c1>1 or pos_deg_c1<-1):
                    break

def main():
    home()
    controller_1 = Controller(controller_ID = 1)

    controller_1.set_position(0.5, max_torque=0.2, kd_scale=0.2, get_data=True, print_data=False)

    time.sleep(1)

    t = time.localtime()
    first_full_timei = time.strftime("%H:%M:%S", t)
    controller_1.set_position(position=r, max_torque=0.2, kd_scale=0.2, get_data=True, print_data=False)

    #setpos(-0.5)   #-180
    t = time.localtime()
    first_full_timef = time.strftime("%H:%M:%S", t)

    time.sleep(1)
    t = time.localtime()
    first_quat_timei = time.strftime("%H:%M:%S", t)
    controller_1.set_position(position=r, max_torque=0.2, kd_scale=0.2, get_data=True, print_data=False)
    
    #setpos(-0.75)    #-270
    t = time.localtime()
    first_quat_timef = time.strftime("%H:%M:%S", t)

    time.sleep(1)

  

if __name__ == '__main__':
    main()