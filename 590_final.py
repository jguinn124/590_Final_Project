# -*- coding: utf-8 -*-
"""
John Guinn

nmap GUI
"""
from tkinter import *
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
		master.title("Easy Network Utility")
		master.geometry("600x600")
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
		
		self.E1 = Entry(self, bd =5)
		self.E1.pack(side = "top")

		print(self.E1.get())
		
		self.p_scan = tk.Button(self, text="Scan Ports", fg="blue", command=self.p_scan)
		self.p_scan.pack()
		
		self.p_scan = tk.Button(self, text="Scan External Ports", fg="blue", command=self.p_scan)
		self.p_scan.pack()
		
		self.port_scan = tk.Button(self, text="Scan Ports With Threading", fg="blue", command=self.port_scan)
		self.port_scan.pack()

		self.ping = tk.Button(self, text="Ping local", fg="blue", command=self.ping)
		self.ping.pack()

		self.ping_button = tk.Button(self, text="Ping out", fg="blue", command=self.ping_out)
		self.ping_button.pack()

		self.ifcon_button = tk.Button(self, text="Network Configuration", fg="blue", command=self.ifconfig)
		self.ifcon_button.pack()

		self.netstat_button = tk.Button(self, text="Router Configuration", fg="blue", command=self.netstat)
		self.netstat_button.pack()
		
		self.arp_button = tk.Button(self, text="ARP Cache", fg="blue", command=self.arp_cache)
		self.arp_button.pack()

		self.ip_button = tk.Button(self, text="My IP Address", fg="blue", command=self.my_ip)
		self.ip_button.pack()

		self.dns_button = tk.Button(self, text="My Hostname and Domain", fg="blue", command=self.my_DNS)
		self.dns_button.pack()
		
		#self.nmap_scan = tk.Button(self, text="Nmap Scan", fg="blue", command=self.nmap_scan)
		#self.nmap_scan.pack()

		self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
		self.quit.pack(side="bottom")
		

	def say_hi(self):
		top = Toplevel()
		top.title("Documentation")
		top.minsize(300, 300)
			
			# put results in data
		data = """       Do not use this application to attack machines that you have no authourity over.
		Scan Ports button (requires address)
		The scanning ports button will allow you to see open ports on your machine if you use localhost or find open ports on other machines
		
		Ping button (requires address)
		This ping button will allow you to test the connection between your machine and another machine.
		Network Configuration button
		The Network Configuration button will allow you to see information about the network you are connected to.
		Router Configuration Button
		The Router Configuration Button will allow you to see how your router is configured and information about it.
		ARP Cashe button
		
		
		For this programming project, we built a tkinter GUI application in python that allowed allows the user to scan the ports on their remote machine, ping the remote machine or a user inputted address, a configuration option to get the ip address of your machine and a netstat option to get the network statistics of you machine. These are the features that we have implemented for our project. The program is built in python as a class and each feature is a method in the class called “Application”. Each feature of this project is a button on the application GUI.
			"""


		label = Text(top)
		label.pack()
		label.insert(END, data)

	def scan_window(seft):
		top = Toplevel()
		top.title("About this application...")

		msg = Message(top, text=about_message)
		msg.pack()

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()
		
	
	def p_scan(self):
		import subprocess
		print_lock = threading.Lock()
		

		print("Scanning...")
		
		subprocess.call('clear', shell=True)
		
		remoteServer    = self.E1.get()
		remoteServerIP  = socket.gethostbyname(remoteServer)
		
		

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
		
		top = Toplevel()
		top.title("Scanning results")
		top.minsize(300, 300)


		
		# put results in data
		data = open_port

		label = Message(top, text="Data \n")
		label.pack()

		label = Message(top, text=data)
		label.pack()
		
		

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()

		
		

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()
		
		
	def scan(self, port):
		
		top = Toplevel()
		top.title("Scanning results")
		top.minsize(300, 300)
		
		T = Text(top, height=30, width=100)
		scrollbar = Scrollbar(top)
		scrollbar.pack( side = RIGHT, fill = Y )
		T.pack(side=LEFT, fill=Y)
		scrollbar.config( command = T.yview )
		T.config(yscrollcommand=scrollbar.set)
		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			con = sock.connect((self.E1.get(),port))
			with self.print_lock:
				data = res
		
				T.insert(END, data)
				#print('port', port + '		Open')
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
			t = threading.Thread(target=self.threader).start()
			
			#t.daemon = True
			#t.start()
			
		start = time.time()
		
		for worker in range(1, 100):
			self.q.put(worker)
		
		self.q.join()
		
	def ping(self):
		
		print("pinging")
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		
		ping = subprocess.check_output(["ping", "localhost", "-c 5"])

		top = Toplevel()
		top.title("Scanning results")
		top.minsize(300, 300)


		
		# put results in data
		data = ping

		label = Message(top, text="Data \n")
		label.pack()

		label = Message(top, text=data)
		label.pack()
		


	def ping_out(self):
		
		print("pinging")
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		addr = input("where to?")
		ping = subprocess.check_output(["ping", addr, "-c 5"])

		top = Toplevel()
		top.title("Scanning results")
		top.minsize(300, 300)
			
			# put results in data
		data = ping

		label = Message(top, text="Data \n")
		label.pack()

		label = Message(top, text=data)
		label.pack()


	def ifconfig(self):
		
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		res = subprocess.check_output(["ipconfig"])

		top = Toplevel()
		top.title("Results")
		top.minsize(300, 300)
		
		T = Text(top, height=10, width=100)
		scrollbar = Scrollbar(top)
		scrollbar.pack( side = RIGHT, fill = Y )
		T.pack(side=LEFT, fill=Y)
		scrollbar.config( command = T.yview )
		T.config(yscrollcommand=scrollbar.set)
			
			# put results in data
		data = res
		
		T.insert(END, data)

	def netstat(self):
		
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		res = subprocess.check_output(["netstat", "-r"])

		top = Toplevel()
		top.title("Results")
		top.minsize(600, 300)
		
		T = Text(top, height=30, width=100)
		scrollbar = Scrollbar(top)
		scrollbar.pack( side = RIGHT, fill = Y )
		T.pack(side=LEFT, fill=Y)
		scrollbar.config( command = T.yview )
		T.config(yscrollcommand=scrollbar.set)
		
		#label = Listbox(top, yscrollcommand = scrollbar.set )
			
			# put results in data
		data = res
		
		T.insert(END, data)
		
	def arp_cache(self):
		
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		res = subprocess.check_output(["arp", "-a"])

		top = Toplevel()
		top.title("Results")
		top.minsize(500, 100)

		
			

		# put results in data
		data = res
		label = Message(top, text="Data \n")
		label.pack()

		label = Text(top)
		label.pack()
		label.insert(END, data)


		scroll1y=Scrollbar(top, command=label.yview)
		scroll1y.pack(side=LEFT, fill=Y)


	def my_ip(self):
		
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		res = subprocess.check_output(["curl", "ifconfig.me"])

		top = Toplevel()
		top.title("Results")
		top.minsize(100, 100)

		
			

		# put results in data
		data = res
		label = Message(top, text="Data \n")
		label.pack()

		label = Text(top)
		label.pack()
		label.insert(END, data)


		scroll1y=Scrollbar(top, command=label.yview)
		scroll1y.pack(side=LEFT, fill=Y)


	def my_DNS(self):
		
		import subprocess
		#subprocess.check_output(['ls','-l']) #all that is technically needed...
		res = subprocess.check_output(["hostname"])

		top = Toplevel()
		top.title("Results")
		top.minsize(100, 100)

		
			

		# put results in data
		data = res
		label = Message(top, text="Data \n")
		label.pack()

		label = Text(top)
		label.pack()
		label.insert(END, data)


		scroll1y=Scrollbar(top, command=label.yview)
		scroll1y.pack(side=LEFT, fill=Y)
		
		
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

