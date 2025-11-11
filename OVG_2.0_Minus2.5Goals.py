import requests
import pandas as pd
from bs4 import BeautifulSoup
import re, os
import statistics
from datetime import datetime, timedelta

##################################################################################################################
##Generates DataFrames with the original DataFrames OverUnderGoalsTotalFullTime, OverUnderGoalsLast8FullTime, OverUnderGoalsHomeFullTime, OverUnderGoalsAwayFullTime
##Sorted by percentage of games with 2.5- goals.
# URL of the page to scrape
argentina_url = 'https://www.soccerstats.com/table.asp?league=argentina&tid=c'
argentina5_url = 'https://www.soccerstats.com/table.asp?league=argentina5&tid=c'
austria_url = 'https://www.soccerstats.com/table.asp?league=austria&tid=c'
austria2_url = 'https://www.soccerstats.com/table.asp?league=austria2&tid=c'
belgium_url = 'https://www.soccerstats.com/table.asp?league=belgium&tid=c'
belgium2_url = 'https://www.soccerstats.com/table.asp?league=belgium2&tid=c'
brazil_url = 'https://www.soccerstats.com/table.asp?league=brazil&tid=c'
brazil2_url = 'https://www.soccerstats.com/table.asp?league=brazil2&tid=c'
bulgaria_url = 'https://www.soccerstats.com/table.asp?league=bulgaria&tid=c'
canada_url = 'https://www.soccerstats.com/table.asp?league=canada&tid=c'
chile_url = 'https://www.soccerstats.com/table.asp?league=chile&tid=c'
chile2_url = 'https://www.soccerstats.com/table.asp?league=chile2&tid=c'
colombia2_url = 'https://www.soccerstats.com/table.asp?league=colombia2&tid=c'
costarica_url = 'https://www.soccerstats.com/table.asp?league=costarica&tid=c'
croatia_url = 'https://www.soccerstats.com/table.asp?league=croatia&tid=c'
croatia2_url = 'https://www.soccerstats.com/table.asp?league=croatia2&tid=c'
cyprus_url = 'https://www.soccerstats.com/table.asp?league=cyprus&tid=c'
czechrepublic_url = 'https://www.soccerstats.com/table.asp?league=czechrepublic&tid=c'
czechrepublic2_url = 'https://www.soccerstats.com/table.asp?league=czechrepublic2&tid=c'
denmark_url = 'https://www.soccerstats.com/table.asp?league=denmark&tid=c'
denmark2_url = 'https://www.soccerstats.com/table.asp?league=denmark2&tid=c'
ecuador3_url = 'https://www.soccerstats.com/table.asp?league=ecuador3&tid=c'
england_url = 'https://www.soccerstats.com/table.asp?league=england&tid=c'
england2_url = 'https://www.soccerstats.com/table.asp?league=england2&tid=c'
england3_url = 'https://www.soccerstats.com/table.asp?league=england3&tid=c'
finland_url = 'https://www.soccerstats.com/table.asp?league=finland&tid=c'
finland2_url = 'https://www.soccerstats.com/table.asp?league=finland2&tid=c'
france_url = 'https://www.soccerstats.com/table.asp?league=france&tid=c'
france2_url = 'https://www.soccerstats.com/table.asp?league=france2&tid=c'
france3_url = 'https://www.soccerstats.com/table.asp?league=france3&tid=c'
germany_url = 'https://www.soccerstats.com/table.asp?league=germany&tid=c'
germany2_url = 'https://www.soccerstats.com/table.asp?league=germany2&tid=c'
germany3_url = 'https://www.soccerstats.com/table.asp?league=germany3&tid=c'
greece_url = 'https://www.soccerstats.com/table.asp?league=greece&tid=c'
guatemala_url = 'https://www.soccerstats.com/table.asp?league=guatemala&tid=c'
hungary_url = 'https://www.soccerstats.com/table.asp?league=hungary&tid=c'
hungary2_url = 'https://www.soccerstats.com/table.asp?league=hungary2&tid=c'
iceland_url = 'https://www.soccerstats.com/table.asp?league=iceland&tid=c'
ireland_url = 'https://www.soccerstats.com/table.asp?league=ireland&tid=c'
ireland2_url = 'https://www.soccerstats.com/table.asp?league=ireland2&tid=c'
israel_url = 'https://www.soccerstats.com/table.asp?league=israel&tid=c'
italy_url = 'https://www.soccerstats.com/table.asp?league=italy&tid=c'
italy2_url = 'https://www.soccerstats.com/table.asp?league=italy2&tid=c'
italy3_url = 'https://www.soccerstats.com/table.asp?league=italy3&tid=c'
japan_url = 'https://www.soccerstats.com/table.asp?league=japan&tid=c'
japan2_url = 'https://www.soccerstats.com/table.asp?league=japan2&tid=c'
jordan_url = 'https://www.soccerstats.com/table.asp?league=jordan&tid=c'
kuwait_url = 'https://www.soccerstats.com/table.asp?league=kuwait&tid=c'
mexico_url = 'https://www.soccerstats.com/table.asp?league=mexico&tid=c'
mexico2_url = 'https://www.soccerstats.com/table.asp?league=mexico2&tid=c'
netherlands_url = 'https://www.soccerstats.com/table.asp?league=netherlands&tid=c'
netherlands2_url = 'https://www.soccerstats.com/table.asp?league=netherlands2&tid=c'
northernireland_url = 'https://www.soccerstats.com/table.asp?league=northernireland&tid=c'
norway_url = 'https://www.soccerstats.com/table.asp?league=norway&tid=c'
norway2_url = 'https://www.soccerstats.com/table.asp?league=norway2&tid=c'
oman_url = 'https://www.soccerstats.com/table.asp?league=oman&tid=c'
paraguay2_url = 'https://www.soccerstats.com/table.asp?league=paraguay2&tid=c'
peru2_url = 'https://www.soccerstats.com/table.asp?league=peru2&tid=c'
poland_url = 'https://www.soccerstats.com/table.asp?league=poland&tid=c'
poland2_url = 'https://www.soccerstats.com/table.asp?league=poland2&tid=c'
portugal_url = 'https://www.soccerstats.com/table.asp?league=portugal&tid=c'
portugal2_url = 'https://www.soccerstats.com/table.asp?league=portugal2&tid=c'
qatar_url = 'https://www.soccerstats.com/table.asp?league=qatar&tid=c'
romania_url = 'https://www.soccerstats.com/table.asp?league=romania&tid=c'
saudiarabia_url = 'https://www.soccerstats.com/table.asp?league=saudiarabia&tid=c'
scotland_url = 'https://www.soccerstats.com/table.asp?league=scotland&tid=c'
scotland2_url = 'https://www.soccerstats.com/table.asp?league=scotland2&tid=c'
slovakia_url = 'https://www.soccerstats.com/table.asp?league=slovakia&tid=c'
slovenia_url = 'https://www.soccerstats.com/table.asp?league=slovenia&tid=c'
southkorea_url = 'https://www.soccerstats.com/table.asp?league=southkorea&tid=c'
southkorea2_url = 'https://www.soccerstats.com/table.asp?league=southkorea2&tid=c'
spain_url = 'https://www.soccerstats.com/table.asp?league=spain&tid=c'
spain2_url = 'https://www.soccerstats.com/table.asp?league=spain2&tid=c'
sweden_url = 'https://www.soccerstats.com/table.asp?league=sweden&tid=c'
sweden2_url = 'https://www.soccerstats.com/table.asp?league=sweden2&tid=c'
switzerland_url = 'https://www.soccerstats.com/table.asp?league=switzerland&tid=c'
switzerland2_url = 'https://www.soccerstats.com/table.asp?league=switzerland2&tid=c'
thailand_url = 'https://www.soccerstats.com/table.asp?league=thailand&tid=c'
turkey_url = 'https://www.soccerstats.com/table.asp?league=turkey&tid=c'
turkey2_url = 'https://www.soccerstats.com/table.asp?league=turkey2&tid=c'
ukraine_url = 'https://www.soccerstats.com/table.asp?league=ukraine&tid=c'
unitedarabemirates_url = 'https://www.soccerstats.com/table.asp?league=unitedarabemirates&tid=c'
uruguay_url = 'https://www.soccerstats.com/table.asp?league=uruguay&tid=c'
usa_url = 'https://www.soccerstats.com/table.asp?league=usa&tid=c'
usa2_url = 'https://www.soccerstats.com/table.asp?league=usa2&tid=c'
venezuela_url = 'https://www.soccerstats.com/table.asp?league=venezuela&tid=c'
wales_url = 'https://www.soccerstats.com/table.asp?league=wales&tid=c'

