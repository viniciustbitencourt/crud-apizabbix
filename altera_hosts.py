#!/usr/bin/env python
# coding:utf-8

#DESCRICAO
#Esse script foi desenvolvido para facilitar a forma como cadastramos, 
#alteramos ou excluímos os principais ativos em dois ou mais servidores zabbix.
#A ideia é utilizar esse script para ambientes onde os eventos não estão sincronizados, 
#permitindo uma ótima facilidade e agilidade nesses processos.
#A integracao e realizada via Zabbix API
# Author: Vinicius Trancoso Bitencourt - <http:github/viniciustbitencourt>
# Zabbix API Versão 2.1
# FileName: altera_hosts.py

import sys
from ConfigParser import SafeConfigParser
from zabbix_api import ZabbixAPI

#Arquivo de configuracao com os parametros conf.ini
config = SafeConfigParser()
config.read('conf.ini')

#pega os valores do arquivo de configuracao QTD
host = config.get('runtest', 'hostname')
usr = config.get('runtest', 'user')
pwd = config.get('runtest', 'passwd')

#pega os valores do arquivo de configuração M1
hostm1 = config.get('auth', 'hostname')
usrm1 = config.get('auth', 'user')
pwdm1 = config.get('auth', 'passwd')

#API Zabbix com a URL de cada Servidor
zapi = ZabbixAPI(host)
zapi2 = ZabbixAPI(hostm1)

#Faz login com a API Zabbix
zapi.login(usr, pwd)
zapi2.login(usrm1, pwdm1)

class AlteraHosts(object):
	pass
	
	##TELA DE EXIBICAO
	print "*************************************************************************"
        print "******************ALTERA HOSTS - EM DOIS SERVIDORES ZABBIX***************"
        print "*             FAVOR INSERIR TODOS OS DADOS CORRETAMENTE!                *"
        print "*************************************************************************"
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

		#Zabbix API - Altera no Zabbix M1
        	for x in zapi.host.get({'filter': {'name': host}}):
                	host_id = x['hostid']
        	altera = zapi.host.update({'hostid': host_id, 'host': rename, 'status': 0})
		
		#Zabbix API - Altera no Zabbix QTD
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

		#Zabbix API - Altera IP Zabbix M1	
        	for x in zapi.host.get({'filter': {'name': host}}):
                	host_id = x['hostid']

        	for x in zapi.hostinterface.get({'hostids': host_id}):
                	host_interface = x['interfaceid']
		
		alteraip = zapi.hostinterface.update({'interfaceid': host_interface, 'ip': rename})

		#Zabbix API - Altera IP Zabbix QTD
		for y in zapi2.host.get({'filter': {'name': host}}):
                        host_id2 = y['hostid']

                for y in zapi2.hostinterface.get({'hostids': host_id2}):
                        host_interface2 = y['interfaceid']

       		alteraip2 = zapi2.hostinterface.update({'interfaceid': host_interface2, 'ip': rename})
        	print ('Equipamento - ' + host +' - alterado IP para: '+ rename)	
	
	else:
		print 'OPÇÃO INVALIDA - FIM!!'
		sys.exit(0)

