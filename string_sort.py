def avg_ascii_weight(s):
    total_weight = 0
    for c in s:
        total_weight += ord(c)
    return total_weight/len(s) if len(s) > 0 else 0

def std_dev_ascii_weight(s):
    if len(s) == 0:
        return 0
    avg_weight = avg_ascii_weight(s)
    variance_sum = 0
    for c in s:
        variance_sum += (ord(c) - avg_weight)
    return (variance_sum/len(s))

def dev_between_avg_and_max_triplet(s):
    if len(s) < 3:
        return float('-inf')
    total_weight = sum(ord(c) for c in s)
    avg_weight = total_weight/len(s)

    max_triplet_avg = float('-inf')
    for i in range (len(s) - 2):
        triplet_avg = (ord(s[i]) + ord(s[i+1]) + ord(s[i+2])) / 3
        if triplet_avg > max_triplet_avg:
            max_triplet_avg = triplet_avg

        return (avg_weight - max_triplet_avg) ** 2

def count_mirror_triplets(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            count += 1
    return count

# Функция для сортировки по всем четырем критериям по отдельности
def sort_strings_individually(strings):
    # Копируем оригинальные строки для отслеживания изменений на каждом этапе
    stage_1 = sorted(strings, key=avg_ascii_weight)  # По среднему весу ASCII-кодов
    stage_2 = sorted(stage_1, key=std_dev_ascii_weight)  # По квадратичному отклонению среднего веса
    stage_3 = sorted(stage_2, key=dev_between_avg_and_max_triplet)  # По квадратичному отклонению между средним и максимальной тройкой
    stage_4 = sorted(stage_3, key=count_mirror_triplets)  # По количеству зеркальных троек

    return {
        "stage_1_avg_ascii": stage_1,
        "stage_2_std_dev": stage_2,
        "stage_3_triplet_dev": stage_3,
        "stage_4_mirror_triplets": stage_4
    }

strings = ["abc", "ada","mnop", "aabcc", "aabaa", "xyz"]

sorted_stages = sort_strings_individually(strings)
print(sorted_stages["stage_1_avg_ascii"])
print(sorted_stages["stage_2_std_dev"])
print(sorted_stages["stage_3_triplet_dev"])
print(sorted_stages["stage_4_mirror_triplets"])