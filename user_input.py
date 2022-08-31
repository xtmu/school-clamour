from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()


def win_d():
    k.press_keys([k.windows_l_key, 'd'])


def win_m():
    k.press_keys([k.windows_l_key, 'm'])


def screen_type(str="Hello World!"):
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)
    # k.type_string(str)


def main():
    print("user_input test")
    # win_m()
    screen_type()


if __name__ == "__main__":
    main()
