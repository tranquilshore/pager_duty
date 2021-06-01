from general_pager import GeneralPager
from collections import defaultdict
from team import Team
from developer import Developer
import random
from notification import Notification

class PagerImpl(GeneralPager):
    def __init__(self):
        #dictionary key as team id and values as list of devs
        self.teams = defaultdict(list)
 
    def create_team(self,team,developers):
        try:
            for dev in developers:
                self.teams[team.id].append(dev)
        except:
            print("Unable to create team!")
        
    def receive_alert(self,team_id):
        try:
            selected_dev = random.choice(self.teams[team_id])
            #print(selected_dev.id, selected_dev.name)
            notification = Notification(selected_dev.phone_number,"401 Error!")
            return notification.send()
        except:
            return "Unable to send alert!"

