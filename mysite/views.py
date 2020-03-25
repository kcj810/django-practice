from django.views.generic import TemplateView
from django.views.generic import CreateView # 이 뷰는 테이블에 새로운 레코드를 생성하기 위해 이에 필요한 폼을 보여주고, 폼에 입력된 데이터로 테이블의 레코드를 생성해주는 뷰
from django.contrib.auth.forms import UserCreationForm # User 모델의 객체를 생성하기 위해 보여주는 폼
from django.urls import reverse_lazy # 인자로 URL 패턴명을 받는다. 패턴명을 인식하기 위해 urls.py 모듈이 메모리에 로딩돼야 함
from django.contrib.auth.mixins import AccessMixin # 뷰 처리 진입 단계에서 적절한 권한을 갖추었는지 판별할때 사용하는 믹스인 클래스

# chapter 03 p.106
class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView): # 적절한 폼을 보여주고, 폼에 입력된 내용에서 에러 여부를 체크한 후 에러가 없으면 입력된 내용으로 테이블에 레코드를 생성
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)