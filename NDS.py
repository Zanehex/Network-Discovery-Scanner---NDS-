import subprocess 
import threading	

def ping(ip):
	result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
	if result.returncode == 0:
		print(f"{ip} is alive")





for ip in range (1, 254):
	ad = "192.168.1." + str(ip)
	thread = threading.Thread(target=ping, args=(ad,))
	thread.start()

