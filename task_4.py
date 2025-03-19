from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Оновлюємо рік народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Обчислюємо різницю в днях
        days_difference = (birthday_this_year - today).days
        
        # Якщо день народження у межах 7 днів
        if 0 <= days_difference <= 7:
            # Якщо день народження випадає на вихідні, переносимо на понеділок
            if birthday_this_year.weekday() in [5, 6]:  # 5 - субота, 6 - неділя
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Приклад вхідних даних
users = [
    {"name": "Джон Доу", "birthday": "1985.01.23"},
    {"name": "Джейн Сміт", "birthday": "1990.01.27"},
    {"name": "Олександр Іванов", "birthday": "1992.01.28"}
]

# Виклик функції
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цей тиждень:", upcoming_birthdays)
