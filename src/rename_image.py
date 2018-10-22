import os


for i, filename in enumerate(os.listdir(".")):
    print(str(filename))
    if filename.startswith('frame'):
        if filename.endswith('.' + 'png'):
            os.rename(filename, str(i) + ".png")
