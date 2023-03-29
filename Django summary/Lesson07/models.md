# How to start storing data with Django?

Now, we want to start saving our data. In real-life projects, we will always need to save what we receive from the user.

To do this, we need to identify what kind of table, in the database, we will need. 
For example:
* What kind of data will we be storing? 
* How many columns will we need?
* What will their names be?

In this case, we will be using four columns: **Investimento**, **Valor**, **Pago**, **Data**.

So the table will be like:

##                         Database Table

| **Investimento** | **Valor** | **Pago**  | **Data** |
| ---------------- |:---------:|:---------:|:--------:|
| investimento1    | valor1    | False/True| data_1   |
| investimento2    | valor2    | False/True| data_2   |
| investimento3    | valor3    | False/True| data_3   |

***
We start off creating find the _models.py_. This file will represent our database. We create a class in it that afterward will become our database. This class is called **model**. Let start:

* Go into the Django app folder.

* Go into the _models.py_ file.

* Create a class with an significant name for you. In this case, we will create a class called _class Investimento(models.Model)_. It needs to inherit from the class _models.Model_. Have a look below:

```
from django.db import models
from date import datetime
class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)

```
Here, we define the columns and the properties from their values. We have defined:
* The column **investimento** will accept text with the maximum length of 255 letters.
* The column **valor** will only accept float values once we want financial values.
* The column **pago** will only accept boolean values, true or false to verify the conditional of the payment.
* The column **data** will only accept date types, we want to register when the information is saved and we do not want to leave this in the user's hands. So we call the function _datetime.now_. Remember to import the module like in the code.

Pay attention that we have only created the model, but we have not created the database.
