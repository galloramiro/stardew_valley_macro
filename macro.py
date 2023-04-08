from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button

def sleep_for_frames(sleep_time_ms: int)  -> None:
    import time
    frames = 16.666
    sleep_by_frame = (sleep_time_ms * frames) / 1000
    time.sleep(sleep_by_frame)


def press_key(key) -> None:
    keyboard.press(key)


def release_key(key) -> None:
    keyboard.release(key)

def left_click() -> None:
    mouse.press(Button.left)
    sleep_for_frames(1)
    mouse.release(Button.left)
    print('Left click pressed')


def on_press(key):
    print('{} pressed'.format(key))

    try:
        valid_char = 'char' in dir(key)

        if valid_char and key.char == "u":
            left_click()

            sleep_for_frames(5)

            press_key("r")
            press_key(Key.delete)
            press_key(Key.shift_r)

            sleep_for_frames(1)

            release_key("r")
            release_key(Key.delete)
            release_key(Key.shift_r)

    except Exception as ex:
        print("Exception:")
        print(ex)


def on_release(key):
    print('{} release'.format(key))

    if key == Key.esc:
        # Stop listener
        return False

# --- main ---

keyboard = Controller()
mouse = MouseController()

listener = Listener(on_press=on_press, on_release=on_release)

listener.start()

# ... other code ...

listener.join()
