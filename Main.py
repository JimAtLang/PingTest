import os

from ping3 import  ping
import time
from datetime import datetime
from os import environ

room = "915"
now = datetime.today()
fn = f'rm{room}-{os.environ['COMPUTERNAME']}-{now.year}{now.month:02}{now.day:02}-{now.hour:02}{now.minute:02}'
print(fn)
# fl = open(fn,"a")
#
# fl.write("Room "+ room + str(now) +"\n")
#
# f = 0
# n = 0
# sum = 0
# times = 3
# succ = 0
# for i in range(times):
#     p = str(ping("8.8.8.8"))
#     fl.write(time.ctime() + "\t" + p + "\n")
#     if p == "False":
#         f+=1
#     elif p == "None":
#         n+=1
#     else:
#         succ+=1
#         try:
#             sum+=float(p)
#         except ValueError:
#             pass
#     time.sleep(1)
# avg = sum/succ
# fl.write("Successful attempts: " + str(succ) + "\n")
# fl.write("Failed attempts: " + str(f) + "\n")
# fl.write("No response: " + str(n) + "\n")
# fl.write("Average response time: " + str(avg) + "\n")