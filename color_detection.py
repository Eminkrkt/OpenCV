# We include library // Kütüphanaleri dahil ediyoruz
import cv2 ; import numpy as np

# We enter the image that we will process // İşlenecek görüntüyü giriyoruz
# '0' camera image or file path // '0' Kamera görüntüsü veya dosya yolu 
video = cv2.VideoCapture('Video/fv1.mp4') 
 
while True:
    # Fİmage is read // Görüntü okunur
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    # Windows resize event // Pencere boyutlandırma
    frame = cv2.resize(frame, (640, 440)) 
 
    # Blur effect is apply  // Bulanıklık Efekti Uygulanır (İstenilen Değeri Daha iyi tespit edebilmek için)
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    # BGR to HSV event // BGR'dan HSV renk uzayına dönüştürülür
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
    # Color code ranges are determined // Renk kodu aralıkları belirlenir (İstenilen renk HSV değerinden en düşük ve en yüksek aralıkları belirlenir)
    lower = [2, 130, 130]
    upper = [38, 255, 255]
    # Ranges are converted to array // Aralıklar Diziye dönüştürülür (İşlenebilmesi için)
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # Masking process  // Maskeleme yapılır (İstenilen renk haricinde ki yerler siyah olur)
    mask = cv2.inRange(hsv, lower, upper)

    # Masking is done with the original image // Asıl görüntü ile maskeleme yapılır
    output = cv2.bitwise_and(frame, hsv, mask=mask)

    # The number of 'pixels' in the image is taken // Görüntü deki 'piksel' sayısı alınır
    no_red = cv2.countNonZero(mask)
    
    # If the number of pixels is greater than the specified value, we call it fire // Piksel sayısı belirlediğimiz değerden büyükse 'ateş' olarak adlandırıyoruz.
    if int(no_red) > 20000:
        print("Ateş tespit edildi.")

    # The image is projected onto the screen // Görüntü ekrana verilir
    cv2.imshow("output", output)
    cv2.imshow('ori',frame)

    # 'q' was pressed and exited // 'q' tuşunu çıkış olarak ayarlıyoruz 
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
 
cv2.destroyAllWindows()
video.release()