ListUrls = [argentina_url,argentina5_url,austria_url,austria2_url,belgium_url,belgium2_url,brazil_url,brazil2_url,bulgaria_url,canada_url,chile_url,chile2_url,colombia2_url,costarica_url,croatia_url,czechrepublic_url,czechrepublic2_url,denmark_url,denmark2_url,ecuador3_url,england_url,england2_url,england3_url,finland2_url,france_url,france2_url,germany2_url,germany3_url,guatemala_url,hungary_url,hungary2_url,iceland_url,ireland_url,ireland2_url,japan_url,japan2_url,mexico_url,netherlands_url,netherlands2_url,northernireland_url,norway_url,norway2_url,paraguay2_url,peru2_url,poland_url,poland2_url,portugal_url,portugal2_url,qatar_url,romania_url,scotland_url,scotland2_url,slovenia_url,southkorea_url,southkorea2_url,sweden_url,sweden2_url,switzerland_url,switzerland2_url,thailand_url,usa_url,usa2_url]
Continent =['America','America','Europe','Europe','Europe','Europe','America','America','Europe','America','America','America','America','America','Europe','Europe','Europe','Europe','Europe','America','Europe','Europe','Europe','Europe','Europe','Europe','Europe','Europe','America','Europe','Europe','Europe','Europe','Europe','Asia','Asia','America','Europe','Europe','Europe','Europe','Europe','America','America','Europe','Europe','Europe','Europe','Asia','Europe','Europe','Europe','Europe','Asia','Asia','Europe','Europe','Europe','Europe','Asia','America','America']
League = ['Argentina (D1)','Argentina (D2)','Austria (D1)','Austria (D2)','Belgium (D1)','Belgium (D2)','Brazil (D1)','Brazil (D2)','Bulgaria (D1)','Canada (D1)','Chile (D1)','Chile (D2)','Colombia (D1, Clausura)','Costa Rica (D1, Apertura)','Croatia (D1)','Czech Republic (D1)','Czech Republic (D2)','Denmark (D1)','Denmark (D2)','Ecuador (D1)','England (D1)','England (D2)','England (D3)','Finland (D2)','France (D1)','France (D2)','Germany (D2)','Germany (D3)','Guatemala (D1, Apertura)','Hungary (D1)','Hungary (D2)','Iceland (D1)','Ireland (D1)','Ireland (D2)','Japan (D1)','Japan (D2)','Mexico (D1)','Netherlands (D1)','Netherlands (D2)','Northern Ireland (D1)','Norway (D1)','Norway (D2)','Paraguay (D1, Apertura)','Peru (D1, Apertura)','Poland (D1)','Poland (D2)','Portugal (D1)','Portugal (D2)','Qatar (D1)','Romania (D1)','Scotland (D1)','Scotland (D2)','Slovenia (D1)','South Korea (D1)','South Korea (D2)','Sweden (D1)','Sweden (D2)','Switzerland (D1)','Switzerland (D2)','Thailand (D1)','USA (D1)','USA (D2)']

rowsTotalFullTime = []
rowsLast8FullTime = []
rowsHomeFullTime = []
rowsAwayFullTime = []

IndexContLeague = 0
for i in ListUrls:
    # Perform the GET request
    response = requests.get(i)
    if response.status_code != 200:
        print(i)

# Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the desired stats
    tables = soup.find_all('table', {'id': 'btable'})

    rows = []
    # Lists to store the categorized data
    for table in tables:
        for tr in table.find_all('tr')[1:]:  # Skip the header row
            cells = tr.find_all('td')
            row = [cell.text.strip() for cell in cells]
            rows.append(row)
    rows = [sublist for sublist in rows if any('%' in item for item in sublist)]
    rows = [sublist for sublist in rows if 'League average' not in sublist]

    # Dictionary to count occurrences of each team
    team_counts = {}

    # Iterate through each sublist in the data
    for sublist in rows:
        team = sublist[0]

        # Initialize the team count if not already in dictionary
        if team not in team_counts:
            team_counts[team] = 0

        # Increment the count for the team
        team_counts[team] += 1

        # Place the sublist in the correct list based on the count
        if team_counts[team] == 1:
            sublist.insert(0,Continent[IndexContLeague])
            sublist.insert(1, League[IndexContLeague])
            rowsTotalFullTime.append(sublist)
        elif team_counts[team] == 2:
            sublist.insert(0,Continent[IndexContLeague])
            sublist.insert(1, League[IndexContLeague])
            rowsLast8FullTime.append(sublist)
        elif team_counts[team] == 3:
            sublist.insert(0,Continent[IndexContLeague])
            sublist.insert(1, League[IndexContLeague])
            rowsHomeFullTime.append(sublist)
        elif team_counts[team] == 4:
            sublist.insert(0,Continent[IndexContLeague])
            sublist.insert(1, League[IndexContLeague])
            rowsAwayFullTime.append(sublist)
    IndexContLeague += 1

headers = ["Continent","League","Team","GP","Avg","0.5+","1.5+","2.5+","3.5+","4.5+","5.5+","BTS","CS","FTS","WTN","LTN"]

dfOverUnderGoalsTotalFullTime = pd.DataFrame(rowsTotalFullTime, columns=headers)
dfOverUnderGoalsLast8FullTime = pd.DataFrame(rowsLast8FullTime, columns=headers)
dfOverUnderGoalsHomeFullTime = pd.DataFrame(rowsHomeFullTime, columns=headers)
dfOverUnderGoalsAwayFullTime = pd.DataFrame(rowsAwayFullTime, columns=headers)

# Replace '%' with an empty string and convert the columns to integers
columns_to_convert = ['0.5+', '1.5+', '2.5+', '3.5+', '4.5+', '5.5+', 'BTS', 'CS', 'FTS', 'WTN', 'LTN']
# Remove the '%' character and convert to integer
for column in columns_to_convert:
    dfOverUnderGoalsTotalFullTime[column] = dfOverUnderGoalsTotalFullTime[column].str.replace('%', '').astype(int)
    dfOverUnderGoalsLast8FullTime[column] = dfOverUnderGoalsLast8FullTime[column].str.replace('%', '').astype(int)
    dfOverUnderGoalsHomeFullTime[column] = dfOverUnderGoalsHomeFullTime[column].str.replace('%', '').astype(int)
    dfOverUnderGoalsAwayFullTime[column] = dfOverUnderGoalsAwayFullTime[column].str.replace('%', '').astype(int)

# Sort the DataFrame by the '2.5+' column in descending order
dfOverUnderGoalsTotalFullTime = dfOverUnderGoalsTotalFullTime.sort_values(by=['2.5+','GP'], ascending=[False,False])
dfOverUnderGoalsTotalFullTime.reset_index(drop=True,inplace=True)
dfOverUnderGoalsLast8FullTime = dfOverUnderGoalsLast8FullTime.sort_values(by=['2.5+','GP'], ascending=[False,False])
dfOverUnderGoalsLast8FullTime.reset_index(drop=True,inplace=True)
dfOverUnderGoalsHomeFullTime = dfOverUnderGoalsHomeFullTime.sort_values(by=['2.5+','GP'], ascending=[False,False])
dfOverUnderGoalsHomeFullTime.reset_index(drop=True,inplace=True)
dfOverUnderGoalsAwayFullTime = dfOverUnderGoalsAwayFullTime.sort_values(by=['2.5+','GP'], ascending=[False,False])
dfOverUnderGoalsAwayFullTime.reset_index(drop=True,inplace=True)

