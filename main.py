from letters import *

letters_list = {'a':a,'b':b, 'c':c, 'd':d, 'e':e,'f':f, 'g':g, 'h':h, 'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p, ' ':space, '.':period, ':':colon}

output1 = []
output2 = []
output3 = []
output4 = []
output5 = []
output6 = []
def main():
    text = input('Input text: ').lower()
    for letters in text:    
        for i in range(6):
            var = letters_list.get(letters)
            if i == 0:
                output1.append(var[i][0])
            elif i == 1:
                output2.append(var[i][0])
            elif i == 2:
                output3.append(var[i][0])
            elif i == 3:
                output4.append(var[i][0])
            elif i == 4:
                output5.append(var[i][0])
            elif i == 5:
                output6.append(var[i][0])
    output()
def output():
    print(*output1, '\n',*output2,'\n',*output3,'\n',*output4,'\n',*output5,'\n',*output6,sep='')
    output1.clear()
    output2.clear()
    output3.clear()
    output4.clear()
    output5.clear()
    output6.clear()
    
if __name__ == '__main__':
    while True:
        main()