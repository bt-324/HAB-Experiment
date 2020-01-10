from counter import geiger
import time 

counter = geiger.GeigerCounter()

while True:
    counter.get_cpm()
    counter.get_high_cpm()
    counter.get_low_cpm()
    counter.cpm_to_usv()
    print(counter.usv_dose, "uSv/h ", counter.cpm, "CPM ", counter.high_cpm, "HICPM ", counter.low_cpm,
          "LOCPM")

