import serial
import time


def moveX(ser):
    # move stepper by 1 unit in x
    ser.write(b'x')


def moveY(ser):
    # move stepper by 1 unit in y
    ser.write(b'y')


def resetPos(ser):
    # reset steppers to 0,0 after each analysis
    pass


def resetPos(ser):
    # reset steppers to 0,0 after each analysis
    pass

def takePhoto():
    # access luminara api:
    # https://www.lumenera.com/media/wysiwyg/support/pdf/Teledyne_Lumenera-USB_Camera-API_Reference_Manual.pdf
    pass


if __name__ == "__main__":
    while True:
        try:
            # make sure the 'COM#' is set according the Windows Device Manager
            ser = serial.Serial('COM13', 115200, timeout=1)
            break
        except:
            print('Serial port error. Reconecting...')
        time.sleep(2)

    stepSizeX = 10
    stepSizeY = 10

    for x in range(stepSizeX):
        moveX(ser)

    ser.close()
    quit()
