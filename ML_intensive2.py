
# https://live.skillbox.ru/webinars/code/pogruzhaemsya-v-mashinnoe-obuchenie300822/?utm_source=expertsender&utm_medium=email&utm_campaign=all_all_expertsender_email_anons_intensive-275-2022-08_all_code_skillbox&utm_content=2022-08-30&utm_term=intensive
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

bitcoin = pd.read_csv("BTCUSD_daily.csv", index_col=0)  # index_col=0 указывает не использовать колонку по индексу
# bitcoin = pd.read_csv("BTCUSD_daily.csv", index_col=0, parse_dates="date") parse_dates другой вариант преобразование даты
print(bitcoin)
bitcoin.date = pd.to_datetime(bitcoin.date)  # преобразуем строку в структуру "DateTime"
print(bitcoin)

plt.plot(bitcoin.date, bitcoin.open, label='open')
x = plt.plot(bitcoin.date, bitcoin["Volume USD"], label="open")

# Rolling Window = Скользящее окно
dfs = bitcoin.open.rolling(window=60).mean().plot  # среднее значение за 60 дней

bitcoin.head()
# X = "добавить колонки на основе недавних значений", y = "цена закрытия завтрашнего дня (какой завтра будет close)", задача = регрессия

# Feature Engineering = придумывание новых колонок, цель = помочь модели, предоставив как можно больше данных
bitcoin["open_mean_7d"] = bitcoin.open.shift(1).rolling(window=7).mean()  #  Средняя цена открытия за последние 7 дней
bitcoin["volume_btc_max_30d"] = bitcoin["Volume BTC"].rolling(window=30).max()  #  Макс. объем торгов за 30 дней
# Важный момент: не включать текущий день = shift(1)

# Создадим 7 колонок с недавними значениями close
for day in range(1, 8):
    print(f"Добавляем колонку close за {day} д. назад")
    bitcoin[f"close_{day}d"] = bitcoin["close"].shift(day)

# Удаление колонок
bitcoin.drop("symbol", axis=1, inplace=True)
bitcoin.drop("date", axis=1, inplace=True)

# Избавляемся от NaN
bitcoin.fillna(method="backfill", inplace=True) # Залить пустые значения

bitcoin["target"] = bitcoin["close"].shift(-1) # target = close следующего дня
# Но мы создали еще один Nan c конца

# [:-1] "все кроме последнего элемента"
x = bitcoin[:-1].drop("target", axis=1)
y = bitcoin[:-1].target

# Разбиваем на трен. и тест. выборку
# train - обучающая - учебник - X_train, y_train

# test - проверочная - экзамен - Даем модели X_test,
# и просим сделать предсказани y_pred, и сравниваем с y_test
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

from sklearn.model_selection import train_test_split
from sklearn.metrics import max_error, mean_absolute_error, r2_score
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)  # Разделяем, отдаем 33% на тест.

#model = RandomForestRegressor()
def try_model(model):
    model.fit(X_train, y_train)  # Обучаем модель на ТРЕНИРОВОЧНОЙ выборке
    y_pred = model.predict(X_test)  # Проверяем модель на ТЕСТОВОЙ выборке
    print("max_error = ", max_error(y_pred, y_test))
    print("mean_absolute_error = ", mean_absolute_error(y_pred, y_test))
    print("r2_score = ", r2_score(y_pred, y_test))

rfr = RandomForestRegressor()
try_model(rfr)

# Пробовать разные модели
# Пробовать разные настройки (?)
# Оценить модель разными метриками качества
# Пробуем разные данные (Feature Engineering)

rfr.feature_importances_  # Важность колонок