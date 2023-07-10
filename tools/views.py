from django.shortcuts import render

def home(request):
    return render(request, 'tools/home.html')

def reverse_string(request):
    return render(request, 'tools/reverse.html')

def split_string(request):
    return render(request, 'tools/split.html')

def join_string(request):
    return render(request, 'tools/join.html')

def sort_string(request):
    return render(request, 'tools/sort.html')

def slice_string(request):
    return render(request, 'tools/slice.html')

def lower2upper(request):
    return render(request, 'tools/lower2upper.html')

def upper2lower(request):
    return render(request, 'tools/upper2lower.html')

def remove_duplicate_words(request):
    return render(request, 'tools/duplicate_words.html')

def numbers2words(request):
    return render(request, 'tools/numbers2words.html')

def sentence_counter(request):
    return render(request, 'tools/sentence_counter.html')
