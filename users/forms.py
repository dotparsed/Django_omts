from django import forms

from registration.forms import RegistrationForm

from .models import Profile
from .models import Order
from .models import City

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout



#======== ФОРМА РЕГИСТРАЦИИ
class MyRegForm(RegistrationForm):

    def __init__(self,*args,**kwargs):
        super(MyRegForm, self).__init__(*args, **kwargs)
        for fieldname in ['username','email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].labels = "None"

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4 text-right'
        self.helper.field_class = 'col-lg-4'
        self.helper.add_input(Submit('submit', 'Отправить'))

        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2'
        )



COUNTRY_CHOICE = [
    ('ru', 'Россия'),
    ('by', 'Беларусь')
]




#======== ФОРМА Профиля
class ProfileForm(forms.ModelForm):
    company = forms.CharField(
        label=False,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Название компании'
            }
        )
    )

    country = forms.CharField(
        label=False,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Город/область',
                'id':'cityauto'
            }
        )
    )


    about = forms.CharField(
        label=False,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'о компании',
                'rows': 4
            }
        )
    )

    inn = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'ИНН или УНП организации'
            }
        )
    )

    tel1 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'рабочий телефон'
            }
        )
    )

    tel2 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'доп. рабочий телефон'
            }
        )
    )

    fax = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'факс'
            }
        )
    )

    email1 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'доп. email'
            }
        )
    )

    email2 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'доп email'
            }
        )
    )

    adres1 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'адрес компании'
            }
        )
    )

    adres2 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'доп. адрес компании'
            }
        )
    )

    website = forms.URLField(
        label=False,
        required=False,
        widget=forms.URLInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Website'
            }
        )
    )

    class Meta:
        model = Profile
        fields = (
        'company', 'country', 'about', 'inn', 'tel1', 'tel2', 'fax', 'email1', 'email2', 'adres1', 'adres2', 'website',)




#======== ФОРМА Заявки



class OrderForm(forms.ModelForm):
    CATEGORY_CHOICE = [
        ('001', 'Оборудование'),
        ('002', 'Продукты'),
        ('003', 'Химикаты'),
        ('004', 'Металопрокат'),
        ('005', 'Канцтовары')
    ]

    order_text = forms.CharField(
        label=False,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg',
                'rows': 4,
                'placeholder': 'Укажите ваш заказ в этом поле \n товар1 - 3шт \n товар2 - 10шт \n или прикрепите файл с заказом'}

        )
    )



    category = forms.ChoiceField(
        label="Категория",
        choices=CATEGORY_CHOICE,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg',
            }
        ))





    tel1 = forms.CharField(
        label=False,
        required=True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'телефон'
            }
    ))
    email1 = forms.CharField(
        label=False,
        required=True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'email'
            }
    ))
    fax1 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'факс'
            }

    ))

    name1 = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'имя/должность'
            }

    ))


    datetime = forms.DateField(
        label=False,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'До какой даты заявка актуальна?',
                'id':'datepicker'
            }
        )
    )

    file1 = forms.FileField(
        required=False,
        label=False,
        widget=forms.FileInput
    )
    file2 = forms.FileField(
        label=False,
        widget=forms.FileInput
    )
    file3 = forms.FileField(
        label=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Order
        fields = ('category', 'order_text', 'tel1','email1','fax1','name1','datetime','file1','file2','file3')