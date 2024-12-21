from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class StoragePixelTest(base_test.BaseTestClass):

    def setup_class(self):
        self.ad = self.register_controller(android_device, min_number=1)[0]
        self.ad.load_snippet('api', 'com.google.android.mobly.snippet.bundled')
    

    def test_storage_directory(self):
        directory_path = self.ad.api.storageGetExternalStorageDirectory()
        print(directory_path)

    def test_storage_root(self):
        directory_root = self.ad.api.storageGetRootDirectory()
        print(directory_root)


if __name__ == '__main__':
    test_runner.main()
