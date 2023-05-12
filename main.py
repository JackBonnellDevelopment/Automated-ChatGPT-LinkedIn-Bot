import selenium
import openai
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from dotenv import dotenv_values

config = dotenv_values(".env")

class ChatGPTLinkedInDriver:

    def __init__(self, Headless: bool = True) -> None:
        chrome_options: Options = Options()
        if(Headless): chrome_options.add_argument("--headless")
        self.driver: webdriver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.linkedin.com/")
        self.username = self.driver.find_element(By.ID, "session_key")
        self.password = self.driver.find_element(By.ID, "session_password")
        
        openai.api_key = config["OPENAIKEY"]
    def GeneratePost(self) -> str:

        model_engine = "text-davinci-003"
        prompt = "Write a inciteful bullet points Linkedin post that uses the following key words and make sure its shorter than 1000 characters: " + self.config["POSTTAGS"]
        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return response
    def run(self):
        self.username.send_keys(config["USERNAME"])
        self.username.send_keys(Keys.RETURN)
        self.password.send_keys(config["PASSWORD"])
        self.username.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "ember24")))
        postelement = self.driver.find_element(By.ID, "ember24")
        postelement.click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ql-editor")))
        textelement = self.driver.find_element(By.CLASS_NAME, "ql-editor")
        textelement.send_keys(self.GeneratePost())
        textelement.send_keys(Keys.RETURN)
        buttonelement = self.driver.find_element(By.CLASS_NAME, "share-actions__primary-action")
        buttonelement.click()

if __name__ == "__main__":
    while(True):
        ChatGPTLinkedInDriver(False).run()
        time.sleep(config["FREQUENCY"]*3600)