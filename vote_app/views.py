from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import PersonalAnswer
import glob

page = {
    'watchlist': [
        {'direction': 'front'},
        {'direction': 'left'},
        {'direction': 'right'}
    ]
}

FRONT_IMG = 2
LEFT_IMG = 2
RIGHT_IMG = 2

def index(request):
    global page
    return render(request, 'vote_app/index.html', page)

@csrf_exempt
def front(request, id):
    global page

    if request.method == 'GET':
        imgs_path_list = glob.glob(f'static/front/comp{id}/*')
        real_imgs_path_list = []
        for img_path in imgs_path_list:
            real_imgs_path_list.append(img_path.split('\\')[-1])

        context = {'cur_page': id, 'votelist': real_imgs_path_list}
        return render(request, 'vote_app/front_display.html', context)

    elif request.method == 'POST':
        q = PersonalAnswer(direction = 'front', count = int(id), score = int(request.POST.get('score')))
        q.save()
        nextId = int(id)+1

        if nextId <= FRONT_IMG:
            return redirect(f'/front/{nextId}')
        else:
            del page['watchlist'][0]
            return redirect('/')

@csrf_exempt
def left(request, id):
    global page

    if request.method == 'GET':
        imgs_path_list = glob.glob(f'static/left/comp{id}/*')
        real_imgs_path_list = []
        for img_path in imgs_path_list:
            real_imgs_path_list.append(img_path.split('\\')[-1])

        context = {'cur_page': id, 'votelist': real_imgs_path_list}
        return render(request, 'vote_app/left_display.html', context)

    elif request.method == 'POST':
        q = PersonalAnswer(direction = 'left', count = int(id), score = int(request.POST.get('score')))
        q.save()
        nextId = int(id)+1

        if nextId <= LEFT_IMG:
            return redirect(f'/left/{nextId}')
        else:
            del page['watchlist'][0]
            return redirect('/')

@csrf_exempt
def right(request, id):
    global page

    if request.method == 'GET':
        imgs_path_list = glob.glob(f'static/right/comp{id}/*')
        real_imgs_path_list = []
        for img_path in imgs_path_list:
            real_imgs_path_list.append(img_path.split('\\')[-1])

        context = {'cur_page': id, 'votelist': real_imgs_path_list}
        return render(request, 'vote_app/right_display.html', context)

    elif request.method == 'POST':
        q = PersonalAnswer(direction = 'right', count = int(id), score = int(request.POST.get('score')))
        q.save()
        nextId = int(id)+1

        if nextId <= RIGHT_IMG:
            return redirect(f'/right/{nextId}')
        else:
            del page['watchlist'][0]
            return redirect('/')