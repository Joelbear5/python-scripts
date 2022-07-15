import ctypes
import time
import datetime

work_time = False
WORK_HOUR_BEGIN = 9 # 9 am local
WORK_HOUR_END = 19 # 7 pm local

while True:
	try:
		timenow =  datetime.datetime.now()
		if timenow.hour < WORK_HOUR_BEGIN or timenow.hour >= WORK_HOUR_END:
			
			if work_time:
				# set to normal (not work time)
				ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
				work_time = False
				print(f"Work time has ended. Enabling screen lock. {timenow}")
		else:
			# prevent screen lock (work time)
			ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
			if not work_time:
				work_time = True
				print(f"Work time has begun. Disabling screen lock. {timenow}")
		time.sleep(100)
		
	except KeyboardInterrupt:
		print("Setting back to normal and exiting. Bye.")
		# set back to normal
		ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
		break
