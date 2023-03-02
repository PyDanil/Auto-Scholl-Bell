from datetime import datetime
import time
import RPi.GPIO as GPIO

led1 = 21      # Номер пина
time_bzzz = 3      # Время подачи звонков

GPIO.setmode(GPIO.BCM)      # BCM - по GPIO,   BOARD - по номеру пина
GPIO.setup(led1, GPIO.OUT)

GPIO.output(led1, True)      # ON
time.sleep(2)
GPIO.output(led1, False)      # OFF

print("Обычное расписание")

while True:
    current_datetime = datetime.now()
    day_week = datetime.today().isoweekday()

    if day_week == 1:      # Понедельник

        if current_datetime.hour == 8 and current_datetime.minute == 15:
            print("Начался 0 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 8 and current_datetime.minute == 45:
            print("Конец 0 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 8 and current_datetime.minute == 55:
            print("Начался 1 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 9 and current_datetime.minute == 35:
            print("Конец 1 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 9 and current_datetime.minute == 45:
            print("Начался 2 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 10 and current_datetime.minute == 25:
            print("Конец 2 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 10 and current_datetime.minute == 40:
            print("Начался 3 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 11 and current_datetime.minute == 20:
            print("Конец 3 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 11 and current_datetime.minute == 35:
            print("Начался 4 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 12 and current_datetime.minute == 15:
            print("Конец 4 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 12 and current_datetime.minute == 30:
            print("Начался 5 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 13 and current_datetime.minute == 10:
            print("Конец 5 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 13 and current_datetime.minute == 20:
            print("Начался 6 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 14 and current_datetime.minute == 0:
            print("Конец 6 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 14 and current_datetime.minute == 10:
            print("Начался 7 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 14 and current_datetime.minute == 50:
            print("Конец 7 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 15 and current_datetime.minute == 0:
            print("Начался 8 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 15 and current_datetime.minute == 40:
            print("Конец 8 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 15 and current_datetime.minute == 45:
            print("Начался 9 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 16 and current_datetime.minute == 25:
            print("Конец 9 урок. Время: ", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            print("Понедельник конец.")
            time.sleep(70)



    if day_week == 2 or day_week == 3 or day_week == 4 or day_week == 5:      # Вторник-Пятница

        if current_datetime.hour == 8 and current_datetime.minute == 15:
            print("Начался 1 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 8 and current_datetime.minute == 55:
            print("Конец 1 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 9 and current_datetime.minute == 5:
            print("Начался 2 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 9 and current_datetime.minute == 45:
            print("Конец 2 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 10 and current_datetime.minute == 0:
            print("Начался 3 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 10 and current_datetime.minute == 40:
            print("Конец 3 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 10 and current_datetime.minute == 55:
            print("Начался 4 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 11 and current_datetime.minute == 35:
            print("Конец 4 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 11 and current_datetime.minute == 50:
            print("Начался 5 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 12 and current_datetime.minute == 30:
            print("Конец 5 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 12 and current_datetime.minute == 45:
            print("Начался 6 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 13 and current_datetime.minute == 25:
            print("Конец 6 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 13 and current_datetime.minute == 35:
            print("Начался 7 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 14 and current_datetime.minute == 15:
            print("Конец 7 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 14 and current_datetime.minute == 25:
            print("Начался 8 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 15 and current_datetime.minute == 5:
            print("Конец 8 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 15 and current_datetime.minute == 15:
            print("Начался 9 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 15 and current_datetime.minute == 55:
            print("Конец 9 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)



    if day_week == 6:      # Суббота

        if current_datetime.hour == 8 and current_datetime.minute == 0:
            print("Начался 1 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 8 and current_datetime.minute == 40:
            print("Конец 1 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 8 and current_datetime.minute == 50:
            print("Начался 2 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 9 and current_datetime.minute == 30:
            print("Конец 2 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 9 and current_datetime.minute == 40:
            print("Начался 3 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 10 and current_datetime.minute == 20:
            print("Конец 3 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 10 and current_datetime.minute == 30:
            print("Начался 4 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 11 and current_datetime.minute == 10:
            print("Конец 4 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 11 and current_datetime.minute == 20:
            print("Начался 5 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 12 and current_datetime.minute == 0:
            print("Конец 5 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)

        if current_datetime.hour == 12 and current_datetime.minute == 10:
            print("Начался 6 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
        if current_datetime.hour == 12 and current_datetime.minute == 50:
            print("Конец 6 урок. Время:", current_datetime)
            GPIO.output(led1, True)
            time.sleep(time_bzzz)
            GPIO.output(led1, False)
            time.sleep(70)
            
