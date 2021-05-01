# AB Test Uygulaması
# bombabomba.com sitesinin "maximum bidding" adı verilen teklif verme türüne alternatif olarak
# "average bidding" teklif verme türünü kullanmak istiyor
# bu iki türü kıyaslamak için gereken verileri hipotez testi kurup karşılaştırcağız.

# H0: M1 = M2 (iki türün uygulanması arasında istatistiksel olarak anlamlı bir fark yoktur.)
# H1: M1 != M2 (iki türün uygulanması arasında istatistiksel olarak anlamlı bir fark vardır)

########### AB TEST ############
###### Bağımsız iki örneklem T Testi ########

# Impression : Kullanıcı bir reklam görür
# Click : Kullanıcı reklam linkini tıklar
# Purchase : Satın alma sayısı
# Earning : Kazanç

import pandas as pd
import statsmodels.stats.api as sms
from scipy.stats import shapiro
from scipy import stats

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df_ = pd.read_excel("dataset/ab_testing_data.xlsx",sheet_name="Test Group")
df_t = df_.copy()
df = pd.read_excel("dataset/ab_testing_data.xlsx",sheet_name="Control Group")
df_c= df.copy()
df_t.head()
df_c.head()

df_t["Purchase"].describe().T
df_t.shape
df_c["Purchase"].describe().T
df_c.shape

sms.DescrStatsW(df_t["Purchase"]).tconfint_mean()
sms.DescrStatsW(df_c["Purchase"]).tconfint_mean()

##################### Varsayım Kontrolü ##################

###### Normallik Varsayımı
# p-value < ise 0.05'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.


test_istatistigi, pvalue = shapiro(df_t["Purchase"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: ...sağlanmamaktadır
# test grubu için normallik varsayımı sağlanmaktadır.Çünkü pvalue değeri 0.05 ten küçük değil.H0 Reddedemiyoruz.
# Normallik varsayımı için istediğimizde buydu zaten

test_istatistigi, pvalue = shapiro(df_c["Purchase"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: ...sağlanmamaktadır
# control grubu için normallik varsayımı sağlanmaktadır.Çünkü pvalue değeri 0.05 ten küçük değil.H0 Reddedemiyoruz.
# Normallik varsayımı için istediğimizde buydu zaten

# Sonuç olarak normallik varsayımı iki grup içinde sağlanıyor.

########### Varyans Homojenligi Varsayımı

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

stats.levene(df_t["Purchase"],df_c["Purchase"])

# p-value < ise 0.05'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.

# Varyanslar homojendir.

########### Bağımsız İki örneklem T testi

# H0: M1 = M2 (iki türün uygulanması arasında istatistiksel olarak anlamlı bir fark yoktur.)
# H1: M1 != M2 (iki türün uygulanması arasında istatistiksel olarak anlamlı bir fark vardır)

test_istatistigi, pvalue = stats.ttest_ind(df_t["Purchase"],df_c["Purchase"],equal_var=True)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

# p_value değeri 0.3493 yani 0.05 ten küçük değil yani H0 reddedemiyoruz.

# İki türün uygulanması arasında istatistiksel olarak anlamlı bir fark yoktur.


############# CEVAPLAR ###########################

# 1.Bu A/B testinin hipotezi nasıl tanımlanır?

# H0: M1 = M2 (iki türün uygulanması arasında istatistiksel olarak anlamlı bir fark yoktur.)
# H1: M1 != M2 (iki türün uygulanması arasında istatistiksel olarak anlamlı bir fark vardır)


# 2.İstatistiksel olarak anlamlı sonuçlar çıkarabilir miyiz?

# Evet istatistiksel olarak anlamlı sonuçlar çıkarabiliriz.Yeterli gözlem sayısı var n>30.


# 3.Hangi test kullanıldı?

# Bağımsız iki örneklem T testi


# 4.Soru 2.ye verilen cevaba göre, müşteri tavsiyesi nedir?

# Gözlem sayısını arttırmak sonuçların netleşmesi için fayda sağlar. Bir süre daha test süreci devam edilebilir.