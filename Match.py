import random

class Match_Engine:
    def __init__(self,name_home,name_away,home,away):
        self.home=home
        self.away=away
        self.name_home=name_home
        self.name_away=name_away
        self.home_goal=0
        self.away_goal=0
        self.home_pass=0
        self.away_pass=0
        self.home_shots=0
        self.away_shots=0
        self.home_shots_on_target=0
        self.away_shots_on_target=0
        self.home_yellow=0
        self.away_yellow=0
        self.home_red=0
        self.away_red=0
        self.pause=False
        self.minute=0
        self.second_half=False
    def add_minute(self):
        self.minute+=1
    def add_home_goal(self):
        self.home_goal+=1
    def add_away_goal(self):
        self.away_goal+=1
    def add_home_pass(self):
        self.home_pass+=1
    def add_away_pass(self):
        self.away_pass+=1
    def add_home_shots(self):
        self.home_shots+=1
    def add_away_shots(self):
        self.away_shots+=1
    def add_home_shots_on_target(self):
        self.home_shots_on_target+=1
    def add_away_shots_on_target(self):
        self.away_shots_on_target+=1
    def add_home_yellow(self):
        self.home_yellow+=1
    def add_away_yellow(self):
        self.away_yellow+=1
    def add_home_red(self):
        self.home_red+=1
    def add_away_red(self):
        self.away_red+=1
    def overall_home(self):
        Overall=0
        for Player in self.home['starting']:
            Overall=Overall+Player['overall']
        Team_Overall=Overall//len(self.home['starting'])
        return Team_Overall
    def overall_away(self):
        Overall=0
        for Player in self.away['starting']:
            Overall=Overall+Player['overall']
        Team_Overall=Overall//len(self.away['starting'])
        return Team_Overall
    def attacking_home(self):
        power=0
        count=0
        for player in self.home['starting']:
            if player['position']!='GK':
                if player['position']=='ST':
                    power=power+(player['shooting']*0.4+player['dribbling']*0.3+player['pace']*0.2+player['passing']*0.1)+8
                    count+=1
                if player['position'] in ['RW','LW']:
                    power=power+(player['shooting']*0.4+player['dribbling']*0.3+player['pace']*0.2+player['passing']*0.1)+6
                    count+=1
                if player['position']=='CAM':
                    power=power+(player['shooting']*0.4+player['dribbling']*0.3+player['pace']*0.2+player['passing']*0.1)+5
                    count+=1
                if player['position']=='CM':
                    power=power+(player['shooting']*0.4+player['dribbling']*0.3+player['pace']*0.2+player['passing']*0.1)+2
                    count+=1
                if player['position']=='CDM':
                    power=power+(player['shooting']*0.4+player['dribbling']*0.3+player['pace']*0.2+player['passing']*0.1)-2
                    count+=1
                if player['position'] in ['RB','LB']:
                    power=power+(player['shooting']*0.4+player['dribbling']*0.3+player['pace']*0.2+player['passing']*0.1)-4
                    count+=1
                if player['position']=='CB':
                    power=power+(player['shooting']*0.4+player['dribbling']*0.3+player['pace']*0.2+player['passing']*0.1)-8
                    count+=1
        Attacking_Power=round(power/count)
        return Attacking_Power
    def attacking_away(self):
        power=0
        count=0
        for player in self.away['starting']:
            if player['position']!='GK':
                if player['position']=='ST':
                    power=power+(player['shooting']*0.40+player['dribbling']*0.20+player['pace']*0.20+player['passing']*0.15+player['physical']*0.05)+8
                    count+=1
                if player['position'] in ['RW','LW']:
                    power=power+(player['shooting']*0.40+player['dribbling']*0.20+player['pace']*0.20+player['passing']*0.15+player['physical']*0.05)+6
                    count+=1
                if player['position']=='CAM':
                    power=power+(player['shooting']*0.40+player['dribbling']*0.20+player['pace']*0.20+player['passing']*0.15+player['physical']*0.05)+5
                    count+=1
                if player['position']=='CM':
                    power=power+(player['shooting']*0.40+player['dribbling']*0.20+player['pace']*0.20+player['passing']*0.15+player['physical']*0.05)+2
                    count+=1
                if player['position']=='CDM':
                    power=power+(player['shooting']*0.40+player['dribbling']*0.20+player['pace']*0.20+player['passing']*0.15+player['physical']*0.05)-2
                    count+=1
                if player['position'] in ['RB','LB']:
                    power=power+(player['shooting']*0.40+player['dribbling']*0.20+player['pace']*0.20+player['passing']*0.15+player['physical']*0.05)-4
                    count+=1
                if player['position']=='CB':
                    power=power+(player['shooting']*0.40+player['dribbling']*0.20+player['pace']*0.20+player['passing']*0.15+player['physical']*0.05)-8
                    count+=1
        Attacking_Power=round(power/count)
        return Attacking_Power
    def defending_home(self):
        power=0
        for player in self.home['starting']:
            if player['position']=='GK':
                power=power+(player['diving']*0.25+player['handling']*0.20+player['reflexes']*0.25+player['positioning']*0.20+player['kicking']*0.05+player['speed']*0.05)+8
            if player['position'] in ['RB','LB']:
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)+5
            if player['position']=='CB':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)+6
            if player['position']=='CDM':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)+3
            if player['position']=='CM':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)
            if player['position']=='CAM':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)-4
            if player['position'] in ['RW','LW']:
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)-6
            if player['position']=='ST':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)-8
        Defending_Power=round(power/len(self.home['starting']))
        return Defending_Power
    def defending_away(self):
        power=0
        for player in self.away['starting']:
            if player['position']=='GK':
                power=power+(player['diving']*0.25+player['handling']*0.20+player['reflexes']*0.25+player['positioning']*0.20+player['kicking']*0.05+player['speed']*0.05)+8
            if player['position'] in ['RB','LB']:
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)+5
            if player['position']=='CB':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)+6
            if player['position']=='CDM':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)+3
            if player['position']=='CM':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)
            if player['position']=='CAM':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)-4
            if player['position'] in ['RW','LW']:
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)-6
            if player['position']=='ST':
                power=power+(player['defending']*0.6+player['physical']*0.3+player['pace']*0.1)-8
        Defending_Power=round(power/len(self.away['starting']))
        return Defending_Power
    def playmaker_home(self):
        power=0
        count=0
        for player in self.home['starting']:
            if player['position']!='GK':
                if player['position'] in ['ST','LW','RW']:
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+2
                    count+=1
                if player['position'] == 'CAM':
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+4
                    count+=1
                if player['position'] =='CM':
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+5
                    count+=1
                if player['position'] =='CDM':
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+2
                    count+=1
                if player['position'] in ['CB','LB','RB']:
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)-3
                    count+=1
        Playmaker_Power=round(power/count)
        return Playmaker_Power
    def playmaker_away(self):
        power=0
        count=0
        for player in self.away['starting']:
            if player['position']!='GK':
                if player['position'] in ['ST','LW','RW']:
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+2
                    count+=1
                if player['position'] == 'CAM':
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+4
                    count+=1
                if player['position'] =='CM':
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+5
                    count+=1
                if player['position'] =='CDM':
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)+2
                    count+=1
                if player['position'] in ['CB','LB','RB']:
                    power=power+(player['passing']*0.5+player['dribbling']*0.3+player['pace']*0.1+player['physical']*0.1)-3
                    count+=1
        Playmaker_Power=round(power/count)
        return Playmaker_Power
    def counter_home(self):
        power=0
        count=0
        for player in self.home['starting']:
            if player['position']!='GK':
                power=power+player['pace']*0.50+player['dribbling']*0.30+player['shooting']*0.20
                count+=1
        Counter_Power=round(power/count)
        return Counter_Power
    def counter_away(self):
        power=0
        count=0
        for player in self.away['starting']:
            if player['position']!='GK':
                power=power+player['pace']*0.50+player['dribbling']*0.30+player['shooting']*0.20
                count+=1
        Counter_Power=round(power/count)
        return Counter_Power
    def goalkeeper_home(self):
        Goalkeeper_power = 0
        for player in self.home['starting']:
            if player['position']=='GK':
                Goalkeeper_power=round(player['diving']*0.25+player['handling']*0.20+player['reflexes']*0.25+player['positioning']*0.20+player['kicking']*0.05+player['speed']*0.05)
        return Goalkeeper_power
    def goalkeeper_away(self):
        Goalkeeper_power = 0
        for player in self.away['starting']:
            if player['position']=='GK':
                Goalkeeper_power=round(player['diving']*0.25+player['handling']*0.20+player['reflexes']*0.25+player['positioning']*0.20+player['kicking']*0.05+player['speed']*0.05)
        return Goalkeeper_power
    def attacking_chance(self):
        home=self.attacking_home()+self.playmaker_home()
        away=self.attacking_away()+self.playmaker_away()
        total=home+away
        attacking_chance_home=home/total
        attacking_chance_away=away/total
        return attacking_chance_home,attacking_chance_away
    def attack_team(self):
        home_chance,away_chance=self.attacking_chance()
        if random.random()<home_chance:
            return 'home'
        return 'away'
    def shot_chance(self,team):
        if team =='home':
            attack=self.attacking_home()
            defense=self.defending_away()
        else:
            attack=self.attacking_away()
            defense=self.defending_home()
        chance=attack/(attack+defense)
        if random.random()<chance:
            return 'shot'
        return 'ball lost'
    def shots_on_target_chance(self,team):
        if team == 'home':
            attack=self.attacking_home()
            goalkeeper=self.goalkeeper_away()
        else:
            attack=self.attacking_away()
            goalkeeper=self.goalkeeper_home()
        chance=attack/(attack+goalkeeper)
        if random.random()<chance:
            return 'on target'
        return 'off target' 
    def goal_chance(self,team):
        if team == 'home':
            attack=self.attacking_home()
            goalkeeper=self.goalkeeper_away()
        else:
            attack=self.attacking_away()
            goalkeeper=self.goalkeeper_home()
        chance=attack/(attack+goalkeeper)
        if random.random()<chance:
            return 'goal'
        return 'save'
    def game_engine(self):
        if self.minute==45 and self.second_half==False:
            self.pause=True
            return 'half time'
        elif self.minute==90:
            return 'full time'
        self.add_minute()
        team=self.attack_team()
        if team=='home':
            self.add_home_pass()
            team_name=self.name_home
        else:
            self.add_away_pass()
            team_name=self.name_away
        if self.shot_chance(team)=='shot':
            if team=='home':
                self.add_home_shots()
            else:
                self.add_away_shots()
            if self.shots_on_target_chance(team)=='on target':
                if team=='home':
                    self.add_home_shots_on_target()
                else:
                    self.add_away_shots_on_target()
                if self.goal_chance(team)=='goal':
                    if team=='home':
                        self.add_home_goal()
                        self.add_home_pass()
                    else:
                        self.add_away_goal()
                        self.add_away_pass()
                    return f'{team_name} goal'
                return f'{team_name} save'
            return f'{team_name} off target'
        return f'{team_name} ball lost'
    def match_possession(self):
        total_possession=self.home_pass+self.away_pass
        if total_possession==0:
            return 50,50
        home_possession=round(self.home_pass*100/total_possession)
        return home_possession,100-home_possession