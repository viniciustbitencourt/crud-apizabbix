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
	#host = raw_input('Digite o nome do equipamento: ')
	
	print zapi.host.get(output=['host', 'groups', 'status'], selectInterfaces=['ip'], selectGroups=['name'])
	
	
	#host = raw_input('Digite o nome o host: ')
	
        #print zapi.host.get({"output": host ["hostid"][0]['hostid']
		
	#host = raw_input('Digite o nome o host: ')
	#hosts =  zapi.hostinterface.get({"output": "extend", "ip": host})[0]['ip']
	#hosts = zapi.host.get({"output": ["hostid"], "filter": {"host":host}})
	#hosts = ["11468"]
	#print hosts
	#a = zapi.host.delete(hosts)
	#print a	
	#get = zapi.host.massremove(
	#{
	#	"params": {
	#		"hostids":[
	#		"10735",
	#		"10770"
	#	]
	#	},
	#})
	
	#print ("O equipamento e " + host_id)
