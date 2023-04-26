'''
This script is used for getting needed parameters for moving shown image to different display
'''

import screeninfo as si


monitors = si.get_monitors()
monitor_count = len(monitors)

def get_display(display_id):
    if -monitor_count > display_id > monitor_count - 1:
        return 0, 0
    return monitors[display_id].x, monitors[display_id].y
