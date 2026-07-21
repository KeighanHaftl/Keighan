if __name__=='__main__':
    PWM = Ordinary_Car() 
    direction = input("Which direction (use WASD and use E to stop)") 
    try:
        if direction == "w":
            PWM.set_motor_model(-2000,-2000,-2000,-2000)   #Forward
        if direction == "s":        
            PWM.set_motor_model(2000,2000,2000,2000)       #Back
        if direction == "a":
            PWM.set_motor_model(2000,2000,-2000,-2000)     #Left 
        if direction == "d":
            PWM.set_motor_model(-2000,-2000,2000,2000)     #Right    
        if direction == "e":
            PWM.set_motor_model(0,0,0,0)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print ("\nEnd of program")
    finally:
        PWM.close()
