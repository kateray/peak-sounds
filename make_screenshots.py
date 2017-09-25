import ass
from subprocess import call
import datetime
import sys

episode_number = str(sys.argv[1])
ass_file = "subs-" + episode_number + ".ass"
mkv_file = "Twin.Peaks.S03E" + episode_number + ".mkv"

with open(ass_file, "r") as f:
    doc = ass.parse(f)
    x = 0
    while x < len(doc.events):
        time = doc.events[x].start + datetime.timedelta(milliseconds=250)
        seconds = time.total_seconds()
        call([
            "ffmpeg",
            "-ss",
            str(time),
            "-i",
            mkv_file,
            "-copyts",
            "-af",
            "asetpts=PTS-"+str(seconds)+"/TB",
            "-vf",
            "ass="+ass_file+",setpts=PTS-"+str(seconds)+"/TB",
            "-frames:v",
            "1",
            episode_number+"-"+str(x)+".png"
        ])
        x +=1
