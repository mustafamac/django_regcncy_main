apps/
├── core/                   # الإعدادات والمشتركات
│   ├── models.py          (SiteSetting, CounterStats)
│   ├── context_processors.py (لتمرير الإعدادات للقوالب)
│   └── admin.py
├── pages/                  # الصفحات الثابتة
│   ├── models.py          (Page, HomePageSection)
│   ├── views.py           (home, about, contact)
│   └── urls.py
├── blog/                   # الأخبار والمحتوى
│   ├── models.py          (Category, Post)
│   ├── views.py           (post_list, post_detail)
│   └── urls.py
├── projects/              # المشاريع
│   ├── models.py          (Project)
│   ├── views.py           (project_list, project_detail)
│   └── urls.py
├── contact/               # نماذج الاتصال
│   ├── models.py          (ContactMessage)
│   ├── forms.py           (ContactForm)
│   ├── views.py           (contact_view)
│   └── urls.py
└── subscriptions/         # النشرة البريدية
    ├── models.py          (Subscriber)
    ├── forms.py           (SubscriptionForm)
    └── views.py           (subscribe_view)