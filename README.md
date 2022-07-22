# Problem statement:
This is a recruitment task for a reputed company in Bangladesh as a Django developer. This task is about changing the sub-domain & customize the url.
#### The previous url is 
	https://techforing.com/category/case_studies/ (present)
	https://blog.techforing.com/category/case_studies/ (what it becomes)

####  But it should be
	https://blog.techforing.com/cybersecurity-case-studies/

# Solution process
#### follow the steps
	Set the local development server as techforingg.com and blog.techforingg.com
	set up Django-host packages & modified according to requirements.
	Change path('category/<name>/', views.categoryView, name='category'), to path('cybersecurity-<str:name>/', views.categoryView, name='cybersecurity'),
	pass the string on the templates like href="{% host_url 'cybersecurity' name='case-studies' host 'blog' %}">

# Some Screenshots

## Blog page
![blog page](https://github.com/MahmudJewel/tech-foring-task/blob/main/screenshot/tf-1%20home.jpg)

## cybersecurity-article page
![Category-article page](https://github.com/MahmudJewel/tech-foring-task/blob/main/screenshot/tf-2%20articles.jpg)

## cybersecurity-case-studies page
![Category- case-studies page](https://github.com/MahmudJewel/tech-foring-task/blob/main/screenshot/tf-3%20case-studies.jpg)

## cybersecurity-podcast page
![Category-podcast page](https://github.com/MahmudJewel/tech-foring-task/blob/main/screenshot/tf-4%20pocasr.jpg)

The End


