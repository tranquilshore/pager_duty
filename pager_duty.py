
'''
Entities:
    
Team:
    id,name
Developer:
    id,name,phone_number

devteam
devid - teamid

    
Abstract Class:

GeneralPager:
    create team (team name, list of developers)
    receive alert (team id)
    notify (phone number, message)

'''
from team import Team
from developer import Developer
from pager_impl import PagerImpl

if __name__=="__main__":
    team_info = "team"
    pager = PagerImpl()
    
    while team_info:
        team_info = input("Enter team info: ")
        team_info_list = team_info.split(',')
        if len(team_info_list)>1:
            team = Team(int(team_info_list[0]), team_info_list[1])
            devs = []
            dev_info = "dev"
            while dev_info:
                dev_info = input("Enter dev info: ")
                dev_info_list = dev_info.split(',')
                if len(dev_info_list)>1:
                    developer = Developer(int(dev_info_list[0]),int(dev_info_list[1]),dev_info_list[2],int(dev_info_list[3]))
                    devs.append(developer)
            
            pager.create_team(team,devs)
        
    team_alert = "alert"
    while team_alert:
        team_alert = input("Enter team id to send alert: ")
        if team_alert:
            print(pager.receive_alert(int(team_alert)))
    
