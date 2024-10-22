from __future__ import print_function
import cv2 as cv
import time
import numpy as np
 

 
 


def backgrond_removal2(frame, background):

    #True to return output, edges, blurred, gray,outline
    #False to return only outline
    return_pictures = True


    output = cv.subtract(frame,background)


    gray = cv.cvtColor(output, cv.COLOR_BGR2GRAY)

    
    # Apply Gaussian blur to reduce noise and smoothen edges 
    blurred = cv.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5) 

      
    # Perform Canny edge detection 
    edges = cv.Canny(blurred, 70, 135)

    #find contours
    contours, hier = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    outline = [] # do this but with np.zeros((44800, 2))?
    for contour in contours:
        outline += [point[0] for point in contour]
    outline = np.array(outline)
    # maxamp = max(abs(outline))
    # outline = outline / maxamp

    if return_pictures == True:
        return output, edges, blurred, gray,outline
    else:
        return outline




def main(): 
    # Open the default webcam
    print('delay for background removal \n')
    print('3 \n')
    time.sleep(1)
    print('2 \n')
    time.sleep(1)
    print('1 \n')
    time.sleep(1)

    print('taking picture \n')
    cap = cv.VideoCapture(1) 
    ret, background_frame = cap.read()
    
    

    print('picture taken \n')

    while True: 
        # Read a frame from the webcam 
        ret, frame = cap.read() 
        if not ret: 
            print('Image not captured') 
            break
        
        output,gray,blurred,edges, outline = backgrond_removal2(frame,background_frame)
        cv.imshow("original",frame)
        cv.imshow("output", output)
        cv.imshow("Gray",gray) 
        
        cv.imshow("Blurred", blurred) 
        cv.imshow("Edges", edges)

        # Exit the loop when 'q' key is pressed 
        if cv.waitKey(1) & 0xFF == ord('q'): 
            break
      
    # Release the webcam and close the windows 
    cap.release() 
    cv.destroyAllWindows()

if __name__ == "__main__": 
    main()

