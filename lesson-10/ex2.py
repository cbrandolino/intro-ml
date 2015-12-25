# Deploying Stemming

#### Boilerplate #################################################################


from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

#### Exercise code #############################################################

    stemmer = SnowballStemmer("english")
    words = " ".join([stemmer.stem(word) for word in text_string.split()])

        
#### Boilerplate #################################################################

    return words    

def main():
    ff = open("../ud120-projects/text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text


if __name__ == '__main__':
    main()

