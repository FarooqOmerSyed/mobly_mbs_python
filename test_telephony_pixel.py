from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class TelephonyPixelTest(base_test.BaseTestClass):

    def setup_class(self):
        self.ad = self.register_controller(android_device, min_number=1)[0]
        self.ad.load_snippet('api', 'com.google.android.mobly.snippet.bundled')


    def test_tele_call_state(self):
        tele_call_state = self.ad.api.getTelephonyCallState(1)
        print(f"the tele call state is {tele_call_state}")

    def test_data_network_type(self):
        data_network_type = self.ad.api.getDataNetworkType()
        print(f"the data network type is {data_network_type}")


if __name__ == '__main__':
    test_runner.main()
