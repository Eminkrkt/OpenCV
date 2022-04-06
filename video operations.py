"""

    @author : Eminn
    @Operating System : Manjora Cinnamon
   
    Requirements : python and opencv
    OpenCv version : opencv-python 4.5.5.64
    Pip install = 'pip install opencv-python==4.5.5.64'

"""  

# Video save // Video kaydetme

"""
import cv2
import time

# File path and extension // Dosya yolu ve uzantısı
file_name = time.ctime().split()[3].replace(":","_")+ ".avi"

cap = cv2.VideoCapture(0)
cikti = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'XVID') , 25 ,(640,480))


while (True):
    success, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    frame_copy = frame.copy()

    cikti.write(frame_copy)

    cv2.imshow('Original',frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

"""

# Video read // Video okuma

"""
import cv2

cap = cv2.VideoCapture('test.mp4')

while (True):
    success , frame = cap.read()
    frame = cv2.resize(frame,(640,440))

    cv2.imshow('Window',frame)

    # You can control the video speed with the value written inside the 'waitkey' // 'waitKey' içine yazılan değer ile video hızı kontrol edilir.
    if(cv2.waitKey(50) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
"""