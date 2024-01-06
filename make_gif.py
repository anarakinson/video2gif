import glob
from PIL import Image
import argparse


h = 720 // 4
w = 1280 // 4

def make_gif(frame_folder, output_name):
    images = glob.glob(f"{frame_folder}/*.jpg")
    images.sort()
    frames = [Image.open(image).resize((w, h), Image.Resampling.LANCZOS) for image in images]
    frame_one = frames[0]
    frame_one.save(f"{output_name}.gif", format="GIF", append_images=frames,
                   save_all=True, duration=50, loop=0)
    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input directory with sliced frames", default="frames")
    parser.add_argument("-o", "--output", help="output file", default="out")

    return parser.parse_args()



if __name__ == "__main__":
    args = parse_args()
    make_gif(args.input, args.output)
