from django.db import models
from Account.models import User
from tinymce.models import HTMLField
from BusinessSecurity.models import Business
import cv2
from django.core.validators import FileExtensionValidator

# Create your models here.
duration = (
    ('one_month', 'One Month'),
    ('two_months', 'Two Months'),
    ('three_months', 'Three Months'),
    ('six_months', 'Six Months'),
    ('one_year', 'One Year'),
)

duration_type = (
    ('month', 'Month'),
    ('year', 'Year'),
)

course_type = (
    ('Business', 'Business'),
    ('Personal', 'Personal'),
)


class CourseCategory(models.Model):
    course_type = models.CharField(max_length=264, choices=course_type)
    category_name = models.CharField(max_length=264)

    def __str__(self):
        return f'{self.course_type} - {self.category_name}'


class Course(models.Model):
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='course_coursecategory')
    course_type = models.CharField(max_length=264, choices=course_type)
    course_name = models.CharField(max_length=264)
    duration = models.CharField(max_length=264, choices=duration)
    price = models.IntegerField()
    short_description = models.TextField(max_length=1000)
    long_description = HTMLField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = 'Courses'


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='section_course')
    section_name = models.CharField(max_length=264)

    def __str__(self):
        return self.section_name


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='content_section')
    lecture_name = models.CharField(max_length=264)
    text_instruction = models.FileField(upload_to='course/', validators=[FileExtensionValidator(['txt'])],
                                        help_text='(Supported Format: .txt)')
    course_video = models.FileField(upload_to='course/', validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'ogv',
                                                                                             'mkv', 'webm'])],
                                    help_text='(Video File Only)')
    preview_video = models.FileField(upload_to='course/',
                                     blank=True, null=True,
                                     validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'ogv',
                                                                         'mkv', 'webm'])],
                                     help_text='(Video File Only)')
    resource_file = models.FileField(upload_to='course/', validators=[FileExtensionValidator(['pdf'])],
                                     help_text='(Supported Format: .pdf)')

    def __str__(self):
        return self.lecture_name

    def get_duration(self):
        filename = self.course_video.url

        cap = cv2.VideoCapture(filename[1:])
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        minutes = int(duration / 60)
        seconds = int(duration % 60)

        cap.release()
        return str(minutes) + ':' + str(seconds) + ' m'


class CoursePurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coursepurchase_user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coursepurchase_course')
    paypal_id = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.full_name} - {self.course.course_name}'


class BCSCourse(models.Model):
    product_id = models.CharField(max_length=255)
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE,
                                        related_name='bcscourse_coursecategory')
    # course_type = models.CharField(max_length=264, choices=course_type)
    course_name = models.CharField(max_length=264)
    short_description = models.TextField(max_length=1000)
    long_description = HTMLField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class BCSSection(models.Model):
    course = models.ForeignKey(BCSCourse, on_delete=models.CASCADE, related_name='bcssection_bcscourse')
    section_name = models.CharField(max_length=264)

    def __str__(self):
        return self.section_name


class BCSContent(models.Model):
    section = models.ForeignKey(BCSSection, on_delete=models.CASCADE, related_name='bcscontent_bcssection')
    lecture_name = models.CharField(max_length=264)
    text_instruction = models.FileField(upload_to='course/', validators=[FileExtensionValidator(['txt'])],
                                        help_text='(Supported Format: .txt)')
    course_video = models.FileField(upload_to='course/', validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'ogv',
                                                                                             'mkv', 'webm'])],
                                    help_text='(Video File Only)')
    preview_video = models.FileField(upload_to='course/',
                                     blank=True, null=True,
                                     validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'ogv',
                                                                         'mkv', 'webm'])],
                                     help_text='(Video File Only)')
    resource_file = models.FileField(upload_to='course/', validators=[FileExtensionValidator(['pdf'])],
                                     help_text='(Supported Format: .pdf)')

    def __str__(self):
        return self.lecture_name

    def get_duration(self):
        filename = self.course_video.url

        cap = cv2.VideoCapture(filename[1:])
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        minutes = int(duration / 60)
        seconds = int(duration % 60)

        cap.release()
        return str(minutes) + ':' + str(seconds) + ' m'


class CoursePackage(models.Model):
    service_id = models.ForeignKey(BCSCourse, on_delete=models.CASCADE, related_name='coursepackage_bcscourse')
    package_id = models.CharField(max_length=255, blank=True)
    package_name = models.CharField(
        max_length=264, verbose_name='Package Name')
    duration = models.IntegerField()
    duration_type = models.CharField(
        choices=duration_type, max_length=264, default='month')
    price = models.IntegerField()
    max_user = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.package_name} - {self.service_id}'


class PackageFeatures(models.Model):
    package = models.ForeignKey(
        CoursePackage, on_delete=models.CASCADE, related_name='packagefeature_coursepackage')
    feature_name = models.CharField(
        max_length=264, verbose_name='Feature Name')
    feature = models.CharField(
        max_length=264, verbose_name='Feature')

    def __str__(self):
        return f'{self.feature_name} - {self.feature}'


class CourseOrder(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE,
                                 related_name='courseorder_business')
    course = models.ForeignKey(BCSCourse, on_delete=models.CASCADE,
                               related_name='courseorder_bcscourse')
    course_package = models.ForeignKey(CoursePackage, on_delete=models.CASCADE,
                                       related_name='courseorder_coursepackage')
    # paypal_email = models.EmailField()
    paypal_id = models.CharField(max_length=255)
    # paypal_user_name = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    # update_time = models.DateTimeField()
    amount = models.IntegerField()
    # currency = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)

    @property
    def total_count(self):
        return self.subscriptionteam_courseorder.filter(subscription_order_id=self.id).count()

    def __str__(self):
        return f'{self.business} - {self.course} - {self.course_package} - {self.is_active}'


class SubscriptionTeam(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='course_subscriptionteam_business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_subscriptionteam_user')
    subscription_order = models.ForeignKey(CourseOrder, on_delete=models.CASCADE,
                                           related_name='subscriptionteam_courseorder')
