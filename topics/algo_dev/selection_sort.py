def _find_min(data):
    idx_min = 0
    for i, val in enumerate(data):
        if data[idx_min] > val:
            idx_min = i
    return idx_min


def selection_sort(data):
    idx_min = 0
    for swap_idx in range(len(data) - 1):
        idx_min = swap_idx
        for j in range(swap_idx, len(data)):
            if data[j] < data[idx_min]:
                idx_min = j
        temp_value = data[swap_idx]
        data[swap_idx] = data[idx_min]
        data[idx_min] = temp_value
    return data


g_raw = [2, 4, 1, 10, 8, 5, 3]
g = g_raw
print(g)

# sorting algorithm:
for idx in range(len(g) - 1):
    print(f"Step number {idx}. searching min in [{g[idx+1:]}]")
    min_idx = idx + 1 + _find_min(g[idx + 1 :])
    print(f"min index {min_idx}, min_value {g[min_idx]}")
    if g[min_idx] < g[idx]:
        temp_val = g[idx]
        g[idx] = g[min_idx]
        g[min_idx] = temp_val

print(g)
print(selection_sort(g_raw))
