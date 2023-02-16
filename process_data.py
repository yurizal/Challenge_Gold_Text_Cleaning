import io
import pandas as pd
import nltk
import re
import string
import numpy as np
from nltk.corpus import stopwords
from wordcloud import WordCloud
import base64
import plotly.graph_objs as go

class text_preprocessing:
    data_hasil = ""
    correction_dict = ""
    text=""

    def __init__(self):
        #ambil data di folder uploads
        file_abusive=  'uploads/abusive.csv'
        file_kamus_alay= 'uploads/new_kamusalay.csv'
        
        #read_csv
        self.df_abusive = pd.read_csv(file_abusive, encoding="latin-1")
        self.words_to_search = self.df_abusive['ABUSIVE'].tolist()
        
        #buat header untuk kamus alay
        header_list=["wrong_type","fix_type"]
        self.df_kamusalay = pd.read_csv(file_kamus_alay, encoding="latin-1",names=header_list)
        text_preprocessing.correction_dict = dict(zip(self.df_kamusalay['wrong_type'], self.df_kamusalay['fix_type']))
    
    #untuk menggantikan kata lama menjadi kata baru
    def replacement(self,data):
        pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in text_preprocessing.correction_dict.keys()) + r')\b')
        data = data.str.lower()
        data_fix = data.str.replace(pattern, lambda m: text_preprocessing.correction_dict.get(m.group(0), m.group(0)))
        return data_fix
      
    #untuk mencari kata2 abuse dan disimpan ke kolom baru
    def find_abusive(self,data):
        hasil = [word for word in self.words_to_search if str(data['Tweet']).lower().find(word.lower()) != -1]
        i= [1,', '.join(hasil)] if hasil else [0,'']
        return pd.Series(i)
    #untuk menghapus kata abuse disetiap baris
    def delete_abusive(self,data):
        text_preprocessing.data_hasil['Tweet'] = data.apply(lambda x: ' '.join([item for item in x.split() if item not in self.words_to_search]))
    
    #untuk melakukan cleaning(replacment, abuse) dan menghilangkan punctuation
    def text_cleaning(self, data):
        if isinstance(data, pd.Series):
            #replacement
            data_fix =self.replacement(data)
            #cleaning punctuation      
            text_preprocessing.data_hasil = data_fix.str.replace('[^\w\s]','',regex=True)
            text_preprocessing.data_hasil = text_preprocessing.data_hasil.str.strip()
            text_preprocessing.data_hasil = text_preprocessing.data_hasil.to_frame()
            ##find_abusive
            text_preprocessing.data_hasil[['value_abuse','words_abuse']] = text_preprocessing.data_hasil.apply(self.find_abusive, axis=1)
            text_preprocessing.data_hasil['Tweet'] = text_preprocessing.data_hasil['Tweet'].apply(lambda x: ' '.join([item for item in x.split() if item not in self.words_to_search]))
            # self.delete_abusive(text_preprocessing.data_hasil['Tweet'])
        else:
            text_preprocessing.text = re.sub(r'[^\w\s]', '', data)
        
    #untuk melakukan tokenize atau menjadikan kalimat menjadi kata2 terpisah
    def tokenize(self,data,columns):
        data['Tokenized'] = data[columns].apply(lambda x: nltk.word_tokenize(x))
        
        
    #untuk melakuakn stop removal yakni membuang imbuhan atau akhiran dari kata 
    def removal(self,data):
        stop_words = set(stopwords.words("indonesian"))
        text_preprocessing.data_hasil['removal'] = data['Tokenized'].apply(lambda x: [word for word in x if word.lower() not in stop_words and word.isalpha() and word not in string.punctuation])
        
    #membuat words cloud    
    def words_cloud(self):
        text1 = " ".join(i for i in text_preprocessing.data_hasil['words_abuse'])
        html1 = self.img_word_cloud(text1)
        
        rm =(text_preprocessing.data_hasil['removal'].transform(lambda x: ",".join(map(str,x))))
        text2 = " ".join(i for i in rm)
        html2 = self.img_word_cloud(text2)       
        
        return html1,html2
    
    #untuk generate words cloud menjadi img
    def img_word_cloud(self,text):
        # x, y = np.ogrid[:300, :400]

        # mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
        # mask = 255 * mask.astype(int)

        wc = WordCloud(background_color="white", repeat=True, width=600, height=280)
        wc.generate(text)
        
        image = wc.to_image()
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')

        image_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
        html = f'<img src="data:image/png;base64,{image_string}" alt="Wordcloud Image">'
        return html
    
    #membuat table plot
    def table_plot(self,data):
        fig = go.Figure(data=[go.Table(header=dict(values=list(data.columns),fill_color='paleturquoise',align='left'),
        cells=dict(values=[data[col] for col in data.columns],fill_color='lavender',align='left',font=dict(color='black', size=12),height=30,))])
        return fig
