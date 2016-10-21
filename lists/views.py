<<<<<<< HEAD
=======
from django.http import HttpResponse
>>>>>>> mixedupstuff
from django.shortcuts import render

# Create your views here.
def home_page(request):
<<<<<<< HEAD
	return render(request, 'home.html')
=======
	return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
>>>>>>> mixedupstuff
