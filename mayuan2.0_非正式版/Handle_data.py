import re
import sqlite3
conn=sqlite3.connect("mayuan.db")
cu=conn.cursor()
mayuan_file=open("new_mayuan.txt",encoding='utf-8')
mayuan_list=[line.rstrip() for line in mayuan_file]
split_question_str="[1234567890]+[、．.]"
split_option_str="[ABCDE]+"
questions_list=re.split(split_question_str,"".join(mayuan_list))
for i in range(1,len(questions_list)):
    line = questions_list[i]
    option_line=re.findall(split_option_str,line)
    line_list=re.split(split_option_str,line)
    question=line_list[0]
    answer = ""
    answer_number=1
    # E -1   D -2   C -3 B -4  A -5
    if(len(option_line[0])>1):
    #     多选题
        if "A" in option_line[0]:
            answer+=str(answer_number)
            answer+="."
            answer+=line_list[-5]
            answer+="  "
            answer_number+=1
        if "B" in option_line[0]:
            answer+=str(answer_number)
            answer+="."
            answer+=line_list[-4]
            answer+="  "
            answer_number+=1
        if "C" in option_line[0]:
            answer+=str(answer_number)
            answer+="."
            answer+=line_list[-3]
            answer+="  "
            answer_number+=1
        if "D" in option_line[0]:
            answer+=str(answer_number)
            answer+="."
            answer+=line_list[-2]
            answer+="  "
            answer_number+=1
        if "E" in option_line[0]:
            answer+=str(answer_number)
            answer+="."
            answer+=line_list[-1]
            answer+="  "
            answer_number+=1
    else:
        if option_line[0]=="A":
            answer+=line_list[-4]
        elif option_line[0]=="B":
            answer+=line_list[-3]
        elif option_line[0]=="C":
            answer+=line_list[-2]
        elif option_line[0]=="D":
            answer+=line_list[-1]
    cu.execute("INSERT INTO mayuandb (question,answer) VALUES ('%s','%s')"%(question,answer))
conn.commit()
conn.close()

