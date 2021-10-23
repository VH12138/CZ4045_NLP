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

### Dependencies

* [To be edited]

### Installing

* [To be edited]

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

Do not remove any file from the result folder for the following steps, since the file will be used for further analysis.

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

Contributors names and contact info
[To be edited]

## Version History

* 0.1
    * Initial Release

## Acknowledgments

* [Insert references]
