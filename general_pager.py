
'''
Entities:
    
Team:
    id,name
Developer:
    id,team_id,name,phone_number
    
Abstract Class:

GeneralPager:
    create team (team name, list of developers)
    receive alert (team id)
    notify (phone number, message)

'''
from abc import ABC, abstractmethod

class GeneralPager(ABC):
    @abstractmethod
    def create_team(self,team_name,developers): pass
    @abstractmethod
    def receive_alert(self,team_id): pass
