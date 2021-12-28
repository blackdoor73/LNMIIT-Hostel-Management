from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

from django.db.models import F
admin.site.site_header = 'LNMIIT Hostel Admin Panel'
admin.site.unregister(Group)


def update_status():
    students = Student.objects.all()
    room_id = {}
    for student in students:
        room_id[student.room.id] = room_id.get(student.room.id, 0) + 1
    rooms = Room.objects.all()
    for room in rooms:
        room.status = room_id.get(room.id, 0)
        room.save()


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('hostel_number', 'warden')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hostel_number', 'wing', 'floor', 'room_num', 'capacity', 'status')
    list_filter = ('capacity', 'status', 'hostel', 'wing', 'floor')
    search_fields = ['room_num']

    def hostel_number(self, obj):
        return obj.hostel.hostel_number


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_num', 'name', 'room', 'mail',
                    'student_contact_num', 'guardian_contact_num', 'gender')
    search_fields = ['roll_num__username', 'first_name', 'last_name', 'room__room_num']
    list_filter = ('room__hostel__hostel_number', 'room__wing', 'room__floor')
    raw_id_fields = ('room', 'roll_num', )

    def name(self, obj):
        return str(obj.first_name) + ' ' + str(obj.last_name)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "room":
    #         kwargs["queryset"] = Room.objects.filter(status__lt=F('capacity'))
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        super(StudentAdmin, self).save_model(request, obj, form, change)
        update_status()


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('hostel_number', 'feedback', 'date')
    date_hierarchy = 'date'

    def hostel_number(self, obj):
        return obj.hostel.hostel_number

    def has_add_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(FeedbackAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'complaint', 'date')
    date_hierarchy = 'date'

    def room(self, obj):
        return obj.student.room

    def has_add_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ComplaintAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


@admin.register(ChangeRoom)
class ChangeRoomAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'reason', 'date')
    date_hierarchy = 'date'

    def room(self, obj):
        return obj.student.room

    def has_add_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ChangeRoomAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'txtReport')
    date_hierarchy = 'date'

         
