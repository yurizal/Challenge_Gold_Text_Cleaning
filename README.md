# Challenge Gold - Text Cleaning

Merupakan project untuk level Gold, dimana melakukan Text Cleaning pada file csv yang telah ditentukan yang berisi cuitan tweet menggunakan Flask Framework.

## Description App
- Terdapat upload button dan file data.csv berada di folder uploads
- Melakukan 3 proses sekaligus yakni : Text Cleaning, Tokenized, Stop Word Removal
- Generate Word Cloud pada kata abusive dan tweet
 
## Function Code
proses_data.py
 | Function | Deskripsi |
 | -------- | --------- |
 | ```def __init__``` | Melakukan read csv pada file abuse.csv dan kamusalay.csv   |
 | ```def text_cleaning()``` | Untuk cleaning teks hapus punctuation, hapus teks abuse, update teks alay |
 | ```def find_abusive()``` | Untuk mencari kata abuse dan disimpan ke kolom baru  |
 | ```def delete_abusive()``` | Untuk menghapus teks abuse yang berada disetiap baris |
 | ```def tokenize()``` | Untuk memisahkan teks menjadi potongan-potongan berupa token|
 | ```def removal()``` | Untuk menghilangkan kata-kata yang tidak memiliki makna   |
 | ```def words_cloud()``` | Fungsi untuk inisiasi pada kolom abuse dan removal |
 | ```def img_word_cloud()``` | Generate words cloud dari method words_cloud() menjadi image|
 | ```def table_plot()``` | Untuk menampilkan data table|

## Running Program
- Buat folder dan environment terlebih dahulu
    ```
    mkdir <folder>
    cd <folder>
    copy program ke dalam folder
    python3 -m venv env
    ```
- Aktifkan environment
    ```
    source ./env/bin/activate
    ```
- Install terlebih dahulu package yang diperlukan pada requirement.txt
    ```
    pip install -r requirement.txt
    ```
    > Package yang digunakan 
    
    | Package | README |
    | ------- | ------ |
    | wordcloud | https://github.com/amueller/word_cloud |
    | nltk.tokenized | https://www.nltk.org/api/nltk.tokenize.html |
    | nltk.stopword | https://www.nltk.org/search.html?q=stopwords&check_keywords=yes&area=default |
    | plotly table | https://plotly.com/python/table/ |
    
- Download data nltk yang dibutuhkan. Open terminal python dan ketik :
    ```
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('omw-1.4')
    ```
    Atau
    ```
    import nltk
    nltk.download('all')
    ```

- Jalankan app di terminal 
    ```
    flask run
    ```
## Test Case
- _Upload file data.csv yang berada di folder uploads_

![01_main](https://user-images.githubusercontent.com/16360023/219389897-a469c090-4f9d-4085-a0d5-53cce94d9bfa.png)

- _Data Raw_

![git_02](https://user-images.githubusercontent.com/16360023/219391296-9a4cc384-db7e-4b67-8685-6cfe749c5029.png)

- _Text Cleaning_

![git_03](https://user-images.githubusercontent.com/16360023/219391305-1a84ec2c-9225-4fa2-b6df-880f95cbd73c.png)

- _Tokenized_

![git_04](https://user-images.githubusercontent.com/16360023/219391313-5e0f07e7-7b9c-4541-a961-0323ee534bd1.png)

- _Stop Words Removal_

![git_05](https://user-images.githubusercontent.com/16360023/219391318-026943cb-1d0c-4542-a235-dab82a4964d1.png)

- _Words Cloud_

![03_words_cloud](https://user-images.githubusercontent.com/16360023/219391662-a84c3bae-3635-4a8b-80f1-e3ec53952325.png)


## Perbaikan kedepan
- ```Dynamic Upload File CSV```
- ```Update text cleaning by form input```
