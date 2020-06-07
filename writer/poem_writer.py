import os
import string


def create_poet_directory(poet):
    newdir = 'poetry/' + poet
    if not os.path.exists(newdir):
        os.makedirs(newdir)
        print("Directory ", newdir, " Created ")
    else:
        print("Directory ", newdir, " already exists")


def write_poems_to_single_file(poems):
    pass


def write_poems_to_files(poems):
    if poems is None:
        return

    for poem in poems:
        create_poet_directory(poem.poet)
        file = open('poetry/' + poem.poet + '/' + poem.poem_title.translate(str.maketrans('', '', string.punctuation)) + '.txt',
                    'w')
        file.write(poem.poem_text)
        file.close()
