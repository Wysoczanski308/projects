import cv2


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
tracker = cv2.legacy.TrackerMOSSE()





while True:
    ret, img = cap.read()

    grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRA)



    cv2.imshow('frame', grayimage)






    if cv2.waitKey(1) & ord('q'):
        pass


