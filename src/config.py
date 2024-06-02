from gi.repository import Gio

class Settings:
    _instance = None
    APP_ID = "io.github.amit9838.mousam"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.init_settings()
        return cls._instance

    def init_settings(self):
        self.settings = Gio.Settings(self.APP_ID)
        self._settings_map = {
            "added_cities": "added-cities",
            "selected_city": "selected-city",
            "is_using_dynamic_bg": "use-gradient-bg",
            "is_using_inch_for_prec": "use-inch-for-prec",
            "should_launch_maximized": "launch-maximized",
            "unit": "unit",
        }

    @property
    def added_cities(self):
        return self.settings.get_strv(self._settings_map["added_cities"])

    @added_cities.setter
    def added_cities(self, value):
        self.settings.set_strv(self._settings_map["added_cities"], value)

    @property
    def selected_city(self):
        return self.settings.get_string(self._settings_map["selected_city"])

    @selected_city.setter
    def selected_city(self, value):
        self.settings.set_string(self._settings_map["selected_city"], value)

    @property
    def is_using_dynamic_bg(self):
        return self.settings.get_boolean(self._settings_map["is_using_dynamic_bg"])

    @is_using_dynamic_bg.setter
    def is_using_dynamic_bg(self, value):
        self.settings.set_boolean(self._settings_map["is_using_dynamic_bg"], value)

    @property
    def is_using_inch_for_prec(self):
        return self.settings.get_boolean(self._settings_map["is_using_inch_for_prec"])

    @is_using_inch_for_prec.setter
    def is_using_inch_for_prec(self, value):
        self.settings.set_boolean(self._settings_map["is_using_inch_for_prec"], value)

    @property
    def should_launch_maximized(self):
        return self.settings.get_boolean(self._settings_map["should_launch_maximized"])

    @should_launch_maximized.setter
    def should_launch_maximized(self, value):
        self.settings.set_boolean(self._settings_map["should_launch_maximized"], value)

    @property
    def unit(self):
        return self.settings.get_string(self._settings_map["unit"])

    @unit.setter
    def unit(self, value):
        self.settings.set_string(self._settings_map["unit"], value)

def get_settings():
    return Settings()

settings = get_settings()
