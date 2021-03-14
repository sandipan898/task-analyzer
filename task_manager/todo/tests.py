from django.test import TestCase
import datetime
# Create your tests here.

date1 = datetime.datetime.now().timestamp()
date2 = datetime.datetime.now().timestamp()
print((date1 - date2))

