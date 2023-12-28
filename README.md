# android-system-build.prop

Android /system/build.prop from official ROMs.

Include both raw `build.prop` and JSON format [props.json](https://raw.githubusercontent.com/mingchen/android-system-build.prop/main/props.json) for easy to use.

## props Folder Structure

```
props/<Vendor>/<Device Model>/<Android Version>/<Build ID>/build.prop
```

`<Device Model>`, `<Build ID>` (or `Build number`) can be found in `Settings` -> `About phone`.

`<Build ID>` also inside `build.prop`, the key is `ro.build.id`. e.g.

```
ro.build.id=QP1A.191005.007.A3
```

e.g.

```
Pixel-XL/10.0.0/QP1A.191005.007.A3/build.prop
```

## How to extract `/system/build.prop` from OTA image?

1. Download OTA image from [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)


2. Unpack OTA image with [android-ota-extractor](https://github.com/tobyxdd/android-ota-payload-extractor). For example, The following command extract "marlin" for Pixel XL version 10.0.0 (QP1A.191005.007.A3, Dec 2019):

```sh
$ android-ota-extractor marlin-ota-qp1a.191005.007.a3-23002a57.zip
```

You will get `system.img`, it is a Linux  `ext2` image file.

```sh
$ file system.img
system.img: Linux rev 1.0 ext2 filesystem data, UUID=4729639d-b5f2-5cc1-a120-9ac5f788683c (extents) (large files) (huge files)
```

3. Mount `system.img` under Linux:

```sh
$ sudo mount -o loop,ro system.img /mnt
$ sudo cp /mnt/system/build.prop /tmp/build.prop
```

Now you get a copy of `build.prop` in `/tmp/build.prop`. Feel feel to fork this repo and send a PR to add your `build.prop`.

## References

- [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images)
- [android-ota-extractor](https://github.com/tobyxdd/android-ota-payload-extractor)