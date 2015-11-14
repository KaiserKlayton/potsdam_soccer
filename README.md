# Potsdam Soccer

## Overview
This project deals with text summarization for soccer tickers via natural language processing and answer 
-set solving techniques. The resulting system utilizes Python and ASP in order to read in multiple tickers, extract information from them, merge them, and output a comprehensive summary.

## Usage
```
python run.py [-h] [--verbose VERBOSE] [--kicktionary KICKTIONARY]
              [--verbnet VERBNET] [--tickers TICKERS] [--luorder LUORDER]

optional arguments:
  -h, --help            show this help message and exit
  --verbose VERBOSE     print helpful messages about the progress
  --kicktionary KICKTIONARY
                        location of kicktionary xml file
  --verbnet VERBNET     location of folder with verbnet xml files
  --tickers TICKERS     location of tickers folder
  --luorder LUORDER     location of folder with lexical unit order file
```

## Requirements
We assume to have a running Python verion 2.7 on the system. Furthermore, we use the well known anna dependecy parser. This parser needs to be placed in ~/parser/. We used anna-3.3 for the english ticker messages. The following structure will be assumed for the program to run correctly:
```
parser
├── anna-3.3.jar
├── anna-3.61.jar
├── models.de
│   ├── lemmatizer.model
│   ├── mtag.model
│   ├── parser.model
│   └── tagger.model
├── models.en
│   ├── lemmatizer.model
│   ├── parser.model
│   └── tagger.model
├── parse2.sh
├── parse.sh
```

## Data
### Input
All ticker files need to be placed in the same directory. This directory is easily selected using the commandline argument `-- tickers DIR`.

### Output
The results are stored in ~/data/output/. Each run gets its own subdir named by a timestamp.
