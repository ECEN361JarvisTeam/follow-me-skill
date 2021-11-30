from mycroft import MycroftSkill, intent_file_handler
import face_recog_functions as frf
import os
import threading
import maestro
import cv2 as cv


class FollowMe(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.stopLoop = False
        self.stopLoopLock = threading.Lock()

    @intent_file_handler('me.follow.intent')
    def handle_me_follow(self, message):
        followName = message.data.get("name")
        
        if not followName == "me":
            self.speak_dialog("me.follow.wait")
        
        videoInput = cv.VideoCapture(0)
        m = maestro.Controller("/dev/ttyACM0")
        frf.panTiltTrackLoop(m, videoInput, frf.mycroftFacesPath, self, followName)
        self.speak_dialog("me.follow.stop")
        videoInput.release()

    def converse(self, message):
        if message.data["utterances"][0] == "stop":
            self.stopLoopLock.acquire()
            self.stopLoop = True
            self.stopLoopLock.release()
            return True

def create_skill():
    return FollowMe()

