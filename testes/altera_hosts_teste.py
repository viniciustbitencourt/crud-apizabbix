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
	
	print "*************************************************************************"
        print "******************ALTERA HOSTS - EM DOIS SERVIDORES ZABBIX***************"
        print "*             FAVOR INSERIR TODOS OS DADOS CORRETAMENTE!                *"
        print "*************************************************************************"
	print'1 - PARA ALTERAR O NOME DO EQUIPAMENTO'
	print'2 - PARA ALTERAR O IP DO EQUIPAMENTO'
	print'3 - PARA SAIR DESSA TELA  !'
	
	a = raw_input('Digite a Opção desejada: ')
	
	if a == '1':
		host  = raw_input('Digite o NOME do HOST: ')
        	rename = raw_input('Digite o nome que deseja alterar: ')

		def valida_dados(host, rename):
                        if host == "":
                                print 'Digite corretamente o NOME do HOST corretamente!'
                                sys.exit(0)
                        elif rename == "":
                                print 'Digite o NOME do HOST que deseja alterar corretamente!'
                                sys.exit(0)
                valida_dados(host, rename)		
		
        	for x in zapi.host.get({'filter': {'name': host}}):
                	host_id = x['hostid']
        	zapi.host.update({'hostid': host_id, 'host': rename, 'status': 0})
        	print ('Equipamento - ' + host + ' - alterado NOME para: ' + rename)
	
	elif a == '2':
		host  = raw_input('Digite o NOME do equipamento: ')
        	rename = raw_input('Digite o IP que deseja alterar: ')
		
		def valida_dados(host, rename):
                	if host == "":
                        	print 'Digite corretamente o NOME do equipamento corretamente!'
                        	sys.exit(0)
                	elif rename == "":
                        	print 'Digite o IP que deseja alterar corretamente!'
                        	sys.exit(0)
		valida_dados(host, rename)

        	for x in zapi.host.get({'filter': {'name': host}}):
                	host_id2 = x['hostid']

        	for x in zapi.hostinterface.get({'hostids': host_id2}):
                	host_interface = x['interfaceid']

       		zapi.hostinterface.update({'interfaceid': host_interface, 'ip': rename})
        	print ('Equipamento - ' + host +' - alterado IP para: '+ rename)	
	
	else:
		print 'OPÇÃO INVALIDA - FIM!!'
		sys.exit(0)

