# custom-object-detection-model

## Install
  
  ```sh
git clone https://github.com/pyinstaller/pyinstaller.git
cd pyinstaller/bootloader
python ./waf all
pip install ..


python3 -c "import platform; print(platform.processor())"
  ```

## Setup


```sh
sudo apt install python-is-python3
python --version
sudo apt install python3-pip
pip install --upgrade pip
pip install mediapipe-model-maker
```

## Test Data
https://storage.googleapis.com/mediapipe-tasks/object_detector/android_figurine.zip

## Known Issues

- `pip` killed when installing `tensorflow`
  ``` sh
   pip3 install tensorflow==2.2.0
  ```
  
     **OR**
  
  ``` sh
   pip3 install tensorflow-cpu
   pip3 install mediapipe-model-maker --no-dependencies
  ```

- `opencv` install on Ubuntu
  ``` sh
  sudo apt-get install python3-opencv
  ```
