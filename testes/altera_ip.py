#!/usr/bin/env python
# coding:utf-8

import sys
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

config = SafeConfigParser()
config.read('conf.ini')

host = config.get('runtest', 'hostname')
usr = config.get('runtest', 'user')
pwd = config.get('runtest', 'passwd')

zapi = ZabbixAPI(host)

zapi.login(usr, pwd)

class AlteraHosts(object):
	pass
	
	host  = raw_input('Digite o NOME do equipamento: ')
	rename = raw_input('Digite o IP que deseja alterar: ')
	
	for x in zapi.host.get({'filter': {'name': host}}):
		host_id2 = x['hostid']
	
	for x in zapi.hostinterface.get({'hostids': host_id2}):
		host_interface = x['interfaceid']

	print zapi.hostinterface.update({'interfaceid': host_interface, 'ip': rename})
	print 'Equipamento IP alterado !'
	
