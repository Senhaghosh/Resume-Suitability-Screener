import re

def cleanResume(txt):
    cleanTxt = re.sub(r'http\S+', '', txt)             # remove URLs
    cleanTxt = re.sub(r'RT|cc', '', cleanTxt)          # remove RT/cc
    cleanTxt = re.sub(r'@', '', cleanTxt)              # remove @
    cleanTxt = re.sub(r'#', '', cleanTxt)              # remove #
    cleanTxt = re.sub(r'[^a-zA-Z]', ' ', cleanTxt)     # remove special chars/numbers
    cleanTxt = re.sub(r'[^\x00-\x7f]', ' ', cleanTxt)  # remove non-ascii
    cleanTxt = re.sub(r'\s+', ' ', cleanTxt)           # remove extra spaces
    return cleanTxt.strip()
