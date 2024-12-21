import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Veriyi yükle
data = pd.read_csv('Processed_Automobile.csv')

# Özellikler (X) ve hedef değişken (y)
X = data.drop('cylinders', axis=1)  # target_column burada hedef değişken olmalı
y = data['cylinders']  # hedef değişken

# Veriyi eğitim ve test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelleri tanımla
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
dt_model = DecisionTreeRegressor(random_state=42)
lr_model = LinearRegression()

# Modelleri eğit
rf_model.fit(X_train, y_train)
dt_model.fit(X_train, y_train)
lr_model.fit(X_train, y_train)

# Tahminler
rf_pred = rf_model.predict(X_test)
dt_pred = dt_model.predict(X_test)
lr_pred = lr_model.predict(X_test)

# Başarı metriklerini hesapla
def print_metrics(model_name, y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} - MSE: {mse:.4f}")
    print(f"{model_name} - R^2 Score: {r2:.4f}")

# Sonuçları yazdır
print_metrics('Random Forest', y_test, rf_pred)
print_metrics('Decision Tree', y_test, dt_pred)
print_metrics('Linear Regression', y_test, lr_pred)
