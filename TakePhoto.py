import sys
import matlab.engine

positionOfPath = 1
# sys.path.insert(positionOfPath, '/Users/jorrynlu/Desktop/220407 ESC204 Design Pitch/esc204/TestFunction.m')
sys.path.insert(positionOfPath, 'C:\\Users\\yangy\\Downloads\\widget_lab_2\\esc204')

def TestFunc(inpNum):
    eng = matlab.engine.start_matlab()
    eng.TestFunction(inpNum)
    eng.quit()

def TakePic(camNumber, filename):
    eng = matlab.engine.start_matlab()
    # eng.simple_script(nargout=1)
    eng.LucamTakeSnapshot(camNumber, filename)
    eng.quit()

if __name__ == "__main__":
    # TestFunc(20)
    filename = 'test.csv'
    TakePic(1, filename)