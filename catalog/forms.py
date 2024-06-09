from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product, Version, Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        exclude = ('product_owner',)
        model = Product

    def clean(self):
        bad_words = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}
        name = set(self.cleaned_data['name'].split(" "))
        description = set(self.cleaned_data['description'].split(" "))
        a = name & bad_words
        b = description & bad_words
        if len(a) > 0 or len(b) > 0:
            print('some')
            raise ValidationError(f'Использование слов {bad_words}, запрещено')


class ArticleForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ('article_owner',)


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        exclude = ('error_message',)
        model = Version

    def clean(self):
        flags = []
        obj_list = Version.objects.all()
        for obj in obj_list:
            flags.append(obj.version_sign)
        print(flags)
        sign = self.cleaned_data['version_sign']
        if sign is True and True in flags:
            raise ValidationError(f'может быть только одна активная версия')

        return sign
