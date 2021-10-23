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
* Change directory accordingly so that the dataeset can be accessed:
```
json_path = '../Dataset/reviewSelected100.json' 
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
* Output of the two methods of POS Tagging will be shown in ternimal. 

### 3.3 Extraction of Adjective Phrases (AP)
* Change directory accordingly so that the dataeset can be accessed:
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
