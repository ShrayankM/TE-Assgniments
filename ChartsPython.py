import pandas as pd
import numpy as np
#import plotly.plotly as py
#import plotly.figure_factory as ff
import matplotlib.pyplot as plt; plt.rcdefaults()



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
#plt.show()

def CalculateClass(marks_array = np.array([0,0])):
    
    distinction = np.where(np.logical_and(marks_array<=100,marks_array>=60))
    first_class = np.where(np.logical_and(marks_array<=59,marks_array>=55))
    h_second_class = np.where(np.logical_and(marks_array<=54,marks_array>=51))
    second_class = np.where(np.logical_and(marks_array<=50,marks_array>=40))
    fail = np.where(marks_array==0)
    return(distinction,first_class,h_second_class,second_class, fail)


subject_index = [8,16,24,32,40,81,95,103,111,119]
subject_names = ['A','B','C','D','E','F','G','H','I','J']
listl = [0,1,2,3,4,5,6,7,8,9]
ind = np.array(listl)
width = 0.1
d_lenL = []
f_lenL = []
h_s_lenL = []
s_lenL = []
fa_lenL = []
subjects = []
max_list = []
min_list = []
avg_list = []
len_list = 0
sum_list = 0

for i,j in  zip(subject_index,subject_names):
    subject_marks=df.iloc[:,i]
    subject_marks.name=j
    marks_list= list(subject_marks)
    
    marks_list = ['FF' if x!=x else x for x in marks_list]
    marks_list = [tempV.replace('FF','0') for tempV in marks_list]
    marks_array=np.array(marks_list,dtype=np.int)
    max_list.append(max(marks_array))
    min_list.append(min(marks_array))
    sum_list = sum(marks_array)
    len_list = len(marks_array)
    avg_list.append(sum_list/len_list)
    returned_array = CalculateClass(marks_array)
    d_lenL.append(len(marks_array[returned_array[0]]))
    f_lenL.append(len(marks_array[returned_array[1]]))
    h_s_lenL.append(len(marks_array[returned_array[2]]))
    s_lenL.append(len(marks_array[returned_array[3]]))
    fa_lenL.append(len(marks_array[returned_array[4]]))
    subjects.append(subject_marks.name)

fig=plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind,d_lenL,width,color='gold')
rects2 = ax.bar(ind+width,f_lenL,width,color='yellowgreen')
rects3 = ax.bar(ind+width*2,h_s_lenL,width,color='lightcoral')
rects4 = ax.bar(ind+width*3,s_lenL,width,color='lightskyblue')
rects5 = ax.bar(ind+width*4,fa_lenL,width,color='red')


ax.set_ylabel('Student Count')
ax.set_xticks(ind+width)
ax.set_xticklabels(subjects)
  
    
plt.show() 



print("Subjects" , "    | MAX","| MIN","| AVG             |")
print("--------------------------------------------")
for i in range(10):
    
    print(subjects[i],' | ',max_list[i],'| ',min_list[i],'|  ',avg_list[i],' |') 
    
    
    
#df2 = pd.DataFrame([[238,'S150234440','XYZ','AB','DF',12,12,12,12,12,'aa','aa',0,'a',0,0,5,80,'PASS',1]],columns=list(210258_Tot%  210258_crd 210258_Grd 210258_Grd Pts 210258_Crd pts   SGPAEarn_CreditResultClass ))
#df.append(df2)

roll_df = df.iloc[:,1]
roll_marks = df.iloc[:,5]
df_merge = pd.DataFrame({'210241_TH':df.iloc[:,5],'seat no':df.iloc[:,1],})
