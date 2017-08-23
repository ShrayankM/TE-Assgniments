import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

first_class = np.where(np.logical_and(sgpa_array<=7.74,sgpa_array>=6.5))

second_class = np.where(np.logical_and(sgpa_array<=6.5,sgpa_array>=5.5))

atkt = np.where(sgpa_array==0)

d_len=np.count_nonzero(distinction)
print(d_len)

f_len=np.count_nonzero(first_class)
print(f_len)

s_len=np.count_nonzero(second_class)
print(s_len)

at_len=np.count_nonzero(atkt)
print(at_len)

labels = 'Distinction','First_Class','Second_Class','ATKT'

sizes = [d_len, f_len, s_len, at_len]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
