import sqlite3,random
import os
import time
import requests

class ShortLinkCreator:
    def __init__(self):
        self.conn = sqlite3.connect('bot.db',check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS shortlinks (userid INTEGER, linkid varchar(30) PRIMARY KEY, reward REAL, used BOOLEAN, created_at REAL)')
        self.conn.commit()

    def createshortlink(self, userid: int, reward: float):
        self.c.execute('Select linkid from shortlinks')
        ids = self.c.fetchall()
        linkid = "".join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=10))
        while linkid in ids:
            linkid = "".join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=10))
        self.c.execute('INSERT INTO shortlinks VALUES (?,?,?,?,?)',(userid,linkid,reward,False,time.time()))
        self.conn.commit()
        return linkid
    
    def useshortlink(self, linkid: str):
        self.c.execute('Select reward,used from shortlinks where linkid=?',(linkid,))
        info = self.c.fetchone()
        #print(info)
        if not info or info[1]: #checks if the link is used
            return None
        elif info[1] == True:
            return None
        reward = info[0]
        self.c.execute('UPDATE shortlinks SET used=TRUE where linkid=?',(linkid,))
        self.conn.commit()
        return reward
    
    def addbalance(self, linkid, amount: float):
        self.c.execute('Select userid from shortlinks where linkid=?',(linkid,))
        userid = self.c.fetchone()[0]
        self.c.execute('Select balance from users where userid=?',(userid,))
        balance = self.c.fetchone()[0]
        self.c.execute('UPDATE users SET balance=? where userid=?',(balance+amount,userid))
        requests.post(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage",json= {
            "chat_id": userid,
            "text": "You have earned "+str(amount)+" "+os.getenv('currency')+" by solving a shortlink!"})
        self.conn.commit()

    def completeshortlink(self, linkid: str):
        reward = self.useshortlink(linkid=linkid)
        if reward == None:
            return "Link already used or dosent exist"
        else:
            self.addbalance(linkid,reward)
            return f"Link used successfully. You have earned {reward} {os.getenv('currency')}"
        
    def returncountlast24h(self, userid: int,timestamp_rn:float):
        self.c.execute('Select count(*) from shortlinks where userid=? and (?-created_at) <86400',(userid,timestamp_rn))
        count = self.c.fetchone()[0]
        return count