###############################################################################################################################################################
##Generates DataFrames with the original DataFrames with the previous results and fixtures.
argentina_url_byDate = 'https://www.soccerstats.com/results.asp?league=argentina&pmtype=bydate'
argentina5_url_byDate = 'https://www.soccerstats.com/results.asp?league=argentina5&pmtype=bydate'
austria_url_byDate = 'https://www.soccerstats.com/results.asp?league=austria&pmtype=bydate'
austria2_url_byDate = 'https://www.soccerstats.com/results.asp?league=austria2&pmtype=bydate'
belgium_url_byDate = 'https://www.soccerstats.com/results.asp?league=belgium&pmtype=bydate'
belgium2_url_byDate = 'https://www.soccerstats.com/results.asp?league=belgium2&pmtype=bydate'
brazil_url_byDate = 'https://www.soccerstats.com/results.asp?league=brazil&pmtype=bydate'
brazil2_url_byDate = 'https://www.soccerstats.com/results.asp?league=brazil2&pmtype=bydate'
bulgaria_url_byDate = 'https://www.soccerstats.com/results.asp?league=bulgaria&pmtype=bydate'
canada_url_byDate = 'https://www.soccerstats.com/results.asp?league=canada&pmtype=bydate'
chile_url_byDate = 'https://www.soccerstats.com/results.asp?league=chile&pmtype=bydate'
chile2_url_byDate = 'https://www.soccerstats.com/results.asp?league=chile2&pmtype=bydate'
colombia2_url_byDate = 'https://www.soccerstats.com/results.asp?league=colombia2&pmtype=bydate'
costarica_url_byDate = 'https://www.soccerstats.com/results.asp?league=costarica&pmtype=bydate'
croatia_url_byDate = 'https://www.soccerstats.com/results.asp?league=croatia&pmtype=bydate'
croatia2_url_byDate = 'https://www.soccerstats.com/results.asp?league=croatia2&pmtype=bydate'
cyprus_url_byDate = 'https://www.soccerstats.com/results.asp?league=cyprus&pmtype=bydate'
czechrepublic_url_byDate = 'https://www.soccerstats.com/results.asp?league=czechrepublic&pmtype=bydate'
czechrepublic2_url_byDate = 'https://www.soccerstats.com/results.asp?league=czechrepublic2&pmtype=bydate'
denmark_url_byDate = 'https://www.soccerstats.com/results.asp?league=denmark&pmtype=bydate'
denmark2_url_byDate = 'https://www.soccerstats.com/results.asp?league=denmark2&pmtype=bydate'
ecuador3_url_byDate = 'https://www.soccerstats.com/results.asp?league=ecuador3&pmtype=bydate'
england_url_byDate = 'https://www.soccerstats.com/results.asp?league=england&pmtype=bydate'
england2_url_byDate = 'https://www.soccerstats.com/results.asp?league=england2&pmtype=bydate'
england3_url_byDate = 'https://www.soccerstats.com/results.asp?league=england3&pmtype=bydate'
finland_url_byDate = 'https://www.soccerstats.com/results.asp?league=finland&pmtype=bydate'
finland2_url_byDate = 'https://www.soccerstats.com/results.asp?league=finland2&pmtype=bydate'
france_url_byDate = 'https://www.soccerstats.com/results.asp?league=france&pmtype=bydate'
france2_url_byDate = 'https://www.soccerstats.com/results.asp?league=france2&pmtype=bydate'
france3_url_byDate = 'https://www.soccerstats.com/results.asp?league=france3&pmtype=bydate'
germany_url_byDate = 'https://www.soccerstats.com/results.asp?league=germany&pmtype=bydate'
germany2_url_byDate = 'https://www.soccerstats.com/results.asp?league=germany2&pmtype=bydate'
germany3_url_byDate = 'https://www.soccerstats.com/results.asp?league=germany3&pmtype=bydate'
greece_url_byDate = 'https://www.soccerstats.com/results.asp?league=greece&pmtype=bydate'
guatemala_url_byDate = 'https://www.soccerstats.com/results.asp?league=guatemala&pmtype=bydate'
hungary_url_byDate = 'https://www.soccerstats.com/results.asp?league=hungary&pmtype=bydate'
hungary2_url_byDate = 'https://www.soccerstats.com/results.asp?league=hungary2&pmtype=bydate'
iceland_url_byDate = 'https://www.soccerstats.com/results.asp?league=iceland&pmtype=bydate'
ireland_url_byDate = 'https://www.soccerstats.com/results.asp?league=ireland&pmtype=bydate'
ireland2_url_byDate = 'https://www.soccerstats.com/results.asp?league=ireland2&pmtype=bydate'
israel_url_byDate = 'https://www.soccerstats.com/results.asp?league=israel&pmtype=bydate'
italy_url_byDate = 'https://www.soccerstats.com/results.asp?league=italy&pmtype=bydate'
italy2_url_byDate = 'https://www.soccerstats.com/results.asp?league=italy2&pmtype=bydate'
italy3_url_byDate = 'https://www.soccerstats.com/results.asp?league=italy3&pmtype=bydate'
japan_url_byDate = 'https://www.soccerstats.com/results.asp?league=japan&pmtype=bydate'
japan2_url_byDate = 'https://www.soccerstats.com/results.asp?league=japan2&pmtype=bydate'
jordan_url_byDate = 'https://www.soccerstats.com/results.asp?league=jordan&pmtype=bydate'
kuwait_url_byDate = 'https://www.soccerstats.com/results.asp?league=kuwait&pmtype=bydate'
mexico_url_byDate = 'https://www.soccerstats.com/results.asp?league=mexico&pmtype=bydate'
mexico2_url_byDate = 'https://www.soccerstats.com/results.asp?league=mexico2&pmtype=bydate'
netherlands_url_byDate = 'https://www.soccerstats.com/results.asp?league=netherlands&pmtype=bydate'
netherlands2_url_byDate = 'https://www.soccerstats.com/results.asp?league=netherlands2&pmtype=bydate'
northernireland_url_byDate = 'https://www.soccerstats.com/results.asp?league=northernireland&pmtype=bydate'
norway_url_byDate = 'https://www.soccerstats.com/results.asp?league=norway&pmtype=bydate'
norway2_url_byDate = 'https://www.soccerstats.com/results.asp?league=norway2&pmtype=bydate'
oman_url_byDate = 'https://www.soccerstats.com/results.asp?league=oman&pmtype=bydate'
paraguay2_url_byDate = 'https://www.soccerstats.com/results.asp?league=paraguay2&pmtype=bydate'
peru2_url_byDate = 'https://www.soccerstats.com/results.asp?league=peru2&pmtype=bydate'
poland_url_byDate = 'https://www.soccerstats.com/results.asp?league=poland&pmtype=bydate'
poland2_url_byDate = 'https://www.soccerstats.com/results.asp?league=poland2&pmtype=bydate'
portugal_url_byDate = 'https://www.soccerstats.com/results.asp?league=portugal&pmtype=bydate'
portugal2_url_byDate = 'https://www.soccerstats.com/results.asp?league=portugal2&pmtype=bydate'
qatar_url_byDate = 'https://www.soccerstats.com/results.asp?league=qatar&pmtype=bydate'
romania_url_byDate = 'https://www.soccerstats.com/results.asp?league=romania&pmtype=bydate'
saudiarabia_url_byDate = 'https://www.soccerstats.com/results.asp?league=saudiarabia&pmtype=bydate'
scotland_url_byDate = 'https://www.soccerstats.com/results.asp?league=scotland&pmtype=bydate'
scotland2_url_byDate = 'https://www.soccerstats.com/results.asp?league=scotland2&pmtype=bydate'
slovakia_url_byDate = 'https://www.soccerstats.com/results.asp?league=slovakia&pmtype=bydate'
slovenia_url_byDate = 'https://www.soccerstats.com/results.asp?league=slovenia&pmtype=bydate'
southkorea_url_byDate = 'https://www.soccerstats.com/results.asp?league=southkorea&pmtype=bydate'
southkorea2_url_byDate = 'https://www.soccerstats.com/results.asp?league=southkorea2&pmtype=bydate'
spain_url_byDate = 'https://www.soccerstats.com/results.asp?league=spain&pmtype=bydate'
spain2_url_byDate = 'https://www.soccerstats.com/results.asp?league=spain2&pmtype=bydate'
sweden_url_byDate = 'https://www.soccerstats.com/results.asp?league=sweden&pmtype=bydate'
sweden2_url_byDate = 'https://www.soccerstats.com/results.asp?league=sweden2&pmtype=bydate'
switzerland_url_byDate = 'https://www.soccerstats.com/results.asp?league=switzerland&pmtype=bydate'
switzerland2_url_byDate = 'https://www.soccerstats.com/results.asp?league=switzerland2&pmtype=bydate'
thailand_url_byDate = 'https://www.soccerstats.com/results.asp?league=thailand&pmtype=bydate'
turkey_url_byDate = 'https://www.soccerstats.com/results.asp?league=turkey&pmtype=bydate'
turkey2_url_byDate = 'https://www.soccerstats.com/results.asp?league=turkey2&pmtype=bydate'
ukraine_url_byDate = 'https://www.soccerstats.com/results.asp?league=ukraine&pmtype=bydate'
unitedarabemirates_url_byDate = 'https://www.soccerstats.com/results.asp?league=unitedarabemirates&pmtype=bydate'
uruguay_url_byDate = 'https://www.soccerstats.com/results.asp?league=uruguay&pmtype=bydate'
usa_url_byDate = 'https://www.soccerstats.com/results.asp?league=usa&pmtype=bydate'
usa2_url_byDate = 'https://www.soccerstats.com/results.asp?league=usa2&pmtype=bydate'
venezuela_url_byDate = 'https://www.soccerstats.com/results.asp?league=venezuela&pmtype=bydate'
wales_url_byDate = 'https://www.soccerstats.com/results.asp?league=wales&pmtype=bydate'

ListUrlsbyDate = [argentina_url_byDate,argentina5_url_byDate,austria_url_byDate,austria2_url_byDate,belgium_url_byDate,belgium2_url_byDate,brazil_url_byDate,brazil2_url_byDate,bulgaria_url_byDate,canada_url_byDate,chile_url_byDate,chile2_url_byDate,colombia2_url_byDate,costarica_url_byDate,croatia_url_byDate,czechrepublic_url_byDate,czechrepublic2_url_byDate,denmark_url_byDate,denmark2_url_byDate,ecuador3_url_byDate,england_url_byDate,england2_url_byDate,england3_url_byDate,finland2_url_byDate,france_url_byDate,france2_url_byDate,germany2_url_byDate,germany3_url_byDate,guatemala_url_byDate,hungary_url_byDate,hungary2_url_byDate,iceland_url_byDate,ireland_url_byDate,ireland2_url_byDate,japan_url_byDate,japan2_url_byDate,mexico_url_byDate,netherlands_url_byDate,netherlands2_url_byDate,northernireland_url_byDate,norway_url_byDate,norway2_url_byDate,paraguay2_url_byDate,peru2_url_byDate,poland_url_byDate,poland2_url_byDate,portugal_url_byDate,portugal2_url_byDate,qatar_url_byDate,romania_url_byDate,scotland_url_byDate,scotland2_url_byDate,slovenia_url_byDate,southkorea_url_byDate,southkorea2_url_byDate,sweden_url_byDate,sweden2_url_byDate,switzerland_url_byDate,switzerland2_url_byDate,thailand_url_byDate,usa_url_byDate,usa2_url_byDate]

