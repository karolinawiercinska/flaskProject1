from flask import Flask, render_template, request
from calculator import Calculator
import pandas as pd

app = Flask(__name__)

# Konfiguracja ścieżki do pliku CSV
csv_path = 'files/tabela.csv'


# Funkcja ucinająca białe znaki
def strip(text):
    try:
        return text.strip()
    except AttributeError:
        return text


# Funckaja zmieniająca stringa na inta
def make_int(text):
    return int(text.strip('" '))


# Wczytanie pliku CSV za pomocą pandas z transformacją danych
df = pd.read_csv(csv_path, converters={
    'Kraj': strip,
    'Waluta': strip,
    'Dieta': make_int,
    'Nocleg': make_int
})

country_list = df['Kraj'].values


# Endpoint do wyświetlania tabeli
@app.route('/')
def display_table():
    # Przekazanie danych do szablonu HTML
    return render_template('table.html', table=df.to_html())


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', countries=country_list)


@app.route('/submit', methods=['POST'])
def submit():
    calculator = Calculator(request.form, df)
    return render_template('result.html', calculator=calculator)


if __name__ == '__main__':
    app.run(debug=True)

