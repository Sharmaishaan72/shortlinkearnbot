import sqlite3

class users:
    def __init__(self):
        self.conn = sqlite3.connect('bot.db',check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS users (userid INTEGER PRIMARY KEY, shortlinks INTEGER, balance REAL)')
        self.conn.commit()
        
    def adduser(self, userid: int):
        self.c.execute('INSERT INTO users VALUES (?,?,?)',(userid,0,0.0))
        self.conn.commit()

    def getbalance(self, userid: int):
        self.c.execute('Select balance from users where userid=?',(userid,))
        return self.c.fetchone()[0]
    
    def addbalance(self, userid: int, amount: float):
        self.c.execute('Select balance from users where userid=?',(userid,))
        balance = self.c.fetchone()[0]
        self.c.execute('UPDATE users SET balance=? where userid=?',(balance+amount,userid))
        self.conn.commit()

    def getuserinfo(self, userid: int):
        self.c.execute('Select * from users where userid=?',(userid,))
        info = self.c.fetchone()
        return {'userid':info[0],'shortlinks':info[1],'balance':info[2]}
    
    def getallusers(self):
        self.c.execute('Select * from users')
        return self.c.fetchall()
    
    def checkuserexists(self, userid: int):
        self.c.execute('Select userid from users where userid=?',(userid,))
        if self.c.fetchone() == None:
            return False
        return True
