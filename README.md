<h1 align="center" id="title">SSDMV2</h1>

<p align="center"><img src="https://socialify.git.ci/aiman-piixel/ssdmV2/image?description=1&amp;descriptionEditable=Automated%20python%20script%20to%20submit%20SSDM%20submission%20from%20StudentQR%20private%20server%20to%20KPM%27s%20SSDM%20portal%20for%20use%20by%20Malaysian%20schools&amp;name=1&amp;owner=1&amp;pattern=Diagonal%20Stripes&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">Automated python script to submit SSDM submission from StudentQR private server to KPM's SSDM portal for use by Malaysian schools. A follow up to the previous version [here](https://github.com/aiman-piixel/SSDM-Sync-Tools).</p>

  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Automated submission of SSDM's submission data
*   Direct integration with StudentQR private server and app
*   Multiprocess on demand for more efficiency

<h2>🛠️ Initial Setups:</h2>

<p>

1. This project make use of isolated python environment. You will need create a seperate enviroment to avoid any clash with the system's default python version. Follow the instructions below to setup your machine.

2. If you are using a Windows machine, you will need to use pyenv-win. If you are using MacOS/Linux or Unix derivative, you will be using pyenv module instead.

---

**pyenv** : [Click Here](https://github.com/pyenv/pyenv) || 
**pyenv-win** : [Click Here](https://github.com/pyenv-win/pyenv-win)


<mark>Follow the instructions in the links above to install the module and the latest isolated python version to your machine.</mark>

---

3. While using the latest python environment, install additional packages using pip3

```
$ pip3 install openpyxl selenium glob2 textdistance pymongo pandas ipython ipykernel natsort sshtunnel
```

4. To use Selenium with Google Chrome you'll need the Chrome WebDriver. Identify the correct version of your Google Chrome's browser so you know which version of the chrome webdriver that you need to install

5. If you are using Chrome version 115 or newer please consult [Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/). This page provides convenient JSON endpoints for specific ChromeDriver version downloading. Look for Stable 64-bit version. Save the downloaded ZIP file to your computer.</p>

<h2>Webdriver Installation on Windows/MacOS/Linux</h2>

<h4>Windows</h4>

<p>

1. Locate the downloaded ZIP file and extract its contents to a location on your computer (e.g. C:\WebDriver).

2. Search for "Environment Variables" in the Windows Start menu and select "Edit the system environment variables". Click the "Environment Variables" button. Under "System variables" find the "Path" variable and click "Edit". Click "New" and enter the full path to the directory containing the WebDriver executable (e.g. 'C:\WebDriver'). Click "OK" to close the windows.

3. For the changes to take effect restart your computer.

4. Open a Command Prompt. Type chromedriver and press Enter. If you see output without errors the WebDriver is installed correctly.</p>

<h4>MacOS</h4>

<p>For MacOS, you don't necessarily need to download chromedriver from the web. You can just use brew package manager. If you haven't install brew yet, follow this steps. If you have, you can skip step 1

1. Open terminal and paste this line. This will install brew on your machine.

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. In the same terminal, paste this line

```
$ brew install chromedriver --cask
```
3. After the installation is done, type chromedriver and press Enter. If you see output without errors, then the webdriver is installed correctly.</p>

<h4>Linux(Debian/Ubuntu derivatives)</h4>

<p>

1. Open your terminal of choice and use these commands to copy chromedriver to Google Chrome's binary path. (Make the terminal has the working directory as the chromedriver)

```
$ sudo chmod +x chromedriver
$ sudo mv chromedriver /usr/local/share/chromedriver
$ sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
$ chromedriver --version (to check if the process is working)
```

Now you have the Chrome WebDriver installed and set up on your Windows system. You can use it with Selenium for automated testing and web scraping.</p>

<h2>Running the script</h2>

<p>

**IMPORTANT**

1. Before running the script, go to the directory of the project and create two empty folders named 'data' and 'split_ssdm'

2. To run the script, open up terminal and use this command. There will be on-screen instructions guiding you on every involved process.</p>

```
$ python3 exec.py
```
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Selenium
*   webdriver

<h2>Extra info</h2>

For any info or question feel free to reach out on aiman.firdaus.rasman@gmail.com. 

<p>Other Link(s):</p>
<p>

[StudentQR Official Website](https://www.studentqr.com/)

[My Personal Github Page](https://github.com/aiman-piixel)
</p>
