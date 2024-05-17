import ctypes
import time
import datetime
import pyautogui

def main() -> None:
	work_time = False
	WORK_HOUR_BEGIN = 7 # 7 am local
	WORK_HOUR_END = 22 # 10 pm local
	pyautogui.FAILSAFE = False #prevents Exception when mouse is in the 0,0 corner
	
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
				# move the mouse a bit
				x,y = pyautogui.position()

				if y==0:
					pyautogui.moveRel(0,1)
					pyautogui.moveRel(0,-1) 
				else: 
					pyautogui.moveRel(0,-1)
					pyautogui.moveRel(0,1)
				if not work_time:
					work_time = True
					print(f"Work time has begun. Disabling screen lock. {timenow}")
			time.sleep(100)
			
		except KeyboardInterrupt:
			print("Setting back to normal and exiting. Bye.")
			# set back to normal
			ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
			break

if __name__ == "__main__":
	main()
