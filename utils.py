import subprocess


class SessionAction(object):

    @classmethod
    def lock(cls):
        return 'dbus-send --session --type=method_call --dest=org.freedesktop.ScreenSaver /org/freedesktop/ScreenSaver org.freedesktop.ScreenSaver.Lock uint32:1'

    @classmethod
    def reboot(cls):
        return 'dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Reboot boolean:false'

    @classmethod
    def power_off(cls):
        return 'dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.PowerOff boolean:false'

    @classmethod
    def suspend(cls):
        return 'dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Suspend boolean:false'

    @classmethod
    def dnd_on(cls):
        return 'gsettings set org.pantheon.desktop.gala.notifications do-not-disturb true'

    @classmethod
    def dnd_off(cls):
        return 'gsettings set org.pantheon.desktop.gala.notifications do-not-disturb false'

    @staticmethod
    def get_dnd_state():
        schema_name = "org.pantheon.desktop.gala.notifications"
        dnd_key = "do-not-disturb"
        return subprocess.check_output(["gsettings", "get", schema_name, dnd_key])[:-1] == 'true'
