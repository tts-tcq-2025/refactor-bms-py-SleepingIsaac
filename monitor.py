import sys
from time import sleep

def is_between_range(min, max, value):
    return min <= value <= max

def is_spo2_ok(spo2):
    #Checks if the oxygen saturation (SpO2) is within the acceptable range
    return spo2 >= 90

def warning_animation():
    #Displays a warning animation
    for i in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def vitals_ok(temperature, pulse_rate, spo2):
    #Checks if all vitals are are ok
    if not is_temperature_ok(95, 102, temperature):
        print('Temperature critical!')
        warning_animation()
        return False
    elif not is_pulse_rate_ok(60, 100, pulse_rate):
        print('Pulse Rate is out of range!')
        warning_animation()
        return False
    elif not is_spo2_ok(spo2):
        print('Oxygen Saturation out of range!')
        warning_animation()
        return False
    return True
