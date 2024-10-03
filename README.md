# Update Xcode Project Settings Action

This action updates the Xcode project settings for code signing in iOS projects.

## Inputs

- `project_path`: Path to the Xcode project file (default: 'ios/Runner.xcodeproj/project.pbxproj')
- `provisioning_profile_specifier`: Provisioning profile specifier
- `code_sign_style`: Code sign style (default: 'Manual')
- `code_sign_identity`: Code sign identity (default: 'iPhone Distribution')
- `code_sign_identity_iphoneos`: Code sign identity for iphoneos SDK (default: 'iPhone Distribution')

## Example usage

```yaml
uses: nextDriveIoE/update-xcode-settings-action@v1
with:
  project_path: 'ios/Runner.xcodeproj/project.pbxproj'
  provisioning_profile_specifier: 'Your Provisioning Profile'
  code_sign_style: 'Manual'
  code_sign_identity: 'iPhone Distribution'
  code_sign_identity_iphoneos: 'iPhone Distribution'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.