input.onGesture(Gesture.Shake, function () {
    steps += 1
})
input.onButtonPressed(Button.AB, function () {
    steps = 0
})
let steps = 0
basic.showNumber(0)
steps = 0
basic.forever(function () {
    if (steps >= 10) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showNumber(steps)
    }
})
