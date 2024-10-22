import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from time import time, sleep
import pyaudio
import threading
import os

"""notes

k so I need to do some background subtraction before I can get this to really work

"""

os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = '0'
final_outline = np.zeros((1,2)).tobytes()

def camera_feed():

    vid = cv2.VideoCapture(0)

    while(True):

        ret, frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3,3), 0)
        edges = cv2.Canny(image=frame, threshold1=100, threshold2=200)
        contours, hier = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        outline = [] # do this but with np.zeros((44800, 2))?
        for contour in contours:
            outline += [point[0] for point in contour]
        outline = np.array(outline)
        # maxamp = max(abs(outline))
        # outline = outline / maxamp

        global final_outline
        final_outline = outline.astype(np.float32).tobytes()

        if False or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

def audio_stream():

    pya = pyaudio.PyAudio()
    stream = pya.open(format=pya.get_format_from_width(width=2),
                  channels=2,
                  rate=44800,
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
