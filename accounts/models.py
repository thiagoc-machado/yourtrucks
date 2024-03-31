# from django.db import models

# # extends django user
# class User(models.Model):
#     phone = models.CharField(max_length=20)
#     type = models.CharField(max_length=20)
#     photo = models.ImageField(upload_to='photos', null=True, blank=True)



# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200) 
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.text
# class answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     message = models.ForeignKey(Message, on_delete=models.CASCADE)
#     is_read = models.BooleanField(default=False)
#     is_answer = models.BooleanField(default=False)
#     answer_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_by')

#     def __str__(self):
#         return self.text

# class Favorites(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     car = models.ForeignKey('car.Car', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.car.car_title
    
# class Last_viwed(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     car = models.ForeignKey('car.Car', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.car.car_title