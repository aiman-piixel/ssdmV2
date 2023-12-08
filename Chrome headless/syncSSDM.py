from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from IPython.display import clear_output
import textdistance
import os
import time
import glob2
import pandas as pd
import sys
import json

def sync(login_num, currentDir):
    #return day value in dropdown
    def return_day(driver, DaySeries):
        select_date = driver.find_element(By.XPATH, "//select[@name='_b_hari_mula_tk']")
        select = Select(select_date)
        if DaySeries == "01" or DaySeries == '1':
            select.select_by_value('1')
        elif DaySeries == "02" or DaySeries == '2':
            select.select_by_value('2')
        elif DaySeries == "03" or DaySeries == '3':
            select.select_by_value('3')
        elif DaySeries == "04" or DaySeries == '4':
            select.select_by_value('4')
        elif DaySeries == "05" or DaySeries == '5':
            select.select_by_value('5')
        elif DaySeries == "06" or DaySeries == '6':
            select.select_by_value('6')
        elif DaySeries == "07" or DaySeries == '7':
            select.select_by_value('7')
        elif DaySeries == "08" or DaySeries == '8':
            select.select_by_value('8')
        elif DaySeries == "09" or DaySeries == '9':
            select.select_by_value('9')
        else:    
            select.select_by_value(DaySeries)

    #return month value in dropdown
    def return_month(driver, MonthSeries):
        select_month = driver.find_element(By.XPATH, "//select[@name='_b_bulan_mula_tk']")
        select = Select(select_month)
        if MonthSeries == "1" or MonthSeries == '01':
            select.select_by_value('JAN')
        elif MonthSeries == "2" or MonthSeries == '02':
            select.select_by_value('FEB')
        elif MonthSeries == "3" or MonthSeries == '03':
            select.select_by_value('MAR')
        elif MonthSeries == "4" or MonthSeries == '04':
            select.select_by_value('APR')
        elif MonthSeries == "5" or MonthSeries == '05':
            select.select_by_value('MAY')
        elif MonthSeries == "6" or MonthSeries == '06':
            select.select_by_value('JUN')
        elif MonthSeries == "7" or MonthSeries == '07':
            select.select_by_value('JUL')
        elif MonthSeries == "8" or MonthSeries == '08':
            select.select_by_value('AUG')
        elif MonthSeries == "9" or MonthSeries == '09':
            select.select_by_value('SEP')
        elif MonthSeries == "10":
            select.select_by_value('OCT')
        elif MonthSeries == "11":
            select.select_by_value('NOV')
        else:
            select.select_by_value('DEC')
            
    #return year value in dropdown
    def return_year(driver, YearSeries):
        select_year = driver.find_element(By.XPATH, "//select[@name='_b_tahun_mula_tk']")
        select = Select(select_year)
        select.select_by_value(YearSeries)
        
    #return hour and AM/PM value in dropdown
    def return_hour(driver, HourSeries):
        select_hour = driver.find_element(By.XPATH, "//select[@name='jam']")
        select = Select(select_hour)
        if HourSeries == "13" or HourSeries == "01" or HourSeries == '1':
            select.select_by_value('01')
        elif HourSeries == "14" or HourSeries == "02" or HourSeries == '2':
            select.select_by_value('02')
        elif HourSeries == "15" or HourSeries == "03" or HourSeries == '3':
            select.select_by_value('03')
        elif HourSeries == "16" or HourSeries == "04" or HourSeries == '4':
            select.select_by_value('04')
        elif HourSeries == "17" or HourSeries == "05" or HourSeries == '5':
            select.select_by_value('05')
        elif HourSeries == "18" or HourSeries == "06" or HourSeries == '6':
            select.select_by_value('06')
        elif HourSeries == "19" or HourSeries == "07" or HourSeries == '7':
            select.select_by_value('07')
        elif HourSeries == "20" or HourSeries == "08" or HourSeries == '8':
            select.select_by_value('08')
        elif HourSeries == "21" or HourSeries == "09" or HourSeries == '9':
            select.select_by_value('09')
        elif HourSeries == "22" or HourSeries == "10":
            select.select_by_value('10')
        elif HourSeries == "23" or HourSeries == "11":
            select.select_by_value('11')
        elif HourSeries == "24" or HourSeries == "00" or HourSeries == "0":
            select.select_by_value('12')    
        else:
            select.select_by_value(HourSeries)

    #return minute value in dropdown
    def return_min(driver, MinSeries):
        select_min = driver.find_element(By.XPATH, "//select[@name='minit']")
        select = Select(select_min)
        select.select_by_value(MinSeries)

    def close_driver(driver):
        try:
            driver.quit()
        except Exception as e:
            print("An error occurred while closing the WebDriver:", e)
    
    login_path = currentDir / f"ssdm_split/login_{login_num}.csv"
    csv_dir = currentDir / f"ssdm_split/ssdm_{login_num}"
    config_dir = currentDir / "config.json"
    
    # Read data from the JSON file
    with open(config_dir, 'r') as jsonfile:
        config = json.load(jsonfile)

    #load required details from excel
    df_login = pd.read_csv(str(login_path))
    schoolName = df_login['NAME']
    ssdmID = df_login['ssdmID']
    ssdmPass = df_login['ssdmPass']
    completion = df_login['done']

    #list out all csv files in excel folder
    csvFiles = glob2.glob(os.path.join(str(csv_dir) + "/*.csv"))
    csvFiles.sort()

    for i in range(len(schoolName)) :
        driver = None
        try:
            df = pd.read_csv(str(csvFiles[i]))
            
            if completion[i] == 1:
                print( schoolName[i] + ' has already been synced')
                continue
            
            else:
                date_column = df['tarikh'].astype('string')
                time_column = df['masa'].astype('string')
                day = []
                month = []
                year = []
                hour = []
                minute = []
                am_pm = []

                for date_string, time_string in zip(date_column, time_column):
                    date_part = date_string.split('/')  # type: ignore # Split the date into year, month, and day
                    time_part = time_string.split() # type: ignore # split AM/PM from time
                    time_section = time_part[0].split(':') # split time into hour and minute

                    day.append(date_part[0])
                    month.append(date_part[1])
                    year.append(date_part[2])
                    hour.append(time_section[0])
                    minute.append(time_section[1])
                    am_pm.append(time_part[1])
                    
                studentName = df['nama']
                amalanID = df['amalanID']
                remark = df['keterangan']
                teacherName = df['teacherName']
                status = df['status'].to_numpy()
                synced = df['synced'].to_numpy()
                
                # set options for chrome
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--headless")
                #initiate chrome session
                driver = webdriver.Chrome(options=chrome_options)
                wait = WebDriverWait(driver, 10)
                driver.set_script_timeout(10)
                driver.get("https://ssdm.moe.gov.my/")
                print( "Syncing for " + schoolName[i])
                
                login_box, pass_box = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR , "input[name='id'], input[name='password']")))
                login_box.send_keys(str(ssdmID[i]))
                pass_box.send_keys(str(ssdmPass[i]))
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button']"))).click()
                
                driver.find_element(By.XPATH, "//a[@href='kemaskini_murid.cfm']").click() 
                totalStudent = len(studentName)
                print(f"Window {login_num} : {schoolName[i]} --> Total submission: "+ str(totalStudent))
                
                for x in range(len(studentName)):
                    #check if submission is already synced
                    if synced[x]==1:
                        totalStudent-=1
                        print("This submission has already been synced")
                        print(f"Window {login_num} : {schoolName[i]} --> Remaining submissions :"+ str(totalStudent)+"\n")
                        continue
                    if status[x]==2:
                        totalStudent-=1
                        print("This submission has already been synced by the school")
                        print(f"Window {login_num} : {schoolName[i]} --> Remaining submissions :"+ str(totalStudent)+"\n")
                        #update sync status
                        synced[x]=3
                        df['synced'] = synced
                        df.to_csv(csvFiles[i], index=False)
                        continue
                    name_search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR , "input[name='nama']")))        
                    name_search.send_keys(studentName[x])
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='cari']"))).click()
                    fail_message = driver.find_elements(By.XPATH, "//span[text()='Maaf tiada padanan dengan data yang di cari dalam pangkalan data murid (APDM)']")
                    #check if student is available in database, skip if not present
                    if len(fail_message) >0:
                        print(studentName[x]+" is not available in the database ")
                        totalStudent-=1
                        print(f"Window {login_num} : {schoolName[i]} --> Remaining submissions :"+ str(totalStudent)+"\n")
                        #update sync status
                        synced[x]=2
                        df['synced'] = synced
                        df.to_csv(csvFiles[i], index=False)
                        continue
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Papar Kes')]"))).click()
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Tambah Amalan Baik']"))).click()
                    
                    #fills out keterangan
                    keterangan = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR , "textarea[name='keteranganamalanbaik']")))
                    keterangan.send_keys(remark[x])
                    #select tempat
                    select_tempat = driver.find_element(By.XPATH, "//select[@name='TEMPAT']")
                    select = Select(select_tempat)
                    select.select_by_value('01')
                    #select amalan baik
                    select_amalan = driver.find_element(By.XPATH, "//select[@name='AB']")
                    select = Select(select_amalan)
                    if (amalanID[x] == 1):
                        select.select_by_value('1')
                    elif (amalanID[x] == 2):
                        select.select_by_value('2')
                    elif (amalanID[x] == 3):
                        select.select_by_value('3')
                    elif (amalanID[x] == 4):
                        select.select_by_value('4')
                    elif (amalanID[x] == 5):
                        select.select_by_value('5')
                    elif (amalanID[x] == 6):
                        select.select_by_value('6')
                    elif (amalanID[x] == 7):
                        select.select_by_value('7')
                    else:
                        select.select_by_value('8')
                        
                    #select date
                    return_day(driver, day[x])
                    return_month(driver, month[x])
                    #select time
                    return_hour(driver, hour[x])
                    return_min(driver, minute[x])
                    #select AM/PM
                    select_AMPM = driver.find_element(By.XPATH, "//select[@name='am_pm']")
                    select = Select(select_AMPM)
                    if(am_pm[x] == 'AM'):
                        select.select_by_value('AM')
                    else:
                        select.select_by_value('PM')
                        
                    #select teacher
                    select_cikgu = driver.find_element(By.XPATH, "//select[@name='papar_guru']")
                    select = Select(select_cikgu)
                    
                    best_match_similarity = 0
                    best_match_option = None
                    
                    if pd.isna(teacherName[x]):
                        select.select_by_index(0)
                    else:
                        # Loop through the options and find the best match for the partial name
                        for option in select.options:
                            similarity = textdistance.jaro_winkler.normalized_similarity(teacherName[x].lower(), option.text.lower())
                            if similarity > best_match_similarity:
                                best_match_similarity = similarity
                                best_match_option = option

                        # Check if a best match was found and select it
                        if best_match_option is not None:
                            select.select_by_visible_text(best_match_option.text)
                        else:
                            # Handle the case when no match was found
                            select.select_by_index(0)
                                        
                    #click checkbox
                    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
                    #submit ssdm
                    driver.find_element(By.XPATH, "//input[@name='simpan_amalanbaik']").click()
                    
                    #update sync status
                    synced[x]=1
                    df['synced'] = synced
                    df.to_csv(csvFiles[i], index=False)
                    
                    #handle alert popup
                    alert = wait.until(EC.alert_is_present())
                    if alert:
                        alert.accept()
                    driver.switch_to.default_content()
                    
                    totalStudent-=1
                    print("Sync is successful!")
                    print(f"Window {login_num} : {schoolName[i]} --> Remaining submissions :"+ str(totalStudent)+"\n")

                    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='kemaskini_murid.cfm']"))).click()
                
                clear_output()
                print("Syncing for " +schoolName[i]+ " is done")

                #update school sync status
                completion[i]=1
                df_login['done'] = completion
                df_login.to_csv(str(login_path), index=False)
                
                time.sleep(1)
                driver.close()
                    
        except Exception as e:
            print("An error occured:", e)
            sys.exit("Error encountered. Stopping the process.")  # Stop the script
        finally:
            close_driver(driver)

    print("Completed")
    
if __name__ == "__main__":
    working_dir = Path.cwd()
    
    if len(sys.argv) > 1:
        login_num = int(sys.argv[1])
        sync(login_num, working_dir)
    else:
        print("Please provide number of folder(s) to sync")