import psutil
import time
import matplotlib.pyplot as plt

cpu_usage=list()
ram_usage=list()

max_ram=psutil.virtual_memory()[0]
max_cpu=100

howlong=int(input("Per quanto tempo puoi monitorare? Inserisci il tempo in secondi: "))
timepassed=0

while(True):
    if(timepassed==howlong+1):
        break
    time.sleep(1)
    cpu_usage.append(int(psutil.cpu_percent()))
    ram_usage.append(int(psutil.virtual_memory()[2]))
    timepassed+=1


y_axis1=cpu_usage
x_axis1=range(len(y_axis1))
plt.subplot( 2 , 1 , 1)
plt.ylabel("CPU USAGE")
plt.axis([0, howlong, 0, max_cpu])
plt.plot(x_axis1, y_axis1)


y_axis2=ram_usage
x_axis2=range(len(y_axis2))
plt.subplot( 2 , 1 , 2)
plt.ylabel("RAM USAGE")
plt.axis([0, howlong, 0, 100])
plt.plot(x_axis2, y_axis2)

plt.savefig("pc_usage.png")