import pandas as pd 
from psycopg2 import sql, connect
import json
import os
import numpy as np
from dict import *


def get_CONFIG(): 
    try: 
        config_path = os.path.join(os.getcwd().split("Dis_project")[0], "config.json")
        with open(config_path) as json_data_file: 
            CONFIG = json.load(json_data_file)
    except: 
        config_path = os.path.join(os.getcwd().split("src")[0], "src", "config.json")
        with open(config_path) as json_data_file: 
            CONFIG = json.load(json_data_file)
    CONFIG["PATHS"]["LAPTOP_DATA"] = os.path.join(os.getcwd().split("src")[0]+CONFIG["PATHS"]["LAPTOP_DATA"])
    return CONFIG
CONFIG = get_CONFIG()


def get_discount(cur): 
    sql_string ="SELECT * FROM specs ORDER BY discount DESC LIMIT (10);"
    user_sql = sql.SQL(sql_string).format(sql.Identifier(CONFIG["DATABASE"]["schema"]))
    cur.execute(user_sql)
    data = cur.fetchall()
    return data 


def get_keys(_data): 
    def get_key(_key,_val):
        for key, value in processor_brand_dict.items():
            if _key in key:
                for local_val in _val: 
                    for dict_val in value: 
                        if local_val==dict_val: 
                            return dict_val

    for row in _data: 
        p_lst = []
        for k, v in processer_name_revert.items():
            if row[3]==k: 
                row[3] = get_key(row[2],v)
        for k,v in weight.items(): 
            if row[12]==v: 
                row[12] = k 
    return _data
    

def get_filted_data(reqs,cur): 
    sql_string ="SELECT * FROM specs "
    where_clause = "where"

    def add_sql(reqs): 
        users_reqs = reqs[0].split(";")
        pos__ = ["Processor_name","ram_GB",'display_size',"weight"]
        for req in users_reqs: 
            if req in pos__: 
                print(req)
                sql_string+=f"{where_clause} {req} in (SELECT {req} FROM specs ORDER BY {req} DESC LIMIT (5)) "
                where_clause = "and"

    # Hvad er formålet med denne pc?  
    if reqs[0]!="0": 
        add_sql(reqs[0])

    # Hvor meget vil du betale for din computer?  
    if reqs[1]!="0":  
        lowest_p, highest_p = pd.to_numeric(reqs[1].split(";"))
        sql_string+=f"{where_clause} latest_price > {lowest_p} and latest_price < {highest_p} "
        where_clause = "and"

    # Hvilket styresystem foretrækker du? 
    if reqs[2]!="0":  
        os = reqs[2]
        sql_string+= f"{where_clause} os='{os}'"
        where_clause = "and"

    # Hvis du valgte gaming, hvad er så det vigtigste for dig?  
    if reqs[3]!="0": 
        add_sql(reqs[3])

    sql_string+=";"
    user_sql = sql.SQL(sql_string).format(sql.Identifier(CONFIG["DATABASE"]["schema"]))
    cur.execute(user_sql)
    return get_keys([list(x) for x in cur.fetchall()])



def init_database(cur): 
    with open("sqlqueries/db_init.sql") as init_db: 
        sql_init = init_db.read().replace("INSERT_PATH_TO_CONFIG.JSON", CONFIG["PATHS"]["LAPTOP_DATA"])
        cur.execute(sql.SQL(sql_init))

    df = pd.read_csv(CONFIG["PATHS"]["LAPTOP_DATA"])

    df["processor_name"] = pd.to_numeric(df["processor_name"].apply(lambda x: Processor_name[x]))
    df["weight"] = pd.to_numeric(df["weight"].apply(lambda x: weight[x]))
    df = df.replace("Missing","0")
    # Cleaning data 
    df[["latest_price", "old_price"]] = df[["latest_price", "old_price"]].apply(lambda x : x/10)
    df["ram_gb"] = pd.to_numeric(df["ram_gb"].apply(lambda x: (x.replace("GB", ""))))

    df["processor_gnrtn"] = pd.to_numeric(df["processor_gnrtn"].apply(lambda x: x.replace("th","")))
    df["hdd"] = pd.to_numeric(df["hdd"].apply(lambda x: x.replace("GB","")))
    df["ssd"] = pd.to_numeric(df["ssd"].apply(lambda x: x.replace("GB","")))
    df = df.rename(columns={"hdd": "hdd_GB","ssd": "ssd_GB" })
    cols = df.columns.to_list()

    df = df.to_numpy()
    # Inserting in Database 
    for x in df: 
        vals = tuple(x)
        sql_string = f"""INSERT INTO public.specs (Brand,
                        Model,
                        Processor_brand ,
                        Processor_name ,
                        Processor_gen ,
                        ram_GB ,
                        ram_type ,
                        ssd ,
                        hdd ,
                        os ,
                        os_bit ,
                        Graphic_card ,
                        Weight ,
                        Display_size ,
                        Warranty ,
                        Touchscreen ,
                        msoffice ,
                        latest_price ,
                        old_price ,
                        discount ,
                        Star_rating ,
                        Ratings ,
                        reviews ) VALUES {vals};"""
        cur.execute(sql.SQL(sql_string))
        # print(sql_string)
    return True,cols


