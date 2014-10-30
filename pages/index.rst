.. title: Netkit-NG Homepage
.. slug: index
.. date: 2014/10/29 10:26:17
.. tags:
.. link:
.. description:
.. type: text

What is Netkit-NG
=================

Netkit-NG is a fork of `the Netkit project`_ to bring 
new functionnalities and support for recent debian kernels and filesystems:

* `netkit-ng-build`_ is a set of reusable scripts to build the fs and kernel binaries for Netkit. The solution is based on `rootstrap` (a script to build UML fs maintained by debian team) and the kernels provided by Debian. At the present time, only Wheezy is supported.
* `netkit-ng-core`_ is an updated version of netkit-core which support the new fs image format and includes other contributions released by various github users.

What is the differences between Netkit-NG and Netkit ?
======================================================

Netkit-NG
  * filesystem and kernel based on Debian Wheezy
  * uml_dump support (UML network sniffer without root rights)
  * The FS and kernel can be rebuild: adding / removing packages and change kernel options are possible

Netkit
  * filesystem and kernel based on Debian lenny (deprected since 02/2012)
  * stable since a long time
  * includes MPLS patches

Latest release
==============

Binaries (for end-users):
  * The netkit-NG core version 3.0.4: `netkit-ng-core-32-3.0.4.tar.bz2`_
  * The Netkit-NG filesystem version 7.0: `netkit-ng-filesystem-i386-F7.0.tar.bz2`_
  * The Netkit-NG kernel version 3.2: `netkit-ng-kernel-i386-K3.2.tar.bz2`_

Installing Netkit-NG
====================

A complete Netkit-NG distribution consists of three different packages:

* the Netkit-NG "core", which contains commands, documentation and other stuff which is necessary for Netkit to work;
* the Netkit-NG filesystem, which contains the filesystem for virtual machines;
* the Netkit-NG kernel, which contains the kernel used by virtual machines.

Step 1: Download and unpack
---------------------------

Download all the files to the same directory of your choice. Then unpack them by using the following commands:

.. code-block:: sh

    $ tar -xjSf netkit-ng-core-32-3.0.4.tar.bz2
    $ tar -xjSf netkit-ng-filesystem-i386-F7.0.tar.bz2
    $ tar -xjSf netkit-ng-kernel-i386-K3.2.tar.bz2


Step2: Configuration
--------------------

The first step is to set the environment variables:

* `NETKIT_HOME` variable to the name of the directory Netkit has been installed into. 
* `MANPATH` variable must be set to `$NETKIT_HOME/man`
* `PATH` environment variable must include `$NETKIT_HOME/bin`

The simplest way to do it is to run the check configuration script and copy/paste the recommandations. Run the `check_configuration.sh' script in the `netkit-ng` directory by typing:

.. code-block:: sh

    $ ./check_configuration.sh

This script takes care of checking whether your system is configured properly to make Netkit run. Any misconfigurations are signalled and instructions for fixing them are reported as well. If the script exits with success, then Netkit is ready for use.

Changes
-------

Version 3.0.4
  * removing documentation to move it to http://netkit-ng.github.io/
  * fixing build 

Version 3.0.3 
  * Fix #3: check-configuration script returns warning about parse file not supported on ext4
  * force `LANG_C` to all scripts to avoid internationalization errors
  * Fix #4: Missing dynamic library dependency when calling vhalt
  * Add tests to check if filesystem supports sparse file for FS and model FS

Version 3.0.2
  * archive name and directory start with netkit-ng to avoid clash with original netkit

Version 3.0.1
  * fixing error during `README.mdown` copy into archive during build

Version 3.0
  * switching to new major version, as scripts are now expecting new fs organization
  * moving console profile to tools directory

Version 2.12
  * uml tools patches are included in git from now
  * moving to new root filesystem from netkit-uml-build

Version 2.11
  * It is now possible to run only bin/manage_tuntap script via sudo, not /bin/sh. (sv75)

Version 2.10
  * support for 32 and 64 bits architecture for UML tools
  * add binary check during check_configuration.d (to detect problem when the user install the wrong version of netkit in respect of his host architecture).

Version 2.9
  * renaming vconfig to vconf (zioproto)
  * support for connection mconsole (babazka)
  * support for vdump (via uml_dump): small utility to connect wireshark or tcpdump directly to a uml_switch
  * add Ktabstart, a tool to run netkit session within konsole tabs (sv75)
  * for developpers:

    - better looking excludes in Makefile (Markus Stenberg)
    - sources of the uml tools are in src/ directory and patches are applied during build
    - removing previous uml tools binaries
    - removing obsolete goals in Makefile

.. _`netkit-ng-build`: https://github.com/netkit-ng/netkit-ng-build/
.. _`netkit-ng-core`: https://github.com/netkit-ng/netkit-ng-core/
.. _`the Netkit project`: http://www.netkit.org/
.. _netkit-ng-core-32-3.0.4.tar.bz2: https://github.com/netkit-ng/netkit-ng-core/releases/download/3.0.4/netkit-ng-core-32-3.0.4.tar.bz2
.. _netkit-ng-filesystem-i386-F7.0.tar.bz2: https://github.com/netkit-ng/netkit-ng-build/releases/download/0.1.2/netkit-ng-filesystem-i386-F7.0.tar.bz2
.. _netkit-ng-kernel-i386-K3.2.tar.bz2: https://github.com/netkit-ng/netkit-ng-build/releases/download/0.1.2/netkit-ng-kernel-i386-K3.2.tar.bz2
