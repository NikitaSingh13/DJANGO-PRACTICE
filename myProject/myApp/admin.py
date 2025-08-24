from django.contrib import admin
from .models import myUsers, myUserReview

#admin.py use karke tum kisi bhi model ko attach kar sakte ho aur admin mein dekh sakte ho 
# Register your models here.

class myUserReviewInLine(admin.TabularInline):
    model = myUserReview

class myUsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'date_addeed')
    inlines = [myUserReviewInLine]

admin.site.register(myUsers)
