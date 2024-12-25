import time 
from mobly import asserts
from mobly import mobly_g3 

from google3.devtools.vinson.mobly import wear_base_test 
from google3.devtools.vinson.mobly.controllers import android_watch_device 
from goolge3.wearables.qa.wac.libs import mcu_util 
from google3.wearables.qa.watch.watchfaces.libs import watchface_lab_util 
from google3.wearables.qa.watch.watchfaces.libs import wear_watchface_constants 

class WatchFaceLoaderTest(wear_base_test.WearBaseTest): 
    watch : android_watch_device.AndroidWatchDevice

    def setup_class(self):
        super().setup_class() 
        self.watch = self.register_controller(android_watch_device)[0]
        watchface_lab_util.prepare_test_mode(self.watch)
        mcu_util.environment_info_to_log(self.watch)
        self.watch.log.info('AP Build ID: %s', self.watch.build_info['build_version_incremental'])
        watchface_lab_util.enable_remote_watchface_operation(self.watch)

    def watch_face_loader_test(self):
        for watchface in wear_watchface_constants.RELEASED_WATCHFACES:
            wf_set = watchface_lab_util.add_and_set_watchface(watch = self.watch, watchface_to_set = watchface)
            asserts.assert_equal(wf_set, watchface, f'Watchface {watchface} not set.')
            self.watch.log.info(f'Watchface {watchface} set successfully.')
            time.sleep(10)
            watchface_lab_util.remove_watchface(watch = self.watch, watchface_to_remove = watchface)
            self.watch.log.info(f'Watchface {watchface} removed successfully.')

if __name__ == '__main__':
    mobly_g3.main()
