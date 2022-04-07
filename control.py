from fileinput import filename
import serial
import time
import sys
import matlab.engine

positionOfPath = 1
sys.path.insert(positionOfPath, '/Users/jorrynlu/Desktop/220407 ESC204 Design Pitch/esc204/LucamTakeSnapshot.m')


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


def takePhoto(camNumber, filename):
    eng = matlab.engine.start_matlab()
    eng.LucamTakeSnapshot(camNumber, filename)
    eng.quit()


if __name__ == "__main__":
    camNumber = 1
    while True:
        try:
            # make sure the 'COM#' is set according the Windows Device Manager
            ser = serial.Serial('/dev/cu.usbmodem11401', 115200, timeout=1)
            print("connected to serial")
            break
        except:
            print('Serial port error. Reconnecting...')
        time.sleep(1)
    path = ""
    j = 1
    for y in range(10): # 100 photos in total
        filename = path + j
        takePhoto(camNumber, filename)
        for x in range(9):
            if y % 2 == 0: 
                moveX(ser)
                time.sleep(1)
                takePhoto(camNumber, filename)
            else:
                moveNX(ser)
                time.sleep(1)
                takePhoto(camNumber, filename)
            j += 1
        if y != 9:
            moveY(ser)
            time.sleep(1)
        j += 1
    resetPos(ser)
    time.sleep(1)

    ser.close()
    quit()
