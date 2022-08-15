from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_p = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    for person in model:
        if person.id_person == id_p:
            return render_template('id_found.html')

    p = Person(id_person=id_p, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/person_delete/<id>', methods=['POST'])
def delete(id):
    for person in model:
        if person.id_person == id:
            model.remove(person)
            break
    return render_template('person_deleted.html')

@app.route('/person_update/<id>', methods=['GET'])
def person_update_form(id):
    for person in model:
        if person.id_person == id:
            data = [(person.id_person, person.name, person.last_name)]
    print(data)
    return render_template('person_update_form.html', value = data)


@app.route('/person_updated/<id>', methods=['POST'])
def person_update(id):
    for person in model:
        if person.id_person == id:
            person.name = request.form['first_name']
            person.last_name = request.form['last_name']
            data = [(person.id_person, person.name, person.last_name)]
            break
    return render_template('person_update.html', value=data)


if __name__ == '__main__':
    app.run(Debug = True)