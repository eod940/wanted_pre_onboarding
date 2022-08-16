from django.core.validators import MinValueValidator
from django.db import models


''' 회사의 채용공고 내용 예시

  "회사_id":회사_id,
  "채용포지션":"백엔드 주니어 개발자",
  "채용보상금":1000000,
  "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
  "사용기술":"Python"
  
'''
class EmploymentsPost(models.Model):
    company_id = models.IntegerField(primary_key=True, verbose_name="회사id")
    employments_position = models.CharField(max_length=100, verbose_name="채용포지션")
    employments_compensation = models.IntegerField(validators=[MinValueValidator(1)],
                                                   verbose_name="채용보상금")
    employments_text = models.TextField(verbose_name="채용내용")
    employments_tech_to_use = models.CharField(max_length=100, verbose_name="사용기술")

