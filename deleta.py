#!/usr/bin/env python
# coding:utf-8

#DESCRICAO
#Esse script foi desenvolvido para facilitar a forma como cadastramos, 
#alteramos ou excluímos os principais ativos em dois ou mais servidores zabbix.
#A ideia é utilizar esse script para ambientes onde os eventos não estão sincronizados, 
#permitindo uma ótima facilidade e agilidade nesses processos.
# Author: Vinicius Trancoso Bitencourt - <http:github/viniciustbitencourt>
# FileName: deleta.py

import sys
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

config = SafeConfigParser()
config.read('conf.ini')

host = config.get('runtest', 'hostname')
usr = config.get('runtest', 'user')
pwd = config.get('runtest', 'passwd')

hostm1 = config.get('auth', 'hostname')
usrm1 = config.get('auth','user')
pwdm1 = config.get('auth','passwd')

zapi = ZabbixAPI(host)
zapi2 = ZabbixAPI(hostm1)

zapi.login(usr, pwd)
zapi2.login(usrm1, pwdm1)

class DeletaHosts(object):
	pass
	
	print "**************************************************************************"
	print "********* BEM VINDO - EXCLUI HOSTS EM DOIS SERVIDORES ********************"
	print "*	      FAVOR INSERIR TODOS OS DADOS CORRETAMENTE  	        *"
	print "**************************************************************************"
	
	host = raw_input('Digite o NOME do equipamento que será EXCLUIDO: ')
	confirm = raw_input('Deseja realmente excluir esse host ? Tecle "S": ')

	def valida_dados(host):
		if host == "":
			print "Digite o nome do equipamento corretamente !!!"	
			sys.exit(0)

	valida_dados(host)		

	if confirm == 'S':	
		for x in zapi.host.get({"filter": {"name": host}}):
			x['hostid']
		deleta = zapi.host.delete([int(x['hostid'])])

		for y in zapi2.host.get({"filter": {"name": host}}):
			y['hostid']
		deleta2 = zapi2.host.delete([int(y['hostid'])])
		
		print "Equipamento excluido %s" % host

	else:
		print 'Favor confirmar a exclusão do equipamento !'
		sys.exit(0)
