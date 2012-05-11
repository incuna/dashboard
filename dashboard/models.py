from profiles.models import Profile, ProfileAdmin

Profile.register_extensions(
    'dashboard.extensions.manager',
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

for field in Profile._meta.fields:
    if field.name == 'is_staff':
        field.default = True

