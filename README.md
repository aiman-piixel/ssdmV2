<h1 align="center" id="title">SSDMV2</h1>

<p align="center"><img src="https://socialify.git.ci/aiman-piixel/ssdmV2/image?description=1&amp;descriptionEditable=Automated%20python%20script%20to%20submit%20SSDM%20submission%20from%20StudentQR%20private%20server%20to%20KPM%27s%20SSDM%20portal%20for%20use%20by%20Malaysian%20schools&amp;name=1&amp;owner=1&amp;pattern=Diagonal%20Stripes&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">Automated python script to submit SSDM submission from StudentQR private server to KPM's SSDM portal for use by Malaysian schools. A follow up to the previous version [here](https://github.com/aiman-piixel/SSDM-Sync-Tools).</p>

  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Automated submission of SSDM's submission data
*   Direct integration with StudentQR private server and app
*   Multiprocess on demand for more efficiency

<h2>🛠️ Initial Setups:</h2>

<p>1. This project make use of isolated python environment through Anaconda Distribution. To begin setup go to https://www.anaconda.com/download and download the installer. Follow the instructions in the installer.</p>

<h3>During Anaconda Distribution installation: (optional)</h3>

Check the option to "Add Anaconda3 to my PATH environment variable." This ensures that Anaconda's commands are available in your system's command prompt or terminal. Check the option to "Register Anaconda3 as the default Python .." This makes Anaconda3 the default Python interpreter.


<p>2. Open a terminal or Anaconda prompt and run the following command to create a new environment named 'py' with the latest version of Python and use conda again to activate the newly created environment.</p>

```
$ conda create --name py python
$ conda activate py
```

<p>3. While the 'py' environment is active install additional packages using pip</p>

```
$ pip install openpyxl selenium glob2 textdistance pymongo pandas ipython ipykernel natsort
```

<p>4. To use Selenium with Google Chrome you'll need the Chrome WebDriver. Identify the correct version of your Google Chrome's browser so you know which version of the chrome webdriver that you need to install</p>

<p>5. If you are using Chrome version 115 or newer please consult [Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/). This page provides convenient JSON endpoints for specific ChromeDriver version downloading. Look for Stable 64-bit version. Save the downloaded ZIP file to your computer.</p>

<h3>Installation on Windows/MacOS/Linux</h3>

<h4>Windows</h4>

<p>1. Locate the downloaded ZIP file and extract its contents to a location on your computer (e.g. C:\WebDriver).</p>

<p>2. Search for "Environment Variables" in the Windows Start menu and select "Edit the system environment variables". Click the "Environment Variables" button. Under "System variables" find the "Path" variable and click "Edit". Click "New" and enter the full path to the directory containing the WebDriver executable (e.g. 'C:\WebDriver'). Click "OK" to close the windows.</p>

<p>3. For the changes to take effect restart your computer.</p>

<p>4. Open a Command Prompt. Type chromedriver and press Enter. If you see output without errors the WebDriver is installed correctly.</p>

<h4>MacOS</h4>

<p>For MacOS, you don't necessarily need to download chromedriver from the web. You can just use brew package manager. If you haven't install brew yet, follow this steps. If you have, you can skip step 1</p>

<p>1. Open terminal and paste this line. This will install brew on your machine.</p>

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

<p>2. In the same terminal, paste this line</p>

```
$ brew install chromedriver --cask
```
<p>3. After the installation is done, type chromedriver and press Enter. If you see output without errors, then the webdriver is installed correctly.</p>

<h4>Linux(Debian/Ubuntu derivatives)</p>

<p>1. Open your terminal of choice and use these commands to copy chromedriver to Google Chrome's binary path. (Make the terminal has the working directory as the chromedriver)</p>

```
$ sudo chmod +x chromedriver
$ sudo mv chromedriver /usr/local/share/chromedriver
$ sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
$ chromedriver --version (to check if the process is working)
```

<p>Now you have the Chrome WebDriver installed and set up on your Windows system. You can use it with Selenium for automated testing and web scraping.</p>

<h2>Running the script</h2>

<p>1. Before running the script, go to the directory of the project and create two empty folders named 'data' and 'split_ssdm' **important**</p>

<p>2. To run the script, open up terminal and use this command to activate our newly created environment and run the script. There will be on-screen instructions guiding you on every involved process.</p>

```
$ conda activate py && python exec.py
```
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   openpyxl
*   Selenium
*   Chrome WebDriver
*   Pandas
*   MongoDB Driver
*   iPython

<h2>Extra info</h2>

For any info or question feel free to reach out on aiman.firdaus.rasman@gmail.com. 

<p>Other Link(s):</p>
<p>StudentQR official website: https://www.studentqr.com/</p>