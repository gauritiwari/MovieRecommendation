
# Movie Recommendation System

- PROBLEM STATEMENT

To design a recommendation engine for a web-streaming app like netflix or spotify. I chose to make a website for movie streaming with a recommendation engine.

- WHAT ARE RECOMMENDATION SYSTEMS? 

A recommendation system is a subclass of Information filtering Systems that seeks to predict the rating or the preference a user might give to an item. In simple words, it is an algorithm that suggests relevant items to users. 

- TYPES OF RECOMMENDATION SYSTEMS: 
 
1)	Content based: 
In Content-Based Recommender, we must build a profile for each item, which will represent the important characteristics of that item. For example, if we make a movie as an item then its actors, director, release year and genre are the most significant features of the movie. 

2)	Collaborative filtering: 
To address some of the limitations of content-based filtering, collaborative filtering uses similarities between users and items simultaneously to provide recommendations

2)	Hybrid recommendation system:: 
A hybrid recommendation system is a special type of recommendation system which can be considered as the combination of the content and collaborative filtering method.

In this project i've made a "Hybrid recommendation system".


## Tech Stack

**Frontend:** HTML , CSS , Javascript 

**Backend:** Flask , Python


## Features

- Recommendation engine based on hybrid filtering i.e. a combination of content-based (which includes genre, actors, overview of a movie into consideration) and collaborative filtering (which calculates the similarity between movies on the basis of ratings given by different users).
- Sign up and login
- Filtering on the basis of genre
- Searching a movie by title
- To know more, hover over the movie's poster
- Play movie trailer by clicking on know more

## Requirements for this project

- Python
- numpy
- flask
- jinja
- pandas
- mysql-connector-python

### For Sign-up and Login functionality
 - Go to your MySQL and run the following command:
  
  
CREATE DATABASE IF NOT EXISTS `Credentials` ;
USE `Credentials`;

CREATE TABLE IF NOT EXISTS `accounts`(
    `email` varchar(100) NOT NULL,
    `password1` varchar(255) NOT NULL,
    `password2` varchar(255) NOT NULL,
    PRIMARY KEY (`email`)
) ;

### For getting similarity.pkl 

- unzip the dataset folder
- Run the commands in jupyter notebook

## To run this project on your local machine
- Complete the Requirements
- Take a copy of this Repository in your local drive
- Run this Command on your Terminal/cmd : `flask run`

## Sources of the dataset

- https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset

- https://www.kaggle.com/rounakbanik/the-movies-dataset
