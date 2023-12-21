import re
import subprocess

def get_signal_level():
	try:
		output = subprocess.check_output(["iwconfig"], universal_newlines=True)
		essid_match = re.search(r'ESSID:"(.*?)"', output)
		signal_level_match = re.search(r'Signal level=(-\d+)', output)
		
		essid = ""
		signal_level = ""

		if essid_match:
			essid = essid_match.group(1)
		
		if signal_level_match:
			signal_level = signal_level_match.group(1)

		if essid and signal_level:
			string = str(essid) + ":" + str(signal_level)
			return (string)
        	
		else:
			print("Some error occurred")

	except subprocess.CalledProcessError as e:
		print(e)

print(get_signal_level())
