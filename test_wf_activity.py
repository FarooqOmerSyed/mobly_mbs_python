from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device
import subprocess

class WFActivityTest(base_test.BaseTestClass):

    def setup_class(self):
        self.ad = self.register_controller(android_device, min_number=1)[0]
        self.ad.load_snippet('api', 'com.google.android.mobly.snippet.bundled')

    def click_on_activity(self, activity_name):
        try:
            subprocess.run(["adb", "shell", "am", "start", "-n", activity_name])
            print(f"Successfully clicked on activity: {activity_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to click on activity: {activity_name}")
            print(f"Reason: {e}")

    def test_click_activity(self):
        activity_to_click = "com.google.android.wearable.watchface.rwf/com.google.android.wearable.watchface.classica.ClassicaWatchFaceService"
        self.click_on_activity(activity_to_click)

if __name__ == '__main__':
    test_runner.main()

    # run this command in terminal 
    # python3 test_wf_activity.py -c config.yml