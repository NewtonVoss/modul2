radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.pause(500)
        servos.P1.setAngle(0)
        basic.pause(500)
        servos.P1.stop()
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        basic.pause(500)
    } else if (receivedNumber == 2) {
        servos.P1.setAngle(90)
        basic.pause(500)
        servos.P1.stop()
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    servos.P1.setAngle(90)
    basic.pause(500)
    servos.P1.stop()
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
    OLED.clear()
    OLED.writeStringNewLine("Lukka")
    OLED.drawLine(
    0,
    64,
    128,
    0
    )
    OLED.drawLine(
    128,
    64,
    0,
    0
    )
})
input.onButtonPressed(Button.B, function () {
	
})
let strip: neopixel.Strip = null
radio.setGroup(1)
led.enable(false)
strip = neopixel.create(DigitalPin.P2, 1, NeoPixelMode.RGB)
OLED.init(128, 64)
basic.forever(function () {
    if (smarthome.ReadNoise(AnalogPin.P3) > 80) {
        radio.sendNumber(2)
        servos.P1.setAngle(2)
        basic.pause(500)
        servos.P1.stop()
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        OLED.clear()
        OLED.writeStringNewLine("Open")
    }
})
