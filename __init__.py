from mycroft import MycroftSkill, intent_file_handler


class FollowMe(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('me.follow.intent')
    def handle_me_follow(self, message):
        self.speak_dialog('me.follow')


def create_skill():
    return FollowMe()

