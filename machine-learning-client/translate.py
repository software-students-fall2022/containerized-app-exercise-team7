from deep_translator import GoogleTranslator

def translate(input,src,tgt):
    return GoogleTranslator(source=src, target=tgt).translate(text=input)


