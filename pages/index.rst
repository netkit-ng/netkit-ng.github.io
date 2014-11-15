.. title: Netkit-NG Homepage
.. slug: index
.. date: 2014/10/29 10:26:17
.. type: text

What is Netkit-NG
=================

Netkit-NG is a fork of `the Netkit project`_ to bring new functionnalities and 
support for recent debian kernels and filesystems:

* `netkit-ng-core`_ is an updated version of netkit-core which support the new 
  fs image format and includes other contributions released by various github 
  users.
* `netkit-ng-build`_ is a set of reusable scripts to build the fs and kernel 
  binaries for Netkit. The solution is based on `rootstrap` (a script to build 
  UML fs maintained by debian team) and the kernels provided by Debian. At the 
  present time, only Wheezy is supported.

What is the differences between Netkit-NG and Netkit ?
======================================================

Netkit-NG
  * filesystem and kernel based on Debian Wheezy
  * uml_dump support (UML network sniffer without root rights)
  * The FS and kernel can be rebuild: adding / removing packages and change 
    kernel options are possible

Netkit
  * filesystem and kernel based on Debian lenny (deprected since 02/2012)
  * stable since a long time
  * includes MPLS patches

Latest release
==============

* The netkit-NG core version 3.0.4: `netkit-ng-core-32-3.0.4.tar.bz2`_
* The Netkit-NG filesystem version 7.0 based on netkit-ng-build version 0.1.3: 
  `netkit-ng-filesystem-i386-F7.0-0.1.3.tar.bz2`_
* The Netkit-NG kernel version 3.2 based on netkit-ng-build version 0.1.3: 
  `netkit-ng-kernel-i386-K3.2-0.1.3.tar.bz2`_

Installing Netkit-NG
====================

A complete Netkit-NG distribution consists of three different packages:

* the Netkit-NG "core", which contains commands, documentation and other stuff 
  which is necessary for Netkit to work;
* the Netkit-NG filesystem, which contains the filesystem for virtual machines;
* the Netkit-NG kernel, which contains the kernel used by virtual machines.

Step 1: Download and unpack
---------------------------

Download all the files to the same directory of your choice. Then unpack them 
by using the following commands:

.. code-block:: sh

    $ tar -xjSf netkit-ng-core-32-3.0.4.tar.bz2
    $ tar -xjSf netkit-ng-filesystem-i386-F7.0-0.1.3.tar.bz2
    $ tar -xjSf netkit-ng-kernel-i386-K3.2-0.1.3.tar.bz2


Step2: Configuration
--------------------

The first step is to set the environment variables:

* `NETKIT_HOME` variable to the name of the directory Netkit has been 
  installed into. 
* `MANPATH` variable must be set to `$NETKIT_HOME/man`
* `PATH` environment variable must include `$NETKIT_HOME/bin`

The simplest way to do it is to run the check configuration script and copy/
paste the recommandations. Run the `check_configuration.sh' script in the `
netkit-ng` directory by typing:

.. code-block:: sh

    $ ./check_configuration.sh

This script takes care of checking whether your system is configured properly 
to make Netkit run. Any misconfigurations are signalled and instructions for 
fixing them are reported as well. If the script exits with success, then 
Netkit is ready for use.

.. _`netkit-ng-build`: link://slug/build
.. _`netkit-ng-core`: link://slug/core
.. _`the Netkit project`: http://www.netkit.org/
.. _netkit-ng-core-32-3.0.4.tar.bz2: https://github.com/netkit-ng/netkit-ng-core/releases/download/3.0.4/netkit-ng-core-32-3.0.4.tar.bz2
.. _netkit-ng-filesystem-i386-F7.0-0.1.3.tar.bz2: https://github.com/netkit-ng/netkit-ng-build/releases/download/0.1.3/netkit-ng-filesystem-i386-F7.0-0.1.3.tar.bz2
.. _netkit-ng-kernel-i386-K3.2-0.1.3.tar.bz2: https://github.com/netkit-ng/netkit-ng-build/releases/download/0.1.3/netkit-ng-kernel-i386-K3.2-0.1.3.tar.bz2
