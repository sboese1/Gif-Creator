from moviepy.editor import *

video = input("Enter the name of the video file (include extension): ")
length = int(input("How long do you want the gif to be in seconds? "))
name = input("What do you want the name of the file to be? ")
clip = VideoFileClip(video)
clip = clip.subclip(0, length)
clip.write_gif(name + ".gif")
