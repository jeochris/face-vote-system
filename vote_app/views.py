from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import PersonalAnswer
import glob

FRONT_IMG = 2000
LEFT_IMG = 800
RIGHT_IMG = 800

def index(request):
    cur_vote_count = len(PersonalAnswer.objects.all())
    if cur_vote_count < FRONT_IMG:
        return redirect(f'/front/{cur_vote_count+1}')
    elif cur_vote_count < FRONT_IMG + LEFT_IMG:
        return redirect(f'/left/{cur_vote_count+1-FRONT_IMG}')
    elif cur_vote_count < FRONT_IMG + LEFT_IMG + RIGHT_IMG:
        return redirect(f'/right/{cur_vote_count+1-FRONT_IMG-LEFT_IMG}')
    else:
        return HttpResponse('<h1>Vote Finish!</h1>')

@csrf_exempt
def front(request, id):

    if request.method == 'GET':
        imgs_path_list = glob.glob(f'static/front/comp{id}/*')
        real_imgs_path_list = []
        for img_path in imgs_path_list:
            real_imgs_path_list.append("/".join(img_path.split('/')[1:]))

        context = {'cur_page': id, 'votelist': real_imgs_path_list}
        return render(request, 'vote_app/front_display.html', context)

    elif request.method == 'POST':
        q = PersonalAnswer(direction = 'front', count = int(id), score = int(request.POST.get('score')))
        q.save()
        nextId = int(id)+1

        if nextId <= FRONT_IMG:
            return redirect(f'/front/{nextId}')
        else:
            return redirect('/')

@csrf_exempt
def left(request, id):

    if request.method == 'GET':
        imgs_path_list = glob.glob(f'static/left/comp{id}/*')
        real_imgs_path_list = []
        for img_path in imgs_path_list:
            real_imgs_path_list.append("/".join(img_path.split('/')[1:]))

        context = {'cur_page': id, 'votelist': real_imgs_path_list}
        return render(request, 'vote_app/left_display.html', context)

    elif request.method == 'POST':
        q = PersonalAnswer(direction = 'left', count = int(id), score = int(request.POST.get('score')))
        q.save()
        nextId = int(id)+1

        if nextId <= LEFT_IMG:
            return redirect(f'/left/{nextId}')
        else:
            return redirect('/')

@csrf_exempt
def right(request, id):

    if request.method == 'GET':
        imgs_path_list = glob.glob(f'static/right/comp{id}/*')
        real_imgs_path_list = []
        for img_path in imgs_path_list:
            real_imgs_path_list.append("/".join(img_path.split('/')[1:]))

        context = {'cur_page': id, 'votelist': real_imgs_path_list}
        return render(request, 'vote_app/right_display.html', context)

    elif request.method == 'POST':
        q = PersonalAnswer(direction = 'right', count = int(id), score = int(request.POST.get('score')))
        q.save()
        nextId = int(id)+1

        if nextId <= RIGHT_IMG:
            return redirect(f'/right/{nextId}')
        else:
            return redirect('/')