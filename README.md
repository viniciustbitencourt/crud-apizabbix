<h1>crud-apizabbix</h1>

<p>This script was developed to insert,
alter or exclude the main assets in two or more zabbix servers.
The idea is to use this script for environments where events are not synchronized,
allowing a great ease and agility in these processes.</p>

<h3>Installation</h3>
<pre>
<b>Clone project</b>
git clone https://github.com/viniciustbitencourt/crud-apizabbix.git

<b>Install dependencies</b>
pip install zabbix_api
python version 2.7.11(lastet)
</pre>

<h3>Configuration</h3>
<pre>Configuration - <b>conf.ini</b>

<b>Zabbix Configuration</b>
<i>[zabbix01]</i>
hostname = hostname of the first server zabbix
user = username of the server
passwd = password of the server

<i>[zabbix02]</i>
hostname = hostname of the second server zabbix
user = username of the server
passwd = password of the server

</pre>
