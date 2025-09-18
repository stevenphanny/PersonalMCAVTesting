import pyzed.sl as sl
import cv2
import numpy as np

def main():
    # Create a ZED camera object
    zed = sl.Camera()

    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD1080  # Set the resolution
    init_params.camera_fps = 30  # Set the frame rate
    init_params.depth_mode = sl.DEPTH_MODE.QUALITY  # Set depth mode to QUALITY

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("Failed to open the camera:", err)
        exit(-1)

    # Create an image object to store the depth map
    depth_image = sl.Mat()

    # Capture depth image
    zed.retrieve_measure(depth_image, sl.MEASURE.DEPTH)

    # Convert depth image to numpy array for OpenCV
    depth_np = depth_image.get_data()

    # Display depth image using OpenCV
    cv2.imshow("Depth Image", depth_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Close the camera
    zed.close()
    return 0

main()
