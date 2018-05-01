# Automation
## Fix & New version OpenCV installation
Sorry everyone for the inconvenience :( \
New installation instructions of opencv version 3.3.0 are provided here. \
If you have any problems please contact me via facebook or mailto: r05631009@ntu.edu.tw 

### Uninstall
$ cd ~/opencv-3.2.0/build \
$ sudo make uninstall \
$ cd ~ \
$ rm opencv opencv_contrib \
$ rm -rf opencv-3.2.0 opencv_contrib-3.2.0 

### Install / ensure dependencies
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev \
$ sudo apt-get install libgtk2.0-dev libgtk-3-dev \
$ sudo apt-get install libatlas-base-dev gfortran \
$ sudo apt-get install fswebcam

### Get new version 3.3.0
$ wget -O opencv https://github.com/opencv/opencv/archive/3.3.0.zip \
$ wget -O opencv_contrib https://github.com/opencv/opencv_contrib/archive/3.3.0.zip \
$ unzip opencv \
$ unzip opencv_contrib \
$ cd opencv-3.3.0 \
$ mkdir build \
$ cd build 

### Start compiling -- may take one or two hours
$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules -D BUILD_EXAMPLES=ON ..  \
$ make -j4 \
$ sudo make install \
$ sudo ldconfig 

### Test code
$ cd Desktop \
$ git clone https://github.com/wildcat5566/Automation.git \
$ cd Automation \
$ python3 test.py \
First python script 'test.py' should display a photograph of a sleeping white puppy. \
Then plug in your USB webcam. \
$ python3 cam.py \
Second python script 'cam.py' should display real-time scene captured by your webcam.
