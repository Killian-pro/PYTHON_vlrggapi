from os import name
import requests
from bs4 import BeautifulSoup
from requests.api import head

class Team:
    """
    Gets all info related to teams
    """
    def team(id):
        
        URL = 'https://www.vlr.gg/team/'+id
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        header_info = {}
        roster_info = []
        matches_info = []
        
        def basic_info():
            """
            Gets basic info based on the team id
            """
            header = soup.find_all('div', class_='team-header')[0]
            header_info['name'] = soup.find_all('div',class_='team-header-name')[0].find_all('h1')[0].get_text().strip()
            if len(soup.find_all('div',class_='team-header-name')[0].find_all('h2')) > 0:
                header_info['short_name'] = soup.find_all('div',class_='team-header-name')[0].find_all('h2')[0].get_text().strip()
            else:
                header_info['short_name'] = ""
            logo = header.find_all('div', class_='team-header-logo')[0].find_all('img')[0]['src']
            if logo == '/img/vlr/tmp/vlr.png':
               header_info['logo']  = "https://vlr.gg" + logo
            else:
               header_info['logo']  = "https:" + logo 
            if len(soup.find_all('div',class_='team-header-website')) > 0:
                header_info['website'] = "https://" + soup.find_all('div',class_='team-header-website')[0].find_all('a')[0].get_text().strip()
            header_info['country'] = soup.find_all('div',class_='team-header-country')[0].get_text().strip()
            if len(soup.find_all('div',class_='team-header-twitter')) > 0:
                header_info['twitter'] = soup.find_all('div',class_='team-header-twitter')[0].find_all('a')[0]['href']
            header_info['country'] = soup.find_all('div',class_='team-header-country')[0].find_all('i',class_=True)[0]['class'][1].split('-')[-1]
        
        def roster():
            """
            Gets Teaam specific roster info
            """
            roster = soup.find_all('div', class_ = 'team-roster-item')
            for roster_item in roster :
                alias_name = roster_item.find_all('div',class_='team-roster-item-name-alias')[0].get_text().strip()
                roster_player = {}
                roster_player['id'] = roster_item.find('a')['href'].split('/')[2]
                roster_player['alias_name'] = alias_name
                if len(roster_item.find_all('div',class_='team-roster-item-name-real')) > 0:
                    roster_player['real_name'] = roster_item.find_all('div',class_='team-roster-item-name-real')[0].get_text().strip()
                roster_player['country'] = roster_item.find_all('div',class_='team-roster-item-name-alias')[0].find_all('i',class_=True)[0]['class'][1].split('-')[-1]
                roster_player['is_captain'] = False
                if len(roster_item.find_all('i',class_='fa-star')) >0 :
                    roster_player['is_captain'] = True
                
                roster_player['player_pic'] = roster_item.find_all('div',class_='team-roster-item-img')[0].find_all('img')[0]['src']
                if roster_player['player_pic'] == '/img/base/ph/sil.png' :
                    roster_player['player_pic'] = 'https://www.vlr.gg'+ roster_player['player_pic']
                else:
                    roster_player['player_pic'] = 'https:'+ roster_player['player_pic']
                roster_player['player_pic'] = roster_player['player_pic']
                roster_player['player_role'] = "active"
                if len(roster_item.find_all('div',class_='team-roster-item-name-role')) > 0:
                    roster_player['player_role'] = roster_item.find_all('div',class_='team-roster-item-name-role')[0].get_text().strip()
                roster_info.append(roster_player)

        def  Matches():
            """
            Gets Matches team
            """
            matches_url = 'https://www.vlr.gg/team/Matches/' + id
            matches_page = requests.get(matches_url)
            bs = BeautifulSoup(matches_page.content,'html.parser')

            match = bs.find_all('a',class_="wf-card fc-flex m-item")
            for match_item in match :
                match_info = {}
                match_info['team_name'] = match_item.find_all('span',class_='m-item-team-name')[0].get_text().strip()
                match_info['team_logo'] = match_item.find_all('div',class_='m-item-logo')[0].find_all('img')[0]['src']
                match_info['team_ennemy'] = match_item.find_all('span',class_='m-item-team-name')[1].get_text().strip()
                match_info['logo_ennemy'] = match_item.find_all('div',class_='m-item-logo')[1].find_all('img')[0]['src']
                match_info['score'] =match_item.find('div',class_='m-item-result').get_text().strip().replace('\n',"")
                matches_info.append(match_info)

        basic_info()
        roster()
        Matches()
        team = header_info
        team['id'] = id
        team['roster'] = roster_info
        team['matches'] = matches_info
        return team
