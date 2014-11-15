.. title: Extending Netkit-NG Core
.. slug: core
.. date: 2014/10/29 10:26:17
.. type: text

Get the sources
===============

On Github: `netkit-ng-core`_ (latest version is 3.0.4)

Master branch contains the latest stable release. Develop branch is to push 
new features or fixing bugs.

Build netkit-ng-core from sources
=================================

To build the netkit-core archive:

.. code-block:: sh

    $ git clone git@github.com:netkit-ng/netkit-ng-core.git
    $ cd netkit-core
    $ git checkout master
    $ make package

Bugs, help...
=============

* Search for help in channel #netkit on freenode.
* If you want to contribute, please fork the 'develop' branch and request 
  pulls.
* Report bug on the `netkit-ng-core bug tracker`_

Changes
=======

Version 3.0.4
  * removing documentation to move it to http://netkit-ng.github.io/
  * fixing build 

Version 3.0.3 
  * Fix #3: check-configuration script returns warning about parse file not 
    supported on ext4
  * force `LANG_C` to all scripts to avoid internationalization errors
  * Fix #4: Missing dynamic library dependency when calling vhalt
  * Add tests to check if filesystem supports sparse file for FS and model FS

Version 3.0.2
  * archive name and directory start with netkit-ng to avoid clash with 
    original netkit

Version 3.0.1
  * fixing error during `README.mdown` copy into archive during build

Version 3.0
  * switching to new major version, as scripts are now expecting new fs 
    organization
  * moving console profile to tools directory

Version 2.12
  * uml tools patches are included in git from now
  * moving to new root filesystem from netkit-uml-build

Version 2.11
  * It is now possible to run only bin/manage_tuntap script via sudo, not /bin/
    sh. (sv75)

Version 2.10
  * support for 32 and 64 bits architecture for UML tools
  * add binary check during check_configuration.d (to detect problem when the 
    user install the wrong version of netkit in respect of his host 
    architecture).

Version 2.9
  * renaming vconfig to vconf (zioproto)
  * support for connection mconsole (babazka)
  * support for vdump (via uml_dump): small utility to connect wireshark or 
    tcpdump directly to a uml_switch
  * add Ktabstart, a tool to run netkit session within konsole tabs (sv75)
  * better looking excludes in Makefile (Markus Stenberg)
  * sources of the uml tools are in src/ directory and patches are applied 
    during build
  * removing previous uml tools binaries
  * removing obsolete goals in Makefile

.. _`netkit-ng-core`: https://github.com/netkit-ng/netkit-ng-core/
.. _`netkit-ng-core bug tracker`: https://github.com/netkit-ng/netkit-ng-core/issues
