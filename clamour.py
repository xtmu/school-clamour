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
        # user_input.screen_type()

        print("弹窗")
        notification.notify(
            title='start',
            message=text,
            app_icon=None,
            timeout=300,
        )

        print("发声")
        # sound_path = r"res\wav\school_bell.wav"
        sound_path = r"res\wav\Westminster_Chime.wav"
        count = 1
        while count:
            playsound(sound_path)
            count = count - 1

    else:
        # 下课
        print("弹窗")
        text = text + " 结束"
        notification.notify(
            title='end',
            message=text,
            app_icon=None,
            timeout=30,
        )

        print("发声")
        # sound_path=r"res\wav\school_bell.wav"
        # sound_path = r"res\wav\XiaKeLingSheng.wav"
        # sound_path = r"res\wav\himitsukoigokoro_ins.wav"
        sound_path = r"res\wav\kawaii.wav"
        count = 1
        while count:
            playsound(sound_path,False)
            count = count - 1
        time.sleep(60)

        print("熄屏")
        user_input.win_d()
        # 熄屏持续时间
        loop=180
        while loop:
            screen.screen_off_lock()
            time.sleep(1)
            loop=loop-1


# timetable = (
#     ("20:55", "22:36", "早餐"),
#     ("22:37", "22:38", "晚餐")
# )

timetable = (
    ("06:00", "06:45", "早餐"),
    ("06:45", "07:35", "晨读"),
    ("07:35", "07:35", "预备"),
    ("07:45", "08:30", "第一节"),
    ("08:40", "09:25", "第二节"),
    ("09:50", "10:35", "第三节"),
    ("10:45", "11:30", "第四节"),
    ("11:40", "12:25", "第五节"),
    ("12:26", "13:10", "午餐"),
    ("13:10", "13:10", "午休"),
    # ("13:10", "14:25", "午休"),
    ("14:30", "14:35", "预备"),
    ("14:35", "15:20", "第一节"),
    ("15:30", "16:15", "第二节"),
    ("16:30", "18:15", "第三节"),
    # ("17:16", "18:15", "运动或游玩"),
    ("18:15", "18:55", "晚餐"),
    ("18:55", "19:00", "预备"),
    ("19:00", "19:40", "第一节"),
    ("19:50", "20:30", "第二节"),
    ("20:30", "20:30", "即将关机!请完成并保存日记!"),
    ("20:34", "20:34", "即将关机!请完成并保存日记!"),
    ("20:39", "20:39", "即将关机!请完成并保存日记!"),
    # ("20:45", "20:45", "保存你的工作，即将关机"),
    # ("21:00", "21:29", "洗澡"),
    # ("21:30", "22:30", "看书听书"),
    # ("22:40", "22:40", "熄灯")
)

# print(len(timetable))
n = len(timetable)
for i in range(n):
    print(timetable[i])
    if timetable[i][0]==timetable[i][1]:
        # 提醒
        schedule.every().day.at(timetable[i][0]).do(clamour, text=timetable[i][2])
    else:
        # 上下课
        schedule.every().day.at(timetable[i][0]).do(clamour, text=timetable[i][2])
        if i==n-1:
            schedule.every().day.at(timetable[i][1]).do(clamour, text=timetable[i][2], start_flag=False)
        else:
            if timetable[i][1]==timetable[i+1][0]:
                # 紧接任务时不播放结束
                continue
            schedule.every().day.at(timetable[i][1]).do(clamour, text=timetable[i][2], start_flag=False)

while True:
    schedule.run_pending()
    time.sleep(1)
