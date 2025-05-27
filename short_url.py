from flask import Flask, render_template, request, redirect, abort
from database.database import create_db, check_url, insert_url, update_hits, get_all_urls
import random
import string

app = Flask(__name__)

def generate_short_code(lenght=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=lenght))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url =None
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        short_code= generate_short_code()
        while check_url(short_code) is not None:
            short_code = generate_short_code()
        if insert_url(long_url, short_code):
            short_url = request.host_url + short_code
        else:
            short_url = "Erro ao gerar short URL"
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirectx(short_url):
    long_url = check_url(short_url)
    if long_url:
        update_hits(short_url)
        return redirect(long_url)
    return render_template('error.html'), 404

@app.route('/database')
def visualizar_database():
    registros = get_all_urls()
    return render_template('dataview.html', registros=registros)

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
