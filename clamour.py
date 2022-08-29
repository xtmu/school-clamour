#!Scripts/python.exe
# -*- coding: utf-8 -*-

import schedule
import time
from os import system
from playsound import playsound
from plyer import notification

def clamour(text):

    print("最小换所有窗口")
    system(r'res\exe\Minimize.exe')


    print("弹窗")
    notification.notify(
        title = 'testing',
        message = text,
        app_icon = None,
        timeout = 10,
    )

    print("发声")
    # sound_path=r"res\wav\school_bell.wav"
    sound_path=r"res\wav\Westminster_Chime.wav"
    count=1
    while count:
        playsound(sound_path)
        count=count-1

timetable=(
    ("06:00","06:44","早餐"),
    ("06:45","07:34","晨读"),
    ("07:35","07:44","预备"),
    ("07:45","08:29","第一节"),
    ("08:40","09:24","第二节"),
    ("09:25","09:34","课间操"),
    ("09:50","10:34","第三节"),
    ("10:45","11:29","第四节"),
    ("11:40","12:24","第五节"),
    ("12:25","13:09","午餐"),
    ("13:10","14:24","午休"),
    ("14:30","14:34","预备"),
    ("14:35","15:19","第一节"),
    ("15:30","16:14","第二节"),
    ("16:30","17:14","第三节"),
    ("17:15","18:14","运动或游玩"),
    ("18:15","18:54","晚餐"),
    ("18:55","18:59","预备"),
    ("19:00","19:39","第一节"),
    ("19:50","20:29","第二节"),
    ("20:30","20:59","日记"),
    ("21:00","21:29","洗澡"),
    ("21:30","22:29","看书听书"),
    ("22:40","22:41","熄灯")
)

# print(len(timetable))
n=len(timetable)
for i in range(n):
    print(timetable[i])
    schedule.every().day.at(timetable[i][0]).do(clamour,text=timetable[i][2])
    schedule.every().day.at(timetable[i][1]).do(clamour,text=timetable[i][2]+" 结束")

while True:
    schedule.run_pending()
    time.sleep(1)
