from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

with open("users.json") as f:
    all_users = json.load(f)


@app.route('/')
def users():
    """Создание представления с роутом "/", вывод карточек пользователей"""
    return render_template('index.html', all_users=all_users)


@app.route('/search/')
def users_search():
    """Поиск карточек по имени"""
    searched_users = []  # создание списка карточек, найденных по введенному в форму имени
    if request.args.get('letter'):

        letter = request.args.get('letter')

        for user in all_users:  # цикл по карточкам пользователей
            # проверка совпадения введенного имени со значением по ключу name
            if letter.lower() in user['name'].lower():
                searched_users.append(user)  # запись карточки в список

    return render_template("search.html", all_users=searched_users, count_users=len(searched_users))


@app.route('/add_user/', methods=["GET", "POST"])
def add_user():
    """По нажатию на кнопку «Добавить» добавляется в список новый пользователь"""

    if request.method == 'GET':
        return render_template('add_user.html', all_users=all_users)
    elif request.method == 'POST':
        data_users = request.values
        all_users.append(data_users)  # добавление данных нового пользователя в существующий список

    with open("users.json", 'w') as f:  # запись списка с добавленным пользователем в файл
        f.write(json.dumps(all_users))

    return redirect('/')


app.run()
