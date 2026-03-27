from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    icon = models.CharField(max_length=100, blank=True, help_text='CSS class or emoji for skill icon')
    proficiency = models.PositiveSmallIntegerField(default=80, help_text='0-100 percentage')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Skill, blank=True, related_name='projects')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Experience(models.Model):
    TYPE_CHOICES = [
        ('work', 'Work'),
        ('education', 'Education'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='work')
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text='Leave empty if current')
    location = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f'{self.role} @ {self.company}'

    @property
    def is_current(self):
        return self.end_date is None

    @property
    def duration(self):
        from datetime import date
        end = self.end_date or date.today()
        months = (end.year - self.start_date.year) * 12 + (end.month - self.start_date.month)
        if months < 12:
            return f'{months} mo{"s" if months != 1 else ""}'
        years = months // 12
        rem = months % 12
        if rem:
            return f'{years} yr{"s" if years != 1 else ""} {rem} mo{"s" if rem != 1 else ""}'
        return f'{years} yr{"s" if years != 1 else ""}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f'{self.name} — {self.subject}'


class Profile(models.Model):
    """Singleton model for site owner information."""
    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, help_text='e.g. Full Stack Developer')
    bio = models.TextField()
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    available_for_work = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        # Ensure only one profile exists
        if not self.pk and Profile.objects.exists():
            Profile.objects.all().delete()
        super().save(*args, **kwargs)
