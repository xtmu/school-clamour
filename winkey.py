import win32api


def down(val):
    # 按下键盘的某个键（根据键值）
    win32api.keybd_event(val, 0, 0, 0)


def up(val):
    # 松开键盘的某个键（根据键值）
    win32api.keybd_event(val, 0, 0, 0)
    # win32api.keybd_event(val, 0, win32api.KEYEVENTF_KEYUP, 0)


def press(val):
    # 按下并松开
    down(val)
    up(val)


def imitate_keys():
    # win e
    down(0x5B)
    press(69)
    up(0x5B)


def main():
    print("Win32 Application in python")
    imitate_keys()


if __name__ == "__main__":
    main()
