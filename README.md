# CZ4045 Natural Language Processing
## Assignment 1: Review Data Analysis and Processing

Nanyang technological University
School of Computer Science and Engineering
Academic Year 2021/2022 Semester 1

This file contains the source codes for CZ4045 Assignment 1.

This README file is best viewed using a text editor that supports Markdown.

---

## Description

In this assignment, we approached the Yelp review dataset through basic textual processing and analysis techniques, including tokenisation, stemming, POS tagging and etc. We also conducted analysis on concepts such as noun-adjective pair and adjective phrases with sampled data.

## Getting Started
This project runs with the Python 3.8.x interpreter. Add the path of your local python.exe installation to your system PATH variable. Please ensure you have the correct Python version and all dependent libraries (listed above) installed. Please note that do not remove any of the generated files from result folders since they will be used for further analysis.

### Dependencies

* nltk: http://www.nltk.org/
* pandas: http://pandas.pydata.org
* matploylib: https://matplotlib.org/
* SpaCy: https://spacy.io/ 

### Installing

For installation of required libraries use command from terminal:
```
pip install <package_name>
``` 

## Program Execution and Desired Outcome

### 3.2 Dataset Analysis
* Make a new directory name 'Dataset' under the root directory. 
Put the file 'reviewSelected100.json' under this 'Dataset' directory.
```
sudo mkdir Dataset
``` 
* Switch to directory Task3.2 to run the following 3 python files.
```
cd Task3.2
```
* Tokenization and Stemming: Run the following command under folder Task3.2
```
python tokenization_stemming.py
```
* A result folder will be generated. Four files will be stored inside the result folder:
    * b1review.txt: Extracted all reviews for random selected business b1
    * b2review.txt: Extracted all reviews for random selected business b2
    * b1_word_frequency.png: Word frequency for b1
    * b2_word_frequency.png: Word frequency for b2
  
* POS Tagging: Run the following command under folder Task3.2
```
python POS_tag.py
```
* Output of the two methods of POS Tagging will be shown in terminal. <br/>


* Most Frequent Noun-Adj-Pairs
```
python Noun_Adj_Pair.py
```
* Output of this file is saved in result folder as a .csv, with name 'noun_adj_starN.csv'. N refers to the star you want to analysis.
You can change the star value with 1,2,3,4,5 in the 10th line of file Noun_Adj_Pair.py.

### 3.3 Extraction of Adjective Phrases (AP)
* Change directory accordingly so that the dataset can be accessed:
```
json_path = '../Dataset/reviewSelected100.json' 
``` 
* Download and install the nltk and spaCy packages, as done in previous section
* Execute the Python script
    * The outcome, i.e. list of indicative APs (raw), is printed out
* Refer to the report for detailed analysis on the indicative APs, as well as the criteria of filtering them

### 3.4 Application
* Application: Run the following command under folder Task3.4
```
python application.py
```
* A result folder will be generated. The detected negation words will be stored in result folder in png form named negation_dis. 

## Authors
Han Jun - HANJ0030@e.ntu.edu.sg  
Joey Hiew Mun Yee - JOEY0028@e.ntu.edu.sg  
Tao Weijing - D180002@e.ntu.edu.sg  
Wang Yifan - D180003@e.ntu.edu.sg  
Yang Yubei - C180052@e.ntu.edu.sg
