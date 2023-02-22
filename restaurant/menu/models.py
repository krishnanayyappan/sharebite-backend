from django.db import models

# Section model includes the fields for storing id, name and description
class Section(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


# Item model includes the fields for storing id, name, description, price,
# and foreign-key to section ID. Using foreign key as it is a one-to-one
#  relationship.
class Item(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sectionid = models.ForeignKey(Section, related_name='items', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# Modifier model includes the fields for storing id, name, description, and a list/array to
# store many-to-many info of items. Items and Modifiers have a many-to-many relationship.
class Modifier(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    items = models.ManyToManyField('Item', blank=True, related_name='modifiers')

    def __str__(self) -> str:
        return self.name


class Mapping(models.Model):
    id = models.AutoField(primary_key=True)
    mod_id = models.ForeignKey(Modifier, on_delete=models.CASCADE)
    items_id = models.ForeignKey(Item, on_delete=models.CASCADE)
