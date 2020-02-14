import nltk
import codecs
load_grammar = nltk.data.load('file:Englishgrammer.cfg')
file_input = codecs.open('EnglishInput.txt', 'r')
for sent in file_input:
    wrong_syntax=1
    sent_split = sent.split()
    print("\n\n"+ sent)
    rd_parser = nltk.RecursiveDescentParser(load_grammar)
    for tree_struc in rd_parser.parse(sent_split):
        s = tree_struc
        wrong_syntax=0
        print("\n Correct Grammer !!! \n")
        print(str(s))
        f = open("demoEnglish.txt", "a")
        f.write("\nCorrect Grammer!!!!! \n")
        f.write(str(s))
        f.close()
    if wrong_syntax==1:
        print("\n Wrong Grammer!!!!!! \n")
        f = open("demoEnglish.txt", "a")
        f.write("\n Wrong Grammer!!!!! \n")
        f.close()
