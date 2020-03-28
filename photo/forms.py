from django.forms import inlineformset_factory
from photo.models import Album, Photo

# 폼셋이란 동일한 폼 여러 개로 구성된 폼을 의미. 인라인 폼셋이란 메인 폼에 딸려 있는 하위 폼셋으로 테이블 간 관계가 1:N인 경우, N 테이블 레코드 여러개를 한꺼번에 입력받기 위한 폼으로 사용
PhotoInlineFormSet = inlineformset_factory(Album, Photo, fields = ['image', 'title', 'description'], extra = 2)