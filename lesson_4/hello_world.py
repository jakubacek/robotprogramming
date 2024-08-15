from microbit import sleep
from microbit import button_a
from microbit import display


def display_text(text="Ahoj"):
    while not button_a.was_pressed():
        display.scroll(text)
        sleep(3000)

def display_text_fix(text="Ahoj"):
    while not button_a.was_pressed():
        display.scroll(text)
        if not button_a.was_pressed():
            sleep(3000)
        else:
            break

display_text_fix()
