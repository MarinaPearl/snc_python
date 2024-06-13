import np as np


def pearson_correlation(x, y):
    n = len(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    numerator = 0
    denominator_x = 0
    denominator_y = 0

    for i in range(n):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        denominator_x += (x[i] - mean_x) ** 2
        denominator_y += (y[i] - mean_y) ** 2

    denominator = np.sqrt(denominator_x * denominator_y)

    correlation = numerator / denominator

    return correlation


def half_match(coord1, coord2):
    n = len(coord1)
    match_count = 0

    for i in range(n):
        if coord1[i] == coord2[i]:
            match_count += 1

    if match_count >= n / 2:
        return True
    else:
        return False


def check_intersection(set1, set2):
    intersection = set1.intersection(set2)
    intersection_ratio = len(intersection) / min(len(set1), len(set2))

    if intersection_ratio > 0.2:
        return True
    else:
        return False
