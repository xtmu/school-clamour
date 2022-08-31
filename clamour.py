#!Scripts/python.exe
# -*- coding: utf-8 -*-

import schedule
import time
import screen
import user_input
from os import system
from playsound import playsound
from plyer import notification


def clamour(text, start_flag=True):
    if start_flag:
        # 上课
        print("亮屏")
        screen.screen_on()
        user_input.screen_type()

        print("弹窗")
        notification.notify(
            title='testing',
            message=text,
            app_icon=None,
            timeout=10,
        )

        print("发声")
        # sound_path = r"res\wav\school_bell.wav"
        sound_path = r"res\wav\Westminster_Chime.wav"
        count = 5
        while count:
            playsound(sound_path)
            count = count - 1

    else:
        # 下课
        print("弹窗")
        text = text + " 结束"
        notification.notify(
            title='testing',
            message=text,
            app_icon=None,
            timeout=10,
        )

        print("发声")
        # sound_path=r"res\wav\school_bell.wav"
        sound_path = r"res\wav\XiaKeLingSheng.wav"
        count = 2
        while count:
            playsound(sound_path)
            count = count - 1

        print("熄屏")
        user_input.win_d()
        screen.screen_off_lock()


# timetable = (
#     ("20:55", "22:36", "早餐"),
#     ("22:37", "22:38", "晚餐")
# )

timetable = (
    ("06:00", "06:44", "早餐"),
    ("06:45", "07:34", "晨读"),
    ("07:35", "07:35", "预备"),
    ("07:45", "08:29", "第一节"),
    ("08:40", "09:24", "第二节"),
    ("09:25", "09:34", "课间操"),
    ("09:50", "10:34", "第三节"),
    ("10:45", "11:29", "第四节"),
    ("11:40", "12:24", "第五节"),
    ("12:25", "13:09", "午餐"),
    ("13:10", "14:24", "午休"),
    ("14:30", "14:34", "预备"),
    ("14:35", "15:19", "第一节"),
    ("15:30", "16:14", "第二节"),
    ("16:30", "17:14", "第三节"),
    ("17:15", "18:14", "运动或游玩"),
    ("18:15", "18:54", "晚餐"),
    ("18:55", "18:59", "预备"),
    ("19:00", "19:39", "第一节"),
    ("19:50", "20:29", "第二节"),
    ("20:30", "20:59", "日记"),
    ("20:45", "20:45", "保存你的工作，即将关机"),
    ("21:00", "21:29", "洗澡"),
    ("21:30", "22:30", "看书听书"),
    ("22:40", "22:40", "熄灯")
)

# print(len(timetable))
n = len(timetable)
for i in range(n):
    print(timetable[i])
    if timetable[i][0]!=timetable[i][1]:
        schedule.every().day.at(timetable[i][0]).do(clamour, text=timetable[i][2])
        schedule.every().day.at(timetable[i][1]).do(clamour, text=timetable[i][2], start_flag=False)
    else:
        schedule.every().day.at(timetable[i][0]).do(clamour, text=timetable[i][2])

while True:
    schedule.run_pending()
    time.sleep(1)
