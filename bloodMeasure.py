import bloodFunctions as b
import time
import matplotlib.pyplot as plt

try:
    b.initSpiAdc()

    measure_time = 60.0

    start = time.time()
    data = []

    print ("Measurements have been started. Wait for", measure_time, "seconds...")
    while time.time() - start < measure_time:
        data.append(b.getAdc())

    finish = time.time()
    print ("Measurements have been finished")
    
    print(len(data))

    a=[str(item) for item in data]
    with open ("angry.txt","w") as outfile:
        outfile.write("\n".join(a))

    plt.plot(data)
    plt.show()


finally:
    b.deinitSpiAdc()
