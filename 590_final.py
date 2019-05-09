# -*- coding: utf-8 -*-
"""
John Guinn
Devin Colbert

Network Utility App
"""
from tkinter import *
import tkinter as tk
import time
import threading
from queue import Queue
import socket

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Network Utility")
        master.geometry("300x300")
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Documentation"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack()


        
        self.E1 = Entry(self, bd =5)
        self.E1.pack(side = "top")

        print(self.E1.get())
        

        


        self.p_scan = tk.Button(self, text="Scan Ports", fg="blue", command=self.p_scan)
        self.p_scan.pack()
        
        self.ping = tk.Button(self, text="Ping", fg="blue", command=self.ping)
        self.ping.pack()


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

        print_lock = threading.Lock()
        remoteServer    = self.E1.get()
        remoteServerIP  = socket.gethostbyname(remoteServer)


        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port", format(port))
                open_port = port
            sock.close()



        
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

                

        
    def ping(self):
        
        print("pinging")
        import subprocess
        #subprocess.check_output(['ls','-l']) #all that is technically needed...
        
        ping = subprocess.check_output(["ping", self.E1.get(), "-c 5"])

        top = Toplevel()
        top.title("Ping results")
        top.minsize(500, 300)


        print(self.E1.get())


        
        # put results in data
        data = ping

        label = Message(top, text="Data \n")
        label.pack()

        label = Message(top, text=data)
        label.pack()
        





    def ifconfig(self):
        
        import subprocess
        #subprocess.check_output(['ls','-l']) #all that is technically needed...
        res = subprocess.check_output(["ifconfig", "-a"])

        top = Toplevel()
        top.title("Results")
        top.minsize(300, 300)

        
            

        # put results in data
        data = res
        label = Message(top, text="Data \n")
        label.pack()

        label = Text(top)
        label.pack()
        label.insert(END, data)


        scroll1y=Scrollbar(top, command=label.yview)
        scroll1y.pack(side=LEFT, fill=Y)

    def netstat(self):
        
        import subprocess
        #subprocess.check_output(['ls','-l']) #all that is technically needed...
        res = subprocess.check_output(["netstat", "-r"])

        top = Toplevel()
        top.title("Network Results")
        top.minsize(600, 300)


            

        # put results in data
        data = res

        label = Message(top, text="Data \n")
        label.pack()

        label = Text(top)
        label.pack()
        label.insert(END, data)

        scroll1y=Scrollbar(top, command=label.yview)
        scroll1y.pack(side=LEFT, fill=Y)

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
        
    
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()

