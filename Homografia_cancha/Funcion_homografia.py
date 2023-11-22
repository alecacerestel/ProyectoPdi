import cv2
import numpy as np

def mouse_handler(event, x, y, flags, data) :
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x,y), 3, (0,0,255), 5, 16)
        cv2.imshow("Image", data['im'])
        if len(data['points']) < 4 :
            data['points'].append([x,y])

def get_four_points(im):
    data = {}
    data['im'] = im.copy()
    data['points'] = []
    
    cv2.imshow("Image",im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)
    
    points = np.vstack(data['points']).astype(float)

    return points

def homography_from_image(im_src):
    # Destination image
    im= cv2.imread(im_src)
    size = (1200, 400, 3)
    im_dst = np.zeros(size, np.uint8)
    
    pts_dst = np.array(
        [
            [0, 0],
            [size[0] - 1, 0],
            [size[0] - 1, size[1] - 1],
            [0, size[1] - 1]
        ], dtype=float
    )

    # Show the original image and get four points by clicking on the image
    cv2.imshow("Image", im)
    pts_src = get_four_points(im)

    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im, h, size[0:2])

    # Show the output
    cv2.imshow("Image", im_dst)
    cv2.waitKey(0)

# Read in the image.
a="cancha2.jpg"

# Call the function with the input image
homography_from_image(a)

cv2.destroyAllWindows()
