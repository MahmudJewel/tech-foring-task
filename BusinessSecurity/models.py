from distutils.command.upload import upload
from xml.sax import default_parser_list
from django.db import models
from tinymce.models import HTMLField
from Account.models import User
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from timezone_field import TimeZoneField
from django.core.validators import FileExtensionValidator


# Create your models here.

class NewsSubscriber(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


category_choice = (
    ('bcs', 'BCS'),
    ('pcs', 'PCS'),
)


class ServiceCategory(models.Model):
    category_choice = models.CharField(choices=category_choice, max_length=255)
    category_name = models.CharField(
        max_length=264, verbose_name='Category Name')

    # category_description = models.TextField(max_length=1000, verbose_name='Category Description')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Service Categories'


class SubscriptionServices(models.Model):
    category_choice = models.CharField(choices=category_choice, max_length=255)
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name='subscription_service_category')
    product_id = models.CharField(max_length=255, blank=True)

    service_icon = models.ImageField(
        upload_to='service_icon/', verbose_name='Service Icon')
    service_title = models.CharField(
        max_length=264, verbose_name='Service Title')
    short_description = models.TextField(
        max_length=1000, verbose_name='Short Description')
    service_header = HTMLField(verbose_name='Service Header', blank=True)
    service_body = HTMLField(verbose_name='Service Body', blank=True)
    service_footer = HTMLField(verbose_name='Service Footer', blank=True)
    total_customer = models.IntegerField(
        verbose_name='Total Customer', default=0, blank=True)

    def __str__(self):
        return self.service_title + '-' + self.category_choice

    class Meta:
        verbose_name_plural = 'Subscription Services'


class Service(models.Model):
    category_choice = models.CharField(choices=category_choice, max_length=255)
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name='service_category')
    service_icon = models.ImageField(
        upload_to='service_icon/', verbose_name='Service Icon')
    service_title = models.CharField(
        max_length=264, verbose_name='Service Title')
    short_description = models.TextField(
        max_length=1000, verbose_name='Short Description')
    service_header = HTMLField(verbose_name='Service Header', blank=True)
    service_body = HTMLField(verbose_name='Service Body', blank=True)
    service_footer = HTMLField(verbose_name='Service Footer', blank=True)
    has_sub_service = models.BooleanField(
        default=True, verbose_name='Has Sub Services')
    is_subscription_based = models.BooleanField(
        default=False, verbose_name='Is Subscription Based')
    total_customer = models.IntegerField(
        verbose_name='Total Customer', default=0, blank=True)

    def __str__(self):
        return self.service_title + '-' + self.category_choice

    class Meta:
        verbose_name_plural = 'Services'


class ServiceAssigned(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='service_assigned_user')
    service = models.ManyToManyField(
        Service, related_name='service_assigned_service')

    class Meta:
        verbose_name_plural = 'Service Assigned'


class Tracking(models.Model):
    service = models.OneToOneField(
        Service, on_delete=models.CASCADE, related_name='tracking_service')
    persons = models.TextField(blank=True)


input_type = (
    ('text', 'text'),
    ('number', 'number'),
    ('file', 'file'),
    ('select', 'select'),
)


class InputFields(models.Model):
    type = models.CharField(max_length=264, choices=input_type)
    # name = models.CharField(max_length=264, blank=True, null=True)
    placeholder = models.CharField(max_length=264, blank=True, null=True)

    def __str__(self):
        return f'{self.type} - {self.placeholder}'

    class Meta:
        verbose_name_plural = 'Input Fields'


class SelectChoice(models.Model):
    choices = models.CharField(max_length=255)

    def __str__(self):
        return self.choices


class SelectChoiceRelation(models.Model):
    input_field = models.ForeignKey(InputFields, on_delete=models.CASCADE,
                                    related_name='selectchoicerelation_inputfield')
    choice_field = models.ManyToManyField(
        SelectChoice, related_name='selectchoicerelation_selectchoice')

    def __str__(self):
        return f'{self.input_field.type} - {self.input_field.placeholder}'


