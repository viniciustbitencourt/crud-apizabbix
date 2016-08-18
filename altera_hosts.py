#!/usr/bin/env python
# coding:utf-8

#DESCRICAO
#Esse script foi desenvolvido para facilitar a forma como cadastramos, 
#alteramos ou excluímos os principais ativos em dois ou mais servidores zabbix.
#A ideia é utilizar esse script para ambientes onde os eventos não estão sincronizados, 
#permitindo uma ótima facilidade e agilidade nesses processos.
#A integracao e realizada via Zabbix API
# Author: Vinicius Trancoso Bitencourt - <http:github/viniciustbitencourt>
#
# FileName: altera_hosts.py

import sys
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

#Arquivo de configuracao com os parametros conf.ini
config = SafeConfigParser()
config.read('conf.ini')

#pega os valores do arquivo de configuracao
host01 = config.get('zabbix01', 'hostname')
usr01 = config.get('zabbix01', 'user')
pwd01 = config.get('zabbix01', 'passwd')

#pega os valores do arquivo de configuração
host02 = config.get('zabbix02', 'hostname')
usr02 = config.get('zabbix02', 'user')
pwd02 = config.get('zabbix02', 'passwd')

#API Zabbix com a URL de cada Servidor
zapi = ZabbixAPI(host01)
zapi2 = ZabbixAPI(host02)

#Faz login com a API Zabbix
zapi.login(usr01, pwd01)
zapi2.login(usr02, pwd02)

class AlteraHosts(object):
	pass
	
	##TELA DE EXIBICAO
	print "***************************************************************************"
        print "*********** SCRIPT - ALTERA HOSTS EM DOIS SERVIDORES ZABBIX ***************"
        print "*             FAVOR INSERIR TODOS OS DADOS CORRETAMENTE!                  *"
        print "***************************************************************************"
	print'1 - PARA ALTERAR O NOME DO EQUIPAMENTO'
	print'2 - PARA ALTERAR O IP DO EQUIPAMENTO'
	print'3 - PARA SAIR DESSA TELA  !'
	
	#Pega opcao selecionada
	a = raw_input('Digite a Opção desejada: ')
	
	if a == '1':
		host  = raw_input('Digite o NOME do HOST: ')
        	rename = raw_input('Digite o nome que deseja alterar: ')
		
		#Funcao valida os dados digitados
		def valida_dados(host, rename):
                        if host == "":
                                print 'Digite corretamente o NOME do HOST corretamente!'
                                sys.exit(0)
                        elif rename == "":
                                print 'Digite o NOME do HOST que deseja alterar corretamente!'
                                sys.exit(0)
                valida_dados(host, rename)		

		#Zabbix API - Altera no Zabbix
        	for x in zapi.host.get({'filter': {'name': host}}):
                	host_id = x['hostid']
        	altera = zapi.host.update({'hostid': host_id, 'host': rename, 'status': 0})
		
		#Zabbix API - Altera no Zabbix
		for y in zapi2.host.get({'filter': {'name':host}}):
			host_id2 = y['hostid']
		altera2 = zapi2.host.update({'hostid': host_id2, 'host': rename, 'status': 0})
	
        	print ('Equipamento - ' + host + ' - alterado NOME para: ' + rename)
	
	elif a == '2':
		host  = raw_input('Digite o NOME do equipamento: ')
        	rename = raw_input('Digite o IP que deseja alterar: ')
	
		#Funcao valida os dados digitados
		def valida_dados(host, rename):
                	if host == "":
                        	print 'Digite corretamente o NOME do equipamento corretamente!'
                        	sys.exit(0)
                	elif rename == "":
                        	print 'Digite o IP que deseja alterar corretamente!'
                        	sys.exit(0)
		valida_dados(host, rename)

		#Zabbix API - Altera IP Zabbix Primeiro Servidor	
        	for x in zapi.host.get({'filter': {'name': host}}):
                	host_id = x['hostid']

        	for x in zapi.hostinterface.get({'hostids': host_id}):
                	host_interface = x['interfaceid']
		
		alteraip = zapi.hostinterface.update({'interfaceid': host_interface, 'ip': rename})

		#Zabbix API - Altera IP Zabbix Segundo Servidor
		for y in zapi2.host.get({'filter': {'name': host}}):
                        host_id2 = y['hostid']

                for y in zapi2.hostinterface.get({'hostids': host_id2}):
                        host_interface2 = y['interfaceid']

       		alteraip2 = zapi2.hostinterface.update({'interfaceid': host_interface2, 'ip': rename})
        	print ('Equipamento - ' + host +' - alterado IP para: '+ rename)	
	
	else:
		print 'OPÇÃO INVALIDA - FIM!!'
		sys.exit(0)

