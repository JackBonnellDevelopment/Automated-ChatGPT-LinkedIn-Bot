# Automated-ChatGPT-LinkedIn-Bot

An automated LinkedIn Bot that uses ChatGPT to Post Content related Chosen Content.
<p align="center">
<img src="https://1000logos.net/wp-content/uploads/2023/01/LinkedIn-logo.png" height= 30% width = 30%/>&nbsp&nbsp&nbsp&nbsp<img src="https://www.outdoored.com/wp-content/uploads/OpenAI-ChatGPT-40.png" height= 30% width = 35%/>
</p>

****
 ## Background

 This bot uses Selenium and ChatGPT to automate the proccess of creating and posting LinkedIn Content. This repository is loosely based of a tutorial on automating linkedIn posts by [ijachipius8](https://ijachipius8.medium.com/automate-linkedin-posts-with-selenium-and-python-f209e276d3c2).



 The code is very basic and uses python. More complete documentation and code will be added as more features are implemented and the ChatGPTLinkedInDriver is moved out of Main.py

****
## Table of Contents

- [Prerequisites](https://github.com/JackBonnellDevelopment/Automated-ChatGPT-LinkedIn-Bot#Prerequisites)
- [Set Up](https://github.com/JackBonnellDevelopment/Automated-ChatGPT-LinkedIn-Bot#set-up)
- [Usage](https://github.com/JackBonnellDevelopment/Automated-ChatGPT-LinkedIn-Bot#usage)
- [Contribute](https://github.com/JackBonnellDevelopment/Automated-ChatGPT-LinkedIn-Bot#contribute)
- [License](https://github.com/JackBonnellDevelopment/Automated-ChatGPT-LinkedIn-Bot#license)
****

## Prerequisites

- Python3
- OpenAI
- Selenium
- Chrome

****

## Set Up

1. Create an .env file in the root of the repository as shown:

```
# LinkedIn User Credentials
USERNAME=jack.bonnell@hotmail.co.uk
PASSWORD=Hillsidenn69ph!
# OPEN AI API KEY
OPENAIKEY=1234
# Frequency of posts (Hours)
FREQUENCY=24
# Tags for generating posts
POSTTAGS = tech AI ML


```
2. Install dependencies

```
pip install -r requirements.txt
```

****

## Usage

-  Run the script

    ```
    Python main.py
    ```

- Example Output
<p align="center">
<img src="https://github.com/JackBonnellDevelopment/Automated-ChatGPT-LinkedIn-Bot/assets/22745183/58764efd-65ba-4cec-83ea-13dd47d154df" height= 50% width = 50%/>
</p>

****

## Contribute

PRs are welcome! If you're looking for something to do, maybe take a look at the Issues?

If updating the README, please stick to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.
****
## License

MIT
