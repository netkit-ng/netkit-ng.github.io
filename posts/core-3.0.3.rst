.. title: netkit-ng-core 3.0.3
.. date: 2014/09/26 11:26:17
.. tags: core, release
.. type: text

* Fix `#3 <https://github.com/netkit-ng/netkit-ng-core/issues/3>`__: 
  check-configuration script returns warning about parse file not supported 
  on ext4
* force `LANG_C` to all scripts to avoid internationalization errors
* Fix `#4 <https://github.com/netkit-ng/netkit-ng-core/issues/4>`__: Missing 
  dynamic library dependency when calling vhalt
* Add tests to check if filesystem supports sparse file for FS and model FS
