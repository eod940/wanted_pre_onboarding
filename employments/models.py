from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

''' 회사의 채용공고 내용 예시
  "회사_id":회사_id,
  "채용포지션":"백엔드 주니어 개발자",
  "채용보상금":1000000,
  "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
  "사용기술":"Python"
'''


# 채용공고
class EmploymentsPost(models.Model):
    employments_position = models.CharField(max_length=100, verbose_name="채용포지션")
    employments_compensation = models.IntegerField(validators=[MinValueValidator(1)],
                                                   verbose_name="채용보상금")
    employments_text = models.TextField(verbose_name="채용내용")
    employments_tech_to_use = models.CharField(max_length=100, verbose_name="사용기술")

    employments_author = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="company_id",
                                   db_column="company_id", verbose_name="회사")

    def __str__(self):
        return '{}'.format(self.employments_position)

    def get_absolute_url(self):
        return 'employments/{}'.format(self.pk)

    def get_update_url(self):
        return self.get_absolute_url() + '/update/'

    class Meta:
        verbose_name = "채용공고"
        verbose_name_plural = "채용공고"


# 회사
class Company(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name="회사id")
    company_name = models.CharField(max_length=100, verbose_name="회사명")
    company_nationality = models.CharField(max_length=30, verbose_name="국가")
    company_address = models.CharField(max_length=100, verbose_name="지역")

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.company_name)

    class Meta:
        verbose_name = "채용기업"
        verbose_name_plural = "채용기업"
