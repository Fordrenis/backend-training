from django.shortcuts import render, HttpResponseRedirect


def add_to_file(word1: str, word2: str):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file():
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return words1, words2


def home(request):
    return render(request, 'home.html')


def wordlist(request):
    sp = read_from_file()
    sp_original = sp[0]
    sp_translate = sp[1]
    sp_norm = []
    for i in range(len(sp_original)):
        sp_norm += [[sp_original[i], sp_translate[i]]]
    return render(request, 'wrdlist.html', {'spk': sp_norm})


def addword(request):
    if request.method == 'POST':
        add_to_file(request.POST['word1'], request.POST['word2'])
        return HttpResponseRedirect('/')
    return render(request, 'addword.html')

