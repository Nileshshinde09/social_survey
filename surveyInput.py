import streamlit as st
import sqlite3
import pandas as pd
def connect():
    try:
        conn = sqlite3.connect("surveyData.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists surveytable (username varchar(50) null,userage INTEGER not null,social_platform varchar(50) not null,violent_speech varchar(400) null,hateful_speech varchar(400) null,harmful_speech varchar(400) null,spam_misleading_speech varchar(400) null,language varchar(20) not null);""")
        return conn,c
    except Exception as e:
        print(f"Error Occured while connecting to database :: {e}") 
def insert_data(surveylst):
    try:
        conn,c=connect()
        with conn:
            c.execute("insert into surveytable values (:username, :userage, :social_platform, :violent_speech, :hateful_speech ,:harmful_speech, :spam_misleading_speech ,:language)", 
                    {'username': surveylst[0], 'userage':surveylst[1] , 'social_platform':surveylst[2] , 'violent_speech':surveylst[3] , 'hateful_speech':surveylst[4] ,'harmful_speech':surveylst[5], 'spam_misleading_speech':surveylst[6] , 'language':surveylst[7]})
        return 1
    except Exception as e:
        print(f"Error Occured while inserting the data :: {e}")
        return -1 
def showDf():
    conn,c=connect()
    try:
        db_df = pd.read_sql_query("SELECT * FROM surveytable", conn)
        db_df.to_csv('df.csv', index=False,header=['username','userage','social_platform','violent_speech','hateful_speech','harmful_speech','spam_misleading_speech','language'])
        return 1
    except Exception as e:
        return -1
        print(e)

def downloadDF():
    conn,c=connect()
    try:
        db_df = pd.read_sql_query("SELECT * FROM surveytable", conn)
        db_df.to_csv('df.csv', index=False)
        return 1
    except Exception as e:
        print(e)
        return -1

def getSurvey(name='',userage='',social_platform='',violent_speech='',hateful_speech='',harmful_speech='',spam_misleading_speech='',language=''):
    if name=='':
        name='unknown'
    if violent_speech=='':
        violent_speech='empty'
    if hateful_speech=='':
        hateful_speech='empty'
    if harmful_speech=='':
        harmful_speech='empty'
    if spam_misleading_speech=='':
        spam_misleading_speech='empty'
    surveylst = [name,userage,social_platform,violent_speech,hateful_speech,harmful_speech,spam_misleading_speech,language]
    
    if insert_data(surveylst):
        return 1
    else:
        return -1

