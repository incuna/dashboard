from profiles.models import Profile, ProfileAdmin, ProfileForm

Profile.register_extensions(
    'dashboard.extensions.manager',
    'dashboard.extensions.holidays',
    'dashboard.extensions.avatars',
    'dashboard.extensions.ssh_key',
    'permissions'
)

ProfileAdmin.fieldsets[0][1]['fields'].insert(0, 'username')

def clean_picture(picture, user=None):
    """Return a picture with the name set to that of the given user"""
    if user:
        ext = picture.name.split('.')[-1]
        picture.name = user + '.' + ext
    return picture

def clean_avatar(self):
    avatar = self.cleaned_data.get('avatar', None)
    user = self.cleaned_data.get('username', None)
    if avatar and user:
        return clean_picture(avatar, user)
ProfileForm.clean_avatar = clean_avatar

def clean_posh_avatar(self):
    posh_avatar = self.cleaned_data.get('posh_avatar', None)
    user = self.cleaned_data.get('username', None)
    if posh_avatar:
        return clean_picture(posh_avatar, user)
ProfileForm.clean_posh_avatar = clean_posh_avatar

for field in Profile._meta.fields:
    if field.name == 'is_staff':
        field.default = True
