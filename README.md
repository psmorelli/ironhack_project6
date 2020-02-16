# Kickstarter Analysis
## Project 6 | Data Analysis Bootcamp - Ironhack

## 0. Contributors
This work was conducted within the ironhack "Visualizing Real World Data" project week by Tobias Glinzer, Alexander Schwinges and Paschoal Morelli.

## 1. Purpose

    The purpose of this project is to demonstrate the application of data analysis to understand Kickstarter success projects.
    For this project, historical data was scraped by webrobots.io and shared on many CSV files with a monthly view of all projects exists on kickstarter.com. 

## 2. Project Structure

    data/
    |    |
    |    |_ extracted
    |    |    |_2016
    |    |    |    |_ Kickstarter_2016-01-28T09_15_08_781Z
    |    |    |    |    |_ Kickstarter001.csv
    |    |    |    |    |_ Kickstarter002.csv
    |    |    |    |    |_ Kickstarter003.csv
    |    |    |     .   .
    |    |    |     .   .
    |    |    |     .
    |    |    |
    |    |    |_ 2017
    |    |    |_ 2018
    |    |    |_ 2019
    |    |    
    |    |_ transformed
    |        |_ Kickstarter_fixed_date_2016.pkl
    |        |_ Kickstarter_fixed_date_2017.pkl
    |        |_ Kickstarter_fixed_date_2018.pkl
    |        |_ Kickstarter_fixed_date_2019.pkl
    |        |_ Kickstarter_2016.pkl
    |        |_ Kickstarter_2017.pkl
    |        |_ Kickstarter_2018.pkl
    |        |_ Kickstarter_2019.pkl
    |        |_ Kickstarter_hist.csv
    |        
    utils
    |    |_ data_wrangling.py
    |
    data_workflow.ipynb
    kickstarter_analysis_2016-2019_TG.ipynb
    README.md

## 3. Workflow

    * Data Gathering (extract data)
    * Data Wrangling (clean and merge files)
    * Define storytelling of analysis 
    * Create Tableau analysis

## 4. Data Gathering
    
    The data used in this project were made available by consultory webrobots.io and represents a dataset with 4 years of monthly scrape execution on kickstarter projects.
    This database contains information regarding project description, category, success/fail/cancelled states,  project duration and other data.
    
    Data Source:
[Kickstarter Datasets](https://webrobots.io/kickstarter-datasets/)
    
    2,672 were used, only a sample of these files are in "data/extracted" directory.

## 5. Data Wrangling (clean and merge files)

    To simplify the process of creating metrics and dimensions, the data wrangling process was divided into two stages:
    
    Merge raw data: Merge all files and save one pickle file per year.
    
    Create one file per year with one row per project.

    Merge all years into one csv file to import in Tableau.

## 6. Define storytelling of analysis

    The following analysis sequence was defined:

         1 - General indicators.
    
         2 - Number of project and success rates per subcategory.
    
         3 - Number of project and success rates per category.
    
         4 - Number of project and success rates per country.
    
         5 - Influence of goal on success rate.

         6 - Projects by goal vs raised money.

         7 - Outliers.

## 7. Create Tableau analysis

    A story published on the Public Tableau cloud service containing the analysis with highlights of insights.

Tableau Story:
[Kickstarte](https://public.tableau.com/profile/psmorelli#!/vizhome/Kickstarter_15816308999740/KIckstarter)

    