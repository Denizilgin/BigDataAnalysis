# Gerçek Zamanlı Büyük Veri Analitiği ile Anomali Tespiti: Spark ve Kafka Entegrasyonu

Bu proje, **Apache Kafka** ve **Apache Spark Streaming** teknolojilerini kullanarak gerçek zamanlı veri işleme ve anomali tespiti gerçekleştirmeyi amaçlamaktadır.

## Özellikler

- Gerçek zamanlı veri işleme
- Anomali tespiti
- Veri ön işleme (eksik veri temizliği, normalizasyon, kategorik veri dönüşümü)
- Makine öğrenmesi modelleriyle değerlendirme: **Random Forest**, **Decision Tree**, ve **Linear Regression**
- Kafka ile veri akışı entegrasyonu
- Spark Streaming ile gerçek zamanlı veri analizi

## Kullanılan Teknolojiler ve Araçlar

- **Apache Kafka**: Veri akışını yönetmek için kullanıldı.
- **Apache Spark Streaming**: Gerçek zamanlı veri işleme.
- **Python**: Veri işleme ve model geliştirme.
- **Pandas** ve **NumPy**: Veri analizi ve matematiksel işlemler.
- **Scikit-learn**: Makine öğrenmesi modellerinin uygulanması.
- **Matplotlib** ve **Seaborn**: Veri görselleştirme.

## Veri Seti

Proje, **"Automobile.csv"** veri setini kullanmaktadır. Bu veri seti:
- Otomobillerin teknik özelliklerini ve kategorik bilgilerini içerir.
- Sürekli ve kategorik veriler ile eksik değerlere sahip olması nedeniyle anomali tespiti için uygundur.

## Uygulanan Adımlar

### 1. Veri Ön İşleme
- Eksik veriler ortalama ile dolduruldu.
- Kategorik veriler **One-Hot Encoding** yöntemiyle dönüştürüldü.
- Sayısal veriler **Min-Max Scaling** yöntemi ile normalize edildi.

### 2. Makine Öğrenmesi Modelleri
- **Random Forest Regressor**
- **Decision Tree Regressor**
- **Linear Regression**

Performans değerlendirmesi için aşağıdaki metrikler kullanıldı:
- **Mean Squared Error (MSE)**
- **R² Skoru**

### 3. Gerçek Zamanlı Veri İşleme
- Kafka, veri akışını yönetmek için kullanıldı.
- Spark Streaming, Kafka’dan gelen verileri analiz etti ve sonuçları tekrar Kafka’ya gönderdi.

## Kurulum

1. Apache Kafka ve Zookeeper'ı indirin ve çalıştırın:
   ```bash
   ./bin/zookeeper-server-start.sh config/zookeeper.properties
   ./bin/kafka-server-start.sh config/server.properties
