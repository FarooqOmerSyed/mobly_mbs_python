import time

from mobly import asserts
from mobly import mobly_g3 

from google3.wearables.qa.watch.libs import constants 
from google3.devtools.vinson.mobly import wear_base_test 
from google3.devtools.vinson.mobly.controllers import android_watch_device 
from goolge3.wearables.qa.wac.libs import mcu_util 
from google3.wearables.qa.watch.watchfaces.libs import watchface_lab_util 
from google3.wearables.qa.watch.watchfaces.libs import wear_watchface_constants 


class WatchFaceEditorTest(wear_base_test.WearBaseTestClass):

    watch: android_watch_device.AndroidWatchDevice
    watchface = wear_watchface_constants.UTILITY_WF
    watchface_2 = wear_watchface_constants.DIAL_WF

    def setup_class(self):
        super().setup_class() 
        self.watch = self.register_controller(android_watch_device)[0]
        watchface_lab_util.prepare_test_mode(self.watch)
        mcu_util.environment_info_to_log(self.watch)
        self.watch.log.info('AP Build ID: %s', self.watch.build_info['build_version_incremental'])
        watchface_lab_util.enable_remote_watchface_operation(self.watch)

    def setup_test(self):
        super().setup_test()
        wf_set = watchface_lab_util.add_and_set_watchface(self.watch, self.watchface)
        asserts.assert_equal(wf_set, self.watchface, f'watchface not set {self.watchface}')
        self.watch.log.info(f'watchface set successfully {self.watchface}')
        time.sleep(3)

    def teardown_class(self):
        super().teardown_class()
        watchface_lab_util.remove_watchface(self.watch, self.watchface)
        time.sleep(constants.ONE_SEC_SLEEP_SEC)

    def test_watchface_editor(self):
        watchface_lab_util.add_and_set_watchface(self.watch, self.watchface)
        watchface_lab_util.launch_watchface_editor(self.watch, self.watchface)
        editor_page = watchface_lab_util.navigate_to_editor_page(self.watch, wear_watchface_constants.BOOL)
        watchface_lab_util.close_watchface_editor(self.watch)
        time.sleep(constants.ONE_SEC_SLEEP_SEC)
        watchface_lab_util.add_and_set_watchface(self.watch, self.watchface_2)
        editor =  watchface_lab_util.launch_watchface_editor(self.watch, self.watchface_2)

        asserts.assert_false(editor_page, editor)


if __name__ == '__main__':
    mobly_g3.main()

        