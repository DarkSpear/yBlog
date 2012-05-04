from django.core.paginator import Paginator, InvalidPage, EmptyPage
from frontend.models import Record, Category
from django.shortcuts import render_to_response


# Output the list of post
# If a user pics a category the list filters by it
# If a user searches something the list filters by it
def listing(request):
    categories = Category.objects.all()
    last_posts = Record.objects.order_by('-pub_date')[:3]

    if request.GET.get('cat'):
        blog_list = Record.objects.filter(category=request.GET.get('cat')).order_by('-pub_date')
    elif request.GET.get('search_button'):
        blog_list = Record.objects.filter(text__contains=str(request.GET.get('search_string'))).order_by('-pub_date')
    else:
        blog_list = Record.objects.order_by('-pub_date')
        
    paginator = Paginator(blog_list, 5)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        blog_posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        blog_posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/list.html', {"blog_posts": blog_posts, 'categories': categories, 'last_posts': last_posts,})

def details(request):
    categories = Category.objects.all()
    last_posts = Record.objects.order_by('-pub_date')[:3]

    try:
        blog_post_details = Record.objects.get(id = request.GET['id'])
    except ValueError:
        raise Http404()


    return render_to_response('blog/details.html', {'blog_post_details': blog_post_details, 'categories': categories, 'last_posts': last_posts})