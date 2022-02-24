# Sqlite Chinook Example Database Case Study

docker-compose.yml dosyası içerisinde gerekli olan servisler ve özellikleri belirtilmiştir.

HTTP istekleri CaseStudy.postman_collection.json dosyası ile Postman uygulamasından import edilebilir.

### Servisler

- db(SQLite)
- web(Flask)

### Volumes

- sqlitedb: Veritabanı verilerini saklar.

### Teknolojiler

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Sqlite](https://www.sqlite.org/index.html)
- [SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

### Docker Kurulum

Docker üzerinde uygulamayı çalıştırmamız için sırasıyla aşağıdaki kodlar çalıştırılmalıdır:

1- ``` docker compose build ```

2- ``` docker compose up ```

Kodlar çalıştırıldıktan sonra chinook.db örnek veritabanı dosyasını oluşturduğumuz volume path'ine yazdırmalıyız.
chinook.db dosyası volume path'ine yazdırılmadığı takdirde uygulama hata verir. Bunun için yeni bir terminal açıp aşağıdaki kodlar sırasıyla çalıştırılmalıdır:

1- ``` docker exec -it flask /bin/bash ```

2- ``` bash script.sh ```


 

 



 









