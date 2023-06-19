from django.db import models

# Create your models here.
class My_profile_nav(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    short_intro = models.CharField(max_length=200,blank=True, null=True)
    side_profile_pic = models.ImageField(blank=True, null=True) 
     
    facebook_link = models.URLField(("facebook_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    linkedin_link = models.URLField(("linkedin_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    github_link = models.URLField(("github_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    
    researchgate_link = models.URLField(("researchgate_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    google_sch_link= models.URLField(("google_sch_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    my_website_link = models.URLField(("my_website_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_kaggle_link = models.URLField(("my_kaggle_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_email = models.EmailField(("my_email"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_twitter = models.URLField(("my_twitter_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_ig = models.URLField(("my_ig_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_stack_overflow = models.URLField(("my_stack_overflow"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_medium_link = models.URLField(("my_medium_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_facebook = models.URLField(("my_facebook"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    

    date_created = models.DateTimeField(auto_now_add=True, null=True)

   
    def __str__(self):
        return self.name