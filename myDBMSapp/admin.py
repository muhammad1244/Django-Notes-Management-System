from django.contrib import admin

from .models import *


# Register your models here.


# registrations make your model show on ADMIN PAGE, bao rami seen yaani k xD
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Courses)
admin.site.register(ContributionFileType)
admin.site.register(Contributions)
