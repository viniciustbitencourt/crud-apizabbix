#!/usr/bin/env python
# coding:utf-8

import sys
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

class CadastrarHosts(object):
	pass

	print "*************************************************************************"
	print "********BEM VINDO - CADASTRO CADA HOST EM DOIS SERVIDORES ***************"
	print "*             FAVOR INSERIR TODOS OS DADOS CORRETAMENTE!                *"
	print "*************************************************************************"

	host = raw_input('Digite o nome do host: ')
	grupo = raw_input('Digite o nome do grupo: ')
	ip = raw_input('Digite o ip do equipamento: ')
	
	def zabbixLogin(path, host, grupo, ip):
		config = SafeConfigParser()
		config.read(path)
		
		#Zabbix
		hostname = config.get('runtest', 'hostname')
		user = config.get('runtest', 'user')
		pwd = config.get('runtest', 'passwd')
		
		zapi = ZabbixAPI(hostname)
		zapi.login(user, pwd)
		
		zapi.host.create(
        	{
                	"host": host,
                	"interfaces":[{
                        	"type": 1,
                        	"main": 1,
                        	"useip": 1,
                        	"ip": ip,
                        	"dns": "",
                        	"port": "10050"
                	}],
                	"groups" : [{"groupid": group_id}],
                	"templates": [{"templateid": template_id}],
        	})
		print "OK DEU CERTO !!!"

	def validaDados(host, grupo, ip):
		if host == "":
			print "Digite o nome do equipamento corretamente!!!"
			sys.exit(0)
		elif grupo == "":
			print "Digite o nome do grupo corretamente !!!"
			sys.exit(0)
		elif ip == "":
			print "Digite o IP do equipamento corretamente !!!"
			sys.exit(0)
	
	#zapi.hostgroup.get({"filter": {"name" : grupo}})[0]['groupid']
	#group_id2 = zapi2.hostgroup.get({"filter": {"name" : grupo}})[0]['groupid']

        #zapi.template.get({"filter": {"name": 'Template ICMP Ping'}})[0]['templateid']
        #template_id2 = zapi2.template.get({"filter": {"name": 'Template ICMP Ping'}})[0]['templateid']
	
	#envio2 = zapi2.host.create(
        #{
        #        "host": host,
        #       "interfaces":[{
        #                "type": 1,
        #                "main": 1,
        #                "useip": 1,
        #                "ip": ip,
        #                "dns": "",
        #                "port": "10050"
        #        }],
        #        "groups" : [{"groupid": group_id2}],
        #        "templates": [{"templateid": template_id2}],
        #})

        #print ("O equipamento " + host + " foi incluido com sucesso !!!")
	
	if __name__ == "__main__":
		path = "conf.ini"
		zabbixLogin(path, host, grupo, ip)
		validaDados(host, grupo, ip)

	
