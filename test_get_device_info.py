from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device
from snippet_uiautomator import uiautomator


class GetDeviceInfoTest(base_test.BaseTestClass):
    
    # setup method ( defines the android device to be used for testing )
    def setup_class(self):
        self.ad = self.register_controller(android_device, min_number=1)[0]
        self.ad.services.register(
    uiautomator.ANDROID_SERVICE_NAME, uiautomator.UiAutomatorService
)
        
    # method to test device info ( prints device info to console/terminal)
    def test_device_info(self):
        device_info = self.ad.ui.info
        print(device_info)


if __name__ == '__main__':
    test_runner.main()