def load_d01kp_data(file_path):
    item_sets = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    numbers = []
    for line in lines:
        line = line.strip()
        # 过滤注释、空行、标题行（只保留看起来像数据的行）
        if not line or line.startswith(('*', 'IDKP', 'The dimension', 'The profit', 'The weight', 'dim', 'pro', 'wei')):
            continue
        # 把所有非数字/负号/空格的字符都去掉
        cleaned = ''.join([c if c in '0123456789- ' else ' ' for c in line])
        # 分割成 token
        tokens = cleaned.split()
        for t in tokens:
            try:
                num = int(t)
                numbers.append(num)
            except ValueError:
                continue

    # 每 6 个数字组成一组（w1 v1 w2 v2 w3 v3）
    for i in range(0, len(numbers) - 5, 6):
        w1 = numbers[i]
        v1 = numbers[i+1]
        w2 = numbers[i+2]
        v2 = numbers[i+3]
        w3 = numbers[i+4]
        v3 = numbers[i+5]
        item_sets.append((w1, v1, w2, v2, w3, v3))

    return item_sets