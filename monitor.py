import sys
from time import sleep

def is_temperature_ok(temperature):
    #Checks if the temperature is within the acceptable range
    return 95 <= temperature <= 102

def is_pulse_rate_ok(pulse_rate):
    #Checks if the pulse rate is within the acceptable range
    return 60 <= pulse_rate <= 100

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
    if not is_temperature_ok(temperature):
        print('Temperature critical!')
        warning_animation()
        return False
    elif not is_pulse_rate_ok(pulse_rate):
        print('Pulse Rate is out of range!')
        warning_animation()
        return False
    elif not is_spo2_ok(spo2):
        print('Oxygen Saturation out of range!')
        warning_animation()
        return False
    print("Vitals are OK!")
    return True
