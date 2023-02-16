from faker import Faker
fake = Faker()

# Writing fake names to the file
with open('output.txt', 'w') as f:
    for i in range(10):
       f.write(f'{fake.name()}\n')

# Reading from the file jsut created
for line in open('output.txt'):
    print(line)