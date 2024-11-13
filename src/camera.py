import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from time import time, sleep
import pyaudio
import threading
import os
from edgeDetection import backgrond_removal2

"""notes

k so I need to do some background subtraction before I can get this to really work

"""

os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = '0'
final_outline = np.zeros((1,2)).tobytes()

def camera_feed():

    vid = cv2.VideoCapture(0)
    print("move")
    sleep(3)

    ret, background = vid.read()

    while(True):

        ret, frame = vid.read()

        global final_outline
        final_outline = backgrond_removal2(frame, background).astype(np.dtype(np.int16)).tobytes()

        if False or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

def audio_stream():

    pya = pyaudio.PyAudio()
    stream = pya.open(format=pyaudio.paInt16,
                  channels=2,
                  rate=22000,
                  output=True)
    global final_outline

    while(True):

        stream.write(final_outline)
    
        # if final_outline.size > 0: print(final_outline)
        if len(final_outline) > 0: print(final_outline)

        if False or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    stream.stop_stream()
    stream.close()
    pya.terminate()

if __name__ == '__main__':

    vid_thread = threading.Thread(target=camera_feed, name='vid_thread')
    aud_thread = threading.Thread(target=audio_stream, name='aud_thread')

    vid_thread.start()
    sleep(1)
    aud_thread.start()

    matplotlib.use('Agg')

    plt.scatter(outline.T[0],-outline.T[1])
    plt.savefig('plot.png')

    cv2.imshow('plot', cv2.imread('plot.png'))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
