from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip

from random import randint


class StockFootageClipMaker:
    ''' StockFootageClipMaker is the class responsible for managing the creation of the short videos.

    Parameters:
    :param videoFilePath: The path to the stock footage video.
    :param audioFilePath: The path to the audio file.
    '''
    def __init__(self, videoFilePath: str, audioFilePath: str):
        self.videoFilePath = videoFilePath
        self.audioFilePath = audioFilePath

    def makeVideoClip(self):
        ''' Creates a movie clip that is equal length to the audio clip.
        The given movie clip will start at a random interval in the stock footage.
        '''
        videoClip = VideoFileClip(self.videoFilePath)
        audioClip = AudioFileClip(self.audioFilePath)

        videoClipLength = audioClip.duration

        videoClipStart = (randint(100, (videoClip.duration - videoClipLength) * 100)) * 0.01
        videoClipEnd = videoClipStart + videoClipLength

        print(audioClip.duration)
        print(videoClip.duration)

        videoClip = videoClip.cutout(0, videoClipStart)
        videoClip = videoClip.cutout(audioClip.duration, videoClip.duration)

        print(videoClip.duration)

        videoClip = videoClip.set_audio(audioClip)
        videoClip.write_videofile("test.mp4")

        videoClip.close()
        audioClip.close()
    