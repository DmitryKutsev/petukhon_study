import datetime

def date_and_time_now():
    """Returns the current date and time"""
    now = datetime.datetime.now()
    with open('log.txt', 'w', encoding='utf-8') as my_file:
        str_now = str(now)
        my_file.write("Текущая дата и время записи в лог ")
        my_file.write(str_now)
    return


date_and_time_now()