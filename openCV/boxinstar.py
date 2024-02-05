import cv2
import numpy as np

a=500/(1+np.cos(np.pi*54/180))
b=int(a*np.cos(np.pi*72/180))
c=int(a*np.sin(np.pi*72/180))

img =np.full((500,500,3),255, dtype=np.uint8)

cv2.line(img, (b,500),(250,0),(255,0,0),3 )
cv2.imshow('Text',img)
cv2.waitKey( 1500 )


cv2.line(img, (250,0),(500-b,500),(255,0,0),3 )
cv2.imshow('Text',img)
cv2.waitKey( 1500 )


cv2.line(img, (500-b,500),(0,500-c),(255,0,0),3 )
cv2.imshow('Text',img)
cv2.waitKey( 1500 )


cv2.line(img, (0,500-c),(500,500-c),(255,0,0),3 )
cv2.imshow('Text',img)
cv2.waitKey( 1500 )

cv2.line(img, (500,500-c),(b,500),(255,0,0),3 )
cv2.imshow('Text',img)
cv2.waitKey(0)

cv2.destroyAllWindows()