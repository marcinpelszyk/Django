from django.db import models
from django.utils.translation import gettext_lazy as _ 


class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )


    def __str__(self):
        return self.name
    
class Product(models.Model):
    """
    The Product table contining all product items.
    """
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_('title'),
        help_text=_('Required'),
        max_length=255,
    )
    description = models.TextField(verbose_name=_('description'), help_text=_('Not Required'), blank=True)
    slug = models.SlugField(max_length=255)
    reqular_price = models.DecimalField(
        verbose_name=_('Regular price'),
        help_text=_('Maximum 9999.99'),
        error_messages={
            'name': {
                "max_length": _('The price must be between 0 and 9999.99.'),
            },
        },
        decimal_places=2,
        max_digits=6
    )
    discount_price = models.DecimalField(
        verbose_name=_('Discount price'),
        help_text=_('Maximum 9999.99'),
        error_messages={
            'name': {
                "max_length": _('The price must be between 0 and 9999.99.'),
            },
        },
        decimal_places=2,
        max_digits=6
    )
    is_active = models.BooleanField(
        verbose_name=_('Product visibility'),
        help_text=_('Change product visiblilty'),
        default=True,
    )
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, editable=False)
    update_at = models.DateTimeField(_('Updated at'), auto_now=True)


    def __str__(self):
        return self.title

   
