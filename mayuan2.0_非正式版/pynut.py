from pynput.keyboard import Listener
import logging
from os import path
from win32 import win32clipboard as w
import win32con
import sqlite3
import win32api
ROOT = path.dirname(path.realpath(__file__))
logging.basicConfig(filename=("keylogger.txt"),format="%(asctime)s:%(message)s",level=logging.DEBUG)

def gettext():
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return t
def press(key):
    logging.info(key)
    try:
        import_key=key.char
        if import_key in ['w','W']:
            question=gettext().decode('gb2312')
            result=get_answer(question)
            win32api.MessageBox(0, result, "answer :")
    except Exception as e:
        print(e)
        print("no")
def get_answer(question):
    return_answer=""
    try:
        conn = sqlite3.connect(path.join(ROOT,"mayuan3.db"))
        cu = conn.cursor()
        result_title=cu.execute("select answer from mayuandb where question  like '%%%%%s%%%%'" %(question)).fetchall()
        # for answer in result_title:
        #     the_id=answer[0]
        #     the_index=answer[1]
        #     result_answer=cu.execute("select content from answer where que_id='%s'and answer_index='%s'"%(the_id,the_index)).fetchall()
        #     return_answer+=result_answer[0][0]
        # mayuan2_list = cu_2.execute("select answer from mayuandb where question like '%%%%%s%%%%'" % (question)).fetchall()
        # for yuan2 in mayuan2_list:
        #     return_answer += "\n"
        #     return_answer += yuan2
        for every_answer in result_title:
            return_answer+=every_answer[0]
            return_answer+="\n"
        print(result_title)
    except Exception as e:
        print(e)
        print("no in sql")
        conn.rollback()
    finally:
        conn.close()
    return return_answer

with Listener(on_press = press) as listener:
        listener.join()
