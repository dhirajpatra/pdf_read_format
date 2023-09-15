## This application will read any pdf after that format with chatgpt openai

You can use this application as a template to create PDF processing. You can read any PDF and then proper meaningful format by OpenAI API [you need to register for this](https://openai.com/blog/openai-api).

There three main scripts. main.py, pypdf_reader.py and openai_to_process_txt.py
It will generate output.txt file as final result. 
However for your idea I have kept a *part* of formatted_output.txt file to see how will it look like the final output and kept output.txt as after reading but before calling openai API output.

### Pre-Requirements

Hope you have already installed python 3.9 and pip. If not get more info how to isntall python and pip (https://www.python.org/downloads/) and (https://pip.pypa.io/en/stable/installation/)
You may also need some more software as per your system.

### How to install

You just need to fork and clone the repo. Run `pip install -r requirements.txt`

### How to run

You can run from command prompt `python main.py example.pdf` just replace the example.pdf with your pdf file name and path.

### Improvement

A lot can possible. This is a template application I have created within 30 min. Even no pytest also there. You need to put optimized processing and saving options as per your need.
