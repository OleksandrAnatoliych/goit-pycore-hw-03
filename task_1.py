from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка у формат дати
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримання поточної дати
        today_date = datetime.today().date()
        
        # Розрахунок різниці у днях
        delta_days = (given_date - today_date).days
        
        return delta_days
    except ValueError:
        return "Неправильний формат дати! Використовуйте 'РРРР-ММ-ДД'."

print(get_days_from_today("2021-10-09"))  # Наприклад, якщо сьогодні 5 травня 2021 року, має вивести -157
print(get_days_from_today("2023-05-01"))  # Тест для іншої дати
print(get_days_from_today("incorrect-date"))  # Тест на некоректні дані
