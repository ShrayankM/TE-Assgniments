import pandas as pd
import numpy as np

import matplotlib.pyplot as plt; plt.rcdefaults()

import numpy as np

sgpa_list = []
sgpa_f = []
sgpa_float = []
distinction = []
first_class = []
second_class = []
atkt = []
df = pd.read_csv("assign_3_data.csv")

df_sgpa = df.iloc[:,-4]
sgpa_list = list(df_sgpa)
for element in sgpa_list:
    sgpa_f.append(element.strip(','))
sgpa_f = [temp.replace('--','0') for temp in sgpa_f]

#for element in sgpa_f:
#    sgpa_float.append(float(element))

sgpa_array = np.array(sgpa_f,dtype=np.float)

distinction = np.where(np.logical_and(sgpa_array<=10,sgpa_array>=7.75))

first_class = np.where(np.logical_and(sgpa_array<=7.74,sgpa_array>=6.75))

h_second_class = np.where(np.logical_and(sgpa_array<=6.74,sgpa_array>=6.25))

second_class = np.where(np.logical_and(sgpa_array<=6.24,sgpa_array>=5.5))

fail = np.where(sgpa_array==0)
d_len=len(sgpa_array[distinction])

f_len=len(sgpa_array[first_class])

h_s_len=len(sgpa_array[h_second_class])

s_len=len(sgpa_array[second_class])

fa_len=len(sgpa_array[fail])


labels = 'Distinction','First_Class','Higher Second_Class','Second_Class','Fail'

sizes = [d_len, f_len, h_s_len,s_len, fa_len]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
explode = (0.1, 0, 0, 0,0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

def CalculateClass(marks_array = np.array([0,0])):
    
    distinction = np.where(np.logical_and(marks_array<=100,marks_array>=60))
    first_class = np.where(np.logical_and(marks_array<=59,marks_array>=55))
    h_second_class = np.where(np.logical_and(marks_array<=54,marks_array>=51))
    second_class = np.where(np.logical_and(marks_array<=50,marks_array>=40))
    fail = np.where(marks_array==0)
    return(distinction,first_class,h_second_class,second_class, fail)


subject_index = [8,16,24,32,40,81,95,103,111,119]

for i in subject_index:
    subject_marks=df.iloc[:,i]
    marks_list= list(subject_marks)
    
    marks_list = [tempV.replace('FF','0') for tempV in marks_list]
    marks_array=np.array(marks_list,dtype=np.int)
    
    returned_array = CalculateClass(marks_array)
    
    d_len=len(marks_array[returned_array[0]])
    f_len=len(marks_array[returned_array[1]])
    h_s_len=len(marks_array[returned_array[2]])
    s_len=len(marks_array[returned_array[3]])
    fa_len=len(marks_array[returned_array[4]])
   
   
    objects = ('Distinction','First','HigherSecond','Second','Fail')
    y_pos = np.arange(len(objects))
    performance = [d_len,f_len,h_s_len,s_len,fa_len]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Total_Students')
    plt.title(subject_marks.name)
    plt.show()
    
    

    


