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

class GetHosts(object):
	pass
	confirm_host = raw_input('Deseja alterar o nome do equipamento (S) para confirmar: ')
	
	if confirm_host == 'S':
	
	#ip = raw_input('Digite o IP do host: ')
	#rename_ip = raw_input('Digite o IP do host para alterar: ')
	
	if confirm_host == 'S':
	
		host = raw_input('Digite o nome o host: ')
		rename = raw_input('Digite o nome do host para alterar: ')
	
		for x in zapi.host.get({'filter': {'name': host}}):
			host_id = x['hostid']

		print zapi.host.update({'hostid': host_id, 'host': rename, 'status': 0})
		print 'Equipamento alterado !!!!'
	else:
		confirm_ip = raw_input('Deseja alterar o IP do equipamento: (S) para confirmar: ')
	
	if confirm_ip == 'S':

		ip = raw_input('Digite o IP do host: ')
        	rename_ip = raw_input('Digite o IP do host para alterar: ')
	
	#print zapi.host.update({'hostid': host_id, 'host': rename, 'status': 0})

	#zapi.host.update([int(x['hostid'])])
	#print "host excluido ! %s" % host
	
	#zapi.host.delete( [{'hostid': a['hostid'] }] )
	#print zapi.host.delete(host_id)
	#host_id = zapi.host.get({"output": "extend", "hostids":{ "host":[host]}})
	#print host_id
	#print list_delete
	#print host_id
	#print zapi.host.delete(list_delete)
