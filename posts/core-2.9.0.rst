.. title: netkit-ng-core 2.9.0
.. date: 2013/04/25 10:26:17
.. tags: core, release
.. type: text

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
