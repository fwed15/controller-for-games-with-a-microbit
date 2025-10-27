import serial
import keyboard

ser = serial.Serial('COM13', 115200)  # Replace with your actual port

a_down = False
b_down = False

while True:
    line = ser.readline().decode().strip()

    if line == "A_DOWN" and not a_down:
        keyboard.press("z")
        a_down = True
    elif line == "A_UP" and a_down:
        keyboard.release("z")
        a_down = False

    elif line == "B_DOWN" and not b_down:
        keyboard.press("x")  # HOLD for jump
        b_down = True
    elif line == "B_UP" and b_down:
        keyboard.release("x")  # RELEASE for robot/wave/etc
        b_down = False
