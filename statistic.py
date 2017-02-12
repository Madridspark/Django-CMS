from central.models import StaticInfo

def counter(request):
    if not request.session.get('visited', False):
        info = StaticInfo.objects.all()[0]
        info.theVisits += 1
        info.save()
        request.session['visited'] = True