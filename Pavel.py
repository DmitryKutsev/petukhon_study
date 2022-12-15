from datetime import datetime

with open('log.txt', 'a', encoding='utf-8') as the_log_file:
    now = str(datetime.now())
    the_log_file.write("\n" + now[:19] + " " + input())




