from moviepy.editor import *


def convert(mp4_file, mp3_file):
    videoClip = VideoFileClip(mp4_file)
    audioClip = videoClip.audio
    audioClip.write_audiofile(mp3_file)
    audioClip.close()
    videoClip.close()


if __name__ == '__main__':
    mp4_file = "data/SampleVideo_360x240_1mb.mp4"
    mp3_file = "output/SampleVideo_360x240_1mb.mp3"
    convert(mp4_file, mp3_file)