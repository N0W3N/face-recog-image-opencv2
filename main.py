import cv2
import sys

# needed input-files via cli as arguments
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# create a new haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# read and convert the image based on given color space
image = cv2.imread(imagePath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect possible faces in the image
faces = faceCascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,  # needs to be adjusted
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

print(f"Found {len(faces)} faces!")

# draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the final image with rectangles around the existing faces

#TODO: cv2 commands appear to be buggy, waitkey() doesn't recognize the key input and destroyAllWindows() doesn't close the window.


cv2.imshow(f"Faces found: {len(faces)}", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
