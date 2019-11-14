import subprocess

for ping in range(1,10):
    address = "10.10.1.4" + str(ping)
    res = subprocess.call(['ping', '-n', '4', address])
    if res == 0:
        print ("ping to", address, "OK")
    elif res == 2:
        print ("no response from", address)
    else:
        print ("ping to", address, "failed!")
        
