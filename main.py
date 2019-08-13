import cv2
import sys

# needed input-files via cli as arguments
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# create a new haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# read and convert the image based on given color space
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect possible faces in the image
faces = faceCascade.detectMultiScale\
        (
            gray,
            scaleFactor = 1.2, # needs to be adjusted
            minNeighbors = 5,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

print("Found {0} faces!".format(len(faces)))

# draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
# show the final image with rectangles around the existing faces

cv2.imshow("Faces found: ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