class SubService(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='subservice_service')
    fields = models.ManyToManyField(
        InputFields, related_name='subservice_inputfields', through='SubServiceInput')
    title = models.CharField(max_length=264, verbose_name='Title')
    # description = models.TextField(verbose_name='Description')
    total_customer = models.IntegerField(
        verbose_name='Total Customer', default=0, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub Services'


class SubServiceInput(models.Model):
    subservice = models.ForeignKey(
        SubService, on_delete=models.CASCADE, related_name='subserviceinput_subservice')
    inputfield = models.ForeignKey(
        InputFields, on_delete=models.CASCADE, related_name='subserviceinput_inputfield')

    # input_value = models.CharField(max_length=264, blank=True, null=True)

    class Meta:
        db_table = 'BusinessSecurity_subservice_inputfields'


class UserSubserviceInput(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_subservice_input')
    inputfield = models.ForeignKey(
        SubServiceInput, on_delete=models.CASCADE, related_name='inputfield_input')
    inputinfo = models.CharField(max_length=255)


duration_type = (
    ('month', 'Month'),
    ('year', 'Year'),
)

order_status = (
    ('new', 'New'),
    ('assigned', 'Assigned'),
    ('attending', 'Attending'),
    ('uploaded', 'Uploaded'),
    ('agreed_to_nda_nca', 'Agreed To NDA/NCA'),
    ('disagreed', 'Disagreed'),
    ('on_progress', 'On Progress'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
)

payment_method = (
    ('paypal', 'Paypal'),
    ('bank_check', 'Bank Check'),
    ('card', 'Card'),
    ('cash', 'Cash'),
    ('wire_transfer', 'Wire Transfer'),
)


class Order(models.Model):
    category_choice = models.CharField(choices=category_choice, max_length=255)
    subserviceinput = models.ManyToManyField(
        UserSubserviceInput, related_name='order_subservice')
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='order_service')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order_user')
    order_status = models.CharField(
        max_length=250, choices=order_status, default='new')
    order_date = models.DateTimeField(auto_now_add=True)
    # price = models.PositiveIntegerField(default=0)
    # payment_method = models.CharField(choices=payment_method, max_length=255)


agreement = (
    ('agree', 'Agree'),
    ('disagree', 'Disagree'),
)


class Quotation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='quotation_order')
    nda_and_nca = models.FileField(upload_to='nda/', blank=True, null=True, validators=[FileExtensionValidator(['pdf'])],
                           help_text='(Supported Format: .pdf)')
    invoice = models.FileField(upload_to='invoice/', blank=True, null=True, validators=[FileExtensionValidator(['pdf'])],
                           help_text='(Supported Format: .pdf)')
    # quotation = models.FileField(upload_to='quotation/', blank=True, null=True)
    quotation_info = HTMLField(blank=True, null=True)
    extra_field = models.CharField(max_length=255, blank=True, null=True)
    agreement = models.CharField(choices=agreement, default='disagree', max_length=255)

    # agree_to_quotation = models.CharField(choices=agreement, default='disagree', max_length=255)
    # agree_to_nda_nca = models.CharField(choices=agreement, default='disagree', max_length=255)
    def get_nda(self):
        print(self.nda)

class QuotationAgreement(models.Model):
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE, related_name='quotation_agreement_quotation')
    agreement = models.CharField(verbose_name='Agree to NDA/NCA', choices=agreement, max_length=255)
    user_nda_nca = models.FileField(upload_to='nda/uploaded/', blank=True, null=True, verbose_name='Upload NDA and NCA',
                                validators=[FileExtensionValidator(['pdf'])], help_text='(Supported Format: .pdf)')
    # user_invoice= models.FileField(upload_to='nca/uploaded/', blank=True, null=True, verbose_name='Upload NCA',validators=[FileExtensionValidator(['pdf'])], help_text='(Supported Format: .pdf)')
    message = HTMLField(blank=True, null=True)


currency = (
    ('euro', 'EURO €'),
    ('pound', 'POUND £'),
    ('usd', 'USD $'),
)


class OrderPrice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='orderprice_order')
    initial_price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0, verbose_name='Discount (%)')
    processing_fee = models.PositiveIntegerField(default=0)
    tax = models.PositiveIntegerField(default=0, verbose_name='Tax (%)')
    price = models.PositiveIntegerField(default=0, blank=True)
    currency = models.CharField(choices=currency, max_length=255)
    payment_method = models.CharField(choices=payment_method, max_length=255)
    # invoice = models.FileField(upload_to='invoice',validators=[FileExtensionValidator(['pdf'])], help_text='(Supported Format: .pdf)', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.discount < 1:
            discount = 0
        else:
            discount = ((self.initial_price * self.discount) / 100)
        if self.tax < 1:
            tax = 0
        else:
            tax = ((self.initial_price * self.tax) / 100)

        self.price = self.initial_price - discount + tax + self.processing_fee
        super(OrderPrice, self).save(*args, **kwargs)


@receiver(post_save, sender=Order)
def create_order_price(sender, instance, created, **kwargs):
    if created:
        OrderPrice.objects.create(order=instance)
        Quotation.objects.create(order=instance)


