# Tutorial 1 - Hello ZED
# https://github.com/stereolabs/zed-sdk/tree/master/tutorials/tutorial%201%20-%20hello%20ZED/python 

import pyzed.sl as sl

def main():
    # Create a ZED camera object
    zed = sl.Camera()

    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD1080 
    init_params.camera_fps = 30 

    # Open the camera
    err = zed.open(init_params)
    if (err != sl.ERROR_CODE.SUCCESS) :
        exit(-1)

    # Get camera information (serial number)
    zed_serial = zed.get_camera_information().serial_number
    print("Hello! This is my serial number: ", zed_serial)

    # Close the camera
    zed.close()
    return 0

main()
