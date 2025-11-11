[![Launch Binder](https://mybinder.org/badge_logo.svg)](.../v2/gh/FabioATMonteiro92/WebScrappingFootballProbabilityMinus2.5GoalsPerGame/HEAD?urlpath=lab)

# Web Scraping & Probabilistic Modeling of Over 2.5 Goals in Football Matches

This project implements a large-scale, fully automated Python pipeline that scrapes football match statistics from SoccerStats.com across 60+ leagues worldwide, processes the data, and computes a rich set of probability indicators for matches finishing with over 2.5 goals.

The script extracts historical results, upcoming fixtures, team scoring profiles, over/under performance metrics, expected goals distributions, and builds combined probability estimates based on home/away tendencies and statistical variance.

All processed information is exported into Excel files with multiple sheets (raw data + enriched data + treated data ready for decision-making).

https://mybinder.org/v2/gh/FabioATMonteiro92/WebScrappingFootballProbabilityOver2.5GoalsPerGame/HEAD?filepath=OVG_v2_Over2_5Goals.ipynb

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


