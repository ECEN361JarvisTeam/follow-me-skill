from mycroft import MycroftSkill, intent_file_handler
import face_recog_functions
import cv2 as cv


class FollowMe(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
	m = maestro.Controller("/dev/ttyACM0")

    @intent_file_handler('me.follow.intent')
    def handle_me_follow(self, message):
	m = maestro.controller("/dev/ttyACM0")
        #person = self.get_response('')
	panTiltTrackLoop(m, cv.VideoCapture(0))
	

def create_skill():
    return FollowMe()

