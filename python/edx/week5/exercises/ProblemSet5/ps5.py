import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #pass #delete this line and replace with your code here
        cipher_dict = {}
        letters = string.ascii_lowercase
        a = ( i for i in letters * 2)  # generator expression of letters

        for i in letters:                                              # 0 - 26 range for all letters in alphabet
            while shift != 0:                                          # skip items from generator expression 'a' n-times according to value of 'shift'
                next(a)
                shift -= 1
            else:
                val = next(a)                                          # when while loop ended, 'a' is at position we want, so know we can save
            cipher_dict[i] = val                                       # put i: val in cipher_dict
            cipher_dict[i.upper()] = val.upper()                       # also put capital of i: val in cipher_dict

        return cipher_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #pass #delete this line and replace with your code here
        our_dict = self.build_shift_dict(shift)                                # build our cipher dict based on 'shift'
        our_text = [ c for c in self.get_message_text() ]
        our_cipher = []

        for char in our_text:
            if char in (string.punctuation + ' ' + string.digits):
                our_cipher.append(char)
            else:
                our_cipher.append(our_dict[char])

        
        return ''.join(our_cipher)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
        #self.message_text = text
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        # Since shift is changing, let's also update our dict and apply cipher on our message
        self.encrypting_dict =  self.build_shift_dict(self.shift)
        self.apply_shift(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #pass #delete this line and replace with your code here
        decrypt_msg_tmp = []
        shift_dict = {}
        count = 1

        while count != 0:
            for s in range(0, 26):
                # if decrypt_msg_tmp not empty then make it empty list (clear for each s)
                if decrypt_msg_tmp:
                    decrypt_msg_tmp = []
                
                decrypted_message = self.apply_shift(26 - s)
                # now check if each word is a valid word
                for word in decrypted_message.split():
                    if ''.join(l.lower() for l in word if l not in string.punctuation + string.digits) in self.get_valid_words():
                        # append word to 'decrypt_msg_tmp'
                        decrypt_msg_tmp.append(word)
                        # if 's' value is 26, change it to '0' as a shift of 26 is the same thing as a shift of '0'
                        #if s == 26:
                        #    s = 0
                        # update shift_dict dictionary
                        if s not in shift_dict:
                            shift_dict[26-s] = [len(decrypt_msg_tmp)]
                        else:
                            shift_dict[s][0] = len(decrypt_msg_tmp)
                        # append another list for to put complete decrypt_msg_tmp
                        # try:
                        #     shift_dict[s][1].append(word)
                        # except IndexError:
                        #     shift_dict[s].append([])
                        #     shift_dict[s][1].append(word)
                        # finally:
                        #     shift_dict[s][1].append(word)
                    else:
                        #shift_dict[s][1].append(word)
                        next
                try:
                    shift_dict[26-s].append(decrypted_message)
                except KeyError:
                    pass
            count = 0

        best = ''.join([str(key) for key in shift_dict.keys() if shift_dict[key] == max(shift_dict.values())])
        return (best, ''.join(shift_dict[int(best)][1]))


#p = PlaintextMessage('Message    is    Nonsense     words: frequency fright ask disturb lose', 1)
p = PlaintextMessage('Message   is  Nonsense    words: funeral sew friendly composition diamond greet sad president ticket even prejudice soap move must wound rub belt so thank vain value clear veil staff damage citizen dress safe spin which level art gun urge comparison', 14)
#print(p.get_message_text_encrypted())
encrypt = p.get_message_text_encrypted()


# print(encrypt)
sup = CiphertextMessage(encrypt)
print(sup.decrypt_message())
# print(p.message_text)
# print('check if equal...')
# print(sup.decrypt_message()[1] == p.message_text)

# Problem 4 - Decrypt a Story. Basically, this problem wants us to create an CiphertextMessage object which 
# opens the 'story.txt' file and use decrypt_message() to decrypt it. we need to create a 'decrypt_story()' function.

def decrypt_story():
    text = get_story_string()
    o = CiphertextMessage(text)
    return o.decrypt_message()
#story = CiphertextMessage(open('story.txt', 'r').readline())
#story.decrypt_message()

print('problem 4...')
print(decrypt_story())