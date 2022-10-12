# #  steps invloved in Data Visualization
# # step-1 import libraries
# import seaborn as sns
# import matplotlib.pyplot as plt

# # step-2 set a theme
# sns.set_theme(style="ticks", color_codes=True)

# # step-3 import data set (you can also import your own data)
# kashti = sns.load_dataset("titanic")
# # print(kashti)

# # step-4 plot basic graph with 1 variable (count plot)
# p1 = sns.countplot(x='sex', data=kashti, hue="class")
# plt.show()

# # step-5 plot basic graph with 2 variable (count plot)
# p1 = sns.countplot(x="sex", data=kashti, hue="class")
# p1.set_title("Baba Aammar ka count plot for kashti")  # is tarah hum title add karenge
# plt.show()






import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the example tips dataset
chilla = pd.read_excel("Chilla_data2_for_plots(google_sheets).xlsx")

chilla["Age"]=chilla["Age"].astype('int16')

sns.boxplot(x="Gender", y="Age", data=chilla)
plt.show()
