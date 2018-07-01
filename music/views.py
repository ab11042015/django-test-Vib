# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# #from django.template import loader --> used in example 2
# from .models import Album
# from django.http import Http404
#
# def index(request):
#     all_albums = Album.objects.all()
#     #****************Example1******************
#     # html =''
#     # for album in All_albums:
#     #     url = '/music/'+str(album.id)+'/'
#     #     html += '<a href ="'+url+'">'+album.album_title+'</a><br>'
#     # return HttpResponse(html)---> This is a python way to do things
#     # ---Now it will be the HTML way
#     #********************Example2***************
#     # template = loader.get_template('music/index.html')
#     # context = {
#     #     'all_albums':all_albums,
#     # }
#     # return HttpResponse(template.render(context,request))
#
#     #context = {'all_albums':all_albums} is substuted as no need
#     return render(request,'music/index.html',{'all_albums':all_albums})
#
# def detail(request,album_id):
#     # try:
#     #     album=Album.objects.get(pk=album_id)
#     #     #songs= album.song_set.all()
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
#     # # context = {
#     # #     'album':album,
#     # #     'songs':songs,
#     # # }
#     album= get_object_or_404(Album,pk=album_id)
#     return render(request,'music/detail.html',{'album':album})
#
# def favorite(request,album_id):
#     album= get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/details.html',{
#         'album':album,
#         'error_message':'You did not select a valid song',
#         })
#     else:
#         selected_song.is_favorite=True
#         selected_song.save()
#         return render(request,'music/detail.html',{'album':album})
from django.views import generic
from .models import Album, Song
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from django.template import loader --> used in example 2
from .models import Album
from django.http import Http404

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'All_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model =Album
    template_name = 'music/detail.html'

def favorite(request,album_id):
    album= get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html',{
        'album':album,
        'error_message':'You did not select a valid song',
        })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})
