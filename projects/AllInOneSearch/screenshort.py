import pyautogui
from pathlib import Path
Path('my_file.mp3').suffix == '.mp3'
class Screensht:
    @staticmethod
    def screenshot():
        print("Taking Screenshot")
        sshot = pyautogui.screenshot()
        print("screenshot taken")
        fname = input("Enter file name\n=>")
        if Path(fname).suffix == ".jpg" or Path(fname).suffix == ".png":
            sshot.save(fname)
        else:
            final = fname+".jpg"
            sshot.save(final)
        
def main():
    Screensht.screenshot()
        

if __name__ == "__main__":
    main()