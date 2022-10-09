import win32api
import time


def down(val):
    # 按下键盘的某个键（根据键值）
    win32api.keybd_event(val, 0, 0, 0)


def up(val):
    # 松开键盘的某个键（根据键值）
    win32api.keybd_event(val, 0, win32api.KEYEVENTF_KEYUP, 0)


def press(val):
    # 按下并松开
    down(val)
    up(val)


def winh_down():
    down(0x58)
    press(6)


def winh_up():
    press(69)
    up(0x58)


def imitate_keys():
    # win
    down(0x58)
    press(69)
    up(0x5B)


def main():
    print("Win32 Application in python")
    # imitate_keys()

    print('1')
    winh_down()

    time.sleep(2)

    print('2')
    winh_up()


if __name__ == "__main__":
    main()
