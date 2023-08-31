import string
import random
from csv import writer

def pwgen():
    str1 = string.ascii_lowercase
    str2 = string.ascii_uppercase
    str3 = string.digits
    str4 = string.punctuation

    pf = input("Enter the Platform: \n")
    length = int(input("Length of the password: \n"))

    # Ensure the password length is sufficient to include at least one character from each category
    if length < 4:
        print("Password length should be at least 4 characters.")
        return

    # Number of characters needed from each category
    lowercase_count = 1
    uppercase_count = 1
    digit_count = 1
    punctuation_count = 1
    remaining_count = length - (lowercase_count + uppercase_count + digit_count + punctuation_count)

    # Select characters from each category
    lowercase_chars = random.sample(str1, lowercase_count)
    uppercase_chars = random.sample(str2, uppercase_count)
    digit_chars = random.sample(str3, digit_count)
    punctuation_chars = random.sample(str4, punctuation_count)
    remaining_chars = random.sample(str1 + str2 + str3 + str4, remaining_count)

    # Combine characters from all categories
    all_chars = lowercase_chars + uppercase_chars + digit_chars + punctuation_chars + remaining_chars

    # Shuffle the combined characters
    random.shuffle(all_chars)

    # Generate the password
    pw = "".join(all_chars)
    pwdata = [pf, pw]

    with open('pwlist.csv', 'a') as f:
        wdata = writer(f)
        wdata.writerow(pwdata)

pwgen()


'''import string
import random
from csv import writer

#head = ['Platform', 'Password']

#with open('pwlist.csv','w') as f:
    #wdata = writer(f)
    #wdata.writerow(head)

def pwgen():
    str1 = string.ascii_lowercase
    str2 =  string.ascii_uppercase
    str3 = string.digits
    str4 = string.punctuation
    
    pf = input("Enter the Platform: \n")
    length = int(input("Length of the password: \n"))
    
    
    p = []
    p.extend(list(str1))
    p.extend(list(str2))
    p.extend(list(str3))
    p.extend(list(str4))
    random.shuffle(p)
    pw = ("".join(p[0:length]))
    #print(pw)
    pwdata = [pf,pw]
    with open('pwlist.csv','a') as f:
        wdata = writer(f)
        wdata.writerow(pwdata)
    
pwgen()'''



