from django.contrib import admin
from shortNotes.models import ShortNotes, ShortNotesType, ShortNotesModuleType


class ShortNotesAdmin(admin.ModelAdmin):
    pass


class ShortNotesTypeAdmin(admin.ModelAdmin):
    pass


class ShortNotesModuleTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShortNotes, ShortNotesAdmin)
admin.site.register(ShortNotesType, ShortNotesTypeAdmin)
admin.site.register(ShortNotesModuleType, ShortNotesModuleTypeAdmin)
