import socket
from PIL import Image
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", "-i")
parser.add_argument("--video", "-v")
args = parser.parse_args()
HOST = '89.58.2.236'
PORT = 1234
IMG_PATH = args.image
VIDEO_PATH = args.video

# CONNECT TO SERVER
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

send = sock.send
def pixel(x, y, r, g, b, a):
    # PIXELFLUT PROTOCOL
    if a == 255:
        return "PX %d %d %02x%02x%02x\n" % (x,y,r,g,b)
    else:
        return "PX %d %d %02x%02x%02x%02x\n" % (x,y,r,g,b,a)

def capFrames(PATH):
    vid = cv2.VideoCapture(PATH)
    while True:
        frame = vid.read()
        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return frame, width, height
        
def drawPixel(PATH):
    img = Image.open(PATH)
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r,g,b = img.getpixel((x, y))
            send(pixel(x,y,r,g,b,255).encode())

# def drawFrames(PATH):
#     vid = cv2.VideoCapture(PATH)
#     ret, frame = vid.read()
#     width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
#     height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
#     height, width, _ = frame.shape
#     while True:
#         for y in range(height):
#             for x in range(width): 
#                 r,g,b = frame[y,x]
#                 send(pixel(x,y,r,g,b,255).encode())

# vid = cv2.VideoCapture(VIDEO_PATH)
# ret, frame = vid.read()
# width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
# height, width, _ = frame.shape

while True:
    if VIDEO_PATH:
        None
    if IMG_PATH:
        drawPixel(IMG_PATH)