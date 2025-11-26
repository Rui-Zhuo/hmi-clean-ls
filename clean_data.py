# {{{ Library imports
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

# 然后正常导入
from src.hmi_clean import HmiClass
from src.globalvars import DopplerVars

# from hmi_clean.hmi_clean import HmiClass
# from hmi_clean.globalvars import DopplerVars
# from hmi_clean import HmiClass
# from globalvars import DopplerVars
import argparse
import glob
import time
import os
import numpy as np
# }}} imports

# {{{ argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--gnup', help="Argument for gnuParallel",
                    default=1, type=int)
ARGS = parser.parse_args()

GVAR = DopplerVars(ARGS.gnup)
# }}} argument parser


if __name__ == "__main__":
    # {{{ directories
    # hmi_data_dir = GVAR.get_dir("hmidata") # Edited by Rui, 2025/11/13
    # hmi_data_dir = 'C:/Users/rzhuo/Desktop/' # Edited by Rui, 2025/11/13, 2025/11/21
    hmi_data_dir = 'E:/Research/Data/SDO/HMI/SHARP/Dopplergram/' # Edited by Rui, 2025/11/21
    hmi_files = glob.glob(f"{hmi_data_dir}/*.fits")
    print("Program started -- reading files")
    # }}} dirs

    # 1. Reading HMI Dopplergrams
    t1 = time.time()

    total_days = len(hmi_files)
    print(f"Total days = {total_days}")

    # 2. Creating SunPy maps
    # daylist = [0] # Edited by Rui, 2025/11/13
    daylist = np.arange(999, 1847) # Edited by Rui, 2025/11/21
    for day in daylist:
        print("### 1. Initializing")
        dop_img = HmiClass(hmi_data_dir, hmi_files[day], day, gvar=GVAR)
        print("### 2. Getting satellite velocity")
        dop_img.get_sat_vel()
        print("### 3. Removing effect of satellite velocity")
        dop_img.remove_sat_vel()
        print("### 4. Removing gravitational redshift")
        dop_img.remove_grav_redshift()
        print("### 5. Removing large scale features")
        dop_img.remove_large_features()
        print("### 6. Saving processed data")

        # dop_img.save_theta_phi() # Edited by Rui, 2025/11/21
        # dop_img.save_theta_phi_DC() # Edited by Rui, 2025/11/21
        dop_img.save_map_data()
    t2 = time.time()
    print(f"Total time taken = {(t2-t1)/60:5.2f} minutes")
