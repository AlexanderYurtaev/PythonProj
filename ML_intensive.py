import pandas
from sklearn.ensemble import RandomForestClassifier

pandas.read_excel("trips_data.xlsx")
trips_data = pandas.read_excel("trips_data.xlsx")
# print(trips_data.shape)
# print(trips_data.tail(3))
trips_data.salary.hist(bins=100)# Гистограмма зарплат
# trips_data.age.hist()
# print(trips_data.city.value_counts())
# print(trips_data.vacation_preference.value_counts())
# trips_data.vacation_preference.value_counts().plot(kind='bar')
# print(trips_data.query("salary > 23000 & age > 65")) # найти все строчки с зп выше указанной и возрастом
# print(trips_data.query("family_members ==4"))

df = pandas.get_dummies(trips_data, columns=["city", "transport_preference", "vacation_preference"])
# Задача модели: найти закономерности между Х и у
y = df.target  # куда человек поедет в отпуск? то что мы пытаемся предсказать
x = df.drop("target", axis=1)  # выбираем все кроме колонки(axis=1) target

# Регрессия - когда модель предсказывает число
# Классификация - когда модель выдает один из заранее известных ответов
print(y.value_counts())

model = RandomForestClassifier()  # Настройки
model.fit(x, y)  # обучаем модель, ищем закономерностти между x и y

# куда поедем?
print(x.columns)
{col:[0] for col in x.columns}
sample = {'salary': [180000],
 'age': [59],
 'family_members': [1],
 'city_Екатеринбург': [0],
 'city_Киев': [0],
 'city_Краснодар': [0],
 'city_Минск': [0],
 'city_Москва': [0],
 'city_Новосибирск': [0],
 'city_Омск': [0],
 'city_Петербург': [0],
 'city_Томск': [1],
 'city_Хабаровск': [0],
 'city_Ярославль': [0],
 'transport_preference_Автомобиль': [1],
 'transport_preference_Космический корабль': [0],
 'transport_preference_Морской транспорт': [0],
 'transport_preference_Поезд': [0],
 'transport_preference_Самолет': [0],
 'vacation_preference_Архитектура': [0],
 'vacation_preference_Ночные клубы': [0],
 'vacation_preference_Пляжный отдых': [1],
 'vacation_preference_Шоппинг': [0]}

sample_df = pandas.DataFrame(sample, columns=x.columns)
sample_df.head()
print(model.predict(sample_df)) #делаем предсказание

