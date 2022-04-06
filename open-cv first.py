"""

   @author : Eminn
   @Operating System : Manjora Cinnamon
   
    Requirements : python and opencv
    OpenCv version : opencv-python 4.5.5.64
    Pip install = 'pip install opencv-python==4.5.5.64'

"""  
#   We include the library // Kütüphaneyi dahil ediyoruz 
"""   ---->       import cv2                                                                        """

#   We enter the image we want to process // İşlemek istediğimiz görüntüyü giriyoruz
"""   ---->       video = cv2.VideoCapture()                                                        """

#       There are two types of methods // İki tür yöntem vardır
#           1 - ) Getting the image from the camera // Kameradan görüntü alma
"""           ---->      video = cv2.VideoCapture(0)                                                """
#           2 - ) Getting the image from the video // Videodan görüntü alma
"""           ---->      video = cv2.VideoCapture('test.mp4')                                       """

#   Continuously reading the image // Sürekli görüntü okuma
"""
    #   'frame' variable is important for us here // 'frame' değişkeni burada bizim için önemli

    while (True):
        success, frame = cap.read()
"""

#   Reflecting the value we read on the screen // Okuduğumuz değeri ekrana yansıtmak
"""   ---->       cv2.imshow('Original',frame)                                                      """

#
#
#   If we want to close the program // Programı kapatmak istersek
""" 
    # Here 'q' is assigned as the shutdown key. You can change it // Burada 'q' tuşu kapatma için atanmış. İsterseniz değiştirebilirsiniz 

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
"""

#   These are used to close the window when the program stops // Program durduğunda pencerenin kapanmasını sağlamak için kodlar
"""
    cap.release() 
    cv2.destroyAllWindows()
"""

# Final version of the code // Kodun son hali

"""

import cv2

cap = cv2.VideoCapture(0)

while (True):
    success , frame = cap.read()

    cv2.imshow('Window',frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

"""