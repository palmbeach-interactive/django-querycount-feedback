Django QueryCount Feedback
==========================

A super simple Django (>=1.10) middleware providing visual (browser) feedback in combination with 
[django-querycount](https://github.com/bradmontgomery/django-querycount) 


It takes into account the `QUERYCOUNT` settings, namely: 

    QUERYCOUNT = {
        'THRESHOLDS': {
            'MEDIUM': 50,
            'HIGH': 200,
            ...
        },
        ...
    }
    
Reaching the `MEDIUM` threshold adds an orange 10px border to the displayed HTML and `HIGH` a red one.

Installing
----------

Using the latest version from PyPI:

    pip install django-querycount-feedback

Using this GitHub repository:

    pip install -e "git://github.com/palmbeach-interactive/django-querycount-feedback.git#egg=django-querycount-feedback"


Then add `querycount_feedback.middleware.QueryCountFeedbackMiddleware` to `MIDDLEWARE`, before `querycount.middleware.QueryCountMiddleware`.  
Pre 1.10 `MIDDLEWARE_CLASSES` is supported as well.

