import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display_max_columns',None)
pd.set_option('display.float_format',lambda x:'%.5f'%x)

populasyon=np.random.randint(0,80,10000)
populasyon.mean()

np.random.seed(115)
orneklem=np.random.choice(a=populasyon,size=100)
orneklem.mean()

np.random.seed(10)
orneklem1=np.random.choice(a=populasyon,size=100)
orneklem2=np.random.choice(a=populasyon,size=100)
orneklem3=np.random.choice(a=populasyon,size=100)
orneklem4=np.random.choice(a=populasyon,size=100)
orneklem5=np.random.choice(a=populasyon,size=100)
orneklem6=np.random.choice(a=populasyon,size=100)
orneklem7=np.random.choice(a=populasyon,size=100)
orneklem8=np.random.choice(a=populasyon,size=100)
orneklem9=np.random.choice(a=populasyon,size=100)
orneklem10=np.random.choice(a=populasyon,size=100)

(orneklem1.mean()+orneklem1.mean()+orneklem2.mean()+orneklem3.mean()+orneklem4.mean()+orneklem5.mean()/
+orneklem6.mean()+orneklem7.mean()+orneklem8.mean()+orneklem9.mean()+orneklem10.mean())/10

orneklem1.mean()
##########################################
#Descriptive Statistics
##########################################

import seaborn as sns
df=sns.load_dataset("tips")
df.describe().T

df.head()
df["sex"].value_counts()

df[["tip","total_bill"]].corr()

import statsmodels.stats.api as sms
df=sns.load_dataset("tips")
df.describe().T

sms.DescrStatsW(df["total_bill"]).tconfint_mean()
sms.DescrStatsW(df["tip"]).tconfint_mean()

############### AB TEST ###########################
#1.Normallik varsayımı
#2.Varyans Homojenliği

################### Normallik Varsayımı ################
#Ho:Normal dağılım varsayımı sağlanmaktadır
#H1: ...sağlanmamaktadır.

from scipy.stats import shapiro

df.loc[df["smoker"]=="Yes","total_bill"]
df.loc[df["smoker"]=="No","total_bill"]

test_istatistigi,p_value=shapiro(df.loc[df["smoker"]=="Yes","total_bill"])
print("Test istatistiği=%.4f,p_degeri=%.4f" % (test_istatistigi,p_value))

# p_value < ise 0.05'ten H0 RED
# p_value < değilse 0.05 H0 REDDEDİLMEZ
# yes grubu için varsayım sağlanmamaktadır

test_istatistigi,p_value=shapiro(df.loc[df["smoker"]=="No","total_bill"])
print("Test istatistiği=%.4f,p_degeri=%.4f"%(test_istatistigi,p_value))

# p_value < ise 0.05'ten H0 RED
# p_value < değilse 0.05 H0 REDDEDİLMEZ
# no grubu için varsayım sağlanmamaktadır

################### Varyans Homejenliği ######################3

# H0: Varyans Homejendir
# H1:Varyanslar homojen değildir.

from scipy import stats
stats.levene(df.loc[df["smoker"]=="Yes","total_bill"],df.loc[df["smoker"]=="No","total_bill"])

# p_value < ise 0.05'ten H0 RED
# p_value < değilse 0.05 H0 REDDEDİLMEZ
# p_value değeri 0.045 yani < 0.05 ten değil. H0 Red Varyanslar homojen değildir.

#############################################################
############ Hipotezin Uygulanması  #########################

# parametrik(varsayımlar sağlanıyorsa 2 örneklem t testi)
# nonparametrik(varsayımlar sağlanmıyorsa manwhitneyu )

# H0: M1 = M2 (..iki grup arasında ist. olarak anlamlı bir fark yoktur)
# H1: M1 != M2 (...vardır)

# Varsayımlar sağlanmış gibi davranıyoruz
test_istatistigi,p_value=stats.ttest_ind(df.loc[df["smoker"]=="Yes","total_bill"],df.loc[df["smoker"]=="No","total_bill"],equal_var=True)
print("Test istatistiği=%.4f,p_degeri=%.4f"%(test_istatistigi,p_value))

# Olması gerekn yani non parametrik mannwhitneyo testi
test_istatistigi,p_value=stats.mannwhitneyu(df.loc[df["smoker"]=="Yes","total_bill"],df.loc[df["smoker"]=="No","total_bill"])
print("Test istatistiği=%.4f,p_degeri=%.4f"%(test_istatistigi,p_value))

# Her iki test sonucuda H0 Reddetmedi yani: iki grup arasında ist olarak anlamlı bir farklılık yoktur.



