from django.shortcuts import render, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from Academy.models import Course, Section, Content, CoursePurchase, CourseCategory, BCSCourse, BCSSection, BCSContent, CourseOrder, CoursePackage, SubscriptionTeam


# Create your views here.

def academyHomeView(request):
    context = {

    }

    return render(request, 'academypages/index.html', context)


def ccspView(request,*args,**kwargs):   
    context = {

    }

    return render(request, 'academypages/pages/ccsp.html', context)


def academyFAQView(request,*args,**kwargs):
    context = {

    }

    return render(request, 'academypages/pages/academy_faq.html', context)


def corporateTrainingView(request,*args,**kwargs):
    context = {

    }

    return render(request, 'academypages/pages/corporate_training.html', context)


def lawEnforcementView(request,*args,**kwargs):
    context = {

    }

    return render(request, 'academypages/pages/law_enforcement.html', context)


def educationalInstituteView(request,*args,**kwargs):
    context = {

    }

    return render(request, 'academypages/pages/educational_institute.html', context)


# to get specific course material
def course_material(request, section, module, content_type):
    template_name = "user_panel/academy/files.html"

    section_no = int(section.split('-')[1])
    module_no = int(module.split('-')[1])

    section_no = 1 if section_no == 0 else section_no
    module_no = 1 if module_no == 0 else module_no

    if module_no > 3:
        section_no += 1
        module_no = 1

    content_type = 'instruction' if content_type == 'video' else 'video'

    print(section_no, module_no, content_type)
    return render(request, template_name,
                  {'content_type': content_type, 'section_no': section_no, 'module_no': module_no})


def UserExams(request):
    template_name = "user_panel/academy/exams.html"

    return render(request, template_name)


def UserEvents(request):
    template_name = "user_panel/academy/events.html"

    return render(request, template_name)


def UserNotifications(request):
    template_name = "user_panel/academy/notifications.html"

    return render(request, template_name)


def UserSettings(request):
    template_name = "user_panel/academy/settings.html"

    return render(request, template_name)


# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


# this function is to control the downloading system for pdf's.
def download_file(request, path=''):
    file_name = path
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/media/' + path
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % file_name
        return response
    except:
        return HttpResponse('File not found on the server.')


# bcs academy user panel
@login_required
def UserCourses(request):
    business_courses = BCSCourse.objects.all()
    personal_courses = Course.objects.all()
    context = {
        'business_courses': business_courses,
        'personal_courses': personal_courses,
    }

    return render(request, "user_panel/academy/courses.html", context)


@login_required
def myCourses(request):
    business_courses = SubscriptionTeam.objects.filter(user=request.user)
    personal_courses = CoursePurchase.objects.filter(user=request.user)

    context = {
        'business_courses': business_courses,
        'personal_courses': personal_courses,
    }

    return render(request, "user_panel/academy/mycourses.html", context)


@login_required
def UserCoursesDetails(request, id):
    try:
        course = Course.objects.get(id=id)
        course_type = 'pcs'
    except:
        course = BCSCourse.objects.get(id=id)
        course_type = 'bcs'

    context = {
        'course': course,
        'course_type': course_type,
    }

    return render(request, "user_panel/academy/details.html", context)



@login_required
def UserFiles(request, id):
    try:
        CoursePurchase.objects.get(user=request.user, course_id=id)
        course = Course.objects.get(id=id)
        # section = Section.objects.filter(course=course)
        contents = Content.objects.filter(section__course=course)
        paginator = Paginator(contents, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'course': course,
            'contents': contents,
            'content_type': 'instruction',
            'course_type': 'pcs',
            'section_no': 1,
            'module_no': 1,
            'page_obj': page_obj
        }

        return render(request, "user_panel/academy/files.html", context)
    except:
        try:
            course = BCSCourse.objects.get(id=id)
            # section = Section.objects.filter(course=course)
            contents = BCSContent.objects.filter(section__course=course)
            # for content in contents:
            #     print(content.course_video)
            paginator = Paginator(contents, 1)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'course': course,
                'contents': contents,
                'content_type': 'instruction',
                'course_type': 'bcs',
                'section_no': 1,
                'module_no': 1,
                'page_obj': page_obj
            }

            return render(request, "user_panel/academy/files.html", context)
        except:
            return HttpResponse('You are not authorized to view this page')
