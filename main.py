# Gerekli kütüphaneleri yükleyin
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# 1. Veri kümesini okuyun
file_path = 'Automobile.csv'  # Dosya yolu
data = pd.read_csv(file_path)

# 2. Eksik Verileri İnceleme
print("\nEksik Değer Sayısı:")
print(data.isnull().sum())

# 3. Eksik Verileri Doldurma (Sadece 'horsepower' eksik)
if 'horsepower' in data.columns:
    data['horsepower'] = data['horsepower'].fillna(data['horsepower'].mean())  # Ortalama ile doldurma

# 4. Kategorik Değişkenleri Dönüştürme (One-Hot Encoding)
if 'origin' in data.columns:
    data = pd.get_dummies(data, columns=['origin'], prefix='origin')

# 5. 'name' sütununu kaldırma (analiz için gerekliyse)
if 'name' in data.columns:
    data = data.drop('name', axis=1)

# 6. Veriyi Normalizasyon
scaler = MinMaxScaler()
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

# 7. Veri Görselleştirme
# Korelasyon matrisi
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi")
plt.show()

# Dağılım grafikleri
sns.pairplot(data)
plt.show()

# 8. İşlenmiş Veriyi Kontrol Et
print("\nİşlenmiş Veri Kümesi:")
print(data.info())
print(data.head())

# 9. İşlenmiş Veriyi Kaydetme
data.to_csv('Processed_Automobile.csv', index=False)  # Yeni bir dosya ismiyle kaydediyoruz
print("\nİşlenmiş Veriği 'Processed_Automobile.csv' dosyasına kaydedildi.")

