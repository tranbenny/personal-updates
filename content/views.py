from django.shortcuts import get_object_or_404, render


# Create your views here.
def list(request):
	return render(request, "updates/updates_list.html")