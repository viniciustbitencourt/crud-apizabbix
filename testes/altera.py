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
	
	host  = raw_input('Digite o NOME do HOST: ')
	rename = raw_input('Digite o nome que deseja alterar: ')
	
	for x in zapi.host.get({'filter': {'name': host}}):
		host_id = x['hostid']
	print host_id
	zapi.host.update({'hostid': host_id, 'host': rename, 'status': 0})
	print 'equipamento alterado com sucesso!'
