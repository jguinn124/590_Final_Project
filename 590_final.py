# -*- coding: utf-8 -*-
"""
John Guinn

nmap GUI
"""
import tkinter as tk
import time
import threading
from queue import Queue
import socket
import sys
from datetime import datetime
#import nmap

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		master.title("Scanner GUI")
		self.pack()
		self.create_widgets()
		self.target = 'hackthissite.org'
		self.q = Queue()
		self.print_lock = threading.Lock()

	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World\n(click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")
		
		self.p_scan = tk.Button(self, text="Scan Ports", fg="blue", command=self.p_scan)
		self.p_scan.pack()
		
		self.p_scan = tk.Button(self, text="Scan External Ports", fg="blue", command=self.p_scan)
		self.p_scan.pack()
		
		self.port_scan = tk.Button(self, text="Scan Ports With Threading", fg="blue", command=self.port_scan)
		self.port_scan.pack()
		
		self.arp_cache = tk.Button(self, text="ARP cache", fg="blue", command=self.arp_cache)
		self.arp_cache.pack()
		
		#self.nmap_scan = tk.Button(self, text="Nmap Scan", fg="blue", command=self.nmap_scan)
		#self.nmap_scan.pack()

		self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
		self.quit.pack(side="bottom")
		

	def say_hi(self):
		print("hi there, everyone!")

	def scan_window(seft):
		top = Toplevel()
		top.title("About this application...")

		msg = Message(top, text=about_message)
		msg.pack()

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()
		
	
	def p_scan(self):
		import subprocess
		
		
		'''top = Toplevel()
		top.title("Scanning results")
		top.minsize(300, 300)


		
		# put results in data
		data = 5

		label = Message(top, text="Data \n")
		label.pack()

		label = Message(top, text=data)
		label.pack()
		
		

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()'''
		print("Scanning...")
		
		subprocess.call('clear', shell=True)
		
		remoteServer = input("Enter a remote host to scan: ")
		remoteServerIP = socket.gethostbyname(remoteServer)
		
		

		time.sleep(1)

		print("-"*60)
		
		time.sleep(1)
   

		print("Please wait, scanning remote host", remoteServerIP) 
		

		
		print("-"*60)
		
		t1 = datetime.now()
		
		try:
			for port in range(1,1025):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((remoteServerIP, port))
				if result == 0:
					print("Port {}:		Open".format(port))
				sock.close()
		
		except KeyboardInterrupt:
			print("You pressed Ctrl+C")
			sys.exit()
		
		except socket.gaierror:
			print("Hostname could not be resolved. Exiting")
			sys.exit()
		
		except socket.error:
			print("Could not connect to server")
			sys.exit()
			
		t2 = datetime.now()
		
		total = t1 - t2
		
		print("Scanning Completed in: ", total)
		
	def arp_cache(self):
		
		print(" Arp stuff")
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		
		ls = subprocess.check_output(['ls'])
		
		a = "\\"
		
		
		str(ls)
		
		ls.split(a)
		
		print(ls)
		
	def scan(self, port):
		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			con = sock.connect((self.target,port))
			with self.print_lock:
				print('port', port)
			con.close()
		except:
			pass
			
	def threader(self):
		while True:
			worker = self.q.get()
			
			self.scan(worker)
			
			self.q.task_done()
			
	def port_scan(self):
		
		for i in range(30):
			t = threading.Thread(target=self.threader)
			
			t.daemon = True
			t.start()
			
		start = time.time()
		
		for worker in range(1, 100):
			self.q.put(worker)
		
		self.q.join()
	'''def nmap_scan(self):
		nm = nmap.PortScanner()
		nm.scan('127.0.0.1', '20-1024')
		print(nm.command_line())
		
		for host in nm.all_hosts():
			print('----------------------------------------------------')
			print('Host : {} ({})'.format(host, nm[host].hostname()))
			print('State : {}'.format(nm[host].state()))
		for proto in nm[host].all_protocols():
			print('---------')
			print('Protocol : {}'.format(proto))
		
		lport = nm[host][proto].keys()
		for port in lport:
			print('port : {}\tstate : {}'.format(port, nm[host][proto][port]['state']))'''
			

		
		
	
		

root = tk.Tk()
app = Application(master=root)
app.mainloop()

