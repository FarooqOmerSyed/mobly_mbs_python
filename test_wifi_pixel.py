from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class WifiPixelTest(base_test.BaseTestClass):

    def setup_class(self):
        self.ad = self.register_controller(android_device, min_number=1)[0]
        self.ad.load_snippet('api', 'com.google.android.mobly.snippet.bundled')

    def test_enable_wifi(self):
        self.ad.api.wifiEnable()

    def test_wifi_scan(self):
        scanned_results = self.ad.api.wifiScanAndGetResults()
        print(scanned_results)

    def test_wifi_band(self):
        wifi_band = self.ad.api.wifiIs5GHzBandSupported()
        print(wifi_band)


if __name__ == '__main__':
    test_runner.main()