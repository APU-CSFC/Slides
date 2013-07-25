How to get python and ipython on windows
========================================
 
get python installed first.
---------------------------
* get python 2.7 for windows at: http://python.org/download/
* install it.
* add python path to your environmental variables.
* [Right Click] My Computer -> Properties -> Advanced System Settings -> Advanced (tab) -> Environmental Variables -> System Variables -> (find) PATH
* [add]::

    ;C:\Python27;C:\Python27\Scripts\

get pip - a tool for installing and managing Python packages installed
----------------------------------------------------------------------
* download http://python-distribute.org/distribute_setup.py
* open **cmd.exe**
* go to your Downloads directory::

    cd Downloads
* execute::

    python distribute_setup.py
*  (might need to restart **cmd.exe**)::

    easy_install pip

get ipython installed via pip
-----------------------------
* open **cmd.exe** if not already and type::

    pip install ipython

get ipython installed via package managers
---------------------------------------------
* open **terminal**
* for Red Hat/CentOS/Fedora and rpm/yum based distros::

    yum install python-ipython -y
* for Debian/Ubuntu/Linux Mint and apt-get/deb based distros::

    apt-get install ipython -y

get requests installed for the tutorial
---------------------------------------
* open **cmd.exe** if not already and type::

    pip install requests
