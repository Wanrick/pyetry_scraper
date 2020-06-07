import os
import string


def merge_poems_by_poet(poet):
    poet_file = poet.lower().replace(' ', '-')
    with open(poet_file + '.txt', 'w') as outfile:
        for file in os.listdir("poetry/" + poet):
            if file.endswith(".txt"):
                with open("poetry/" + poet + "/" + file) as infile:
                    for line in infile:
                        outfile.write(line)


def create_poet_directory(poet):
    newdir = 'poetry/' + poet
    if not os.path.exists(newdir):
        os.makedirs(newdir)
        print("Directory ", newdir, " Created ")
    else:
        print("Directory ", newdir, " already exists")


def write_poems_to_single_file(poems):
    if poems is None:
        return
    poet = poems[0].poet
    create_poet_directory(poet)
    poet_file = poet.lower().replace(' ', '-')
    with open('poetry/' + poet + '/' + poet_file + '.txt', 'w') as outfile:
        for poem in poems:
            outfile.write(poem.poem_text + '\n\n')
        outfile.close()


def write_poems_to_files(poems):
    if poems is None:
        return

    for poem in poems:
        create_poet_directory(poem.poet)
        file = open(
            'poetry/' + poem.poet + '/' + poem.poem_title.translate(str.maketrans('', '', string.punctuation)) + '.txt',
            'w')
        file.write(poem.poem_text)
        file.close()
