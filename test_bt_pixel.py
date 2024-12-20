from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class TestPixelBluetooth(base_test.BaseTestClass):
    # Setup
    def setup_class(self):
        self.ad = self.register_controller(android_device, min_number=1)[0]
        self.ad.load_snippet('api', 'com.google.android.mobly.snippet.bundled')

    def test_cached_bluetooth_result(self):
        cached_bt_addr = self.ad.api.btGetCachedScanResults()
        print(cached_bt_addr)

    def test_bt_addr(self):
        get_bt_addr = self.ad.api.btGetAddress()
        print(get_bt_addr)


    def test_paired_bt(self):
        paired_bt = self.ad.api.btGetPairedDevices()
        print(paired_bt)


if __name__ == "__main__":
    test_runner.main()