@receiver(post_save, sender=Order)
def save_order_price(sender, instance, **kwargs):
    instance.orderprice_order.save()


# @receiver(post_save, sender=Order)
# def save_order_quotation(sender, instance, **kwargs):
#     instance.quotation_order.save()

#
# class ServiceSales(models.Model):
#     service = models.ManyToManyField(Service, related_name='service_sales_service')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_sales_user')


class OrderStaff(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderstaff_order')
    staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orderstaff_user')


ticket_status = (
    ('open', 'Open'),
    ('closed', 'Closed'),
)

issue_category = (
    ('technical_issue', 'Technical Issue'),
    ('billing_issue', 'Billing Issue'),
    ('service_issue', 'Service Issue'),
)


class Ticket(models.Model):
    category_choice = models.CharField(choices=category_choice, max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ticket_user')
    ticket_category = models.CharField(max_length=255, verbose_name='Category')
    issue_category = models.CharField(max_length=255, choices=issue_category)
    ticket_title = models.CharField(max_length=255, verbose_name='Title')
    ticket_description = HTMLField(verbose_name='Description')
    ticket_attachment = models.FileField(
        verbose_name='Attachment', upload_to='ticket/', validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'ogv',
                                                                                            'mkv', 'webm', 'apng',
                                                                                            'avif', 'gif', 'jpeg',
                                                                                            'jpg', 'png', 'svg', 'webp',
                                                                                            'bmp', 'mp3', 'wav',
                                                                                            'ogg', 'pdf', 'csv'])],
        help_text='(Supported Format: Video/Audio/Images/Documents)',default='ticket/default.gif')
    ticket_status = models.CharField(max_length=255, choices=ticket_status)
    ticket_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_title


class TicketStaff(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name='ticketstaff_order')
    staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ticketstaff_user')


class TicketComment(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name='ticketcomment_ticket')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ticketcomment_user')
    comment = HTMLField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket} - comment - {self.user}'


class SubscriptionBasedPackage(models.Model):
    category_choice = models.CharField(max_length=255, choices=category_choice)
    service_id = models.ForeignKey(SubscriptionServices, on_delete=models.CASCADE,
                                   related_name='package_subscription_service')
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

    class Meta:
        verbose_name_plural = 'Subscription Based Packages'


class SubscriptionFeatures(models.Model):
    package = models.ForeignKey(
        SubscriptionBasedPackage, on_delete=models.CASCADE, related_name='feature_subscription')
    feature_name = models.CharField(
        max_length=264, verbose_name='Feature Name')
    feature = models.CharField(
        max_length=264, verbose_name='Feature')

    def __str__(self):
        return f'{self.feature_name} - {self.feature}'

    class Meta:
        verbose_name_plural = 'Package Features'


class SubscriptionOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscriptionorder_user')
    subscription_service = models.ForeignKey(SubscriptionServices, on_delete=models.CASCADE,
                                             related_name='subscriptionorder_subscriptionservice')
    subscription_package = models.ForeignKey(SubscriptionBasedPackage, on_delete=models.CASCADE,
                                             related_name='subscriptionorder_subscriptionpackage')
    # paypal_email = models.EmailField()
    paypal_order_id = models.CharField(max_length=255)
    # paypal_user_name = models.CharField(max_length=255)
    paypal_subscription_id = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    # currency = models.CharField(max_length=255)
    category_choice = models.CharField(choices=category_choice, max_length=255)

    is_active = models.BooleanField(default=False)

    @property
    def total_count(self):
        return self.subscriptionteam_subscriptionorder.filter(subscription_order_id=self.id).count()

    def __str__(self):
        return f'{self.user} - {self.subscription_service} - {self.subscription_package} - {self.is_active}'


class UserAllowed(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='allowed_user')
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='allowed_service')

    def __str__(self):
        return f"{self.user.full_name} - {self.service.service_title}"

    class Meta:
        verbose_name_plural = 'Users Allowed'


industry_type = (
    ('software_companies', 'Software Companies'),
    ('government_agencies', 'Government Agencies'),
    ('law_enforcement', 'Law Enforcement'),
    ('financial_institutes', 'Financial Institutes'),
    ('telecommunication_companies', 'Telecommunication Companies'),
    ('wealth_management', 'Wealth Management'),
    ('educational_institutes', 'Educational Institute'),
    ('isp_companies', 'ISP Companies'),
    ('ecommerce_business', 'Ecommerce Business'),
    ('law_firm', 'Law Firm'),
    ('small_and_medium_business', 'Small and Medium Business'),
    ('health_care_institutes', 'Health Care Institutes'),
)

