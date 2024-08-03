import pyttsx3

class TTS():
    @staticmethod    
    def convert(text):
        en = pyttsx3.init()
        en.say(text)
        en.runAndWait()
    
    
def main():
    text = input("Enter Text \n==>")
    TTS.convert(text)
    
if __name__ == "__main__":
    main()