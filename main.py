import cv2

import lib.cam_funcs as cf
import lib.ml.main as ml
import lib.process_file as pf
import lib.create_output_image as oi

from lib.process_text import create_file_name
from lib.keycodes import Keycode


WINDOW_NAME = 'JXR'
DISPLAY_ID = 0

last_filename = pf.DEFAULT_FILENAME

cam_id = 0
cam = cf.create_fullscreen_window(WINDOW_NAME, cam_id, DISPLAY_ID)

while cv2.getWindowProperty(WINDOW_NAME, 0) >= 0:
    _, frame = cam.read()

    texts = ml.get_text_from_image(frame)
    filenames = create_file_name(texts)
    medical_info = pf.get_info_from_file(filenames)
    frame = oi.text_to_img(medical_info)
    cv2.imshow(WINDOW_NAME, frame)

    key = cv2.waitKey(1)

    match key:
        case Keycode.QUIT:
            break
        case Keycode.PREV_CAM:
            cam_id, cam = cf.change_cam_id(cam_id, cam, negative=True)
        case Keycode.NEXT_CAM:
            cam_id, cam = cf.change_cam_id(cam_id, cam)

cf.safe_exit(cam)