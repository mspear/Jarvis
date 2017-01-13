import pyttsx

def speak(words):
	global speechengine
	speechenginw.say(words)
def main():
	global speechengine
	speechengine = pyttsx('nsss')
	speak('hello world')
if __name__ == '__main__':
	main()
