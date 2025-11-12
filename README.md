[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FabioATMonteiro92/WebScrappingFootballProbabilityOver2.5GoalsPerGame/HEAD?urlpath=lab/tree/OVG_v2_Over2_5Goals.ipynb)

# Web Scraping & Probabilistic Modeling of Over 2.5 Goals in Football Matches

---

## Presentation
This repository contains a fully automated Python pipeline that scrapes league tables, recent results, and upcoming fixtures from **SoccerStats.com** for 60+ leagues from different continents and divisions (e.g.,D1, D2, and D3 where applicable), processes the data, and computes a set of probability indicators for matches finishing with **over 2.5 goals**.

The script extracts historical results, upcoming fixtures, team scoring profiles, and builds combined probability estimates based on home/away tendencies and statistical variance.  

The output is delivered as Excel workbooks (full data and treated data) designed for quick filtering, ranking, and decision support.

---

## What this project does
- Scrapes over/under performance tables (Total, Last 8, Home, Away) and parses results/fixtures per league.  
- Builds team-level profiles of goals scored and conceded based on:
  - all fixtures played so far, last 8 matches, home games, and away games.  
  - mean and standard deviation (goals scored (GS)/goals conceded (GC)).
- Derives match probabilities for games finishing with over 2.5 goals using:
  - low average bounds from team O/U percentages.  
  - home/away over 2.5 goals tendencies.  
  - GS/GC means and SDs combined (worst- and best-case expectations).  
- Ranks upcoming matches using a multi-criteria sort (low-bound prob, average home/away prob, sums of GS/GC means & SDs, GP).  
- Exports tidy, analysis-ready Excel files (full + treated).

---

## What is produced
The pipeline creates two Excel workbooks:

### 1️⃣ Full Data
**Filename:** `FullDatabase+2.5Goals_<DD-MM-YYYY>.xlsx`  
**Sheets:**
- `OverUnderGoalsTotalFullTime`:
  – unified table with league
  - team, games played (GP)
  - information about next match
  - low and high bound probability of the games finishing with +2.5 goals (based on the proportion of previous home and away matches that each team’s games ended with over 2.5 goals)
  - probability (home and away) based on the proportion of previous matches in which the home team’s home games and the away team’s away games ended with over 2.5 goals
  - goals scored and conceded by the home team at home games (means and SDs)
  - goals scored and conceded by the away team at away games (means and SDs)  
- `Results` – parsed historical results (date, teams, score)  
- `Fixtures` – upcoming fixtures (date, time, teams)

### 2️⃣ Treated Data
**Filename:** `Treated_+2.5Goals_<DD-MM-YYYY>.xlsx`  
**Sheet:**
- `TreatedData` – filtered view with:
  - GP ≥ 12  
  - low-bound home/away O2.5 ≥ 50.    
  - Defines the best and worst case scenarios for a match finishing with over 2.5 goals:
    - *Worst-case scenario*:
      - Home team’s expected goals = the lower value between their average goals scored at home and the average goals conceded by the away team.
      - Away team’s expected goals = the lower value between their average goals scored away and the average goals conceded by the home team.
    - *Best-case scenario*:
      - Home team’s expected goals = the higher value between their average goals scored at home and the average goals conceded by the away team.
      - Away team’s expected goals = the higher value between their average goals scored away and the average goals conceded by the home team.

---

## How it works (pipeline overview)
### 🔹 League setup
Two URL lists per league:
- O/U tables (Total, Last 8, Home, Away)  
- Results & fixtures (by date)

### 🔹 Scraping & parsing
- Fetch league pages, parse the main table (`id="btable"`), keep O/U rows (ignore “League average”).  
- From results/fixtures pages, identify rows by a date pattern (e.g., `Mon 4 Nov`), split results vs fixtures.  

### 🔹 Team metrics
- For each team: collect GS/GC series overall, last 8, home, away.  
- Compute mean and SD per series; compute goal-distribution proportions (score 0–6).  

### 🔹 Match enrichment
- Create “Next match” strings and propagate per-team metrics.  
- Compute low/high/avg O2.5 bounds and home/away O2.5.  
- Combine GS/GC means & SDs for quick triage features and expected odd/prob columns.  

### 🔹 Ranking & export
- Sort by: low-bound prob → average home/away prob → sum of GS/GC means → sum of SDs → GP.  
- Deduplicate on “Next match”.  
- Write Full Data and Treated Data workbooks.

---

## How to run
•	Click the **Binder badge at the top of this section**. 

•	Once Binder is launched, execute cells by pressing **Ctrl/Cmd + Enter**.

•	Locally: download the .py script “Data_Cleaning_Chrono.py” and run with a local Python 3 environment. To run the script locally, you need to create two folders named **"DataTreated"** and **"FullData"**. These folders will store the Excel workbooks generated by the script.

*Note:* Binder may take some time to launch the notebook on the first load, as it needs to build the execution environment. Please be patient. If the session hangs for too long, simply close the tab and relaunch Binder.
