import random
import win32com.client

questionWeb = [
        'ISP'
    ]


def interviewWeb():
    while True:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        words = '请说一下' + random.choice(questionWeb)
        speaker.Speak(words)
        input('点击回车继续')

if __name__ == '__main__':
    interviewWeb()