rows_results = []
rows_fixtures = []
IndexContLeague = 0
for i in ListUrlsbyDate:
    # Perform the GET request
    response = requests.get(i)
    if response.status_code != 200:
        print(i)

# Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the desired stats
    tables = soup.find_all('table', {'id': 'btable'})

    rows = []
    # Lists to store the categorized data
    for table in tables:
        for tr in table.find_all('tr')[1:]:  # Skip the header row
            cells = tr.find_all('td')
            row = [cell.text.strip() for cell in cells]
            rows.append(row)

    # Regular expression to match the 'xx xx xxx' structure
    pattern = re.compile(r'^[A-Za-z]{3} [0-9]{1,2} [A-Za-z]{3}$')

    # Filter the list to keep only sublists where the first element matches the pattern
    rows = [sublist for sublist in rows if pattern.match(sublist[0])]
    for i in range(0,len(rows)):
        rows[i] = rows[i][:4]

    for i in rows:
        if "-" in i[2]:
            i.insert(0,Continent[IndexContLeague])
            i.insert(1, League[IndexContLeague])
            rows_results.append(i)
        elif ":" in i[2]:
          i.insert(0, Continent[IndexContLeague])
          i.insert(1, League[IndexContLeague])
          rows_fixtures.append(i)
    IndexContLeague += 1

for i in range(0,len(rows_results)):
    score = rows_results[i][4].split(' - ')
    temp = [rows_results[i][0], rows_results[i][1], rows_results[i][2], rows_results[i][3], int(score[0]), '-', int(score[1]), rows_results[i][5]]
    rows_results[i] = temp

headers_results = ["Continent","League","Date","Home team","Goals Home","Hifen","Goals Away","Away Team"]
headers_fixtures = ["Continent","League","Date","Home team","Schedule","Away Team"]

dfresults = pd.DataFrame(rows_results, columns=headers_results)
dffixtures = pd.DataFrame(rows_fixtures, columns=headers_fixtures)

##Generates list with unique names of the teams.
listTeamNamesUnique =  dfresults["Home team"].drop_duplicates().tolist()

##########################################################################################################################################################################
#Dict 1.1: GoalsbyTeamTotalDict for dfOverUnderGoalsTotalFullTime
GoalsbyTeamTotalDict = {team: [] for team in listTeamNamesUnique}

# Iterate through the DataFrame
for index, row in dfresults.iterrows():
    # Home team case
    home_team = row['Home team']
    home_goals = row['Goals Home']
    if home_team in GoalsbyTeamTotalDict:
        GoalsbyTeamTotalDict[home_team].append(home_goals)

    # Away team case
    away_team = row['Away Team']
    away_goals = row['Goals Away']
    if away_team in GoalsbyTeamTotalDict:
        GoalsbyTeamTotalDict[away_team].append(away_goals)

# Now team_goals dictionary contains the list of goals scored by each team
AverageSDGoalsbyTeamTotalDict = GoalsbyTeamTotalDict.copy()

# Replace each list with the average and standard deviation
for team, goals in AverageSDGoalsbyTeamTotalDict.items():
    if len(goals) == 1:
        AverageSDGoalsbyTeamTotalDict[team] = [goals[0], '-']
    else:
        average = round(statistics.mean(goals), 2)
        stdev = round(statistics.stdev(goals), 2)
        AverageSDGoalsbyTeamTotalDict[team] = [average, stdev]

#################################################################
#Dict 1.2: GoalsbyTeamTotalDict for dfOverUnderGoalsTotalFullTime
# Create a new dictionary to store goals conceded by each team
GoalsConcededbyTeamTotalDict = {team: [] for team in listTeamNamesUnique}

# Iterate through the dfresults DataFrame to calculate goals conceded
for index, row in dfresults.iterrows():
    # Home team case: Home team concedes the away team's goals
    home_team = row['Home team']
    away_goals = row['Goals Away']
    if home_team in GoalsConcededbyTeamTotalDict:
        GoalsConcededbyTeamTotalDict[home_team].append(away_goals)

    # Away team case: Away team concedes the home team's goals
    away_team = row['Away Team']
    home_goals = row['Goals Home']
    if away_team in GoalsConcededbyTeamTotalDict:
        GoalsConcededbyTeamTotalDict[away_team].append(home_goals)

# Calculate the average and standard deviation for goals conceded
AverageSDGoalsConcededbyTeamTotalDict = {}
for team, goals_conceded in GoalsConcededbyTeamTotalDict.items():
    if len(goals_conceded) == 1:  # Only calculate if there are goals conceded recorded
        AverageSDGoalsConcededbyTeamTotalDict[team] = [goals_conceded[0], '-']
    else:
        average_gc = round(statistics.mean(goals_conceded), 2)
        stdev_gc = round(statistics.stdev(goals_conceded), 2)
        AverageSDGoalsConcededbyTeamTotalDict[team] = [average_gc, stdev_gc]

##########################################################################################################################################################################
#
#
#
##########################################################################################################################################################################
#Dict 2.1: GoalsbyTeamLast8Dict for dfOverUnderGoalsLast8FullTime
GoalsbyTeamLast8Dict = GoalsbyTeamTotalDict.copy()

# Update the dictionary by replacing lists with length < 8 with '-'
for team in GoalsbyTeamLast8Dict:
    if len(GoalsbyTeamLast8Dict[team]) < 8:
        GoalsbyTeamLast8Dict[team] = ['-'] * len(GoalsbyTeamLast8Dict[team])
    else:
        GoalsbyTeamLast8Dict[team] = GoalsbyTeamLast8Dict[team][-8:]

AverageSDGoalsbyTeamLast8Dict = GoalsbyTeamLast8Dict.copy()

# Replace each list with the average and standard deviation
for team, goals in AverageSDGoalsbyTeamLast8Dict.items():
    if len(goals) == 1:
        AverageSDGoalsbyTeamLast8Dict[team] = [goals[0], '-']
    elif "-" in goals:
        AverageSDGoalsbyTeamLast8Dict[team] = ['-', '-']
    else:
        average = round(statistics.mean(goals), 2)
        stdev = round(statistics.stdev(goals), 2)
        AverageSDGoalsbyTeamLast8Dict[team] = [average, stdev]

#################################################################
#Dict 2.2: GoalsConcededbyTeamLast8Dict for dfOverUnderGoalsLast8FullTime
# Create a new dictionary to store goals conceded by each team
GoalsConcededbyTeamLast8Dict = GoalsConcededbyTeamTotalDict.copy()

# Update the dictionary by replacing lists with length < 8 with '-'
for team in GoalsConcededbyTeamLast8Dict:
    if len(GoalsConcededbyTeamLast8Dict[team]) < 8:
        GoalsConcededbyTeamLast8Dict[team] = ['-'] * len(GoalsConcededbyTeamLast8Dict[team])
    else:
        GoalsConcededbyTeamLast8Dict[team] = GoalsConcededbyTeamLast8Dict[team][-8:]

# Calculate the average and standard deviation for goals conceded
AverageSDGoalsConcededbyTeamLast8Dict = {}
for team, goals_conceded in GoalsConcededbyTeamLast8Dict.items():
    if len(goals_conceded) == 1:
        AverageSDGoalsConcededbyTeamLast8Dict[team] = [goals_conceded[0], '-']
    elif "-" in goals_conceded:
        AverageSDGoalsConcededbyTeamLast8Dict[team] = ['-', '-']
    else:
        average_gc = round(statistics.mean(goals_conceded), 2)
        stdev_gc = round(statistics.stdev(goals_conceded), 2)
        AverageSDGoalsConcededbyTeamLast8Dict[team] = [average_gc, stdev_gc]

##########################################################################################################################################################################
#
#
#
##########################################################################################################################################################################
#Dict 3.1: GoalsbyTeamHomeDict for dfOverUnderGoalsHomeFullTime
GoalsbyTeamHomeDict = {team: [] for team in listTeamNamesUnique}

# Iterate through the DataFrame
for index, row in dfresults.iterrows():
    # Home team case
    home_team = row['Home team']
    home_goals = row['Goals Home']
    if home_team in GoalsbyTeamHomeDict:
        GoalsbyTeamHomeDict[home_team].append(home_goals)

AverageSDGoalsbyTeamHomeDict = GoalsbyTeamHomeDict.copy()

# Replace each list with the average and standard deviation
for team, goals in AverageSDGoalsbyTeamHomeDict.items():
    if len(goals) == 1:
        AverageSDGoalsbyTeamHomeDict[team] = [goals[0], '-']
    else:
        average = round(statistics.mean(goals), 2)
        stdev = round(statistics.stdev(goals), 2)
        AverageSDGoalsbyTeamHomeDict[team] = [average, stdev]

