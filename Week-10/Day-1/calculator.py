import os

print(os.getcwd())
for x in range(5):
    os.mkdir(f'Week-'+str(x+11))
    for i in range(1,6):
        os.mkdir(f'Week-{x+11}/Day-{i}')
    