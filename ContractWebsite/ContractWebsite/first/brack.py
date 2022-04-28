   # # Save data and set current user to last updated by fields
    # def form_valid(self, form):
    #     object = form.save(commit=False)
    #     object.last_updated_by = self.request.user.get_full_name()
    #     object.last_updated_by_id = self.request.user
    #
    #     return super(EditUsers, self).form_valid(form)

    # def get_queryset(self):
    #     criteria1 = Q(owner=self.request.user)
    #     criteria2 = Q(organizationmembers__member=self.request.user)
    #     criteria3 = Q(organizationmembers__organization_admin=1)
    #     org_list = UserModel.objects. \
    #         filter(criteria1 | (criteria2 & criteria3)).distinct()

        # if org_list.count() != 0:
        #     return org_list
        # else:
        #     raise Http404('You don\'t have permissions!')
    #template_name_suffix = '_update_form'
   # success_url = reverse_lazy('admins')
    # def get_context_object_name(self, obj):
    #     print(obj)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_profil = UserModel.objects.get(id=self.object.id)
    #     print(user_profil.id)
    #     context['user'] = user_profil
    #     return context


    # def post(self, request, *args, **kwargs):
    #     user_for_edit=UserModel.objects.get(username=self.object.username)
    #     print(user_for_edit)


# class FormEditUser(forms.ModelForm):
#     class Meta:
#         model=UserModel
#         fields='__all__'
#
# class EditUsers(auth_mixin.LoginRequiredMixin,views.UpdateView):
#     model = UserModel
#     form_class = FormEditUser
#     template_name = 'edit_user.html'
#
#     def get_object(self, queryset=None):
#         pk = self.kwargs.get(self.pk_url_kwarg)
#         print(pk)