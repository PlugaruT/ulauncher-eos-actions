class SessionAction(object):

    @classmethod
    def lock(cls):
        return 'dbus-send --session --type=method_call --dest=org.freedesktop.ScreenSaver /org/freedesktop/ScreenSaver org.freedesktop.ScreenSaver.Lock uint32:1'

    @classmethod
    def reboot(cls):
        return 'dbus-send --system --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Reboot boolean:false'

    @classmethod
    def power_off(cls):
        return 'dbus-send --system --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.PowerOff boolean:false'
    
    @classmethod
    def suspend(cls):
        return 'dbus-send --system --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Suspend boolean:false'
