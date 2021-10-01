import os
import random
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []


def getVideos():
    global videos
    videos = []
    for file in sorted(os.listdir(directory)):
        if file.lower().endswith('.mkv'):
            videos.append(os.path.join(directory, file))


def playVideos():
    global videos
    if len(videos) == 0:
        getVideos()
        time.sleep(5)
        return
    index = random.randint(0, len(videos)-1)
    videos = videos[index:] + videos[:index]
    for video in videos:
        playProcess = Popen(['omxplayer', '--no-osd', '--aspect-mode', 'fill', video])
        playProcess.wait()


while (True):
    playVideos()
