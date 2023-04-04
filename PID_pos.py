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

def main():
    home()
    controller_1 = Controller(controller_ID = 1)

    controller_1.set_position(0.5, max_torque=0.2, kd_scale=0.2, get_data=True, print_data=False)

    time.sleep(1)
  

if __name__ == '__main__':
    main()