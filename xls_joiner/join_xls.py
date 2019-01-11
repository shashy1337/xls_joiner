import pandas as pd
import os
path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-3:] == 'xls']
all_file_frames = []
for f in files_xls:
    print('Reading %s'%f)
    tab = pd.read_excel(f)
    all_file_frames.append(tab)
all_frame = pd.concat(all_file_frames,axis=0, sort=True)
all_frame.to_excel('final_file.xlsx') 
