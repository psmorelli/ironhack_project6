import pandas as pd
import numpy as np
import json
from os import path

def ks_merge_files(input_file,output_file,extract_date):

    #
    df_kickstarter = pd.read_csv(input_file)

    #
    df_kickstarter["usd_goal"]      =   df_kickstarter["goal"] * df_kickstarter["static_usd_rate"]
    df_kickstarter["created_at"]    =   pd.to_datetime(df_kickstarter["created_at"], unit='s')
    df_kickstarter["deadline"]      =   pd.to_datetime(df_kickstarter["deadline"], unit='s')
    df_kickstarter["launched_at"]   =   pd.to_datetime(df_kickstarter["launched_at"], unit='s')
    df_kickstarter["state_changed_at"]   =   pd.to_datetime(df_kickstarter["state_changed_at"], unit='s')

    #
    def extract_category_lvl1(json_data):
        parsed_json = (json.loads(json_data))
        try:
            cat = parsed_json["slug"].split("/")[0]
        except:
            cat = np.nan
        return  cat

    #
    def extract_category_lvl2(json_data):
        parsed_json = (json.loads(json_data))
        try:
            cat = parsed_json["slug"].split("/")[1]
        except:
            cat = np.nan
        return  cat

    #
    def extrat_user_id(json_data):
        try:
            json_data = json_data
            parsed_json = (json.loads(json_data))
            id = str(parsed_json["id"])
        except:
            id = np.nan
        return id
    
    #
    def extrat_url(json_data):
        try:
            json_data = json_data
            parsed_json = (json.loads(json_data))
            url = parsed_json["web"]["project"]
        except:
            url = np.nan
        return url

    #
    df_kickstarter["category_lvl1"] = df_kickstarter["category"].apply(lambda x: extract_category_lvl1(x))
    df_kickstarter["category_lvl2"] = df_kickstarter["category"].apply(lambda x: extract_category_lvl2(x))
    df_kickstarter["user_id"] = df_kickstarter["creator"].apply(lambda x: extrat_user_id(x))
    df_kickstarter["project_url"] = df_kickstarter["urls"].apply(lambda x: extrat_url(x))

    #
    columns =   ["slug",
             "name",
             "blurb",
             "category_lvl1",
             "category_lvl2",
             "country",
             "created_at",
             "deadline",
             "launched_at",
             "usd_goal",
             "usd_pledged",
             "state",
             "state_changed_at",
             "backers_count",
             "user_id",
             "project_url"
             ]

    #
    df_kickstarter = df_kickstarter[columns]
    df_kickstarter["extract_date"] = pd.to_datetime(extract_date)

    # 
    if path.exists(output_file):
        df_hist = pd.read_pickle(output_file)
        df_hist = pd.concat([df_hist,df_kickstarter], ignore_index=True)
        df_hist.to_pickle(output_file)
    else:
        df_kickstarter.to_pickle(output_file)
    
def success_failed_unique_rows(input_file,output_file,extract_month):

    df_kickstarter = pd.read_pickle(input_file)

    df_kickstarter = df_kickstarter[df_kickstarter["state"].isin(["successful","failed"])]

    df_kickstarter['extract_month'] = pd.to_datetime(df_kickstarter['extract_date']).dt.to_period('M').dt.to_timestamp()
    df_kickstarter['created_month'] = pd.to_datetime(df_kickstarter['created_at']).dt.to_period('M').dt.to_timestamp()

    df_kickstarter = df_kickstarter[df_kickstarter["extract_month"] == extract_month]

    df_kickstarter["rank_row"] = (df_kickstarter.sort_values(["usd_pledged"], ascending=True)
             .groupby(['project_url'])
             .cumcount() + 1)

    df_kickstarter = df_kickstarter[df_kickstarter["rank_row"] == 1]
    df_kickstarter = df_kickstarter.drop(columns="rank_row")

    df_kickstarter.to_pickle(output_file)


