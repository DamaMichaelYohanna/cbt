from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from gallary.models import Post
from gallary.forms import Image_upload_form,CommentForm,MessageForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def Homepage(request):
	object_list = Post.objects.all()
	first_three = object_list[:2]
	paginator = Paginator(object_list, 12) # 12 posts in each page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		Upload_form = Image_upload_form(request.POST)
		if Upload_form.is_valid():
			print('form is valid')
			Upload_form.save()
		else:
			Upload_form = Image_upload_form()
			print('form gad some issue')
	else:
		Upload_form = Image_upload_form

	context = {'object_list':object_list,'form':Upload_form,'page':page,
					'posts':posts,'recent':first_three}
	return render(request,'post_list.html',context)


class Details(generic.DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'post_details.html'


def index(request):
	object_list = Post.objects.filter(category='published')
	paginator = Paginator(object_list,5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		Upload_form = Image_upload_form(request.POST)
		if Upload_form.is_valid():
			print('form is valid')
			Upload_form.save()
		else:
			Upload_form = Image_upload_form()
			print('form gad some issue')
	else:
		Upload_form = Image_upload_form
	context = {'objects':posts,'page':page,'Upload_form':Upload_form}
	return render(request,"index.html",context)

def Info(request,pk):
	"""this class handle the detail of each post and is a
		"""
	post_info = Post.objects.get(pk=pk)
	comments = post_info.comments.filter(active=True)
	comment = None
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit = False)
			new_comment.post = post_info
			new_comment.save()
			messages.success(request,'Your comment was posted')
			return redirect('/gallary/index/'+str(pk)+'/')
		else:
			comment_form = CommentForm()
	else:
		print('not a post method')
		comment_form = CommentForm()

	context = {'post':post_info,'comment_form':comment_form,'comments':comments}
	return render(request,'info.html',context)

def contact_us(request):

	if request.method == "POST":
		message = MessageForm(request.POST)
		if message.is_valid():
			print('every thing is good')
		else:
			message = MessageForm()
	else:
		message = MessageForm()
	context = {'form':message}
	print(message)
	return render(request,'contact.html',context)

@login_required(login_url = '/gallary/login/')
def upload(request):
	if request.method =="POST":
		upload_form = Image_upload_form(request.POST,request.FILES)
		if upload_form.is_valid():
			upload_form.save()
			messages.success(request,'Your post was uploaded successfully. ')
			return redirect('/gallary/upload/')
		else:
			upload_form = Image_upload_form()
			print('we gad issue')
	else:
		upload_form = Image_upload_form()
	context = {'upload_form':upload_form}
	return render(request,'upload.html',context)


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(
			user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			return render(request,'register_done.html',)
		else:
			user_form = UserRegistrationForm()
	else:
		user_form = UserRegistrationForm()
	return render(request,'register.html',{'form': user_form})
