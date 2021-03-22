# StringMatching
This is a python-based commandline tool that allows you to search for
one or more search patterns inside a raw text string, a text file or a
directory containing several txt-files.

This tool has been developed and tested using Python 3.7.

## Installation
To install this commandline tool, execute the following commands in 
your terminal:
```bash
git clone https://github.com/bogdankostic/StringMatching.git
cd StringMatching
sudo -H ./install.sh
```

## Usage
After installation, you can use this tool directly from the commandline
by executing the following command:
```bash
 search [-h] [-n] [-i] SEARCH_PATTERN [SEARCH_PATTERN ...] TEXT_INPUT
```
**Positional Arguments:**
- SEARCH_PATTERN – *Search pattern to search for in the provided text inputs*
- TEXT_INPUT – *Raw text, text file or directoy containing .txt-files*

**Optional Arguments:**
- -h / --help – *Show help message explaining how to use this tool*
- -n / --naive – *Use naive string matching algorithm instead of Boyer-Moore algorithm*
- -i / --case-insensitive – *Perform case-insensitive search*

### Output
Each match is printed on a new line with the following tab-seperated formats:

#### Format for single text files and raw text input
SEARCH_PATTERN \t POSITION_IN_TEXT/FILE

#### Format for directories containing txt-files
FILE_NAME \t SEARCH_PATTERN \t POSITION_IN_FILE

### Example usages
#### Search in raw text input
```bash
search text "This tool allows you to search through texts."
```
Output:
```
text    39
```

#### Search case-insensitive
```bash
search -i covid "The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2)"
```
Output:
```
covid   4
covid   115
```

#### Search through a single text file
```bash
search -i covid sample_data/astra_zeneca.txt
```
Output:
```
covid   77
```

#### Search through a directory of txt-files
```bash
search -i covid sample_data
```
Output:
```
biontech_pfizer.txt     covid   774
biontech_pfizer.txt     covid   1432
moderna.txt     covid   41
moderna.txt     covid   66
astra_zeneca.txt        covid   77
johnson_johnson.txt     covid   154
johnson_johnson.txt     covid   1079
```

#### Use multiple search patterns
```bash
search Vektor RNA sample_data
```
Output:
```
biontech_pfizer.txt     RNA     184
biontech_pfizer.txt     RNA     435
moderna.txt     RNA     1
moderna.txt     RNA     262
astra_zeneca.txt        Vektor  322
astra_zeneca.txt        Vektor  330
johnson_johnson.txt     Vektor  527
```

#### Use naïve string matching algorithm instead of Boyer-Moore algorithm
```bash
search -n string "This example uses the naive string matching algorithm."
```
Output:
```
string  28
```

## Used String Matching Algorithms
As default string matching algorithm, this tool uses the Boyer-Moore
algorithm which makes use of the bad-character heuristic and the
good-suffix heuristic. Furthermore, the naïve string matching algorithm
can be used by setting th option '-n'.  
Both algorithms have been implemented according to the pseudo-code
presented in Cormen et al.'s (1990) *Introduction to Algorithms.*

## References
Cormen, T. H., Leiserson, C. E., & Rivest, R. L. (1990). Introduction
to Algorithms. In McGraw-Hill. MIT Press. Chapter 34 String Matching.
