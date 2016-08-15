#!/usr/bin/env python
# coding:utf-8

#DESCRICAO
#Esse script foi desenvolvido para facilitar a forma como cadastramos, 
#alteramos ou excluímos os principais ativos em dois ou mais servidores zabbix.
#A ideia é utilizar esse script para ambientes onde os eventos não estão sincronizados, 
#permitindo uma ótima facilidade e agilidade nesses processos.
# Author: Vinicius Trancoso Bitencourt - <http:github/viniciustbitencourt>
# FileName: cadastro.py

import sys
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

config = SafeConfigParser()
config.read('conf.ini')

host = config.get('runtest', 'hostname')
usr = config.get('runtest', 'user')
pwd = config.get('runtest', 'passwd')

hostm1 = config.get('auth', 'hostname')
usrm1 = config.get('auth', 'user')
pwdm1 = config.get('auth', 'passwd')

zapi = ZabbixAPI(host)
zapi2 = ZabbixAPI(hostm1)

zapi.login(usr, pwd)
zapi2.login(usrm1, pwdm1)

class CadastrarHosts(object):
	pass

	print "*************************************************************************"
	print "********BEM VINDO - CADASTRA CADA HOST EM DOIS SERVIDORES ZABBIX*********"
	print "*             FAVOR INSERIR TODOS OS DADOS CORRETAMENTE!                *"
	print "*************************************************************************"

	host = raw_input('Digite o nome do host: ')
	grupo = raw_input('Digite o nome do grupo: ')
	ip = raw_input('Digite o ip do equipamento: ')

	def valida_dados(host, grupo, ip):
		if host == "":
			print "Digite o nome do equipamento corretamente!!!"
			sys.exit(0)
		elif grupo == "":
			print "Digite o nome do grupo corretamente !!!"
			sys.exit(0)
		elif ip == "":
			print "Digite o IP do equipamento corretamente !!!"
			sys.exit(0)

	valida_dados(host, grupo, ip)
	
	group_id = zapi.hostgroup.get({"filter": {"name" : grupo}})[0]['groupid']
	group_id2 = zapi2.hostgroup.get({"filter": {"name" : grupo}})[0]['groupid']

        template_id = zapi.template.get({"filter": {"name": 'Template ICMP Ping'}})[0]['templateid']
        template_id2 = zapi2.template.get({"filter": {"name": 'Template ICMP Ping'}})[0]['templateid']

	envio = zapi.host.create(
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
	
	envio2 = zapi2.host.create(
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
                "groups" : [{"groupid": group_id2}],
                "templates": [{"templateid": template_id2}],
        })

        print ("O equipamento " + host + " foi incluido com sucesso !!!")
