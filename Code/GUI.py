import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import os
import time
import random

from FIFO import run_fifo
from LRU import run_lru
from OPT import run_opt

class VMEApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Memory Management Simulator - Group 08")
        self.root.geometry("1050x650") 
        self.root.configure(padx=20, pady=20)

        self.pages = []
        self.num_frames = tk.IntVar(value=3)
        self.algorithm = tk.StringVar(value="FIFO") 
        self.history = []
        self.faults = 0
        
        self.setup_ui()

    def setup_ui(self):
        # Khung
        input_frame = tk.LabelFrame(self.root, text="Settings & Input", padx=10, pady=10)
        input_frame.pack(fill=tk.X, pady=(0, 10))

        # Nhóm Nút điều chỉnh Number of Frames 
        tk.Label(input_frame, text="Number of Frames:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        frame_control = tk.Frame(input_frame)
        frame_control.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Ô nhập số trang
        tk.Entry(frame_control, textvariable=self.num_frames, width=5, font=("Arial", 11, "bold"), justify="center").pack(side=tk.LEFT, padx=(0, 5))
        # Nút Tăng (➕) và Giảm (➖)
        tk.Button(frame_control, text="➕", command=self.increase_frames, width=3, bg="#e0e0e0").pack(side=tk.LEFT, padx=2)
        tk.Button(frame_control, text="➖", command=self.decrease_frames, width=3, bg="#e0e0e0").pack(side=tk.LEFT, padx=2)
      

        tk.Label(input_frame, text="Reference String (Pages):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_pages = tk.Entry(input_frame, width=70)
        self.entry_pages.insert(0, "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1")
        self.entry_pages.grid(row=1, column=1, columnspan=3, sticky=tk.W, pady=5)

        # Các Nút bấm 
        btn_frame = tk.Frame(input_frame)
        btn_frame.grid(row=2, column=0, columnspan=4, pady=15, sticky=tk.W)
        
        tk.Button(btn_frame, text="📁 Load CSV", command=self.load_csv, bg="#f0ad4e", fg="white", width=12).pack(side=tk.LEFT, padx=(0, 15))
        tk.Button(btn_frame, text=" Run FIFO", command=lambda: self.run_simulation("FIFO"), bg="#5cb85c", fg="white", width=12, font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text=" Run LRU", command=lambda: self.run_simulation("LRU"), bg="#428bca", fg="white", width=12, font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text=" Run OPT", command=lambda: self.run_simulation("OPT"), bg="#5bc0de", fg="white", width=12, font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=(3, 15))
        
        tk.Button(btn_frame, text=" Export Result", command=self.export_csv, bg="#6c757d", fg="white", width=13).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text=" Run Stress Test", command=self.run_stress_test, bg="#8a2be2", fg="white", width=15).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text="✖ Clear", command=self.clear_data, bg="#d9534f", fg="white", width=10).pack(side=tk.LEFT, padx=(15, 0))

        # Khung Hiển thị Kết quả & Đồ họa
        self.result_label = tk.Label(self.root, text="Total Page Faults: 0", font=("Arial", 14, "bold"), fg="red")
        self.result_label.pack(anchor=tk.W, pady=5)

        visual_frame = tk.LabelFrame(self.root, text="Virtual Memory Allocation Simulation", padx=10, pady=10)
        visual_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(visual_frame, bg="white")
        
        scroll_y = tk.Scrollbar(visual_frame, orient="vertical", command=self.canvas.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scroll_x = tk.Scrollbar(visual_frame, orient="horizontal", command=self.canvas.xview)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

    # HÀM XỬ LÝ NÚT TĂNG/GIẢM 
    def increase_frames(self):
        try:
            current = self.num_frames.get()
            if current < 50: # Giới hạn tối đa 50 frames
                self.num_frames.set(current + 1)
        except tk.TclError:
            self.num_frames.set(3) # Nếu người dùng lỡ nhập chữ rồi bấm nút, reset về 3

    def decrease_frames(self):
        try:
            current = self.num_frames.get()
            if current > 1: # Giới hạn tối thiểu 1 frame
                self.num_frames.set(current - 1)
        except tk.TclError:
            self.num_frames.set(3)
  

    def clear_data(self):
        self.entry_pages.delete(0, tk.END)
        self.num_frames.set(3)
        self.result_label.config(text="Total Page Faults: 0")
        self.canvas.delete("all")
        self.history = []
        self.faults = 0

    def run_stress_test(self):
        num_pages = 5000
        frames = 10
        messagebox.showinfo("Stress Test Info", f"Bắt đầu chạy Stress Test với {num_pages} trang ngẫu nhiên và {frames} frames.\nQuá trình này có thể mất vài giây, vui lòng chờ...")
        
        pages = [random.randint(0, 99) for _ in range(num_pages)]
        
        start_time = time.time()
        faults_fifo, _ = run_fifo(pages, frames) 
        time_fifo = (time.time() - start_time) * 1000
        
        start_time = time.time()
        faults_lru, _ = run_lru(pages, frames) 
        time_lru = (time.time() - start_time) * 1000
        
        start_time = time.time()
        faults_opt, _ = run_opt(pages, frames) 
        time_opt = (time.time() - start_time) * 1000
        
        report = f"--- STRESS & PERFORMANCE TEST RESULT ---\n"
        report += f"Total Pages Generated: {num_pages}\n"
        report += f"Number of Frames: {frames}\n\n"
        report += f"1. Thuật toán FIFO:\n   - Lỗi trang (Faults): {faults_fifo}\n   - Thời gian xử lý: {time_fifo:.2f} ms\n\n"
        report += f"2. Thuật toán LRU:\n   - Lỗi trang (Faults): {faults_lru}\n   - Thời gian xử lý: {time_lru:.2f} ms\n\n"
        report += f"3. Thuật toán OPT (Tối ưu nhất):\n   - Lỗi trang (Faults): {faults_opt}\n   - Thời gian xử lý: {time_opt:.2f} ms\n\n"
        report += "Kết luận:\n- OPT luôn cho số lỗi trang ít nhất, nhưng thời gian tính toán có thể lâu nhất (do phải duyệt tương lai).\n- FIFO và LRU chạy cực nhanh, rất phù hợp với thực tế phần cứng."
        
        messagebox.showinfo("Performance Test Result - Proof", report)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader, None)
                data = next(reader, None)
                if data:
                    self.num_frames.set(int(data[0]))
                    self.entry_pages.delete(0, tk.END)
                    self.entry_pages.insert(0, data[1])
            messagebox.showinfo("Success", "Loaded input from CSV successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

    def run_simulation(self, algo_name):
        try:
            pages_str = self.entry_pages.get()
            self.pages = [int(p.strip()) for p in pages_str.split(',') if p.strip().isdigit()]
            frames = self.num_frames.get()
            if not self.pages or frames <= 0:
                raise ValueError("Invalid input.")
        except Exception:
            messagebox.showerror("Input Error", "Please enter valid integers separated by commas.")
            return

        self.algorithm.set(algo_name)

        if algo_name == "FIFO":
            self.faults, self.history = run_fifo(self.pages, frames)
        elif algo_name == "LRU":
            self.faults, self.history = run_lru(self.pages, frames)
        elif algo_name == "OPT":
            self.faults, self.history = run_opt(self.pages, frames)

        self.result_label.config(text=f"Total Page Faults ({algo_name}): {self.faults}")
        self.draw_simulation()

    def draw_simulation(self):
        self.canvas.delete("all")
        frames = self.num_frames.get()
        cell_w, cell_h = 40, 40
        start_x, start_y = 80, 50 

        canvas_width = start_x + len(self.pages) * cell_w + 50
        canvas_height = start_y + (frames + 3) * cell_h + 50
        self.canvas.configure(scrollregion=(0, 0, canvas_width, canvas_height))

        self.canvas.create_text(start_x - 10, start_y - 20, text="Pages", font=("Arial", 10, "bold", "italic"), anchor=tk.E)
        for f in range(frames):
            y = start_y + f * cell_h
            self.canvas.create_text(start_x - 10, y + cell_h/2, text=f"Frame {f+1}", font=("Arial", 10, "bold"), anchor=tk.E)

        for i, p in enumerate(self.pages):
            x = start_x + i * cell_w
            self.canvas.create_text(x + cell_w/2, start_y - 20, text=str(p), font=("Arial", 12, "bold"))

        for step_idx, step_data in enumerate(self.history):
            page, memory_state, is_fault = step_data
            x = start_x + step_idx * cell_w
            
            for f in range(frames):
                y = start_y + f * cell_h
                self.canvas.create_rectangle(x, y, x + cell_w, y + cell_h, outline="black")
                
                if f < len(memory_state):
                    self.canvas.create_text(x + cell_w/2, y + cell_h/2, text=str(memory_state[f]), font=("Arial", 11))

            if is_fault:
                y_fault = start_y + frames * cell_h + 10
                self.canvas.create_text(x + cell_w/2, y_fault + 10, text="F", fill="red", font=("Arial", 12, "bold"))

    def export_csv(self):
        if not hasattr(self, 'history') or not self.history:
            messagebox.showwarning("Warning", "Please run the simulation first!")
            return

        if not os.path.exists("output"):
            os.makedirs("output")
        output_file = f"output/result_{self.algorithm.get()}.csv"
        
        try:
            with open(output_file, 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["Algorithm Run", self.algorithm.get()])
                writer.writerow(["Total Frames", self.num_frames.get()])
                writer.writerow(["Total Page Faults", self.faults])
                writer.writerow([]) 
                
                header = ["Step", "Page Accessed"] + [f"Frame {i+1}" for i in range(self.num_frames.get())] + ["Page Fault"]
                writer.writerow(header)
                
                for i, (page, mem_state, is_fault) in enumerate(self.history):
                    row = [i+1, page]
                    for f in range(self.num_frames.get()):
                        if f < len(mem_state):
                            row.append(mem_state[f])
                        else:
                            row.append("-")
                    row.append("Yes" if is_fault else "No")
                    writer.writerow(row)
                    
            messagebox.showinfo("Success", f"Detailed results and Total Faults exported to {output_file}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export CSV: {e}")