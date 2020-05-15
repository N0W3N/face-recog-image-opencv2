OpenCV2 - Face recognition
==================
Some basic code to detect possible faces in one or more pictures using OpenCV2 and Python.
In order to detect faces or several other options such as smiling faces, eyes, full body.. vice versa,
OpenCV2 uses (haar-)cascades to detect certain patterns in a picture.
Cascade files are trained models from neural networks and can also contain other objects; e.g. cars, trees, houses or motions.
Ìf any faces are found in the picture, the code draws rectangles on them - unfortunately it's pretty inefficient without optimizing, therefore in some cases it can find faces and draw rectangles on non-face-objects.

### Installation

1) ``git clone https://github.com/N0W3N/Picture-based-face-recognition.git``
2) `` pip install -r requirements.txt``  
Note: Mac requires an installation via homebrew  
-> ```brew update```  
-> ```brew install opencv-python```
-> ```brew install opencv-contrib-python```

### Usage

``cascade`` contains all cascade files
`pictures` contains all used pictures for face recognition

`python3 main.py <image path> <cascade path>`

### Example

`python3 main.py pictures/nicholas-green-nPz8akkUmDI-unsplash.jpg cascade/haarcascade_frontalface_default.xml`


![ALT TEXT](https://www1.xup.in/exec/ximg.php?fid=39784458)

### Credits

All pictures are copyright-free and free usable

https://unsplash.com/s/photos/group