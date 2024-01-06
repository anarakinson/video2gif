import cv2
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input directory with sliced frames", default="frames")
    parser.add_argument("-o", "--output", help="output file", default="out")

    return parser.parse_args()


def convert_mp4_to_jpgs(filename, path):
    video_capture = cv2.VideoCapture(filename)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"{path}/frame_{frame_count:03d}.jpg", image)
        
        # read next image
        still_reading, image = video_capture.read()
        frame_count += 1


if __name__ == "__main__":
    args = parse_args()
    convert_mp4_to_jpgs(args.input, args.output)