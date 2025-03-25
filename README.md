# A/B Test Application 

## Project Goal

Bombabomba.com aims to use the "average bidding" method as an alternative to the "maximum bidding" method. This A/B test is conducted to compare the performance of both bidding methods based on user engagement, purchase rates, and earnings.

## Hypothesis

- **H0**: M1 = M2 (There is no statistically significant difference between the two bidding methods.)
- **H1**: M1 != M2 (There is a statistically significant difference between the two bidding methods.)

## Data Used

The dataset includes data from two groups (Test and Control) with the following features:
- **Impression**: Users' exposure to an advertisement.
- **Click**: Users clicking the ad link.
- **Purchase**: Number of purchases made.
- **Earning**: Earnings generated.

The dataset focuses on analyzing the purchase numbers (`Purchase`) for both groups.

## Methods

Key statistical tests used in this project include:

- **Normality Test**: Checking if the data is normally distributed (Shapiro-Wilk Test).
- **Homogeneity of Variance Test**: Testing if the variances of both groups are similar (Levene Test).
- **Independent Two-Sample T Test**: Evaluating whether the difference between the two groups is statistically significant.

## Results

- Normality assumption was met for both groups.
- Variances were homogeneous.
- The independent two-sample T test resulted in a `p-value` of 0.3493, which is greater than 0.05, meaning **H0** cannot be rejected. Therefore, there is no statistically significant difference between the two bidding methods.

## Technologies Used

- **Python**: Used for data processing and analysis.
- **Pandas**: Data manipulation and analysis.
- **SciPy**: Statistical tests (Shapiro-Wilk, Levene, T-test).
- **Statsmodels**: Descriptive statistics and confidence interval calculations.
- **Excel**: Used for storing and analyzing datasets.

## Importance of A/B Testing

A/B testing is a critical tool in digital marketing and product development processes to test the effectiveness of different strategies and make data-driven decisions. These tests help businesses identify the best strategies, improve user experiences, and increase customer engagement. Therefore, A/B testing plays a vital role in making user-centric decisions, measuring the efficiency of marketing campaigns, and optimizing overall business strategies.

## Conclusion and Recommendations

According to the results of this test, there is no statistically significant difference between the "maximum bidding" and "average bidding" methods. However, increasing the sample size is recommended for more definitive results. The test process can continue for a longer period, and further analysis can be conducted using different metrics.

----

# A/B Test Uygulaması - Bombabomba.com

## Proje Amacı

Bombabomba.com sitesi, "maximum bidding" adlı teklif verme türüne alternatif olarak "average bidding" teklif verme türünü kullanmayı planlamaktadır. Bu iki teklif verme türünü karşılaştırmak amacıyla yapılan A/B testi, her iki teklif türünün kullanıcı etkileşimi, satın alma oranları ve kazançlar gibi performans ölçütleri arasındaki farkları değerlendirmek için kullanılmıştır.

## Hipotez

- **H0**: M1 = M2 (İki teklif türü arasında istatistiksel olarak anlamlı bir fark yoktur.)
- **H1**: M1 != M2 (İki teklif türü arasında istatistiksel olarak anlamlı bir fark vardır.)

## Kullanılan Veriler

Veri seti, aşağıdaki özellikleri içeren iki farklı grup (Test ve Control) verilerini içermektedir:
- **Impression**: Kullanıcıların reklamı görme durumu.
- **Click**: Kullanıcıların reklam linkine tıklama durumu.
- **Purchase**: Satın alma sayısı.
- **Earning**: Kazanç.

Veri seti, her iki grup için de satış sayıları (`Purchase`) üzerinden yapılan analizlere odaklanmaktadır.

## Yöntemler

Bu projede kullanılan temel istatistiksel testler:

- **Normallik Testi**: Verilerin normal dağılıma uygun olup olmadığı kontrol edilmiştir (Shapiro-Wilk Testi).
- **Varyans Homojenliği Testi**: İki grubun varyanslarının birbirine yakın olup olmadığı test edilmiştir (Levene Testi).
- **Bağımsız İki Örneklem T Testi**: İki grup arasındaki farkların istatistiksel olarak anlamlı olup olmadığı değerlendirilmiştir.

## Sonuçlar

- Normallik varsayımı her iki grup için de sağlanmıştır.
- Varyanslar homojendir.
- Bağımsız iki örneklem T testi sonucunda, `p-value` değeri 0.3493 bulunmuştur, bu da 0.05'ten küçük olmadığından **H0** reddedilememiştir. Yani, iki teklif türü arasında istatistiksel olarak anlamlı bir fark bulunmamaktadır.

## Kullanılan Teknolojiler

- **Python**: Veri işleme ve analiz için kullanıldı.
- **Pandas**: Veri manipülasyonu ve analiz.
- **SciPy**: İstatistiksel testler (Shapiro-Wilk, Levene, T testi).
- **Statsmodels**: Descriptive statistics ve confidence interval hesaplamaları.
- **Excel**: Veri setlerinin depolanması ve analizler için kullanıldı.

## Projelerin Önemi

A/B testleri, dijital pazarlama ve ürün geliştirme süreçlerinde, farklı stratejilerin etkinliğini test etmek ve doğru kararlar almak için kritik bir araçtır. Bu tür testler, şirketlerin doğru stratejileri belirlemelerine, kullanıcı deneyimini iyileştirmelerine ve son kullanıcı etkileşimini arttırmalarına yardımcı olur. Bu nedenle, A/B testleri; kullanıcı odaklı kararlar almak, pazarlama kampanyalarının verimliliğini ölçmek ve genel iş stratejilerini optimize etmek için büyük önem taşır.

## Sonuç ve Öneriler

Bu testin sonuçlarına göre, şu anda yapılan "maximum bidding" ve "average bidding" teklif türleri arasında istatistiksel olarak anlamlı bir fark bulunmamaktadır. Ancak, daha net sonuçlar alabilmek için gözlem sayısının artırılması önerilmektedir. Test süreci bir süre daha devam edebilir ve farklı metrikler üzerinden incelemeler yapılabilir.

---

