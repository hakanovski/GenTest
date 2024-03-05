# GenTest
An innovative application utilizing Meta's LLaMA for automating test case generation from user stories and product documentation, enhancing QA efficiency.

# Test Case Generator

## Overview

This project aims to create a Test Case Generator application that analyzes user stories, product decks, and other documentation uploaded by the users in various formats such as PowerPoint, PDF, or Word. The application will leverage the Meta's LLaMA Large Language Model to generate a set of test cases based on the analyzed information, contributing to a more automated and efficient quality assurance process.

## Technologies

- **Python**: Main programming language for application development.
- **LLaMA (Large Language Model Meta AI)**: Generative AI model for processing natural language and generating test cases.
- **python-pptx, python-docx, PyPDF2/pdfplumber**: Libraries for reading PowerPoint, Word, and PDF documents, respectively.
- **Tkinter/PyQt/Kivy**: GUI frameworks for creating the user interface in Windows environment.
- **Visual Studio Code**: Recommended IDE for application development.

## Features

- Upload and parsing of user story documentation.
- Analysis of documents to extract key information using NLP techniques.
- Integration with LLaMA to generate relevant test cases.
- Output generated test cases in Word, PDF, or Excel format.

## Setup and Installation

1. Clone the repository to your local machine.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Register and download the LLaMA model from Meta's official website.
4. Follow the installation instructions provided in the LLaMA repository to set up the model for inference.

## Usage

To run the application:

1. Navigate to the cloned repository directory.
2. Run the main script using `python main.py`.
3. Follow the GUI prompts to upload documents and generate test cases.

## Contribution

Contributions to the project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is released under [SOFTWEARENGINEERS], which allows for [TBD].

---
