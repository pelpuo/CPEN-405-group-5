# CPEN 405 Group Project
This repository contains the project files of Group 5, for the CPEN 405 capstone project, 2022.

## Group Members
* Emmanuel Amoah Kwame - 10464434
* Amanfo Oforiwaa Abena - 10714326
* Dumenu Ernest Mawuse - 10726400
* Kayang Edwin Pelpuo - 10728521 
* El-Karece Amoakoa Asiedu - 10735358


## This project comes in 3 parts, namely:
* Machine Learning
* Optimization with MATLAB
* Predicting Stock Prices

## Machine Learning
PART 1 is mainly about machine learning using WEKA. The project's goal is to gain practical experience with machine learning methods by using software such as WEKA to solve real-world data mining problems, as well as to gain a better understanding of some of the algorithmic issues that arise when designing and applying various machine learning algorithms. For our experiments, we used 10-fold cross validation with 5 classification schemes for Soybean Disease Diagnosis. After which, we used the WEKA  Experiment Paired Corrected T-Tester to compare the classification schemes for their performance. 

The dataset used was Soybean, with its training and test database combined into a single file, from the UCI Machine Learning Repository, and 5 classification schemes were applied to it for evaluation. These data sets were selected because they are large enough to allow moderate size train and validation sets, and still have data left for large final test sets. It proved to be the best fit for the constraints provided in the instructions given.

### Steps To Run
* Install WEKA on your computer if not already installed
* Navigate to part_1
* Open any of the .arff files

## Optimization with MATLAB
The drive to achieve better or be the best in one field or another is the concept of optimization. Numerical optimization can be used in engineering to attain this goal of optimization. MATLAB is a strong piece of software that lets you handle optimization issues with a variety of tools. Our goal in this section is to tackle an optimization problem involving pricing under pressure using functions from the MATLAB optimization toolbox as well as genetic and simulated annealing procedures

### Steps To Run
* Install MATLAB on your computer if not already installed
* Navigate to part_2
* Open objfunc.m in matlab

## Predicting Stock Prices
Artificial intelligence is the brains behind a lot of technological innovations such as natural language processing, speech recognition, computer vision, machine translation as well as pose detection. 

Recently, python has become one of the primary languages, equipped by programmers as they venture into the world of developing intelligent machines. This is due to its readability as well as its numerous libraries, which allow the programmer to focus more on the logic on the artificial intelligence algorithm, rather than the correct procedures and syntaxes for implementing lower level functions.

The task which was accomplished in this project, involved developing a machine learning algorithm which was efficient at predicting stock prices. This was done using the python programming language, and a graphical interface was to be developed to serve as a medium for user input as well as visualisation of results.

### Steps To Run
* Install python on your computer if not already installed
* Navigate to part_3
* In the terminal, run the command `python -m venv env`
* Next, run `.\env\Scripts\activate`
* Run `pip install -r requirements.txt` to install libraries
* Finally, run `py app.py`