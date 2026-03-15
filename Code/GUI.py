import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import os
import time
import random

from FIFO import run_fifo
# from LRU import run_lru
# from OPT import run_opt

class VMEApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Memory Management Simulator - Group 08")
        self.root.geometry("1000x650")
        self.root.configure(padx=20, pady=20)

        self.pages = []
        self.num_frames = tk.IntVar(value=3)
        self.algorithm = tk.StringVar(value="FIFO")
        self.history = []
        self.faults = 0
        
        self.setup_ui()

    def setup_ui(self):
        #Khung
        input_frame = tk.LabelFrame(self.root, text="Settings & Input", padx=10, pady=10)
        input_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(input_frame, text="Number of Frames:").grid(row=0, column=0, sticky=tk.W, pady=5)
        tk.Spinbox(input_frame, from_=1, to=50, textvariable=self.num_frames, width=5).grid(row=0, column=1, sticky=tk.W, pady=5)

        tk.Label(input_frame, text="Algorithm:").grid(row=0, column=2, sticky=tk.W, padx=(20, 5))
        ttk.Combobox(input_frame, textvariable=self.algorithm, values=["FIFO", "LRU", "OPT"], state="readonly", width=10).grid(row=0, column=3, sticky=tk.W)

        tk.Label(input_frame, text="Reference String (Pages):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_pages = tk.Entry(input_frame, width=60)
        self.entry_pages.insert(0, "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1")
        self.entry_pages.grid(row=1, column=1, columnspan=3, sticky=tk.W, pady=5)

        btn_frame = tk.Frame(input_frame)
        btn_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        tk.Button(btn_frame, text="Load from CSV", command=self.load_csv, bg="#f0ad4e", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Run Simulation", command=self.run_simulation, bg="#5cb85c", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Export Result", command=self.export_csv, bg="#5bc0de", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_data, bg="#d9534f", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Run Stress Test", command=self.run_stress_test, bg="#8a2be2", fg="white", width=15).pack(side=tk.LEFT, padx=5)
