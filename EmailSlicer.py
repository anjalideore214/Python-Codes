email=input("Enter your Email:" ).strip()

username=email[:email.index('@')]
domain=email[email.index('@') +1:]

print(f"Your Username is {username} & Domain is {domain}")