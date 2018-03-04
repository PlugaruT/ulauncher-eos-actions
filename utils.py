import subprocess


class SessionAction(object):

    @classmethod
    def lock(cls):
        return 'dbus-send --session --type=method_call --dest=org.freedesktop.ScreenSaver /org/freedesktop/ScreenSaver org.freedesktop.ScreenSaver.Lock uint32:1'

    @classmethod
    def logout(cls):
        return 'dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1/user/self org.freedesktop.login1.User.Terminate'

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

    @classmethod
    def show_battery_percentage(cls):
        return 'gsettings set org.pantheon.desktop.wingpanel.indicators.power show-percentage true'

    @classmethod
    def hide_battery_percentage(cls):
        return 'gsettings set org.pantheon.desktop.wingpanel.indicators.power show-percentage false'

    @classmethod
    def get_dnd_state(cls):
        schema_name = 'org.pantheon.desktop.gala.notifications'
        dnd_key = 'do-not-disturb'
        return cls._get_state(schema_name, dnd_key)

    @classmethod
    def get_battery_percentage_state(cls):
        schema_name = 'org.pantheon.desktop.wingpanel.indicators.power'
        battery_percentage_key = 'show-percentage'
        return cls._get_state(schema_name, battery_percentage_key)

    @staticmethod
    def _get_state(schema_name, key):
        return subprocess.check_output(["gsettings", "get", schema_name, key])[:-1] == 'true'
