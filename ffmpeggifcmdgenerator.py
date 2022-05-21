import pyperclip
ogVid = input("what is the name of the video? ")
fps = input("what is the fps? ")
scale = input("what is the height? ")
loop = input("loopable(-1 for no, 0 for yes)? ")

skip = input("how much time to skip(just press enter for nothing)? ")
if skip == "":
    skipTime = ""
else:
    skipTime = "-ss {} ".format(skip)

time = input("duration of the gif(press enter to change nothing)? ")
if time == "":
    timeLast = ""
else:
    timeLast = "-t {} ".format(time)

outputName = input("what do you want to call the gif? ")

output1 = 'ffmpeg {}{}-i {}.mp4 -vf '.format(skipTime, timeLast, ogVid)
output2 = '"fps={},scale={}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"'.format(
    fps, scale)
output3 = ' -loop {} {}.gif'.format(loop, outputName)
output = output1 + output2 + output3
print("Your output is:")
print(output)
pyperclip.copy(output)
input("output copied, press enter to exit")
