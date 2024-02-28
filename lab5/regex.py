#1
import re
txt = "ab abbb abb"
pattern = r'ab+'
print(re.findall(pattern, txt))


#2
import re
txt = "ab abbb abb"
pattern = r'ab{2,3}'
print(re.findall(pattern, txt))

#3
import re
txt = "text_words to_check the code"
pattern = r'\b[a-z]+_[a-z]+\b'
print(re.search(pattern, txt))

#4
import re
txt = "ab Abbb Abb"
pattern = r'\b[A-Z][a-z]+\b'
print(re.search(pattern, txt))

#5
import re
txt = "ab Abx aooooob"
pattern = r'a.*b'
print(re.search(pattern, txt))

#6
import re

txt = "abbbbbb ,ab.b ab..bbb"
txt1 = "abbbbbb, abb ,abbbb"
txt2 = "........ksjsj"

pattern = r'[\s.,]'

# print(re.sub("\s", ":", txt))
# print(re.sub(",", ":", txt1))
# print(re.sub("[.]", ":", txt2))
print(re.sub(pattern, ':', txt))

#7
import re
def f(mObject):
    return mObject.group("g1").casefold()+ " "

text="my_world"
pattern = "(?P<g1>[a-z])(?P<g2>[_])+"
print(re.sub(pattern, f, text))

#8
import re

def w_to_upper(text):
    wordd = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,text)
    for i, word in enumerate(words):
        if i != 0:  
            wordd += " " + word
        else:
            wordd += word
    return wordd
text=input()
print(w_to_upper(text))

#9
import re

def spaces(txt):
    result = ""
    pattern = r'[A-Z][a-z]+'
    words = re.findall(pattern,txt)
    for i, word in enumerate(words):
        if i != 0:
            result += " " + word
        else:
            result += word
    return 

#10
import re
def f(mObject):
    return mObject.group("g1")+ "_" + mObject.group("g2").lower()
text = "myCamelCase" #camel case
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"
print(re.sub(pattern, f, text))