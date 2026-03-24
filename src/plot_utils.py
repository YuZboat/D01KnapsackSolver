import matplotlib.pyplot as plt

# 解决中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False

def draw_weight_value_scatter(item_sets):
    weights = []
    values = []
    for s in item_sets:
        weights.append(s[0])
        values.append(s[1])
        weights.append(s[2])
        values.append(s[3])
        weights.append(s[4])
        values.append(s[5])

    plt.scatter(weights, values, s=10, color='blue')
    plt.xlabel('Weight')
    plt.ylabel('Value')
    plt.title('D01KP Weight-Value Scatter Plot')
    plt.grid(alpha=0.3)
    plt.show()