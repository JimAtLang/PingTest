from ping3 import  ping
import time

fl = open("905-20241022-4pm.txt","a")

f = 0
n = 0
sum = 0
times = 21600
succ = 0
for i in range(times):
    p = str(ping("8.8.8.8"))
    fl.write(time.ctime() + "\t" + p + "\n")
    if p == "False":
        f+=1
    elif p == "None":
        n+=1
    else:
        succ+=1
        try:
            sum+=float(p)
        except ValueError:
            pass
    time.sleep(1)
avg = sum/succ
fl.write("Successful attempts: " + str(succ) + "\n")
fl.write("Failed attempts: " + str(f) + "\n")
fl.write("No response: " + str(n) + "\n")
fl.write("Average response time: " + str(avg) + "\n")