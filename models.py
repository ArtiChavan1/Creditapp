from django.db import models

class LoanApplication(models.Model):
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_name
