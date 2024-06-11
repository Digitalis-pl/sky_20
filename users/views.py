from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView,
                                       PasswordChangeView)
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy, reverse
import secrets
from config.settings import EMAIL_HOST_USER
from users.services import make_random_password



# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:user_log_in')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        user.set_password(user.password)

        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='подтверждение почты',
            message=f'Для подтверждения почты пройдите по ссылке \n {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:user_log_in'))


class ChangePassword(PasswordChangeView):
    pass


class PasswordReset(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:password_reset_done')

    def form_valid(self, form):
        if self.request.method == 'POST':
            user_email = self.request.POST.get('email')
            user = User.objects.filter(email=user_email).first()
            if user:
                new_password = make_random_password()
                user.set_password(new_password)
                user.save()
                try:
                    send_mail(
                        subject="Восстановление пароля",
                        message=f"Здравствуйте! Ваш пароль для доступа на наш сайт изменен:\n"
                                f"Данные для входа:\n"
                                f"Email: {user_email}\n"
                                f"Пароль: {new_password}",
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[user.email]
                    )
                except Exception:
                    print(f'Ошибка пр отправке письма, {user.email}')
                return HttpResponseRedirect(reverse('users:password_reset_done'))


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password-confirm')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class ResetComplete(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('avatar', 'email', 'phone', 'country',)

    def get_success_url(self):
        return reverse('users:user_change', kwargs={'pk': self.object.pk})
