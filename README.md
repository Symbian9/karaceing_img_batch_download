# karaceing_img_batch_download
simple Python 2/3 compatible script for downloading batches of images from dokuwiki type sites


## Do you have Python 2 or 3 installed?

### Yes 
* Download [karaceing_img_batch_download](https://github.com/engelhardtnick/karaceing_img_batch_download)

### No
* Are you on Linux or Windows?

#### Linux (Ubuntu >16)
* run `sudo apt-get install python3.6`
* run `sudo apt install python3-pip`
* run `pip install lxml` and `pip install beautifulsoup4`
* done: go back to "Yes"
#### Windows
* download latest [Python 3](https://www.python.org/downloads/windows/ "Python Homepage")
* install `Windows x86-64 executable installer` (64bit) or `Windows x86 executable installer` (32bit)
  * most new PCs are use 64 bit, 32 bit will always work
* `Windows Button` -> type in `cmd` -> `enter`
* run `pip install lxml` and `pip install beautifulsoup4`
* done: go back to "Yes"

## Usage
### Windows
* put `wiki_batch_download.py` in a new directory
* doubleclick or run from shell
  * `Windows Button` -> type `cmd` -> enter -> `cd your\new\directory`
  * run `python wiki_batch_download.py`
* follow instructions
### Linux
* put `wiki_batch_download.py` in a new directory
* open terminal in new directory
* run `python3 wiki_batch_download.py`
* follow instructions

## Saving username+password
* edit file `wiki_batch_download.py`
* find lines 
```
if False:
    username = "YOUR USERNAME"
    password = "YOUR PASSWORD"
else:
    username = raw_input("Please enter username: \n")
    password = getpass.getpass("Please enter password: \n")
```
* change `False` to `True` 
* enter `YOUR USERNAME` and `YOUR PASSWORD` in ` "" ` and save file
