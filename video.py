import cv2
import time

capture_duration = 3.10

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 40)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


    # Define the codec and create VideoWriter object
out = cv2.VideoWriter("p_video.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 40, (frame_width, frame_height))

start_time = time.time()
while float(time.time() - start_time) < capture_duration:
        ret, frame = cap.read()
        if ret:

            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()