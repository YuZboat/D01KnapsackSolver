import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import tkinter.font as tkfont
import time
import os
from src.data_loader import load_d01kp_data
from src.solver import solve_d01kp_dp
from src.plot_utils import draw_weight_value_scatter
from src.sort_utils import sort_by_third_ratio
from src.file_writer import save_result_to_txt, save_result_to_excel

# 修复中文
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(family="SimHei", size=10)

class D01KPSolverUI:
    def __init__(self, root):
        self.root = root
        self.root.title("D01KP Knapsack Solver")
        self.root.geometry("500x350")

        self.data = []
        self.best_val = 0
        self.selected = []
        self.cost_time = 0

        ttk.Button(root, text="Load Data", command=self.load_data).pack(pady=5)
        ttk.Button(root, text="Draw Scatter Plot", command=self.draw_plot).pack(pady=5)
        ttk.Button(root, text="Sort by Ratio", command=self.do_sort).pack(pady=5)
        ttk.Button(root, text="Solve DP", command=self.solve).pack(pady=5)
        ttk.Button(root, text="Save Result", command=self.save).pack(pady=5)

    def load_data(self):
        path = filedialog.askopenfilename(filetypes=[("TXT", "*.txt")])
        if not path:
            return
        self.data = load_d01kp_data(path)
        messagebox.showinfo("Success", f"Loaded {len(self.data)} item sets")

    def draw_plot(self):
        if not self.data:
            messagebox.showwarning("Warning", "Please load data first")
            return
        draw_weight_value_scatter(self.data)

    def do_sort(self):
        if not self.data:
            messagebox.showwarning("Warning", "Please load data first")
            return
        self.data = sort_by_third_ratio(self.data)
        messagebox.showinfo("Success", "Sorted by ratio")

    def solve(self):
        if not self.data:
            messagebox.showwarning("Warning", "Please load data first")
            return
        max_w = 500  # 非常重要！！！
        t0 = time.time()
        self.best_val, self.selected = solve_d01kp_dp(self.data, max_w)
        t1 = time.time()
        self.cost_time = t1 - t0
        messagebox.showinfo("Done", f"Best Value: {self.best_val}\nTime: {self.cost_time:.4f}s")

    def save(self):
        if self.best_val == 0:
            messagebox.showwarning("Warning", "Please solve first")
            return
        os.makedirs("results", exist_ok=True)
        save_result_to_txt("results/result.txt", self.best_val, self.cost_time, self.selected)
        save_result_to_excel("results/result.xlsx", self.best_val, self.cost_time)
        messagebox.showinfo("Success", "Result saved to results folder")