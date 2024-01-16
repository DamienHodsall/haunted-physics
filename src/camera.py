import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

vid = cv2.VideoCapture(0)

while(True):

    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    edges = cv2.Canny(image=blur, threshold1=100, threshold2=200)
    contours, hier = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contour = [list(coord[0]) for coord in max(contours, key = len)]

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(contour)

line = []

for contour in contours:

    for coord in contour:

        line.append(list(coord[0]))

line = np.array(line)
print(line)

matplotlib.use('Agg')

plt.plot(line.T[0],-line.T[1])
plt.savefig('plot.png')

vid.release()
cv2.destroyAllWindows()

cv2.imshow('plot', cv2.imread('plot.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
