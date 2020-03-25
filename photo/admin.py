from django.contrib import admin
from photo.models import Album, Photo

# p.199 ~ 200

class PhotoInline(admin.StackedInline): # StackedInline은 세로로 나열되는 형식으로 보여줌 TabularInline은 테이블 모양처럼 행으로 나열되는 형식으로 보여줌
    model = Photo # 추가로 보여주는 것은 Photo 테이블
    extra = 2 # 이미 존재하는 객체 외에 추가로 입력할 수 있는 Photo 테이블 객체의 수는 2개

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,) # 앨범 객체 수정 화면을 보여줄 때 PhotoInline 클래스에서 정의한 사항을 같이 보여줌
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')