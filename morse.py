MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', '.':'.-.-.-', '?':'..--..', '!':'-.-.--', 
                    '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}


##########################################################################
# Function to encrypt the string
# according to MORSE_CODE_DICT
##########################################################################

class Solution:
    def encrypt(self, message):
            #type message: string
            #return type: string
            newstr=""
            message= message.upper()
            #TODO: Write code below to return a string with the solution to the prompt.
            for i in range(len(message)):
                print(message[i])
                if(message[i]==" "):
                     newstr+= " "
                else:
                    newstr+=MORSE_CODE_DICT[message[i]]

            return newstr

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.encrypt(str1)
     print(ans)

if __name__ == '__main__':
    main()