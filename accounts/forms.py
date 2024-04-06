# from django import forms
# from django.contrib.auth.forms import AuthenticationForm, UsernameField
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import authenticate

# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
#     password = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].label = _("Username or Email")

#     def clean(self):
#         username_or_email = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")

#         if username_or_email and password:
#             if "@" in username_or_email:
#                 kwargs = {"email": username_or_email}
#             else:
#                 kwargs = {"username": username_or_email}

#             self.user_cache = authenticate(self.request, **kwargs, password=password)
#             if self.user_cache is None:
#                 raise forms.ValidationError(
#                     self.error_messages["invalid_login"],
#                     code="invalid_login",
#                     params={"username": self.username_field.verbose_name},
#                 )
#             else:
#                 self.confirm_login_allowed(self.user_cache)
        
#         return self.cleaned_data
