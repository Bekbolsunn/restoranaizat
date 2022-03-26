from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Food(models.Model):
    DoesNotExist = None
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text


# class Basket(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     food = models.ForeignKey(Food, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user
