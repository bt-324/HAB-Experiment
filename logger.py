from counter import geiger
import time 

counter = geiger.GeigerCounter()

f = open("geigerResults.txt", "a+")

f.write("Geiger results. Date:"datetime.datetime.now()"\n")

while True:
    #counter.get_cpm()
    #counter.get_high_cpm()
    #counter.get_low_cpm()
    #counter.cpm_to_usv()
    #print(counter.usv_dose, "uSv/h ", counter.cpm, "CPM ", counter.high_cpm, "HICPM ", counter.low_cpm, "LOCPM")
    f.write(counter.usv_dose, "uSv/h ", counter.cpm, "CPM ", counter.high_cpm, "HICPM ", counter.low_cpm, "LOCPM")

f.close()
