def on_gesture_shake():
    global steps
    steps += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global steps
    steps = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

steps = 0
basic.show_number(0)
steps = 0

def on_forever():
    if steps >= 10:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_number(steps)
basic.forever(on_forever)
