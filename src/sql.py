# import sqlite3
import psycopg2

def clean_db():
    cur = conn.cursor()
    sql = "DROP TABLE IF EXISTS settings"
    cur.execute(sql)
    sql = """CREATE TABLE IF NOT EXISTS settings (
        id BIGINT PRIMARY KEY,
        delete BOOLEAN,
        delay INT
    )"""
    cur.execute(sql)
    conn.commit()

def clean_prefix():
    cur = conn.cursor()
    sql = "DROP TABLE IF EXISTS guild_prefix"
    cur.execute(sql)

    sql = """CREATE TABLE IF NOT EXISTS guild_prefix (
        id BIGSERIAL PRIMARY KEY,
        prefix VARCHAR(5)
    )"""
    cur.execute(sql)
    conn.commit()

def u_prefix(values):
    cur = conn.cursor()
    sql = """UPDATE guild_prefix SET id=%s, prefix=%s"""
    cur.execute(sql, values)
    conn.commit()

def i_prefix(values):
    cur = conn.cursor()
    sql = """INSERT INTO guild_prefix(id, prefix) VALUES(%s, %s)"""
    cur.execute(sql, values)
    conn.commit()

def read_prefix(values):
    cur = conn.cursor()
    sql = """SELECT prefix FROM guild_prefix WHERE id=%s"""
    cur.execute(sql, values)
    rows = cur.fetchall()
    print('read_pref', rows)
    return rows
def read_settings(values):
    sql = """SELECT delete, delay FROM settings WHERE id=%s"""
    cur = conn.cursor()
    cur.execute(sql, values)
    rows = cur.fetchall()
    print('read_settings', rows)
    return rows, rows

def i_guild_settings(values):
    cursor = conn.cursor()
    sql = """INSERT INTO settings(id, delete, delay) VALUES(%s, %s, %s)"""
    cursor.execute(sql, values)
    conn.commit()

def read_table(table):
    sql = "SELECT delete, delay FROM settings"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    return rows

def u_guild_settings(values):
    cursor = conn.cursor()
    sql = """UPDATE settings SET 
            delete=%s,
            delay=%s
            WHERE id=%s"""
    cursor.execute(sql, values)
    conn.commit()

def d_guild(values):
    cursor = conn.cursor()
    sql = """DELETE FROM settings WHERE id=%s"""
    cursor.execute(sql, values)
    conn.commit()

def d_prefix(values):
    cursor = conn.cursor()
    sql = """DELETE FROM guild_prefix WHERE id=%s"""
    cursor.execute(sql, values)
    conn.commit()

try:
    # conn = sqlite3.connect('./db/settings.db')
    conn = psycopg2.connect('postgres://tlmugcbktybmrk:9495720bb66625b4ceb47d5520a3a1784c5d6583d2cca376f030f1f8102c5a1f@ec2-46-137-187-23.eu-west-1.compute.amazonaws.com:5432/d2bj38648d3ukp')
    print(read_table('settings'))
    # clean_db()
    # clean_prefix()
    # u_prefix((55555555, 'a',))
    # print(read_prefix())
    # clean_db()
    # create_prefix()
    # print(read_prefix((146952202815012864,)))
except psycopg2.Error as error:
    print("Error while connecting to sqlite", error)