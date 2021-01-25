username = input()
password = input()
input_pass = input()

while input_pass != password:
    input_pass = input()

print(f'Welcome {username}!')