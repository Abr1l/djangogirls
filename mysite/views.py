from django.shortcuts import render

def post_list(request):
	return render(resquest, 'blog/post_list.html', {})
