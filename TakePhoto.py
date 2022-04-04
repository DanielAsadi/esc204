import sys
import matlab.engine

positionOfPath = 1
sys.path.insert(positionOfPath, '/Users/jorrynlu/Desktop/220407 ESC204 Design Pitch/esc204/TestFunction.m')
# sys.path.insert(positionOfPath, 'C:\\Users\\yangy\\OneDrive\\Documents\\MATLAB\\Lumenera')

def TestFunc(inpNum):
    eng = matlab.engine.start_matlab()
    eng.TestFunction(inpNum)
    eng.quit()

# def TakePic(camNumber):
#     eng = matlab.engine.start_matlab()
#     eng.LucamGetSnapshot(camNumber)
#     eng.quit()

if __name__ == "__main__":
    TestFunc(20)

    # if some input prompts camera to take a photo...
    # TakePic(13)