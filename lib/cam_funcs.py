import cv2

from lib.choose_display import get_display


def change_cam_id(cam_id, cam, negative=False):
    if negative:
        new_cam_id = cam_id - 1
    else:
        new_cam_id = cam_id + 1

    new_cam = cv2.VideoCapture(new_cam_id)

    if new_cam.isOpened():
        print(f'New camera id is {new_cam_id}')
        cam.release()
        return new_cam_id, new_cam
    else:
        print(f'Port {new_cam_id} is not working. Going to previous id: {cam_id}...')
        new_cam.release()
        return cam_id, cam


def create_fullscreen_window(window_name, cam_id, display_id):
    cam = cv2.VideoCapture(cam_id)

    _, _ = cam.read()
    for cam_id in range(cam_id, cam_id + 10):
        if cam.isOpened():
            break
        else:
            cam = cv2.VideoCapture(cam_id)
            print(f"Port {cam_id} is not working. Trying {cam_id + 1}")

        if cam_id == 10:
            print("No working cameras found. Bailing...")
            safe_exit(cam, 1)

    move_display = get_display(display_id)

    # create a window
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, move_display[0], move_display[1])
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    print(f'Created a window on display {display_id}.\nCurrent id of camera is {cam_id}.\nName of window is \'{window_name}\'')
    return cam


def safe_exit(cam, exit_code=0):
    cam.release()
    cv2.destroyAllWindows()
    exit(exit_code)