privilege = (
    ('admin', 'Admin'),
    ('general_admin', 'General Admin'),
    ('general_staff', 'General Staff'),
)


class Business(models.Model):
    industry_type = models.CharField(max_length=264, choices=industry_type)
    company_name = models.CharField(max_length=264, unique=True)
    company_logo = models.ImageField(upload_to='company/', default='company/default.jpg')
    website = models.URLField(max_length=264, default='https://')
    phone_number = models.CharField(max_length=24, verbose_name='Company Phone Number')
    email = models.EmailField(max_length=264, verbose_name='Company Email')
    address_one = models.CharField(max_length=255)
    address_two = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    business_size = models.IntegerField(
        default=10, verbose_name='Number of Employees')
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.company_name

    def address(self):
        return f'{self.address_one} {self.address_two}, {self.city}, {self.zipcode}, {self.country}'

    class Meta:
        verbose_name_plural = 'Businesses'


class UsersBusiness(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='business_user')
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='business_business')
    position = models.CharField(max_length=264, default='staff')
    privilege = models.CharField(max_length=264, choices=privilege, default='general_staff')
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.business} - {self.position}'

    class Meta:
        verbose_name_plural = 'User Businesses'


medium_list = (
    ('online', 'Online'),
    ('offline', 'Offline'),
)
category_list = (
    ('for_business_security', 'For Business CyberSecurity'),
    ('for_personal_security', 'For Personal CyberSecurity'),
)
status_list = (
    ('active', 'Active'),
    ('completed', 'completed'),
    ('canceled', 'canceled'),
)


class Events(models.Model):
    event_name = models.CharField(max_length=264)
    medium = models.CharField(choices=medium_list, max_length=264)
    speaker = models.CharField(max_length=264)
    category = models.CharField(choices=category_list, max_length=264)
    address = models.CharField(max_length=264)
    timezone = TimeZoneField(choices_display='WITH_GMT_OFFSET', default='Europe/London')
    date_time = models.DateTimeField()
    # time_field = models.TimeField()
    status = models.CharField(choices=status_list, max_length=264)
    event_description = HTMLField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    event_image=models.ImageField(upload_to='events/', default='events/default.jpg')

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name_plural = 'Events'


class RegisteredEvents(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='registered_event_user')
    event = models.ForeignKey(
        Events, on_delete=models.CASCADE, related_name='registered_event_event')

    def __str__(self):
        return f'{self.user} - {self.event}'

    class Meta:
        verbose_name_plural = 'Registered Events'


class Notification(models.Model):
    category_choice = models.CharField(max_length=255)
    notification = HTMLField()
    notification_time = models.DateTimeField()
    is_read = models.BooleanField(default=False)
    # date_time = models.DateTimeField()


class AdminNotification(models.Model):
    category_choice = models.CharField(max_length=255, choices=category_choice)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_notification_user', blank=True,
                             null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='admin_notification_business',
                                 blank=True, null=True)
    notification = HTMLField()
    notification_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


"""
Subscription Input Sections
Admin will create form for subscription services
Where team member of business can insert their info
"""


class SubscriptionField(models.Model):
    subscriptionservice = models.OneToOneField(
        SubscriptionServices, on_delete=models.CASCADE, related_name='subscriptionservice_service',
        blank=True, null=True)
    fields = models.ManyToManyField(
        InputFields, related_name='subscriptionservice_inputfields', through='SubscriptionInput')


class SubscriptionInput(models.Model):
    subscription_field = models.ForeignKey(
        SubscriptionField, on_delete=models.CASCADE, related_name='subscriptioninput_subscriptionfield')
    inputfield = models.ForeignKey(
        InputFields, on_delete=models.CASCADE, related_name='subscriptioninput_inputfield')

    # input_value = models.CharField(max_length=264, blank=True, null=True)

    class Meta:
        db_table = 'BusinessSecurity_subscriptionfield_inputfields'


class TeamSubscriptionInput(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='team_subscription_input')
    inputfield = models.ForeignKey(
        SubscriptionInput, on_delete=models.CASCADE, related_name='inputfield_subscriptioninput')
    inputinfo = models.CharField(max_length=255)


class SubscriptionTeam(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='subscriptionteam_business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptionteam_user')
    subscription_order = models.ForeignKey(SubscriptionOrder, on_delete=models.CASCADE,
                                           related_name='subscriptionteam_subscriptionorder')
