from flask import Flask, request, render_template
import tensorflow as tf

app = Flask(__name__)# создаём` новый экземпляр приложения Flask

@app.route('/') # указываем путь до домашней страницы веб-приложения
def choose_prediction_method(): # функция возвращающая main.html
    return render_template('main.html')


def nn_prediction(params): # функция которая принимает список параметров и возвращает прогноз на основе предварительно обученной модели
    model = tf.keras.models.load_model('models/Net_app')
    pred = model.predict([params])
    return pred


@app.route('/nn/', methods=['POST', 'GET']) # создает новый путь для URL-адреса "/nn/", для обработки запросов POST и GET.
def nn_predict():
    message = ''
    if request.method == 'POST':
        param_list = ('parameter1', 'parameter2', 'parameter3', 'parameter4', 'parameter5', 'parameter6',  
                      'parameter7', 'parameter8', 'parameter9', 'parameter10', 'parameter11', 'parameter12')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        message = f'Спрогнозированное Соотношение матрица-наполнитель для введенных параметров: {nn_prediction(params)}'
    return render_template('nn.html', message=message) # Эта строка отображает "nn.html" и передает строку сообщения в качестве параметра.

if __name__ == '__main__': # проверяет, выполняется ли текущий сценарий в качестве основной программы
    app.run() # запускает приложение Flask
