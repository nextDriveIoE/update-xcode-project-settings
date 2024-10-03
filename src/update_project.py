import os
from pbxproj import XcodeProject

project_path = os.environ['PROJECT_PATH']
provisioning_profile_specifier = os.environ['PROVISIONING_PROFILE_SPECIFIER']
code_sign_style = os.environ['CODE_SIGN_STYLE']
code_sign_identity = os.environ['CODE_SIGN_IDENTITY']
code_sign_identity_iphoneos = os.environ['CODE_SIGN_IDENTITY_IPHONEOS']

project = XcodeProject.load(project_path)

for target in project.objects.get_targets():
    project.set_flags('PROVISIONING_PROFILE_SPECIFIER', provisioning_profile_specifier, target.name)
    project.set_flags('CODE_SIGN_STYLE', code_sign_style, target.name)
    project.set_flags('CODE_SIGN_IDENTITY', code_sign_identity, target.name)
    project.set_flags('CODE_SIGN_IDENTITY[sdk=iphoneos*]', code_sign_identity_iphoneos, target.name)

project.save()

print("Xcode project settings updated successfully.")