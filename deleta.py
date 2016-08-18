#!/usr/bin/env python
# coding:utf-8

#DESCRICAO
#Esse script foi desenvolvido para facilitar a forma como cadastramos, 
#alteramos ou excluímos os principais ativos em dois ou mais servidores zabbix.
#A ideia é utilizar esse script para ambientes onde os eventos não estão sincronizados, 
#permitindo uma ótima facilidade e agilidade nesses processos.
# Author: Vinicius Trancoso Bitencourt - <http:github/viniciustbitencourt>
#
# FileName: deleta.py

import sys
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

config = SafeConfigParser()
config.read('conf.ini')

host01 = config.get('zabbix01', 'hostname')
usr01 = config.get('zabbix01', 'user')
pwd01 = config.get('zabbix01', 'passwd')

host02 = config.get('zabbix02', 'hostname')
usr02 = config.get('zabbix02','user')
pwd02 = config.get('zabbix02','passwd')

zapi = ZabbixAPI(host01)
zapi2 = ZabbixAPI(host02)

zapi.login(usr01, pwd01)
zapi2.login(usr02, pwd02)

class DeletaHosts(object):
	pass
	
	print "**************************************************************************"
	print "************ SCRIPT - EXCLUI HOSTS EM DOIS SERVIDORES ********************"
	print "*	    FAVOR INSERIR TODOS OS DADOS CORRETAMENTE  	                *"
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
