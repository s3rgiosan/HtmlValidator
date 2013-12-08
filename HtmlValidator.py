# -*- coding: utf-8 -*-
'''
  W3C HTML Validator
  Sublime Text 2 plugin to validate HTML using the W3C Markup Validation Service.

  @version 1.0.0
  @author  Sérgio Santos
  @email   me@s3rgiosan.com
  @url     http://s3rgiosan.com
'''
import sublime, sublime_plugin, os

# Execute the HTML Validator when a file is saved
class HtmlValidator(sublime_plugin.EventListener):
  def on_post_save(self, view):
    view.window().run_command('html_validator', { 'saving': True })

# Execute the HTML Validator
class HtmlValidatorCommand(sublime_plugin.TextCommand):
  def run(self, edit, saving = False):

    view = self.view
    window = view.window()
    settings = sublime.load_settings(__name__ + '.sublime-settings')

    # Check if it's a valid file
    if len(view.file_name()) > 0 and view.file_name().endswith(('.html')):

      folder_name, file_name = os.path.split(view.file_name())
      validate_on_save = view.settings().get('validate_on_save', settings.get('validate_on_save', False))

      # Check if it's supposed to validate on save
      if saving and not validate_on_save:
        return

      window.run_command('exec', {
        'cmd': ['python', sublime.packages_path() + '/HtmlValidator/w3c-validator.py', file_name],
        'working_dir': folder_name
      })
      sublime.status_message(('Validating %s...') % file_name)
