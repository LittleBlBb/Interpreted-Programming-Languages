def calculate_distance(k, pos1, pos2):
    """Вычисляет минимальное расстояние по кольцевой дороге."""
    return min(abs(pos1 - pos2), k - abs(pos1 - pos2))


def calculate_cost(stations, v, k, pos):
    """Вычисляет общие затраты при размещении бензохранилища на станции pos."""
    total_cost = 0
    for station_pos, fuel_amount in stations:
        trips = (fuel_amount + v - 1) // v  # Количество поездок бензовоза
        distance = calculate_distance(k, pos, station_pos)
        total_cost += distance * trips  # Умножаем расстояние на количество рейсов
    return total_cost


def find_optimal_station(k, v, stations):
    """Находит оптимальную станцию для размещения бензохранилища на основе медианы."""
    # Сортируем станции по их позиции на кольце
    stations.sort()

    # Ищем медианную позицию (она минимизирует общие затраты)
    median_station_pos = stations[len(stations) // 2][0]

    # Вычисляем затраты для медианной станции и её ближайших соседей (если они есть)
    min_cost = calculate_cost(stations, v, k, median_station_pos)
    optimal_pos = median_station_pos

    # Проверка соседних позиций медианы для возможного улучшения
    if len(stations) > 1:
        left_neighbor = stations[len(stations) // 2 - 1][0]
        right_neighbor = stations[(len(stations) // 2 + 1) % len(stations)][0]

        left_cost = calculate_cost(stations, v, k, left_neighbor)
        right_cost = calculate_cost(stations, v, k, right_neighbor)

        # Обновляем минимальную стоимость и оптимальную позицию, если соседи дают меньше
        if left_cost < min_cost:
            min_cost = left_cost
            optimal_pos = left_neighbor
        if right_cost < min_cost:
            min_cost = right_cost
            optimal_pos = right_neighbor

    return optimal_pos, min_cost


# Чтение данных из файла
with open('27-123b.txt', 'r') as f:
    n, k, v = map(int, f.readline().split())
    stations = []
    for line in f:
        pos, fuel = map(int, line.split())
        stations.append((pos, fuel))

# Вычисление оптимальной станции и минимальных затрат
optimal_station, min_cost = find_optimal_station(k, v, stations)
print(f"Оптимальная станция: {optimal_station}, минимальные затраты: {min_cost}")
