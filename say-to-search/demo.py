import speech_recognition as sr
import webbrowser as wb


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[FOR GOOGLE SEARCH : Say "The Nation wants to know about"]')
    print('[FOR YOUTUBE SEARCH : Say "Video"]')
    print('speak now....')
    audio = r3.listen(source, phrase_time_limit=15)

if 'the nation wants to know about' in r2.recognize_google(audio, language="en-US", show_all=False):
    r2 = sr.Recognizer()
    url = 'https://www.google.co.in/?#q='
    with sr.Microphone() as source:
        print('What do you want to Google.....')
        audio = r2.listen(source, phrase_time_limit=10)

        try:
            get = r2.recognize_google(audio, language="en-US", show_all=False)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print(e)


if 'video' in r1.recognize_google(audio, language="en-US", show_all=False):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('What are you searching for on Youtube.....')
        audio = r1.listen(source, phrase_time_limit=10)

        try:
            get = r1.recognize_google(audio, language="en-US", show_all=False)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print(e)
