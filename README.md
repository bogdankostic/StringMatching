# StringMatching
This is a python-based commandline tool that allows you to search for
one or more search patterns inside a raw text string, a text file or a
directory containing several txt-files.

## Installation
To install this commandline tool, execute the following commands in 
your terminal:
```bash
git clone https://github.com/bogdankostic/StringMatching.git
cd StringMatching
sudo ./install.sh
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
