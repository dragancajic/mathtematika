from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # нови пост направљен -> сачувај датум
    created_on = models.DateTimeField(auto_now_add=True)

    # пост измијењен/едитован -> сачувај датум
    last_modified = models.DateTimeField(auto_now=True)

    # у једној категорији може бити више постова, али исто тако
    # један пост може припадати различитим категоријама, ДАКЛЕ
    # веза је више-на-према-више -> many-to-many, m:n
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # страни кључ у табели за коментаре, јер један пост може имати више коментара,
    # ДАКЛЕ, веза је један-на-према-више -> 1:n, а на страни `више` иде страни кључ;
    # приликом брисања поста, бришу се и коментари везани за тај пост - има логике!
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.author} on '{self.post}'"