#################################################################
#Dict 3.2: GoalsConcededbyTeamTotalDict for dfOverUnderGoalsTotalFullTime
# Create a new dictionary to store goals conceded by each team
GoalsConcededbyTeamHomeDict = {team: [] for team in listTeamNamesUnique}

# Iterate through the dfresults DataFrame to calculate goals conceded
for index, row in dfresults.iterrows():
    # Home team case: Home team concedes the away team's goals
    home_team = row['Home team']
    away_goals = row['Goals Away']
    if home_team in GoalsConcededbyTeamHomeDict:
        GoalsConcededbyTeamHomeDict[home_team].append(away_goals)

# Calculate the average and standard deviation for goals conceded
AverageSDGoalsConcededbyTeamHomeDict = {}
for team, goals_conceded in GoalsConcededbyTeamHomeDict.items():
    if len(goals_conceded) == 1:
        AverageSDGoalsConcededbyTeamHomeDict[team] = [goals_conceded[0], '-']
    else:
        average_gc = round(statistics.mean(goals_conceded), 2)
        stdev_gc = round(statistics.stdev(goals_conceded), 2)
        AverageSDGoalsConcededbyTeamHomeDict[team] = [average_gc, stdev_gc]

##########################################################################################################################################################################
#
#
#
##########################################################################################################################################################################
#Dict 4.1: GoalsbyTeamAwaylDict for dfOverUnderGoalsAwayFullTime
GoalsbyTeamAwaylDict = {team: [] for team in listTeamNamesUnique}

# Iterate through the DataFrame
for index, row in dfresults.iterrows():
    # Away team case
    away_team = row['Away Team']
    away_goals = row['Goals Away']
    if away_team in GoalsbyTeamAwaylDict:
        GoalsbyTeamAwaylDict[away_team].append(away_goals)

AverageSDGoalsbyTeamAwaylDict = GoalsbyTeamAwaylDict.copy()

# Replace each list with the average and standard deviation
for team, goals in AverageSDGoalsbyTeamAwaylDict.items():
    if len(goals) == 1:
        AverageSDGoalsbyTeamAwaylDict[team] = [goals[0], '-']
    else:
        average = round(statistics.mean(goals), 2)
        stdev = round(statistics.stdev(goals), 2)
        AverageSDGoalsbyTeamAwaylDict[team] = [average, stdev]

#################################################################
#Dict 4.2: GoalsbyTeamAwayDict for dfOverUnderGoalsTotalFullTime
# Create a new dictionary to store goals conceded by each team
GoalsConcededbyTeamAwayDict = {team: [] for team in listTeamNamesUnique}

# Iterate through the dfresults DataFrame to calculate goals conceded
for index, row in dfresults.iterrows():
    # Away team case: Away team concedes the home team's goals
    away_team = row['Away Team']
    home_goals = row['Goals Home']
    if away_team in GoalsConcededbyTeamAwayDict:
        GoalsConcededbyTeamAwayDict[away_team].append(home_goals)

# Calculate the average and standard deviation for goals conceded
AverageSDGoalsConcededbyTeamAwayDict = {}
for team, goals_conceded in GoalsConcededbyTeamAwayDict.items():
    if len(goals_conceded) == 1:
        AverageSDGoalsConcededbyTeamAwayDict[team] = [goals_conceded[0], '-']  # Handle case where no goals are conceded
    else:  # Only calculate if there are goals conceded recorded
        average_gc = round(statistics.mean(goals_conceded), 2)
        stdev_gc = round(statistics.stdev(goals_conceded), 2)
        AverageSDGoalsConcededbyTeamAwayDict[team] = [average_gc, stdev_gc]

#########################################################################################################################################################################
#Adds the dicitonary with the averages and SD of the teams to the dataframes with over ubnder goals information sorted by percentage of games with 2.5- goals
dfOverUnderGoalsTotalFullTime['average_GS'] = dfOverUnderGoalsTotalFullTime['Team'].map(lambda x: AverageSDGoalsbyTeamTotalDict[x][0])
dfOverUnderGoalsTotalFullTime['SD_GS'] = dfOverUnderGoalsTotalFullTime['Team'].map(lambda x: AverageSDGoalsbyTeamTotalDict[x][1])

dfOverUnderGoalsLast8FullTime['average_GS'] = dfOverUnderGoalsLast8FullTime['Team'].map(lambda x: AverageSDGoalsbyTeamLast8Dict[x][0])
dfOverUnderGoalsLast8FullTime['SD_GS'] = dfOverUnderGoalsLast8FullTime['Team'].map(lambda x: AverageSDGoalsbyTeamLast8Dict[x][1])

dfOverUnderGoalsHomeFullTime['average_GS'] = dfOverUnderGoalsHomeFullTime['Team'].map(lambda x: AverageSDGoalsbyTeamHomeDict[x][0])
dfOverUnderGoalsHomeFullTime['SD_GS'] = dfOverUnderGoalsHomeFullTime['Team'].map(lambda x: AverageSDGoalsbyTeamHomeDict[x][1])

dfOverUnderGoalsAwayFullTime['average_GS'] = dfOverUnderGoalsAwayFullTime['Team'].map(lambda x: AverageSDGoalsbyTeamAwaylDict[x][0])
dfOverUnderGoalsAwayFullTime['SD_GS'] = dfOverUnderGoalsAwayFullTime['Team'].map(lambda x: AverageSDGoalsbyTeamAwaylDict[x][1])

# Add the averages and standard deviations for goals conceded to the dataframe
dfOverUnderGoalsTotalFullTime['average_GC'] = dfOverUnderGoalsTotalFullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamTotalDict.get(x, [None, None])[0])
dfOverUnderGoalsTotalFullTime['SD_GC'] = dfOverUnderGoalsTotalFullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamTotalDict.get(x, [None, None])[1])

dfOverUnderGoalsLast8FullTime['average_GC'] = dfOverUnderGoalsLast8FullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamLast8Dict.get(x, [None, None])[0])
dfOverUnderGoalsLast8FullTime['SD_GC'] = dfOverUnderGoalsLast8FullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamLast8Dict.get(x, [None, None])[1])

dfOverUnderGoalsHomeFullTime['average_GC'] = dfOverUnderGoalsHomeFullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamHomeDict.get(x, [None, None])[0])
dfOverUnderGoalsHomeFullTime['SD_GC'] = dfOverUnderGoalsHomeFullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamHomeDict.get(x, [None, None])[1])

dfOverUnderGoalsAwayFullTime['average_GC'] = dfOverUnderGoalsAwayFullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamAwayDict.get(x, [None, None])[0])
dfOverUnderGoalsAwayFullTime['SD_GC'] = dfOverUnderGoalsAwayFullTime['Team'].map(lambda x: AverageSDGoalsConcededbyTeamAwayDict.get(x, [None, None])[1])

dffixtures_forExcel = dffixtures.copy()

# Initialize an empty DataFrame to store the first appearances
first_appearances = pd.DataFrame()

# Track teams that have already appeared
home_appeared_teams = set()
away_appeared_teams = set()

# Iterate through df2 to find the first appearance of each team
for index, row in dffixtures_forExcel.iterrows():
    home_team = row['Home team']
    away_team = row['Away Team']

    # Check if the home team has already appeared as either home or away
    if home_team not in home_appeared_teams and home_team not in away_appeared_teams:
        first_appearances = pd.concat([first_appearances, pd.DataFrame([row])])
        home_appeared_teams.add(home_team)

    # Check if the away team has already appeared as either home or away
    if away_team not in home_appeared_teams and away_team not in away_appeared_teams:
        first_appearances = pd.concat([first_appearances, pd.DataFrame([row])])
        away_appeared_teams.add(away_team)

first_appearances.reset_index(drop=True, inplace=True)
first_appearances = first_appearances.drop(columns=['Continent', 'League'])

# Extracting the relevant column "2.5-" from df1 to map with team names
df_relevant = dfOverUnderGoalsTotalFullTime[['Team', '2.5+']]

# Creating dictionaries for quick lookup of 2.5+ values
team_2_5_plus = df_relevant.set_index('Team')['2.5+'].to_dict()

# Adding two new columns to first_appearances_dropped
first_appearances['low bound probability'] = first_appearances.apply(
    lambda row: min(team_2_5_plus.get(row['Home team'], float('inf')),
                    team_2_5_plus.get(row['Away Team'], float('inf'))), axis=1)

first_appearances['high bound probability'] = first_appearances.apply(
    lambda row: max(team_2_5_plus.get(row['Home team'], float('-inf')),
                    team_2_5_plus.get(row['Away Team'], float('-inf'))), axis=1)

first_appearances['low bound probability'] = 100 - first_appearances['low bound probability']
first_appearances['high bound probability'] = 100 - first_appearances['high bound probability']

first_appearances['average probability'] = (first_appearances['low bound probability'] + first_appearances['high bound probability']) / 2

