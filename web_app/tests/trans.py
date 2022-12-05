#moved to web-app folder because i was having a hard time importing it into controller.py 
#- can be moved if someone can figure out import
from deep_translator import GoogleTranslator

def trans(input,src,tgt):
    #if src does not have any input that use "auto" functionality - this has not been implemented yer
    if src != "":
        return GoogleTranslator(source=src, target=tgt).translate(text=input)
    #translate given the src and target, etc
    else:
        return GoogleTranslator(source='auto', target=tgt).translate(text=input)

