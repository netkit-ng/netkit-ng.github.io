.. title: UML-dump
.. slug: umldump
.. date: 2014/10/29 10:26:17
.. tags:
.. link:
.. description:
.. type: text


Netkit-NG includes support for `uml_dump`. 

`uml_dump` is a program for UML tools (various tools to connect several User-mode Linux instances 
together) developed by Julien Iguchi-Cartigny and two students (Jean-Baptiste Machemie and Benoit 
Bitarelle) during Spring 2009. It dumps packets from the virtual switch (`uml_switch`) using CAP 
format to the standard output. Thus, it is possible to see packets exchanged between UML machines in any CAP 
viewer (for instance wireshark or tcpdump) or save packets in a file.

It was already possible to dump packet using the original Netkit but it requires root access and 
TUN/TAP tunnels (not very useful using shared Linux computers).

Usage
=====


.. code-block:: sh

    $ vdump switch_name

Where `switch_name` is the network id shared between machines using the same collision domain in 
Netkit. For instance, to dump all packet from the network A and print them using wireshark:

.. code-block:: sh

    $ vdump A | wireshark -i - -k

Behind the scene, the `vdump` command calls `uml_dump`:

.. code-block:: sh

    $ uml_dump fifo

where fifo is the named pipe to connect to the `uml_switch` instance. If omitted `/tmp/uml.ctl` 
is used.