# Rounding the values in the "average probability" column to 2 decimal places
first_appearances['average probability'] = first_appearances['average probability'].round(2)


# Ensure the columns exist in df_original_correct
required_columns = ['Date', 'Home team', 'Schedule', 'Away Team',
                    'low bound probability', 'high bound probability', 'average probability']

for col in required_columns:
    if col not in dfOverUnderGoalsTotalFullTime.columns:
        dfOverUnderGoalsTotalFullTime[col] = None  # Add the column if it doesn't exist

for index, row in first_appearances.iterrows():
    home_team = row['Home team']
    away_team = row['Away Team']

    # Find rows in the original dataframe that match the home or away team
    matching_home_team = dfOverUnderGoalsTotalFullTime['Team'] == home_team
    matching_away_team = dfOverUnderGoalsTotalFullTime['Team'] == away_team

    # Assign the values from df_first_appearances to df_original_correct
    dfOverUnderGoalsTotalFullTime.loc[matching_home_team, ['Date', 'Home team', 'Schedule', 'Away Team',
                                                 'low bound probability', 'high bound probability',
                                                 'average probability']] = row[
        ['Date', 'Home team', 'Schedule', 'Away Team',
         'low bound probability', 'high bound probability', 'average probability']].values

    dfOverUnderGoalsTotalFullTime.loc[matching_away_team, ['Date', 'Home team', 'Schedule', 'Away Team',
                                                 'low bound probability', 'high bound probability',
                                                 'average probability']] = row[
        ['Date', 'Home team', 'Schedule', 'Away Team',
         'low bound probability', 'high bound probability', 'average probability']].values

# Create a dictionary mapping from the "Team" to the "2.5+" value in both df2 and df3
home_team_2_5_map = dfOverUnderGoalsHomeFullTime.set_index('Team')['2.5+'].to_dict()
away_team_2_5_map = dfOverUnderGoalsAwayFullTime.set_index('Team')['2.5+'].to_dict()

# Now, map these values to the first dataframe
dfOverUnderGoalsTotalFullTime['probability home team'] = dfOverUnderGoalsTotalFullTime['Home team'].map(home_team_2_5_map)
dfOverUnderGoalsTotalFullTime['probability away team'] = dfOverUnderGoalsTotalFullTime['Away Team'].map(away_team_2_5_map)

dfOverUnderGoalsTotalFullTime['probability home team'] = 100 - dfOverUnderGoalsTotalFullTime['probability home team']
dfOverUnderGoalsTotalFullTime['probability away team'] = 100 - dfOverUnderGoalsTotalFullTime['probability away team']

# First, create the new "next match" column by concatenating the values from "Date", "Home team", "Schedule", and "Away Team".
dfOverUnderGoalsTotalFullTime["Date1"] = dfOverUnderGoalsTotalFullTime["Date"]
dfOverUnderGoalsTotalFullTime['Next match'] = dfOverUnderGoalsTotalFullTime.apply(lambda row: f"{row['Date']}, {row['Schedule']}, {row['Home team']} - {row['Away Team']}", axis=1)

# Drop the original four columns
dfOverUnderGoalsTotalFullTime = dfOverUnderGoalsTotalFullTime.drop(columns=['Date', 'Home team', 'Schedule', 'Away Team'])

# Move "next match" to the 21th position
columns = dfOverUnderGoalsTotalFullTime.columns.tolist()  # Get list of columns
columns.insert(20, columns.pop(columns.index('Next match')))  # Move "next match" to position 21 (index 20)
dfOverUnderGoalsTotalFullTime = dfOverUnderGoalsTotalFullTime[columns]  # Reorder the dataframe

dfOverUnderGoalsTotalFullTime['low bound home/away probability'] = dfOverUnderGoalsTotalFullTime[['probability home team', 'probability away team']].min(axis=1)
columns = dfOverUnderGoalsTotalFullTime.columns.tolist()  # Get list of columns
columns.insert(26, columns.pop(columns.index('low bound home/away probability')))  # Move "next match" to position 21 (index 20)
dfOverUnderGoalsTotalFullTime = dfOverUnderGoalsTotalFullTime[columns]  # Reorder the dataframe

dfOverUnderGoalsTotalFullTime['average home/away probability'] = round(dfOverUnderGoalsTotalFullTime[['probability home team', 'probability away team']].mean(axis=1),2)
columns = dfOverUnderGoalsTotalFullTime.columns.tolist()  # Get list of columns
columns.insert(27, columns.pop(columns.index('average home/away probability')))  # Move "next match" to position 21 (index 20)
dfOverUnderGoalsTotalFullTime = dfOverUnderGoalsTotalFullTime[columns]  # Reorder the dataframe

# Function to extract home and away team names
def extract_teams(match_info):
    match_details = match_info.split(', ')[-1]  # Get the "Landskrona - Brage" part
    home_team, away_team = match_details.split(' - ')  # Split into home and away teams
    return home_team.strip(), away_team.strip()

# Populate the columns based on the extracted home and away teams
dfOverUnderGoalsTotalFullTime['average_GS_Home'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsbyTeamHomeDict.get(extract_teams(x)[0], [None, None])[0]
)
dfOverUnderGoalsTotalFullTime['SD_GS_Home'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsbyTeamHomeDict.get(extract_teams(x)[0], [None, None])[1]
)
dfOverUnderGoalsTotalFullTime['average_GC_Home'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsConcededbyTeamHomeDict.get(extract_teams(x)[0], [None, None])[0]
)
dfOverUnderGoalsTotalFullTime['SD_GC_Home'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsConcededbyTeamHomeDict.get(extract_teams(x)[0], [None, None])[1]
)
dfOverUnderGoalsTotalFullTime['average_GS_Away'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsbyTeamAwaylDict.get(extract_teams(x)[1], [None, None])[0]
)
dfOverUnderGoalsTotalFullTime['SD_GS_Away'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsbyTeamAwaylDict.get(extract_teams(x)[1], [None, None])[1]
)
dfOverUnderGoalsTotalFullTime['average_GC_Away'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsConcededbyTeamAwayDict.get(extract_teams(x)[1], [None, None])[0]
)
dfOverUnderGoalsTotalFullTime['SD_GC_Away'] = dfOverUnderGoalsTotalFullTime['Next match'].map(
    lambda x: AverageSDGoalsConcededbyTeamAwayDict.get(extract_teams(x)[1], [None, None])[1]
)

date1_column = dfOverUnderGoalsTotalFullTime.pop('Date1')

# Add the "Date1" column back at the end of the DataFrame
dfOverUnderGoalsTotalFullTime['Date1'] = date1_column

dfOverUnderGoalsTotalFullTime['Sum avg Goals Scored/Conceded'] = dfOverUnderGoalsTotalFullTime[['average_GS_Home', 'average_GC_Home','average_GS_Away', 'average_GC_Away']].sum(axis=1)
dfOverUnderGoalsTotalFullTime['Sum SD Goals Scored/Conceded'] = dfOverUnderGoalsTotalFullTime[['SD_GS_Home', 'SD_GC_Home','SD_GS_Away', 'SD_GC_Away']].sum(axis=1)

# Sort the DataFrame by the '2.5+' column in descending order
dfOverUnderGoalsTotalFullTime = dfOverUnderGoalsTotalFullTime.sort_values(by=['low bound home/away probability','average home/away probability','Sum avg Goals Scored/Conceded','Sum SD Goals Scored/Conceded','GP'], ascending=[False,False,True,True,False])
dfOverUnderGoalsTotalFullTime = dfOverUnderGoalsTotalFullTime.iloc[:, :-2]
dfOverUnderGoalsTotalFullTime.reset_index(drop=True,inplace=True)
dfOverUnderGoalsLast8FullTime = dfOverUnderGoalsLast8FullTime.sort_values(by=['2.5+','GP'], ascending=[False,False])
dfOverUnderGoalsLast8FullTime.reset_index(drop=True,inplace=True)
dfOverUnderGoalsHomeFullTime = dfOverUnderGoalsHomeFullTime.sort_values(by=['2.5+','GP'], ascending=[False,False])
dfOverUnderGoalsHomeFullTime.reset_index(drop=True,inplace=True)
dfOverUnderGoalsAwayFullTime = dfOverUnderGoalsAwayFullTime.sort_values(by=['2.5+','GP'], ascending=[False,False])
dfOverUnderGoalsAwayFullTime.reset_index(drop=True,inplace=True)

#################################################################################################
###Computes the sheets with info regarding the goals scores and conceded by each teams

##########################################################################################################################################################################
#1: df_GoalsScoredConcedbyTeamTotal

data = {
    'Teams': list(GoalsbyTeamTotalDict.keys()),
    'GP': [len(goals) for goals in GoalsbyTeamTotalDict.values()],
    'scored 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsbyTeamTotalDict.values()],
    'scored 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsbyTeamTotalDict.values()],
    'scored 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsbyTeamTotalDict.values()],
    'scored 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsbyTeamTotalDict.values()],
    'scored 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsbyTeamTotalDict.values()],
    'scored 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsbyTeamTotalDict.values()],
    'scored 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsbyTeamTotalDict.values()],
}

