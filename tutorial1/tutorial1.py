"""
Tutorial 1 - Hello ZED
https://github.com/stereolabs/zed-sdk/tree/master/tutorials/tutorial%201%20-%20hello%20ZED/python 

The commented out is from the tutorial but doesn't work for me since it uses AI features by default. I think I didn't intall the AI models in the sdk install
"""

# import pyzed.sl as sl

# def main():
#     # Create a ZED camera object
#     zed = sl.Camera()

#     # Set configuration parameters
#     init_params = sl.InitParameters()
#     init_params.camera_resolution = sl.RESOLUTION.HD1080 
#     init_params.camera_fps = 30 

#     # Explicitly disable AI features
#     init_params.enable_object_detection = False  # Disable object detection (AI)
#     init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE  # Use performance mode for basic depth sensing

#     # Open the camera
#     err = zed.open(init_params)
#     if (err != sl.ERROR_CODE.SUCCESS) :
#         print("Failed to open the camera:", err)
#         exit(-1)

#     # Get camera information (serial number)
#     zed_serial = zed.get_camera_information().serial_number
#     print("Hello! This is my serial number: ", zed_serial)

#     # Close the camera
#     zed.close()
#     return 0

# main()

import pyzed.sl as sl

def main():
    # Create a ZED camera object
    zed = sl.Camera()

    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD1080  # Set the resolution
    init_params.camera_fps = 30  # Set the frame rate

    # Set depth mode to PERFORMANCE (no AI/Neural depth processing)
    # init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE  # Avoid neural depth processing
    init_params.depth_mode = sl.DEPTH_MODE.QUALITY  # Quality depth mode for better results 

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("Failed to open the camera:", err)
        exit(-1)

    # Get camera information (serial number)
    zed_serial = zed.get_camera_information().serial_number
    print("Hello! This is my serial number:", zed_serial)

    # Close the camera
    zed.close()
    return 0

main()
