.. title: Extending Netkit-NG Kernel and Filesystem
.. slug: build
.. date: 2014/10/29 10:26:17
.. type: text


Get the sources
===============

On Github: `netkit-ng-build`_ (latest version is 0.1.3)

Master branch contains the latest stable release. Develop branch is to push 
new features or fixing bugs.

Build netkit-ng-core from sources
==============================================

It is recommended to build the kernal and fs on a non-critical VM running a 
fresh install of Debian wheezy, as the install requires root rights.

To build the fs and kernel, you need to configure NAT as rootstrap builds the 
filesystem inside an UML VM:

.. code-block:: sh

    $ iptables -j MASQUERADE -t nat -o eth0 -A POSTROUTING

Then:

.. code-block:: sh

    $ git clone git@github.com:netkit-ng/netkit-ng-build.git
    $ cd netkit-ng-build
    $ git checkout master
    $ make

Add a debian package in the filesystem
======================================

The list of installed packages (beside base packages) are listed int the 
`packages-list`_ file: 

* Add your new applications into the file `package-list` of the `fs` directory
* Add the daemon name into the file `disabled-services` of the `fs` directory 
  (to disable it at boot)
* Build the fs with `make fs`

Add a new file or modify a file in the filesystem
=================================================

* Add the file in the 'fs/filesystem-tweaks'
* Build the fs with `make fs`

Bugs, help...
=============

* Search for help in channel #netkit on freenode.
* If you want to contribute, please fork the 'develop' branch and request 
  pulls.
* Report bug on the `netkit-ng-build bug tracker`_

Changes
=======

Version 0.1.3
  * Moving documentation to https://netkit-ng.github.io
  * replace openswan by strongswan
  * add xl2tpd to packages list
  * fix ppp add in packages list
  * add version to archive name

Version 0.1.2
  * enable networking init.d at startup

Version 0.1.1
  * disable lvm2 asinit.d service
  * remove lvm2 from packages-list
  * directory is now `netkit-ng`
  * add lxc and openswan

Version 0.1.1
  * first release

.. _`netkit-ng-build`: https://github.com/netkit-ng/netkit-ng-build/
.. _`packages-list`: https://github.com/netkit-ng/netkit-ng-build/blob/master/fs/packages-list
.. _`netkit-ng-build bug tracker`: https://github.com/netkit-ng/netkit-ng-build/issues
