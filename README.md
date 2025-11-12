[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FabioATMonteiro92/WebScrappingFootballProbabilityOver2.5GoalsPerGame/HEAD?urlpath=lab/tree/OVG_v2_Over2_5Goals.ipynb)

# Web Scraping & Probabilistic Modeling of Over 2.5 Goals in Football Matches

---

## Presentation
This repository contains a fully automated Python pipeline that scrapes league tables, recent results, and upcoming fixtures from **SoccerStats.com** for 60+ leagues, then processes and enriches the data to estimate the likelihood of matches finishing with **Over 2.5 goals**.  
The output is delivered as Excel workbooks (full data and treated data) designed for quick filtering, ranking, and decision support.

---

## What this project does
- Scrapes over/under tables (Total, Last 8, Home, Away) and parses results/fixtures per league.  
- Builds team-level profiles of goals scored and conceded:
  - overall, last 8, home, and away  
  - mean and standard deviation (GS/GC)  
  - empirical goal-distribution proportions (e.g., % of times scoring 0/1/2/3/… goals)  
- Derives match probabilities for O/U 2.5 using:
  - low/high/average bounds from team O/U percentages  
  - home/away O/U tendencies  
  - GS/GC means and SDs combined (worst- and best-case expectations)  
- Ranks upcoming matches using a multi-criteria sort (low-bound prob, average home/away prob, sums of GS/GC means & SDs, GP).  
- Exports tidy, analysis-ready Excel files (full + treated).

---

## Data sources
**SoccerStats.com**
- League O/U tables: `table.asp?league=...&tid=c`  
- Results & fixtures: `results.asp?league=...&pmtype=bydate`  

Coverage: 60+ leagues across **Europe**, **the Americas**, and **Asia** (D1/D2/D3 where applicable).

> **Note:** Team names must match across sources. Minor naming inconsistencies across pages can reduce matches unless normalized.

---

## What is produced
The pipeline creates two Excel workbooks:

### 1️⃣ Full Data
**Filename:** `+2.5Goals_<DD-MM-YYYY>.xlsx`  
**Sheets:**
- `OverUnderGoalsTotalFullTime` – unified table with league, team, GP, O/U percentages, next match string (Date, HH:MM, Home - Away), low/high/avg O2.5 bounds, home/away O2.5 probs, GS/GC (home & away) means and SDs, and ranking helpers.  
- `Results` – parsed historical results (date, teams, score).  
- `Fixtures` – upcoming fixtures (date, time, teams).  

### 2️⃣ Treated Data
**Filename:** `Treated_+2.5Goals_<DD-MM-YYYY>.xlsx`  
**Sheet:**
- `TreatedData` – filtered view with:
  - GP ≥ 12  
  - low-bound home/away O2.5 ≥ 50 (threshold configurable in code)  
  - computed Expected Odd (1 / prob), placeholder Odd House, and Excel formulas for Probability House, Good/Bad Margin, Margin (Prob/Odd)  
  - worst/best expected score aggregations and a CaseEvaluation tag: *Both Cases Ok*, *Best Case Scenario Ok*, or *No Case Ok*

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

## Repository contents (key files/folders)

- **`OVG_2.0_Over2.5Goals.py`** — main pipeline script  
- **`FullData/`** — exported full workbooks *(created at runtime)*  
- **`DataTreated/`** — exported treated workbooks *(created at runtime)*  
- **`URLs.csv`** *(recommended)* — league metadata and URLs *(if you externalize away from hard-coded variables)*

## How to run
•	Click the **Binder badge at the top of this section**. 

•	Once Binder is launched, execute cells by pressing **Ctrl/Cmd + Enter**.

•	Locally: download the .py script “Data_Cleaning_Chrono.py” and run with a local Python 3 environment. 

*Note:* Binder may take some time to launch the notebook on the first load, as it needs to build the execution environment. Please be patient. If the session hangs for too long, simply close the tab and relaunch Binder.

### Notes
•	All data are **de-identified**.

•	This notebook focuses on **data processing**; inferential results are out of scope for this portfolio demo.

################################################################################################################################
############################

# Web Scraping & Probabilistic Modeling of Over 2.5 Goals in Football Matches

This project implements a large-scale, fully automated Python pipeline that scrapes football match statistics from SoccerStats.com across 60+ leagues worldwide, processes the data, and computes a set of probability indicators for matches finishing with over 2.5 goals.

The script extracts historical results, upcoming fixtures, team scoring profiles, over/under performance metrics, expected goals distributions, and builds combined probability estimates based on home/away tendencies and statistical variance.

All processed information is exported into Excel files with multiple sheets (raw data + enriched data + treated data ready for decision-making).

# What is produced by the script

This script produces an excel file, containing multiple sheets/databases. These databases/sheets contain the following information:

**1. Full Data**: (name format example: "-2.5Goals\_10-11-2025.xlsx")

**2. Treated Data**: (name format example: "Treated\_-2.5Goals\_10-11-2025.xlsx"): 

## What you’ll find here

For demonstration, we include an anonymized subset (*n* = 4). The pipeline:

•	Merges heterogeneous sources, 

•	Aligns timestamps, standardizes variable names, computes trial- and aggregate-level metrics,

•	Exports tidy, analysis-ready datasets.

## How to run

•	Click the **Binder badge at the top of this section**. 

•	Once Binder is launched, execute cells by pressing **Ctrl/Cmd + Enter**.

•	Locally: download the .py script “OVG\_2.0\_Over2.5Goals.py” and run with a local Python 3 environment. 

*Note:* Binder may take some time to launch the notebook on the first load, as it needs to build the execution environment. Please be patient. If the session hangs for too long, simply close the tab and relaunch Binder.

•	This notebook focuses on **data processing**; inferential results are out of scope for this portfolio demo.


