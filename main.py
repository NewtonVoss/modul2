def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.pause(500)
        servos.P1.set_angle(0)
        basic.pause(500)
        servos.P1.stop()
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(500)
    elif receivedNumber == 2:
        servos.P1.set_angle(90)
        basic.pause(500)
        servos.P1.stop()
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(1)
    servos.P1.set_angle(90)
    basic.pause(500)
    servos.P1.stop()
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    OLED.clear()
    OLED.write_string_new_line("Lukka")
    OLED.draw_line(0, 64, 128, 0)
    OLED.draw_line(128, 64, 0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

strip: neopixel.Strip = None
radio.set_group(1)
led.enable(False)
strip = neopixel.create(DigitalPin.P2, 1, NeoPixelMode.RGB)
OLED.init(128, 64)

def on_forever():
    if smarthome.read_noise(AnalogPin.P3) > 80:
        radio.send_number(2)
        servos.P1.set_angle(2)
        basic.pause(500)
        servos.P1.stop()
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        OLED.clear()
        OLED.write_string_new_line("Open")
basic.forever(on_forever)
