'''
Text Conversion from german speech to text.....
'''
def GermanTextFromSpeech(wav_file):
    text_generated = ''
    try:
        import speech_recognition as sr
        from pydub import AudioSegment
    except Exception as e:
        print("[-] ModuleNotFoundError: ", e)

    try:
        r = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
            audio_text = r.listen(source)
            try:
                text = r.recognize_google(audio_text, language="de-DE")
                # print('[+] -> ', text)
                text_generated = text
                return False, text_generated
            except Exception as err:
                # print(f"[-] Error Found: {err}")
                pass
    except Exception as er:
        # print(f"[-] Error Occured: {er}")
        pass
