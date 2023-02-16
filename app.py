from flask import Flask, render_template, request
import os
import pandas as pd
from process_data import text_preprocessing


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    df = pd.read_csv(file_path)

    #instance object
    p = text_preprocessing()
    p.text_cleaning(df['Tweet'])
    clean = p.data_hasil[['Tweet','value_abuse','words_abuse']]
    
    p.tokenize(p.data_hasil,'Tweet')
    tokens = p.data_hasil[['Tokenized']]
    
    p.removal(p.data_hasil)
    removal = p.data_hasil[['removal']]
    
    # Buat tabel Plotly
    fig = p.table_plot(df)
    fig1 = p.table_plot(clean)
    fig2 = p.table_plot(tokens)
    fig3 = p.table_plot(removal)
    
    # Konversi tabel Plotly ke HTML dan kirim ke halaman HTML
    table_html = fig.to_html(full_html=False)
    clean = fig1.to_html(full_html=False)
    tokens = fig2.to_html(full_html=False)
    removal = fig3.to_html(full_html=False)

    wcl1,wcl2 = p.words_cloud()
    return render_template('upload.html', table_html=table_html, clean=clean, tokens=tokens,removal=removal,wcl1=wcl1,wcl2=wcl2)

@app.route('/result', methods=['POST'])
def text_file():
    t = text_preprocessing()
    text = request.form['text']
    t.text_cleaning(text)
    return render_template('result.html',clean=t.text)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', active_page='index')

@app.route('/text')
def text():
    return render_template('text.html', active_page='text')

if __name__ == "__main__":
    app.run(debug=True)
