from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required


# Create your views here.
def signupfunc(request):
  # どこでシングルクォーテーションつけるべきかわからなくなる
  if request.method == 'POST':
    username2 = request.POST['username']
    password2 = request.POST['password']
    try:
      User.objects.get(username = username2)
      return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})
    except:
      user = User.objects.create_user(username2, '', password2)
    # この状態でサーバーを立ち上げてもno such table: auth_userエラーが出る。なぜならuserモデルはデフォルトで用意されているがuserテーブルが作られていないからだ。（makemigrations,migrate）
    # ここまででユーザ登録の実装をすることができた
      return render(request, 'signup.html', {'some': 100})
  return render(request, 'signup.html', {'some': 100})

def loginfunc(request):
  if request.method == 'POST':
    username2 = request.POST['username']
    password2 = request.POST['password']
    user = authenticate(request, username=username2, password=password2)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('list')
    else:
        # Return an 'invalid login' error message.
        return redirect('login')
  return render(request, 'login.html')

@login_required
def listfunc(request):
  # データベースのデータを使うにはこの宣言が必要、これでlist.htmlのほうでデータの表示をすることができる
  object_list = BoardModel.objects.all()
  return render(request, 'list.html', {'object_list': object_list})

@login_required
def logoutfunc(request):
  logout(request)
  # Redirect to a success page.
  return redirect('login')

@login_required
def detailfunc(request, pk):
  object = BoardModel.objects.get(pk = pk)
  return render(request, 'detail.html', {'object':object})

@login_required
def goodfunc(request, pk):
  post = BoardModel.objects.get(pk = pk)
  post.good += 1
  post.save()
  # postをcontextとして返さなくていいのか
  return redirect('list')

    