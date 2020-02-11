# Automate Machine Learning Pipeline

End to end project from data collection to putting models into production.


# 1. Minimum Viable Product Structure

C:.

└───deployment

    └───data
    └───templates
        └───index.html
               Front-end web app. Any request that is given to the ML model will be in 
               the form of API (hosted through flask). It allows user to enter house 
               detail and displays the predicted value in the market.            
    └───model.py
                Model building file that is responsible for creating a model, including:
                    - feature engineering
                    - all data preprocessing
                    - model training

Deploy a model that predict sales of houses.

## Environment and tools
1. scikit-learn
2. pandas
3. numpy
4. flask

## Installation

`pip install scikit-learn pandas numpy flask`

`python model.py`

`python app.py`

![Logo](logo.png)


## Citing

```
@misc{Flavia:2020,
  Author = {Flavia Santos},
  Title = {Automation-Machine-Learning-Pipeline},
  Year = {2020},
  Publisher = {GitHub},
  Journal = {GitHub repository},
  Howpublished = {\url{https://github.com/flaviassantos/machinelearning}}
}
```

"# machinelearning" 
