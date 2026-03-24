import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import time
import os
from src.data_loader import load_d01kp_data
from src.solver import solve_d01kp_dp
from src.plot_utils import draw_weight_value_scatter
from src.sort_utils import sort_by_third_ratio
from src.file_writer import save_result_to_txt, save_result_to_excel

class D01KPSolverUI:
    def __init__(self, root):
        self.root = root
        self.root.title("D{0-1}KP 背包求解器")
        self.root.geometry("500x350")

        self.data = []
        self.best_val = 0
        self.selected = []
        self.cost_time = 0

        ttk.Button(root, text="1. 读取数据文件", command=self.load_data).pack(pady=5)
        ttk.Button(root, text="2. 绘制重量-价值散点图", command=self.draw_plot).pack(pady=5)
        ttk.Button(root, text="3. 按第三项价值/重量比降序排序", command=self.do_sort).pack(pady=5)
        ttk.Button(root, text="4. 动态规划求最优解", command=self.solve).pack(pady=5)
        ttk.Button(root, text="5. 保存结果 TXT + Excel", command=self.save).pack(pady=5)

    def load_data(self):
        path = filedialog.askopenfilename(filetypes=[("TXT", "*.txt")])
        if not path:
            return
        self.data = load_d01kp_data(path)
        messagebox.showinfo("成功", f"已加载 {len(self.data)} 个项集")

    def draw_plot(self):
        if not self.data:
            messagebox.showwarning("提示", "请先加载数据")
            return
        draw_weight_value_scatter(self.data)

    def do_sort(self):
        if not self.data:
            messagebox.showwarning("提示", "请先加载数据")
            return
        self.data = sort_by_third_ratio(self.data)
        messagebox.showinfo("完成", "已按第三项价值/重量比降序排序")

    def solve(self):
        if not self.data:
            messagebox.showwarning("提示", "请先加载数据")
            return
        max_w = 300
        t0 = time.time()
        self.best_val, self.selected = solve_d01kp_dp(self.data, max_w)
        t1 = time.time()
        self.cost_time = t1 - t0
        messagebox.showinfo("求解完成", f"最优价值：{self.best_val}\n耗时：{self.cost_time:.4f}s")

    def save(self):
        if self.best_val == 0:
            messagebox.showwarning("提示", "请先求解")
            return
        os.makedirs("results", exist_ok=True)
        save_result_to_txt("results/result.txt", self.best_val, self.cost_time, self.selected)
        save_result_to_excel("results/result.xlsx", self.best_val, self.cost_time)
        messagebox.showinfo("成功", "结果已保存到 results 文件夹")