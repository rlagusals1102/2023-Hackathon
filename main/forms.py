from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='이메일 주소'
    )
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput,
        help_text=(
            "비밀번호는 8자 이상이어야 하며, 숫자로만 이루어질 수 없습니다."
        )
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': '사용자 이름',
        }
        help_texts = {
            'username': '필수 항목. 150자 이하. 문자, 숫자, @/./+/-/_ 만 사용 가능.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': '사용자 이름'})
        self.fields['email'].widget.attrs.update({'placeholder': '이메일'})
        self.fields['password1'].widget.attrs.update({'placeholder': '비밀번호'})
        self.fields['password2'].widget.attrs.update({'placeholder': '비밀번호 확인'})