df_GoalsbyTeamTotal = pd.DataFrame(data)

data = {
    'Teams': list(GoalsConcededbyTeamTotalDict.keys()),
    'GP': [len(goals) for goals in GoalsConcededbyTeamTotalDict.values()],
    'conceded 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsConcededbyTeamTotalDict.values()],
    'conceded 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsConcededbyTeamTotalDict.values()],
    'conceded 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsConcededbyTeamTotalDict.values()],
    'conceded 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsConcededbyTeamTotalDict.values()],
    'conceded 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsConcededbyTeamTotalDict.values()],
    'conceded 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsConcededbyTeamTotalDict.values()],
    'conceded 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsConcededbyTeamTotalDict.values()],
}

df_GoalsConcededbyTeamTotal = pd.DataFrame(data)

df_GoalsScoredConcedbyTeamTotal = pd.concat([df_GoalsbyTeamTotal, df_GoalsConcededbyTeamTotal.iloc[:, 2:]], axis=1)

########
df_appendContinentLeague = dfOverUnderGoalsTotalFullTime.iloc[:,:3]

# Merging the necessary columns from df_appendContinentLeague with df_GoalsScoredConcedbyTeamTotal
df_GoalsScoredConcedbyTeamTotal = pd.merge(df_GoalsScoredConcedbyTeamTotal, df_appendContinentLeague[['Continent', 'League', 'Team']], left_on='Teams', right_on='Team', how='left')

# Dropping the duplicate 'Team' column from df_appendContinentLeague after the merge
df_GoalsScoredConcedbyTeamTotal = df_GoalsScoredConcedbyTeamTotal.drop(columns=['Team'])

# Reordering the columns to place 'Continent' and 'League' at the beginning
columns_order = ['Continent', 'League'] + df_GoalsScoredConcedbyTeamTotal.columns[:-2].tolist()
df_GoalsScoredConcedbyTeamTotal = df_GoalsScoredConcedbyTeamTotal[columns_order]

##########################################################################################################################################################################
#
#
#
##########################################################################################################################################################################
#2: df_GoalsScoredConcedbyTeamLast8

data = {
    'Teams': list(GoalsbyTeamLast8Dict.keys()),
    'GP': [len(goals) for goals in GoalsbyTeamLast8Dict.values()],
    'scored 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsbyTeamLast8Dict.values()],
    'scored 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsbyTeamLast8Dict.values()],
    'scored 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsbyTeamLast8Dict.values()],
    'scored 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsbyTeamLast8Dict.values()],
    'scored 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsbyTeamLast8Dict.values()],
    'scored 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsbyTeamLast8Dict.values()],
    'scored 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsbyTeamLast8Dict.values()],
}

df_GoalsbyTeamLast8 = pd.DataFrame(data)

data = {
    'Teams': list(GoalsConcededbyTeamLast8Dict.keys()),
    'GP': [len(goals) for goals in GoalsConcededbyTeamLast8Dict.values()],
    'conceded 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsConcededbyTeamLast8Dict.values()],
    'conceded 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsConcededbyTeamLast8Dict.values()],
    'conceded 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsConcededbyTeamLast8Dict.values()],
    'conceded 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsConcededbyTeamLast8Dict.values()],
    'conceded 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsConcededbyTeamLast8Dict.values()],
    'conceded 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsConcededbyTeamLast8Dict.values()],
    'conceded 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsConcededbyTeamLast8Dict.values()],
}

df_GoalsConcededbyTeamLast8 = pd.DataFrame(data)

df_GoalsScoredConcedbyTeamLast8 = pd.concat([df_GoalsbyTeamLast8, df_GoalsConcededbyTeamLast8.iloc[:, 2:]], axis=1)
for i in range(0,len(df_GoalsScoredConcedbyTeamLast8)):
    if df_GoalsScoredConcedbyTeamLast8.loc[i,"GP"] < 8:
        df_GoalsScoredConcedbyTeamLast8.iloc[i,2:] = '-'


# Merging the necessary columns from df_appendContinentLeague with df_GoalsScoredConcedbyTeamTotal
df_GoalsScoredConcedbyTeamLast8 = pd.merge(df_GoalsScoredConcedbyTeamLast8, df_appendContinentLeague[['Continent', 'League', 'Team']], left_on='Teams', right_on='Team', how='left')

# Dropping the duplicate 'Team' column from df_appendContinentLeague after the merge
df_GoalsScoredConcedbyTeamLast8 = df_GoalsScoredConcedbyTeamLast8.drop(columns=['Team'])

# Reordering the columns to place 'Continent' and 'League' at the beginning
columns_order = ['Continent', 'League'] + df_GoalsScoredConcedbyTeamLast8.columns[:-2].tolist()
df_GoalsScoredConcedbyTeamLast8 = df_GoalsScoredConcedbyTeamLast8[columns_order]

##########################################################################################################################################################################
#
#
#
##########################################################################################################################################################################
#3: df_GoalsScoredConcedbyTeamHome

data = {
    'Teams': list(GoalsbyTeamHomeDict.keys()),
    'GP': [len(goals) for goals in GoalsbyTeamHomeDict.values()],
    'scored 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsbyTeamHomeDict.values()],
    'scored 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsbyTeamHomeDict.values()],
    'scored 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsbyTeamHomeDict.values()],
    'scored 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsbyTeamHomeDict.values()],
    'scored 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsbyTeamHomeDict.values()],
    'scored 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsbyTeamHomeDict.values()],
    'scored 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsbyTeamHomeDict.values()],
}

df_GoalsbyTeamHome = pd.DataFrame(data)

data = {
    'Teams': list(GoalsConcededbyTeamHomeDict.keys()),
    'GP': [len(goals) for goals in GoalsConcededbyTeamHomeDict.values()],
    'conceded 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsConcededbyTeamHomeDict.values()],
    'conceded 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsConcededbyTeamHomeDict.values()],
    'conceded 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsConcededbyTeamHomeDict.values()],
    'conceded 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsConcededbyTeamHomeDict.values()],
    'conceded 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsConcededbyTeamHomeDict.values()],
    'conceded 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsConcededbyTeamHomeDict.values()],
    'conceded 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsConcededbyTeamHomeDict.values()],
}

df_GoalsConcededbyTeamHome = pd.DataFrame(data)

df_GoalsScoredConcedbyTeamHome = pd.concat([df_GoalsbyTeamHome, df_GoalsConcededbyTeamHome.iloc[:, 2:]], axis=1)

# Merging the necessary columns from df_appendContinentLeague with df_GoalsScoredConcedbyTeamTotal
df_GoalsScoredConcedbyTeamHome = pd.merge(df_GoalsScoredConcedbyTeamHome, df_appendContinentLeague[['Continent', 'League', 'Team']], left_on='Teams', right_on='Team', how='left')

# Dropping the duplicate 'Team' column from df_appendContinentLeague after the merge
df_GoalsScoredConcedbyTeamHome = df_GoalsScoredConcedbyTeamHome.drop(columns=['Team'])

# Reordering the columns to place 'Continent' and 'League' at the beginning
columns_order = ['Continent', 'League'] + df_GoalsScoredConcedbyTeamHome.columns[:-2].tolist()
df_GoalsScoredConcedbyTeamHome = df_GoalsScoredConcedbyTeamHome[columns_order]

##########################################################################################################################################################################
#
#
#
##########################################################################################################################################################################
#4: df_GoalsScoredConcedbyTeamAway

data = {
    'Teams': list(GoalsbyTeamAwaylDict.keys()),
    'GP': [len(goals) for goals in GoalsbyTeamAwaylDict.values()],
    'scored 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsbyTeamAwaylDict.values()],
    'scored 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsbyTeamAwaylDict.values()],
    'scored 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsbyTeamAwaylDict.values()],
    'scored 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsbyTeamAwaylDict.values()],
    'scored 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsbyTeamAwaylDict.values()],
    'scored 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsbyTeamAwaylDict.values()],
    'scored 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsbyTeamAwaylDict.values()],
}

df_GoalsbyTeamAway = pd.DataFrame(data)

data = {
    'Teams': list(GoalsConcededbyTeamAwayDict.keys()),
    'GP': [len(goals) for goals in GoalsConcededbyTeamAwayDict.values()],
    'conceded 0g': [round(goals.count(0)/len(goals), 2) for goals in GoalsConcededbyTeamAwayDict.values()],
    'conceded 1g': [round(goals.count(1)/len(goals), 2) for goals in GoalsConcededbyTeamAwayDict.values()],
    'conceded 2g': [round(goals.count(2)/len(goals), 2) for goals in GoalsConcededbyTeamAwayDict.values()],
    'conceded 3g': [round(goals.count(3) / len(goals), 2) for goals in GoalsConcededbyTeamAwayDict.values()],
    'conceded 4g': [round(goals.count(4) / len(goals), 2) for goals in GoalsConcededbyTeamAwayDict.values()],
    'conceded 5g': [round(goals.count(5) / len(goals), 2) for goals in GoalsConcededbyTeamAwayDict.values()],
    'conceded 6g': [round(goals.count(6) / len(goals), 2) for goals in GoalsConcededbyTeamAwayDict.values()],
}

