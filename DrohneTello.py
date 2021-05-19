#Drohne Tello
#pip install easytello
#pip install tello-python
#pip install opencv-python

from easytello import tello
import cv2

my_drone = tello.Tello()

my_drone.streamoff()
my_drone.streamon()


telloVideo = cv2.VideoCapture("udp://@0.0.0.0:11111")
print(my_drone.get_battery())

# wait for frame
ret = False
# scale down
scale = 1

while(True):
    
    # Capture frame-by-framestreamon
    ret, frame = telloVideo.read()

    if(ret):
    # Our operations on the frame come here
        height , width , layers =  frame.shape
        #print(frame.shape)
        #new_h=int(height/scale)
        #new_w=int(width/scale)
        resize = cv2.resize(frame, (320, 240)) # <- resize for improved performance
        # Display the resulting frame
        cv2.imshow('Tello', resize)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("test.jpg",resize) # writes image test.bmp to disk
        print("Take Picture")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('u'):
        my_drone.takeoff()
    if cv2.waitKey(1) & 0xFF == ord('d'):
        my_drone.land()

# When everything done, release the capture
telloVideo.release()
cv2.destroyAllWindows()



# my_drone.takeoff()

# for i in range(4):
# 	my_drone.forward(50)
# 	my_drone.cw(90)

# my_drone.land()
