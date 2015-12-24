# Min/Max Rescaler Coding Quiz

def featureScaling(arr):
    min_value = min(arr)
    max_value = max(arr)
    max_min_diff = float(max_value - min_value)
    return [((item -  min_value) / max_min_diff) for item in arr]
