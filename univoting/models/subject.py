from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from univoting.models.subject_review import SubjectReview


class Subject(models.Model):
    MAX_ECTS = 30
    MIN_ECTS = 1

    name = models.CharField(max_length=64, default="New Subject")
    ects = models.PositiveSmallIntegerField(validators=[MaxValueValidator(MAX_ECTS), MinValueValidator(MIN_ECTS)])
    description = models.TextField(max_length=250, default="No description added yet")
    review = models.ForeignKey(SubjectReview, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.name, self.ects)

    def get_absolute_url(self):
        return reverse('univoting:subject_detail', kwargs={'pk': self.pk})
