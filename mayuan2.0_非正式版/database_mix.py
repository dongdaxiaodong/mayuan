import sqlite3
conn=sqlite3.connect("mayuan3.db")
cu=conn.cursor()
# write_file=open("mayuan_1.txt",'w')
# all_data=cu.execute("SELECT id, title,answer_index from question").fetchall()
# all_data_list=[]
# for i in range(len(all_data)):
#     now_id=all_data[i][0]
#     now_question=all_data[i][1]
#     now_index=all_data[i][2]
#     now_answer=cu.execute("select content from answer where answer_index = '%s' and que_id='%s'"%(now_index,now_id)).fetchall()[0][0]
#     print(now_question+"*"+now_answer)
the_file=open("mayuan_1.txt",encoding='utf-8')
the_file_list=[line.rstrip() for line in the_file]
for i in range(len(the_file_list)):
    question=the_file_list[i].split("*")[0]
    answer=the_file_list[i].split("*")[1]
    cu.execute("INSERT into mayuandb (question,answer) values ('%s','%s')"%(question,answer))

the_file.close()
conn.commit()
conn.close()


