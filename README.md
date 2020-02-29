# Welcome to Dashboard!

A end to end project from data collection to putting a machine learning model into production.

The application is available at [flavia-dashboard-ml.herokuapp.com]( https://flavia-dashboard-ml.herokuapp.com/ ).

## How to install

If you have docker installed, you can test the code locally with:


```
$ docker pull flaviassantos/dashboard:latest

$ docker build -t dashboard:latest .

$ docker run --name dashboard -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<email@gmail> -e MAIL_PASSWORD=<email-password> \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://dashboard:<database-password>@dbserver/dashboard 
    --link elasticsearch:elasticsearch 
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 dashboard:latest

```

The application is then available on http://127.0.0.1:5000/ in your web browser.

The documentation is available on [Docker hub](https://hub.docker.com/repository/docker/flaviassantos/dashboard).

### Environment and tools

1. python 3.7
2. pandas
3. numpy
4. flask
5. docker
6. scikit-learn


```
@misc{Flavia: 2020,
  Author = {Flavia Santos},
  Title = {Dashboard},
  Year = {2020},
  Publisher = {GitHub},
  Journal = {GitHub repository},
  Howpublished = {\url{https://https://github.com/flaviassantos/dashboard}}
}
```

