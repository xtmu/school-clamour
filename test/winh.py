import os
import time

import win32api


def down(val):
    # ���¼��̵�ĳ���������ݼ�ֵ��
    win32api.keybd_event(val, 0, 0, 0)


def up(val):
    # �ɿ����̵�ĳ���������ݼ�ֵ��
    win32api.keybd_event(val, 0, win32api.KEYEVENTF_KEYUP, 0)


def press(val):
    # ���²��ɿ�
    down(val)
    up(val)


# def imitate_keys():
#     # win e
#     down(0x5B)
#     press(69)
#     up(0x5B)

def winh_down():
    down(0x58)
    press(6)


def winh_up():
    press(69)
    winh_down()
    up(0x58)


def main():
    print("Win32 Application in python")

    winh_down()
    # os.system()
    time.sleep(2000)
    winh_up()


if __name__ == "__main__":
    main()
