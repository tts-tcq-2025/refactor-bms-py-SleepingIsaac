import sys
from time import sleep

def is_between_range(min, max, value):
    return min <= value <= max

def is_spo2_ok(spo2):
    #Checks if the oxygen saturation (SpO2) is within the acceptable range
    return spo2 >= 90

def warning_animation(tempOK, pulseOK, spo20K):
    #Displays a warning animation
    for i in range(6):
        print('\r* ', end='')
        if(tempOK):
            print(" Temperature Warning ")
        elif(pulseOK):
            print(" Pulse Warning ")
        elif(spo20K):
            print(" Spo2 Warning ")
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def vitals_ok(temperature, pulse_rate, spo2):
    #Checks if all vitals are are ok
    tempOK  = is_temperature_ok(95, 102, temperature)
    pulseOK = is_pulse_rate_ok(60, 100, pulse_rate)
    spo2OK  = s_spo2_ok(spo2)
    if(tempOK or pulseOK or spo20K):
        wrong_animation(tempOK, pulseOK, spo20K)
        return False
    return True
