import matplotlib.pyplot as plt

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
    plt.xlabel('重量')
    plt.ylabel('价值')
    plt.title('D01KP 重量-价值散点图')
    plt.grid(alpha=0.3)
    plt.show()