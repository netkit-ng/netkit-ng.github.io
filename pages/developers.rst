.. title: Extending Netkit-NG
.. slug: extending
.. date: 2014/10/29 10:26:17
.. tags:
.. link:
.. description:
.. type: text

Get the sources
===============

On Github:
  * `netkit-ng-build`_ (latest version is 0.1.2)
  * `netkit-ng-core`_ (latest version is 3.0.4)

Master branches contain the latest stable release. Develop branches is to push new features or fixing bugs.

How can I re-build Netkit-NG from sources
=========================================

It is recommended to build the sources on an non-critical VM running a fresh install of Debian wheezy, as the install requires root rights.

To build the netkit-core archive:

.. code-block:: sh

    $ git clone git@github.com:netkit-ng/netkit-ng-core.git
    $ cd netkit-core
    $ git checkout 3.0.2
    $ make package

To build the fs and kernel, you need to configure NAT as rootstrap build the filesystem inside an UML VM:

.. code-block:: sh

    $ iptables -j MASQUERADE -t nat -o eth0 -A POSTROUTING

Then:

.. code-block:: sh

    $ git clone git@github.com:netkit-ng/netkit-ng-build.git
    $ cd netkit-ng-build
    $ git checkout master
    $ make

How can I add a new package ?
=============================

Using `netkit-uml-build`:

* Add your new applications into the file `package-list` of the `fs` directory
* Add the daemon name into the file `disabled-services` of the `fs` directory
* Rebuild the fs 

Bugs, help...
=============

Search for help in channel #netkit on freenode.

If you want to contribute, please fork the 'develop' branch and request pulls.

Bug trackers:

* `netkit-ng-build bug tracker`_ to report bug on fs and kernel.
* `netkit-ng-core bug tracker`_ to report bug on Netkit-NG tools.

.. _`netkit-ng-build`: https://github.com/netkit-ng/netkit-ng-build/
.. _`netkit-ng-core`: https://github.com/netkit-ng/netkit-ng-core/
.. _`list of packages`:
.. _`netkit-ng-build bug tracker`: https://github.com/netkit-ng/netkit-ng-build/issues
.. _`netkit-ng-core bug tracker`: https://github.com/netkit-ng/netkit-ng-core/issues
