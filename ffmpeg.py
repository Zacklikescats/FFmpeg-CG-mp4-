import subprocess

print("Enter file name:")
DRCRTY = input("> ")
print("Directory of file:")
SI = input("> ")
print("Enter the place where you want the file to end up:")
TI = input("> ")
print("Enter FPS:")
FPS = input("> ")

command = f'ffmpeg -i "{SI}/{DRCRTY}" -vf "scale=1280:-2,fps={FPS}" -c:v libx264 -preset veryfast -profile:v baseline -level 3.0 -crf 28 -c:a aac -b:a 96k -movflags +faststart "{TI}/{DRCRTY}-processed.mp4"'

print("This is your command:")
print(command)
