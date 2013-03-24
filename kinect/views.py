# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from kinect.models import Player, Session, SessionData, Asset

def dashboard(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render_to_response('index.html',{'player': player},context_instance=RequestContext(request))

def simpleemotion(request):
    player = get_object_or_404(Player, pk=request.GET.get('player', ''))
    session = get_object_or_404(Session, pk=request.GET.get('session', ''))
    data = request.GET.get('data', '')
                                   
    obj = SessionData(session=session, data_name="simpleemotion", data_type="SEJ", url=data)
    obj.save()
    return HttpResponse("OK")
