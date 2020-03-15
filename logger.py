from counter import geiger
import time 
from pathlib import Path
import os

counter = geiger.GeigerCounter()

data_path = "/home/alarm/HAB-Experiment/geigerResults.txt"

f = open(data_path, "a+")

f.write("Geiger results.\n")
f.write("uSv/h   CPM   HICPM   LOCPM\n")

while True:
    counter.get_cpm()
    counter.get_high_cpm()
    counter.get_low_cpm()
    counter.cpm_to_usv()

    f.write(str(counter.usv_dose) + "   ")
    f.write(str(counter.cpm) + "   ")
    f.write(str(counter.high_cpm) + "   ")
    f.write(str(counter.low_cpm) + "\n")

    os.fsync()

f.close()
