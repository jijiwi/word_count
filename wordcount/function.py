# from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return render(request, 'home.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)
    # 字频统计
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    # 字频排序
    sorted_dict = sorted(word_dict.items(), key= lambda w: w[1], reverse=True)
    # 传递到count页面
    return render(request, 'count.html', {'count': total_count,
                                          'text': user_text,
                                          'wordict': word_dict,
                                          'sorted': sorted_dict})


def about(request):

    return render(request, 'about.html')
