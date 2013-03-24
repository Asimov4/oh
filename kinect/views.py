# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from kinect.models import Player, Session, SessionData, Asset

def player(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render_to_response('player.html',{'player': player},context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html',{},context_instance=RequestContext(request))

def simpleemotion(request):
    player = get_object_or_404(Player, pk=request.GET.get('player', ''))
    session = get_object_or_404(Session, pk=request.GET.get('session', ''))
    data = request.GET.get('data', '')
                                   
    obj = SessionData(session=session, data_name="simpleemotion", data_type="SEJ", url=data)
    obj.save()
    return HttpResponse("OK")

def emotiongraph(request,player_id,session_id):
    output = ""
    session_data = SessionData.objects.all().filter(session=session_id)
    for data in session_data:
        output += data.url
    return HttpResponse("OK" + output)
