from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'world'
    return render(request, 'base.html' , {'name': name})

def book_search(request):
    search_text = request.GET.get('search', '')
    return render(request, 'search-results.html', {'search_text': search_text})

def survey(request):
    question = 'question 1'
    answer = 'answer 1'
    list_answer = [i for i in range(1, 4)]
    return render(request, 'survey/index.html', {
        'question': question,
        'answer': answer,
        'list_answer': list_answer}
    )