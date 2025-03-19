import random

def get_numbers_ticket(min_num, max_num, quantity):
    """
    Генерує відсортований список унікальних випадкових чисел у заданому діапазоні.
    
    :param min_num: Мінімальне можливе число в наборі (не менше 1).
    :param max_num: Максимальне можливе число в наборі (не більше 1000).
    :param quantity: Кількість чисел, які потрібно вибрати.
    :return: Відсортований список унікальних випадкових чисел або пустий список при некоректних параметрах.
    """
    # Перевірка на валідність вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000) or not (min_num <= quantity <= max_num):
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    
    # Повернення відсортованого списку чисел
    return sorted(numbers)

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
