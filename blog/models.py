from django.db import models

# Characteristics of a blog post are Title, Author and Body
class Post(models.Model):
    
    # Limit the characters in the title to 200
    title = models.CharField(max_length=200)

	# ForeignKey allows for many-to-one relationship such that the user
	# can be the author of many different blog posts but not the other
	# way around
    author = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE,
	)
    
    # The textfield will automatically expand as the user needs
    body = models.TextField()

def __str__(self):
    return self.title