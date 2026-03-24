def sort_by_third_ratio(item_sets):
    def ratio(s):
        w = s[4]
        v = s[5]
        return v / w if w != 0 else 0
    return sorted(item_sets, key=ratio, reverse=True)