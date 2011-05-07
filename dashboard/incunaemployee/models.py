from profiles.models import Profile

Profile.register_extensions('manager', 'avatars', 'ssh_key', 'permissions')#, 'profiles.modules.options.extensions.options')

