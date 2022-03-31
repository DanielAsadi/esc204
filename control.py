import serial
import time


def moveX(ser):
    # move stepper by 1 unit in x
    ser.write(b'x')


def moveNX(ser):
    # move stepper by 1 unit in -x
    ser.write(b'X')

def moveY(ser):
    # move stepper by 1 unit in y
    ser.write(b'y')


def resetPos(ser):
    # reset steppers to 0,0 after each analysis
    # basically move up 9 ops to restore to original position
    ser.write(b'Y')

def takePhoto():
    # access luminara api:
    # https://www.lumenera.com/media/wysiwyg/support/pdf/Teledyne_Lumenera-USB_Camera-API_Reference_Manual.pdf
    pass


if __name__ == "__main__":
    while True:
        try:
            # make sure the 'COM#' is set according the Windows Device Manager
            ser = serial.Serial('/dev/cu.usbmodem11401', 115200, timeout=1)
            print("connected to serial")
            break
        except:
            print('Serial port error. Reconnecting...')
        time.sleep(1)

    # stepSizeX = 10
    # stepSizeY = 10

    for y in range(10): # 100 photos in total
        # takePhoto()
        for x in range(9):
            if y % 2 == 0: 
                moveX(ser)
                time.sleep(1)
                # takePhoto()
            else:
                moveNX(ser)
                time.sleep(1)
                # takePhoto()
        if y != 9:
            moveY(ser)
            time.sleep(1)
    resetPos(ser)
    time.sleep(1)

    ser.close()
    quit()
