from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class TestPixelAudio(base_test.BaseTestClass):
    # Setup
    def setup_class(self):
        self.ad = self.register_controller(android_device, min_number=1)[0]
        self.ad.load_snippet('api', 'com.google.android.mobly.snippet.bundled')

    def test_max_alarm_vol(self):
        max_volume = self.ad.api.getAlarmMaxVolume()
        print(max_volume)

    def test_alarm_vol(self):
        alarm_vol = self.ad.api.getAlarmVolume()
        print(alarm_vol)

    def test_music_vol(self):
        music_vol = self.ad.api.setMusicVolume(3)
        print(music_vol)

    def test_set_alarm_vol(self):
        set_alarm_vol = self.ad.api.setAlarmVolume(4)
        print(set_alarm_vol)

if __name__ == "__main__":
    test_runner.main()