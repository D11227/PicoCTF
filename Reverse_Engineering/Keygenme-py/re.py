import hashlib

key = 'picoCTF{1n_7h3_|<3y_of_'
username_trial = 'PRITCHARD'

for i in [4, 5, 3, 6, 2, 7, 1, 8]:
    key += hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[i]

print(key + '}')
