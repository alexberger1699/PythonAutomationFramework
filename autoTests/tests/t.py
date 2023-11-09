import random
import string



random_email_string_length = 3

random_email = ''.join(random.choices(string.ascii_lowercase, k = random_email_string_length))

print(random_email)


rand_pssw_length = 20

rand_pssw = ''.join(random.choices(string.ascii_letters, k = rand_pssw_length))

print(rand_pssw)

rand_info = {'email':random_email, 'password':rand_pssw}

print(f'this is dictionary: {rand_info}')


m = 10

mn = ''.join(random.choices(string.ascii_letters, k=m))

print(f'second is dictionary: {mn}')



##