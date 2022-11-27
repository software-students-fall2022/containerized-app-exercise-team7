from deep_translator import GoogleTranslator

def trans(input,src,tgt):
    if src != "":
        return GoogleTranslator(source=src, target=tgt).translate(text=input)
    else:
        return GoogleTranslator(source='auto', target=tgt).translate(text=input)

