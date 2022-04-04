import sys
# import matlab.engine

positionOfPath = 1
# sys.path.insert(positionOfPath, 'C:\\Users\\yangy\\Downloads\\Matlab')
sys.path.insert(positionOfPath, 'C:\\Users\\yangy\\OneDrive\\Documents\\MATLAB\\Lumenera')

# def TestFunc(inpNum):
#     eng = matlab.engine.start_matlab()
#     eng.TestFunction(nargout = 1)
#     eng.quit()

def TakePic(camNumber):
    eng = matlab.engine.start_matlab()
    eng.LucamGetSnapshot(nargout = 1)
    eng.quit()

if __name__ == "__main__":
    # TestFunc(20)

    # if some input prompts camera to take a photo...
    TakePic(13)