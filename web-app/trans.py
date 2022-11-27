from deep_translator import GoogleTranslator

def trans(input,src,tgt):
    #if src does not have any input that use "auto" functionality - this has not been implemented yer
    if src != "":
        return GoogleTranslator(source=src, target=tgt).translate(text=input)
    #translate given the src and target, etc
    else:
        return GoogleTranslator(source='auto', target=tgt).translate(text=input)

