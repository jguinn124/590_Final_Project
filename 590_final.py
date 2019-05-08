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

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Scanner GUI")
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
        
        self.arp_cache = tk.Button(self, text="ARP cache", fg="blue", command=self.arp_cache)
        self.arp_cache.pack()

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
        
        print("Scanning...")



        top = Toplevel()
        top.title("Scanning results")
        top.minsize(300, 300)


        
        # put results in data
        data = 5

        label = Message(top, text="Data \n")
        label.pack()

        label = Message(top, text=data)
        label.pack()
        
        

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()

                

        
    def arp_cache(self):
        
        print(" Arp stuff")
        import subprocess
        #subprocess.check_output(['ls','-l']) #all that is technically needed...
        
        ls = subprocess.check_output(['ls'])
        
        a = "\\"
        
        
        str(ls)
        
        ls.split(a)
        
        print(ls)
        
        
    
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()

