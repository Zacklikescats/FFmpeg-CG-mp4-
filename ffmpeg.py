import subprocess

print("Enter file name:")
I = input("> ")
print("Directory of file:")
SI = input("> ")
print("Enter the place where you want the file to end up.")
TI = input("> ")

command = f'ffmpeg -i {SI}/{I} -vf "scale=1280:-2,fps=30" -c:v libx264 -preset veryfast -profile:v baseline -level 3.0 -crf 28 -c:a aac -b:a 96k -movflags +faststart "{TI}/{I}.mp4"'

print("This is your command:")
print(command)
