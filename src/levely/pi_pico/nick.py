import machine
import time

# Definování pinů
RED_PIN = 0
YELLOW_PIN = 1
GREEN_PIN = 2
RED_PIN2 = 3
YELLOW_PIN2 = 4
GREEN_PIN2 = 5
RED_PIN3 = 6
YELLOW_PIN3 = 7
GREEN_PIN3 = 8
RED_PIN4 = 9
YELLOW_PIN4 = 10
GREEN_PIN4 = 11

# Initialize GPIO pinů
red_led = machine.Pin(RED_PIN, machine.Pin.OUT)
yellow_led = machine.Pin(YELLOW_PIN, machine.Pin.OUT)
green_led = machine.Pin(GREEN_PIN, machine.Pin.OUT)
red_led2 = machine.Pin(RED_PIN2, machine.Pin.OUT)
yellow_led2 = machine.Pin(YELLOW_PIN2, machine.Pin.OUT)
green_led2 = machine.Pin(GREEN_PIN2, machine.Pin.OUT)
red_led3 = machine.Pin(RED_PIN3, machine.Pin.OUT)
yellow_led3 = machine.Pin(YELLOW_PIN3, machine.Pin.OUT)
green_led3 = machine.Pin(GREEN_PIN3, machine.Pin.OUT)
red_led4 = machine.Pin(RED_PIN4, machine.Pin.OUT)
yellow_led4 = machine.Pin(YELLOW_PIN4, machine.Pin.OUT)
green_led4 = machine.Pin(GREEN_PIN4, machine.Pin.OUT)

# Function to control the traffic lights
def run_traffic_lights():
        red_led.off()
        red_led2.off()
        red_led3.off()
        red_led4.off()
        yellow_led.off()
        yellow_led2.off()
        yellow_led3.off()
        yellow_led4.off()
        green_led.off()
        green_led2.off()
        green_led3.off()
        green_led4.off()


# Run the traffic lights
run_traffic_lights()

