import sublime, sublime_plugin
import os

class SimpleTestCommand(sublime_plugin.TextCommand):
  def run(self, *args):
    cmd = "echo \""+self.view.file_name()+"\" > ~/.last_test"
    os.system(cmd)
    cmd = '''
tell application "iTerm"
  activate
  tell the current terminal
    tell the current session
      write text "t"
    end
  end
end
EOF
'''
    os.system('osascript <<EOF'+cmd)
