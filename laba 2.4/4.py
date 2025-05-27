from datetime import datetime
input_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
def format_date(input_date):
    date_obj = datetime.strptime(input_date, "%d.%m.%Y")
    formatted_date = date_obj.strftime("%A, %d %B, %Y год")
    weekdays = {
        'Monday': 'Понедельник',
        'Tuesday': 'Вторник',
        'Wednesday': 'Среда',
        'Thursday': 'Четверг',
        'Friday': 'Пятница',
        'Saturday': 'Суббота',
        'Sunday': 'Воскресенье'
    }
    months = {
        'January': 'Января',
        'February': 'Февраля',
        'March': 'Марта',
        'April': 'Апреля',
        'May': 'Мая',
        'June': 'Июня',
        'July': 'Июля',
        'August': 'Августа',
        'September': 'Сентября',
        'October': 'Октября',
        'November': 'Ноября',
        'December': 'Декабря'
    }
    for english, russian in weekdays.items():
        formatted_date = formatted_date.replace(english, russian)
    for english, russian in months.items():
        formatted_date = formatted_date.replace(english, russian)
    return formatted_date
output = format_date(input_date)
print(output)
