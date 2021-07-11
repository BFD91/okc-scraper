"""
A bot to scrape profiles (and swipe left or right depending on certain parameters) from online dating site OKCupid.
Was functional in July 2020, but probably requires modification to work today. Helped the creator find his wife; hope it
may serve others too!
"""


from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import xlrd
import xlwt
from xlutils.copy import copy
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import os
import cv2
import urllib.request
import numpy as np
#import xlwt 
#from xlwt import Workbook


class OKC():
  
    def __init__(self,username,password):
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.username = username
        self.password = password

        # Deprecated. Used to cycle between locations before OKC changed their system. Left in case of renewed relevance.
        self.locations = [('United States', '94112'), ('United States', '90011'), ('United States', '98115'),
                          ('United States', '60629'), ('United States', '77036'), ('United States', '85032'),
                          ('United States', '19120'), ('United States', '92154'), ('United States', '32210'),
                          ('United States', '80219'), ('United States', '64114'), ('United States', '37211'),
                          ('United States', '20011'), ('United States', '27312'), ('United States', '02124'),
                          ('United States', '11368'), ('United Kingdom', 'London'), ('Canada', 'Toronto'),
                          ('Canada', 'Montreal'), ('Algeria', 'Alger'), ('Australia', 'Melbourne'),
                          ('Australia', 'Brisbane'), ('Australia', 'Perth'), ('Singapore', 'Singapore'),
                          ('Ireland', 'Dublin'), ('New Zealand', 'Wellington'), ('Philippines', 'Manila'),
                          ('Sweden', 'Uppsala'), ('Sweden', 'Göteborg'), ('Finland', 'Helsinki'), ('Algeria', 'Alger'),
                          ('Angola', 'Luanda'), ('Argentina', 'Buenos Aires'), ('Austria', 'Vienna'),
                          ('Azerbaijan', 'Baku'), ('Bangladesh', 'Dhaka'), ('Belarus', 'Minsk'),
                          ('Belgium', 'Brussels'), ('Bolivia', 'Santa Cruz'), ('Brazil', 'Rio de Janeiro'),
                          ('Chile', 'Santiago'), ('China', 'Beijing'), ('China', 'Shanghai'), ('China', 'Shenzhen'),
                          ('China', 'Tianjin'), ('China', 'Wuhan'), ('China', 'Chengdu'), ('China', 'Nanjing'),
                          ('China', 'Shenyang'), ('China', 'Hangzhou'), ('Colombia', 'Bogota'),
                          ('Czech Republic', 'Prague'), ('Democratic Republic of the Congo', 'Kinshasa'),
                          ('Denmark', 'Copenhagen'), ('Ecuador', 'Guayaquil'), ('Egypt', 'Cairo'),
                          ('Estonia', 'Tallinn'), ('Ethiopia', 'Addis Abeba'), ('France', 'Paris'),
                          ('Germany', 'Berlin'), ('Greece', 'Athens'), ('Hong Kong', 'Hong Kong'),
                          ('Hungary', 'Budapest'), ('Iceland', 'Reykjavik'), ('India', 'Mumbai'),
                          ('India', 'New Delhi'), ('India', 'Bangalore'), ('India', 'Hyderabad'),
                          ('India', 'Ahmedabad'), ('India', 'Chennai'), ('India', 'Kolkata'), ('Indonesia', 'Jakarta'),
                          ('Iraq', 'Bagdad'), ('Israel', 'Tel Aviv'), ('Italy', 'Rome'), ('Japan', 'Tokyo'),
                          ('Japan', 'Osaka'), ('Kenya', 'Nairobi'), ('Laos', 'Vientiane'), ('Malaysia', 'Kuala Lumpur'),
                          ('Mexico', 'Mexico City'), ('Mongolia', 'Ulaanbaatar'), ('Nepal', 'Katmandu'),
                          ('Netherlands', 'Amsterdam'), ('Nigeria', 'Lagos'), ('Norway', 'Oslo'),
                          ('Pakistan', 'Islamabad'), ('Peru', 'Lima'), ('Poland', 'Warsaw'), ('Portugal', 'Lisbon'),
                          ('Qatar', 'Doha'), ('Romania', 'Brasov'), ('Russia', 'Saint Petersburg'),
                          ('Russia', 'Moscow'), ('Russia', 'Novosibirsk'), ('Serbia', 'Belgrade'),
                          ('South Africa', 'Cape Town'), ('South Korea', 'Seoul'), ('Spain', 'Madrid'),
                          ('Sri Lanka', 'Colombo'), ('Switzerland', 'Zurich'), ('Taiwan', 'Taipei'),
                          ('Tanzania', 'Dar es Salaam'), ('Thailand', 'Bangkok'), ('Turkey', 'Istanbul'),
                          ('Ukraine', 'Kiev'), ('Venezuela', 'Caracas'), ('Vietnam', 'Ho Chi Minh City'),
                          ('Vietnam', 'Hanoi')]

        # For each OKC profile, the bot will count the number of desired keywords from the below list. Exchange for your own.
        self.good_words = ['mathematics', 'math', 'programming', 'programmer', 'python', 'c++', 'computer science',
                           'physics', 'quantum',
                           'phd', 'rational', 'rationality', 'rationalist', 'rationalism', 'effective altruism',
                           'homeschooling',
                           'quantitative', 'intelligence', 'intelligent', 'transhumanism', 'transhumanist', 'aging',
                           'futurism', 'futurist',
                           'embryo selection', 'deep learning', 'neural network', 'artificial intelligence', 'science',
                           'philosophy',
                           'history', 'literature', 'learning', 'data', 'algebra', 'intellectual dark web',
                           'sam harris', 'less wrong', 'cifar',
                           'slatestar codex', ' iq ', 'tech', 'peter thiel', 'elon musk', 'evolutionary',
                           'computational', 'nerd', '7 days to die',
                           'gamer', 'family', 'elder scrolls', 'software', 'neuro', 'mathematical', 'game theor',
                           'nash equilibrium', 'economics',
                           'financial independence', 'medicine', 'med school', 'INTJ', 'Skyrim', 'Cyberpunk', 'fantasy']
        self.store_path = ''
    
    def login(self):
        """
        Logs the user into the platform using username and password.
        """
        self.driver.get('https://www.okcupid.com/login')
        time.sleep(5)
        okc.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)
        #self.driver.find_element_by_name('username').send_keys(self.username)
        time.sleep(0.2)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(0.2)
        try:
            self.driver.find_element_by_xpath('//*[@id="p_login"]/div[1]/div[2]/div[4]/div[2]/div/button').click()
            time.sleep(1)
        except:
            pass
        self.driver.find_element_by_xpath(
            '//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input').click()
        time.sleep(2)
    
    def change_location(self, i):
        """
        Deprecated. Was used to change the users geographical location when this affected match filtering.
        """
        try:
            if self.driver.current_url is not 'https://www.okcupid.com/settings?':
                self.driver.get('https://www.okcupid.com/settings?')
                time.sleep(1)
            location_menu = Select(self.driver.find_element_by_xpath(
                '//*[@id="settings-container"]/div/div/main/div/fieldset[4]/div[1]/label/select')).select_by_visible_text(
                self.locations[i][0])
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="location"]').clear()
            time.sleep(0.2)
            self.driver.find_element_by_xpath('//*[@id="location"]').send_keys(self.locations[i][1])
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath(
                    '//*[@id="settings-container"]/div/div/main/div/fieldset[4]/div[2]/span/div/div/button[1]').click()
            except:
                pass
            time.sleep(3)
        except:
            time.sleep(5)
            if self.driver.current_url is not 'https://www.okcupid.com/settings?':
                self.driver.get('https://www.okcupid.com/settings?')
                time.sleep(1)
            location_menu = Select(self.driver.find_element_by_xpath(
                '//*[@id="settings-container"]/div/div/main/div/fieldset[4]/div[1]/label/select')).select_by_visible_text(
                self.locations[i][0])
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="location"]').clear()
            time.sleep(0.2)
            self.driver.find_element_by_xpath('//*[@id="location"]').send_keys(self.locations[i][1])
            time.sleep(2)
            try:
                time.sleep(3)
                self.driver.find_element_by_xpath(
                    '//*[@id="settings-container"]/div/div/main/div/fieldset[4]/div[2]/div/button[2]').click()
                time.sleep(2)
            except:
                pass
            self.driver.find_element_by_xpath(
                '//*[@id="settings-container"]/div/div/main/div/fieldset[4]/div[2]/span/div/div/button[1]').click()
            self.current_location = self.locations[i][0]
            time.sleep(3)
            
    def fetch_profiles(self, min_percent=90):
        """
        Deprecated. Used on to get profiles with a minimum match percentage from the matches page, before it was removed.
        """
        if self.driver.current_url is not 'https://www.okcupid.com/match':
            self.driver.get('https://www.okcupid.com/match')
            time.sleep(2)
        dropdown = self.driver.find_element_by_xpath('//*[@id="match-filters"]/div[3]/div/span/div/select')
        self.driver.execute_script("arguments[0].style.display = 'block';", dropdown)
        time.sleep(0.2)
        match_sort = Select(
            self.driver.find_element_by_xpath('//*[@id="match-filters"]/div[3]/div/span/div/select')).select_by_value(
            'MATCH')
        profiles = set()
        keep_looking = True
        scrolls = 0
        time.sleep(1)
        while keep_looking==True:
            matches = okc.driver.find_element_by_xpath('//*[@id="match_results"]/span[1]/div')
            matches_list = matches.find_elements_by_class_name('match-results-card')
            for match in matches_list:
                percentage = int(match.find_element_by_class_name('match-percentage').text.strip('%'))
                if percentage < min_percent:
                    keep_looking = False
                    break
                profiles.add({'href': match.get_attribute('href'), 'Match percentage': percentage,
                              'Location': self.current_location})
                #print(match.get_attribute('href'))
            self.driver.execute_script('window.scrollTo(0, '+str((scrolls+1)*500)+')')
            scrolls += 1
            time.sleep(2)
        return list(profiles)
    
    def fetch_all_profiles(self, path='okcmatches.xls'):
        """
        Deprecated. Used to cycle through locations and record matches in each location, before that possibility was removed.
        """
        wb = Workbook()
        print('Workbook saved')
        sheet = wb.add_sheet('Matches')
        sheet.write(0, 0, 'href')
        sheet.write(0, 1, 'Match percentage')
        sheet.write(0, 2, 'Location')
        wb.save(path)
        line = 1
        for i in range(len(self.locations)):
            self.change_location(i)
            profiles = fetch_profiles()
            for profile in profiles:
                sheet.write(line,0,profile['href'])
                sheet.write(line,1,profile['Match percentage'])
                sheet.write(line,2,profile['Location'])
                print('Profile number '+str(line)+' added: ',profile)
                line += 1
            wb.save(path)
            print('Workbook saved')
            
    def go_to_doubletake(self):
        """
        Goes to the double take page, where profiles can be swiped.
        """
        self.driver.get('https://www.okcupid.com/doubletake')
        
    def get_profile_text(self, save_dir):
        """
        Obtaines and saves the profile text of the currently viewed profile.
        """
        profile_id = self.get_profile_url().split('/profile/')[1]
        save_path = os.path.join(save_dir, profile_id + '.txt')
        profile_text = ''
        paragraph_num = 1
        while True:
            try:
                profile_paragraph = okc.driver.find_element_by_xpath(
                    '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[3]/span/span/div/div[' + str(
                        paragraph_num) + ']/p').text
                profile_text = profile_text + profile_paragraph + '\n'
            except:
                break
            paragraph_num += 1
        with open(save_path, 'w', encoding="utf-8") as out_file:
            out_file.write(profile_text)
        return profile_text

    def swipe(self, direction):
        """
        Swipes a profile in the double take either left (nay) or right (yay) direction.
        """
        if direction == 'right':
            self.driver.find_element_by_xpath(
                '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[2]/div').click()
        if direction == 'left':
            self.driver.find_element_by_xpath(
                '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[1]/div').click()
        time.sleep(1)
        
    def get_profile_url(self):
        """
        Fetches the profile url from a double take profile.
        """
        profile_url = self.driver.find_element_by_xpath(
            '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[1]/div[5]/a').get_attribute(
            'href').split('?cf=quickmatch')[0]
        return profile_url
        
    def get_profile_pics(self, save_dir):
        """
        Saves the profile pictures of the currently viewed profile.
        """
        profile_id = self.get_profile_url().split('/profile/')[1]
        pic_num = 1
        while True:
            try:
                pic_url = self.driver.find_element_by_xpath(
                    '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[2]/div/div/div[' + str(
                        pic_num) + ']/span/img').get_attribute('src').replace('400x400/400x400/', '')
                print('Pic url: ', pic_url)
                save_path = os.path.join(save_dir, profile_id+'N'+str(pic_num)+'.jpg')
                print('save path: ', save_path)
                urllib.request.urlretrieve(pic_url,save_path)
                print('Pic saved!')
            except:
                break
            pic_num += 1
            
    def get_match_percentage(self):
        """
        Obtains the match percentage of the currently viewed profile.
        """
        match_percentage = int(self.driver.find_element_by_xpath(
            '//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[1]/div[4]/span').text.strip(
            '%'))
        return match_percentage
    
    def compute_text_score(self, profile_text):
        """
        Computes the number of keywords in a profile text, using the keywords list attribute.
        """
        good_words = self.good_words
        score = 0
        for word in good_words:
            if word in profile_text.lower():
                score += 1
        return score
        
    def get_location(self):
        """
        Obtains the location (country) of the currently viewed profile.
        """
        try:
            location = self.driver.find_element_by_xpath('//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[1]/div[3]').text.split(', ')[1]
        except:
            location = 'Sweden'
        return location

        
    def run(self, number_to_swipe, path='okcprofiles.xls'):
        """
        Swipes and scrapes (saves images, pictures and profile data) a select number of profiles.
        """
        self.go_to_doubletake()
        time.sleep(5)
        rb = xlrd.open_workbook(path,formatting_info=True)
        r_sheet = rb.sheet_by_index(0) 
        r = r_sheet.nrows
        wb = copy(rb) 
        sheet = wb.get_sheet(0) 
        #sheet = wb.add_sheet('Matches')
        #sheet.write(0,0,'href')
        #sheet.write(0,1,'Match percentage')
        #sheet.write(0,2,'Location')
        #sheet.write(0,3,'Text score')
        #wb.save(path)
        print('Workbook saved')
        line = r
        while line <= number_to_swipe:
            match_percentage = self.get_match_percentage()
            self.get_profile_pics(self.store_path)
            profile_text = self.get_profile_text(self.store_path)
            text_score = self.compute_text_score(profile_text)
            profile_url = self.get_profile_url()
            location = self.get_location()
            sheet.write(line,0,profile_url)
            sheet.write(line,1,match_percentage)
            sheet.write(line,2,location)
            sheet.write(line,3,text_score)
            print('Profile number ' + str(line) + ' added. Url: ', profile_url, ' Match percentage: ', match_percentage,
                  'Location: ', location, ' Score: ', text_score)
            line += 1
            wb.save(path)
            print('Workbook saved')
            try:
                self.driver.find_element_by_xpath(
                    '//*[@id="main_content"]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/button/span').click()
                print('Got a match!')
            except:
                pass
            if match_percentage >= 90 or text_score > 0:
                self.swipe('right')
            else:
                self.swipe('left')
        
##################################################################################

# Main

##################################################################################

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Scrape a number of OKC profiles and swipe left/right on each.')
    parser.add_argument('--username', required=True, help='Your OKC username.')
    parser.add_argument('--password', required=True, help='Your OKC password.')
    parser.add_argument('--num-to-scrape', required=False, default=2500, help='The number of profiles to run through.')
    args = parser.parse_args()

    okc = OKC(args.username, args.password)
    time.sleep(10)
    okc.login()
    time.sleep(7)
    okc.run(args.num_to_scrape)