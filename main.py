from letters import *

letters_list = {'a':a,'b':b, 'c':c, 'd':d, 'e':e,'f':f, 'g':g, 'h':h, 'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s, ' ':space, '.':period, ':':colon, '-':hyphen}

output1 = []
output2 = []
output3 = []
output4 = []
output5 = []
output6 = []
def main():
	text = input('Enter text: ')
	for rows in range(len(space)):
		string = ''
		for chars in text:
			var = letters_list.get(chars)
			string += var[rows][0]
		print(string)
    
if __name__ == '__main__':
    while True:
        main()

