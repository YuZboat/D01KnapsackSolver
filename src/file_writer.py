import pandas as pd

def save_result_to_txt(path, best_value, cost_time, selected):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"最优价值：{best_value}\n")
        f.write(f"求解时间：{cost_time:.4f}s\n\n")
        f.write("选择详情（项集编号, 物品）：\n")
        for idx, item in selected:
            f.write(f"{idx} : {item}\n")

def save_result_to_excel(path, best_value, cost_time):
    df = pd.DataFrame({
        "最优价值": [best_value],
        "求解时间(s)": [round(cost_time, 4)]
    })
    df.to_excel(path, index=False)