df_GoalsConcededbyTeamAway = pd.DataFrame(data)

df_GoalsScoredConcedbyTeamAway = pd.concat([df_GoalsbyTeamAway, df_GoalsConcededbyTeamAway.iloc[:, 2:]], axis=1)

# Merging the necessary columns from df_appendContinentLeague with df_GoalsScoredConcedbyTeamTotal
df_GoalsScoredConcedbyTeamAway = pd.merge(df_GoalsScoredConcedbyTeamAway, df_appendContinentLeague[['Continent', 'League', 'Team']], left_on='Teams', right_on='Team', how='left')

# Dropping the duplicate 'Team' column from df_appendContinentLeague after the merge
df_GoalsScoredConcedbyTeamAway = df_GoalsScoredConcedbyTeamAway.drop(columns=['Team'])

# Reordering the columns to place 'Continent' and 'League' at the beginning
columns_order = ['Continent', 'League'] + df_GoalsScoredConcedbyTeamAway.columns[:-2].tolist()
df_GoalsScoredConcedbyTeamAway = df_GoalsScoredConcedbyTeamAway[columns_order]

dfOverUnderGoalsTotalFullTime_v2_0 = dfOverUnderGoalsTotalFullTime.drop_duplicates(subset='Next match', keep='first')
dfOverUnderGoalsTotalFullTime_v2_0 = dfOverUnderGoalsTotalFullTime_v2_0.drop(columns=[f'Avg', '0.5+', '1.5+', '2.5+', '3.5+', '4.5+', '5.5+', 'BTS', 'CS', 'FTS', 'WTN', 'LTN', 'average_GS', 'SD_GS', 'average_GC','SD_GC'])

DateForFileName = "-2.5Goals_" + datetime.now().strftime("%d-%m-%Y") + ".xlsx"
with pd.ExcelWriter(os.path.join("FullData",DateForFileName)) as writer:
    dfOverUnderGoalsTotalFullTime_v2_0.to_excel(writer,sheet_name='OverUnderGoalsTotalFullTime', index=False)
    dfresults.to_excel(writer,sheet_name='Results', index=False)
    dffixtures.to_excel(writer,sheet_name='Fixtures', index=False)

##########################################
##Treated File
Treated_dfOverUnderGoalsTotalFullTime_v2_0 = dfOverUnderGoalsTotalFullTime_v2_0

##########
##Select next dates
DatePlus1Day = datetime.now() + timedelta(days=1)
DatePlus1Day = DatePlus1Day.strftime("%d-%m-%Y")
date_obj = datetime.strptime(DatePlus1Day, "%d-%m-%Y")
formatted_DatePlus1Day = f"{date_obj.strftime('%a')[:2]} {date_obj.day} {date_obj.strftime('%b')}"

DatePlus2Day = datetime.now() + timedelta(days=2)
DatePlus2Day = DatePlus2Day.strftime("%d-%m-%Y")
date_obj = datetime.strptime(DatePlus2Day, "%d-%m-%Y")
formatted_DatePlus2Day = f"{date_obj.strftime('%a')[:2]} {date_obj.day} {date_obj.strftime('%b')}"

DatePlus3Day = datetime.now() + timedelta(days=3)
DatePlus3Day = DatePlus3Day.strftime("%d-%m-%Y")
date_obj = datetime.strptime(DatePlus3Day, "%d-%m-%Y")
formatted_DatePlus3Day = f"{date_obj.strftime('%a')[:2]} {date_obj.day} {date_obj.strftime('%b')}"

DatePlus4Day = datetime.now() + timedelta(days=4)
DatePlus4Day = DatePlus4Day.strftime("%d-%m-%Y")
date_obj = datetime.strptime(DatePlus4Day, "%d-%m-%Y")
formatted_DatePlus4Day = f"{date_obj.strftime('%a')[:2]} {date_obj.day} {date_obj.strftime('%b')}"

ListFilterDates = [formatted_DatePlus1Day,formatted_DatePlus2Day,formatted_DatePlus3Day,formatted_DatePlus4Day]
#Treated_dfOverUnderGoalsTotalFullTime_v2_0 = Treated_dfOverUnderGoalsTotalFullTime_v2_0[Treated_dfOverUnderGoalsTotalFullTime_v2_0['Date1'].isin(ListFilterDates)]

################################
#Keeping only lines with GP >= 12
Treated_dfOverUnderGoalsTotalFullTime_v2_0.loc[:, 'GP'] = pd.to_numeric(Treated_dfOverUnderGoalsTotalFullTime_v2_0['GP'], errors='coerce')
Treated_dfOverUnderGoalsTotalFullTime_v2_0 = Treated_dfOverUnderGoalsTotalFullTime_v2_0[Treated_dfOverUnderGoalsTotalFullTime_v2_0['GP'] >= 12]

################################
#Keeping only lines with low bound home/away probability >= 70
Treated_dfOverUnderGoalsTotalFullTime_v2_0.loc[:, 'low bound home/away probability'] = pd.to_numeric(Treated_dfOverUnderGoalsTotalFullTime_v2_0['low bound home/away probability'], errors='coerce')
#Treated_dfOverUnderGoalsTotalFullTime_v2_0 = Treated_dfOverUnderGoalsTotalFullTime_v2_0[Treated_dfOverUnderGoalsTotalFullTime_v2_0['low bound home/away probability'] >= 70]
Treated_dfOverUnderGoalsTotalFullTime_v2_0 = Treated_dfOverUnderGoalsTotalFullTime_v2_0[Treated_dfOverUnderGoalsTotalFullTime_v2_0['low bound home/away probability'] >= 50]

Treated_dfOverUnderGoalsTotalFullTime_v2_0['Expected Odd'] = round(1 / (Treated_dfOverUnderGoalsTotalFullTime_v2_0['low bound home/away probability'] / 100), 2)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['Odd House'] = 1

Treated_dfOverUnderGoalsTotalFullTime_v2_0['Expected Probability'] = round((Treated_dfOverUnderGoalsTotalFullTime_v2_0['low bound home/away probability'] / 100), 2)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['Probability House'] = [f'=ROUND(1/$W{i+2},2)' for i in range(len(Treated_dfOverUnderGoalsTotalFullTime_v2_0))]

Treated_dfOverUnderGoalsTotalFullTime_v2_0['Good/Bad Margin'] = [f'=IF(($X{i+2})>$Y{i+2},"Good","Bad")' for i in range(len(Treated_dfOverUnderGoalsTotalFullTime_v2_0))]

Treated_dfOverUnderGoalsTotalFullTime_v2_0['Margin (Prob)'] = [f'=($X{i+2}*100)-($Y{i+2}*100)&"%"' for i in range(len(Treated_dfOverUnderGoalsTotalFullTime_v2_0))]

Treated_dfOverUnderGoalsTotalFullTime_v2_0['Margin (Odd)'] = [f'=-1*($V{i+2}-$W{i+2})' for i in range(len(Treated_dfOverUnderGoalsTotalFullTime_v2_0))]

Treated_dfOverUnderGoalsTotalFullTime_v2_0[''] = None

Treated_dfOverUnderGoalsTotalFullTime_v2_0['WorstCaseExpGS_Home'] = Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Home','average_GC_Away']].max(axis=1)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['WorstCaseExpGS_Away'] = Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Away','average_GC_Home']].max(axis=1)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['WorstCaseExpResult'] = Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Home','average_GC_Away']].max(axis=1) + Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Away','average_GC_Home']].max(axis=1)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['       '] = None

Treated_dfOverUnderGoalsTotalFullTime_v2_0['BestCaseExpGS_Home'] = Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Home','average_GC_Away']].min(axis=1)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['BestCaseExpGS_Away'] = Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Away','average_GC_Home']].min(axis=1)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['BestCaseExpResult'] = Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Home','average_GC_Away']].min(axis=1) + Treated_dfOverUnderGoalsTotalFullTime_v2_0[['average_GS_Away','average_GC_Home']].min(axis=1)

Treated_dfOverUnderGoalsTotalFullTime_v2_0['            '] = None

def evaluate_cases(row):
    if row['WorstCaseExpResult'] < 2.5 and row['BestCaseExpResult'] < 2.5:
        return "Both Cases Ok"
    elif row['BestCaseExpResult'] < 2.5:
        return "Best Case Scenario Ok"
    else:
        return "No Case Ok"

Treated_dfOverUnderGoalsTotalFullTime_v2_0['CaseEvaluation'] = Treated_dfOverUnderGoalsTotalFullTime_v2_0.apply(evaluate_cases, axis=1)

DateForTreatedFileName = "Treated_-2.5Goals_" + datetime.now().strftime("%d-%m-%Y") + ".xlsx"
with pd.ExcelWriter(os.path.join("DataTreated",DateForTreatedFileName)) as writer:
    Treated_dfOverUnderGoalsTotalFullTime_v2_0.to_excel(writer,sheet_name='TreatedData', index=False)