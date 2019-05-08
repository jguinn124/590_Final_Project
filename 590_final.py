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
        master.title("Easy Network Utility")
        master.geometry("300x300")
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Documentation"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        

        
        self.p_scan = tk.Button(self, text="Scan Local Ports", fg="blue", command=self.p_scan)
        self.p_scan.pack()

        self.p_scan = tk.Button(self, text="Scan External Ports", fg="blue", command=self.p_scan)
        self.p_scan.pack()
        
        self.ping = tk.Button(self, text="Ping local", fg="blue", command=self.ping)
        self.ping.pack()

        self.ping_button = tk.Button(self, text="Ping out", fg="blue", command=self.ping_out)
        self.ping_button.pack()

        self.ifcon_button = tk.Button(self, text="Network Configuration", fg="blue", command=self.ifconfig)
        self.ifcon_button.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        top = Toplevel()
        top.title("Scanning results")
        top.minsize(300, 300)
            
            # put results in data
        data = """ Blah Blah dont use this application to attack servers that you have no authourity over.
            """

        label = Message(top, text="Documentation")
        label.pack()

        label = Message(top, text=data)
        label.pack()


        

    def scan_window(seft):
        top = Toplevel()
        top.title("About this application...")

        msg = Message(top, text=about_message)
        msg.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()
        
    
    def p_scan(self):

        print_lock = threading.Lock()
        remoteServer    = "localhost"
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
        
        print("pinging")
        import subprocess
        #subprocess.check_output(['ls','-l']) #all that is technically needed...
        res = subprocess.check_output(["ifconfig"])

        top = Toplevel()
        top.title("Scanning results")
        top.minsize(300, 300)
            
            # put results in data
        data = res

        label = Message(top, text="Data \n")
        label.pack()

        label = Message(top, text=data)
        label.pack()
            
        
    
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()

