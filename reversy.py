def encrypt (data):
    data = input( "What is the password that you want to encrypt? ")
    reversed_data = data[::-1]
    print(reversed_data)

encrypt("123")