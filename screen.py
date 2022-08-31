from ctypes import *

HWND_BROADCAST = 0xffff
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MonitorPowerOn = -1
MonitorPowerOff = 2
MonitorPowerStanby = 1
SW_SHOW = 5


def screen_on():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                               SC_MONITORPOWER, MonitorPowerOn)

    shell32 = windll.LoadLibrary("shell32.dll")
    shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                          'USER32', '', SW_SHOW)


def screen_off():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                               SC_MONITORPOWER, MonitorPowerOff)

    shell32 = windll.LoadLibrary("shell32.dll")
    shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                          'USER32', '', SW_SHOW)


def screen_off_lock():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                               SC_MONITORPOWER, MonitorPowerOff)

    shell32 = windll.LoadLibrary("shell32.dll")
    shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                          'USER32,LockWorkStation', '', SW_SHOW)


def main():
    print("Win32 Application in python")
    screen_off()

if __name__ == "__main__":
    main()
