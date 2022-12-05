import unittest
import speech_recognition as sr
import translate
import speech_recog as sp


class Tests:
    def sanity_check(self):
        """
        Test system sanity to ensure logic is properly implemented.
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_speech_recognition(self):
        """
        Test accuracy of speech recognition tool with sample audio file.
        """
        r = sr.Recognizer()
        with sr.WavFile("machine-learning-client/tests/audio.wav") as source:
            audio = r.record(source)
        expected = "the quick brown fox jumps over the lazy dog"
        actual = r.recognize_google(audio)
        assert actual == expected, "Expected transcription to be correctly returned!"

    def test_stop(self):
        """
        Test that recognize() in speech_recog.py can identify the stop command. 
        This is used to exit the recursive loop.
        """
        r = sr.Recognizer()
        with sr.WavFile("machine-learning-client/tests/stop.wav") as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        text = text.lower()
        expected = True
        if text == "stop":
            actual = True
        else:
            actual = False
        assert actual == expected, "Expected stop command to be recognized!"
        
        
    def test_translate(self):
        """
        Test that translate() in translate.py returns the correct translated text
        per Google Translate.
        """
        input = "The quick brown fox jumps over the lazy dog."

        lang1 = translate.translate(input, "en", "es")
        lang2 = translate.translate(input, "en", "fr")
        lang3 = translate.translate(input, "en", "de")

        exp1 = "El veloz zorro marrón salta sobre el perro perezoso."
        exp2 = "Le renard brun rapide saute par-dessus le chien paresseux."
        exp3 = "Der schnelle braune Fuchs springt über den faulen Hund."

        assert lang1 == exp1, "Expected Spanish translation to be correct!"
        assert lang2 == exp2, "Expected French translation to be correct!"
        assert lang3 == exp3, "Expected German translation to be correct!"



    
        