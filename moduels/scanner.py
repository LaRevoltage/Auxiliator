from concurrent.futures import ThreadPoolExecutor
import socket
def portscan(host):
	ports=list(range(1, 65535))
	portsopened=[]
	def scanner(port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.5)
		try:
			con = s.connect((host, port))
			portsopened.append(port)
			con.close()
		except:
			pass
	with ThreadPoolExecutor(max_workers=5000) as pool:
		pool.map(scanner, ports)
	return(portsopened)