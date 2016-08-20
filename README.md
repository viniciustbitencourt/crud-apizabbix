<h1>crud-apizabbix</h1>

<p>
Esse script foi desenvolvido para facilitar a forma como cadastramos,
alteramos ou excluímos os principais ativos em dois ou mais servidores zabbix.
A ideia é utilizar esse script para ambientes onde os eventos não estão sincronizados,
permitindo uma ótima facilidade e agilidade nesses processos.</p>

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
hostname = hostname of the first server in zabbix 
user = username of the server
passwd = password of the server

<i>[zabbix02]</i>
hostname = hostname of the second server in zabbix
user = username of the server
passwd = password of the server

</pre>
