#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coded by ./isilent
# Gausah direcode ya bro :) - Tinggal pake aja apa susahnya si:)
import sys
import time as t
import base64 as b
import os
import random

exec(b.b64decode("aXkgPSAoIiAgICAg4qCA4qCA4qCA4qCA4qK44qO/4qO/4qCA4qCA4qCA4qOA4qOg4qOk4qOk4qOk4qOk4qOk4qOk4qOk4qO84qOH4qOA4qOA4qOA4qOb4qOb4qOS4qOy4qK+4qG3Iik="))

W = '\033[0m'
R = '\033[91m'

os.system('clear')

dukcapil = ['https://dukcapil.kemendagri.go.id/','3315130105570003|3321062905170003','3321056208680003|3321062905170003','3321051103960003|3321062905170003','3315130512080004|3321062905170003','3321052605920001|3321062905170003']

exec(b.b64decode("IyBDaWUgZGkgRGVjcnlwdCA6diAtIFRlcnVzIGRpIHJlY29kZSA6diBhd2tva3dvYWtvCmhlcmUgPSBbJzMzMjEwNjA3MDY5MjAwMDF8MzMyMTA2MDUwODA1MDAwMScsJzMzMjEwNjIxMDk4NzAwMDF8MzMyMTA2MTEwOTA2MDAxOScsJzMzMjEwNjAzMDQ5MDAwMDZ8MzMyMTA2MTAxMDA3MDAwMScsJzMzMjEwNjIwMDM3NTAwMDJ8MzMyMTA2MTUwMzEyMDAwNScsJzMzMjEwNjEzMDY5OTAwMDV8MzMyMTA2MjgwMjA3MDAxMicsJzMyMDExNzAzMTE4NzAwMDR8MzMyMTA2MDExMjE0MDAxMCcsJzMzMjEwNjA1MDM2NTAwMDR8MzMyMTA2MDIwNDA3MDczMicsJzMzMjEwNjYyMDg2OTAwMDR8MzMyMTA2MDIwNDA3MDczMScsJzMzMjEwNjA3MDI2MzAwMDJ8MzMyMTA2MDIwNDA3MDczMScsJzMzMjEwNjU1MDMwMzAwMDJ8MzMyMTA2MDIwNDA3MDczMScsJzMzMjEwNjU4MTIxNTAwMDJ8MzMyMTA2MDExMjE0MDAxMCcsJzMzMjEwNjE4MDQ5NTAwMDF8MzMyMTA2MDIwNTE2MDAwNycsJzMzMjEwNjYxMDQwMDAwMDF8MzMyMTA2MDIwNTE2MDAwNycsJzMzMjEwNTEzMDY4NDAwMDd8MzMyMTA2MDIxMjE2MDAwMScsJzMzMjEwNTYyMDg5MjAwMDF8MzMyMTA2MDIxMjE2MDAwMScsJzMzMjEwNjAxMDkxMjAwMDJ8MzMyMTA2MDIxMjE2MDAwMScsJzMzNzQxMTI2MDU3OTAwMDh8MzMyMTA2MDMwNDEyMDAwNCcsJzMzNzQxMTU2MDQ3OTAwMDh8MzMyMTA2MDMwNDEyMDAwNCcsJzMzMjEwNjA2MTExMjAwMDF8MzMyMTA2MDMwNDEyMDAwNCcsJzMzNzQxMTMwMDEwMzAwMDN8MzMyMTA2MDMwNDEyMDAwNCcsJzMzMjEwNjAyMDc4NTAwMDR8MzMyMTA2MDMwODExMDAwMScsJzMzMjEwNjY5MDU5MDAwMDF8MzMyMTA2MDMwODExMDAwMScsJzMzMjEwNjIyMDYxMTAwMDN8MzMyMTA2MDMwODExMDAwMScsJzMzMjEwNjE1MDI1MzAwMDF8MzMyMTA2MDQxMjA2MDAwNCcsJzMzMjEwNjY2MDU1NDAwMDN8MzMyMTA2MDQxMjA2MDAwNCcsJzMzMjEwNjYzMTE5NjAwMDN8MzMyMTA2MDcxMDE1MDAwNCcsJzMzMjEwNjE2MDI4MTAwMDR8MzMyMTA2MDgwMTExMDAwNScsJzMzMjEwNjEyMTA2NDAwMDN8MzMyMTA2MDgwMjA3MDAxMScsJzMzMjEwNjQ1MDg3MTAwMDN8MzMyMTA2MDgwMjA3MDAxMScsJzMzMjEwNjYwMDYwNTAwMDF8MzMyMTA2MDgwMjA3MDAxMScsJzMzMjEwNjIyMDU5MjAwMDN8MzMyMTA2MDgwMjA3MDAxMScsJzMzMjEwNjI5MTI2NTAwMDF8MzMyMTA2MDgwODA1MDAxMycsJzMzMjEwNjQ1MDY2NzAwMDF8MzMyMTA2MDgwODA1MDAxMycsJzMzMjEwNjA0MTA4NzAwMDF8MzMyMTA2MDgwODA1MDAxMycsJzMzMjEwNjU4MDY5NzAwMDF8MzMyMTA2MDgwODA1MDAxMycsJzMzMjExMjEyMDU4MzAwMDV8MzMyMTA2MDgxMTEzMDAwMScsJzMzMjEwNjUxMDU5NDAwMDR8MzMyMTA2MDgxMTEzMDAwMScsJzMzMjEwNjI5MDkxMzAwMDF8MzMyMTA2MDgxMTEzMDAwMScsJzMzMjExMTA2MDM3ODAwMDN8MzMyMTA2MDkwMjEyMDAwNScsJzMzMjExMjYyMDI5MjAwMDJ8MzMyMTA2MDkwMjEyMDAwNScsJzMzMjEwNjUwMDgxNTAwMDF8MzMyMTA2MDkwMjEyMDAwNScsJzMzMjEwNjU0MDIxMjAwMDF8MzMyMTA2MDkwMjEyMDAwNScsJzMzMjEwNjA4MDU5MDAwMDJ8MzMyMTA2MTAwNjE1MDAwNicsJzMzMjEwNDU2MDI5NTAwMDN8MzMyMTA2MTAwNjE1MDAwNicsJzMzMjEwNjAyMDYxNTAwMDF8MzMyMTA2MTAwNjE1MDAwNicsJzMzMjEwNjIyMDQ5MDAwMDF8MzMyMTA2MTEwMjE0MDAwNScsJzMzMjEwNjU4MTA5NTAwMDN8MzMyMTA2MTEwMjE0MDAwNScsJzMzMjEwNjUzMTIxMzAwMDJ8MzMyMTA2MTEwMjE0MDAwNScsJzMzMjEwNjA3MDQ4NTAwMDZ8MzMyMTA2MTEwMzE0MDAwNCcsJzMzMjEwNjUzMDIxNDAwMDJ8MzMyMTA2MTEwMzE0MDAwNCcsJzMzMjExMTY0MDQ5MzAwMDJ8MzMyMTA2MTEwMzE0MDAwNCcsJzMzMjEwNjI1MDM3MTAwMDJ8MzMyMTA2MTEwODA2MDAwNCcsJzMzMjEwNjQ4MDg3MzAwMDJ8MzMyMTA2MTEwODA2MDAwNCcsJzMzMjEwNjY2MDgwMDAwMDJ8MzMyMTA2MTEwODA2MDAwNCcsJzMzMjEwNjU1MTA5NjAwMDF8MzMyMTA2MTEwODA2MDAwNCcsJzMzNzQwOTcwMDY3NjAwMDN8MzMyMTA2MTMwMzE0MDAwMicsJzMzNzQwOTAyMDUwNTAwMDN8MzMyMTA2MTMwMzE0MDAwMicsJzMzMjEwNTE0MTA4MjAwMDF8MzMyMTA2MTMwNDA5MDAwMScsJzMzMjEwNjI1MDU3NzAwMDN8MzMyMTA2MTMwNzA2MDAzMicsJzMzMjEwNjQ2MDk3MTAwMDR8MzMyMTA2MTMwNzA2MDAzMicsJzMzMjEwNjI4MDQxMDAwMDJ8MzMyMTA2MTMwNzA2MDAzMicsJzMzMjEwNjUwMDYwMjAwMDF8MzMyMTA2MTMwNzA2MDAzMicsJzMzMjEwNjA5MTA3NTAwMDZ8MzMyMTA2MTQwMjA2MDAwNicsJzMzMjEwNjUzMDg4MDAwMDF8MzMyMTA2MTQwMjA2MDAwNicsJzMzMjEwNjY0MDUxMzAwMDN8MzMyMTA2MTQwMjA2MDAwNicsJzMzMjEwNjI4MDMwMzAwMDN8MzMyMTA2MTQwMjA2MDAwNicsJzMzMjEwNjU5MDgwOTAwMDF8MzMyMTA2MTQwMjA2MDAwNidd"))

waktu = t.ctime()
print ("⠀ ⠀ ⠀⠀⠀⠀ ⠀⠀  ⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀")
print ("⠀⠀  ⠀⠀⠀ ⠀  ⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀")
print ("⠀  ⠀⠀⠀   ⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀")
print ("⠀  ⠀   ⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄")
print ("     ⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇")
print (iy)
print ("     ⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃")
print ("     ⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀")
print ("     ⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀")
print ("    ⠀⠀ ⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁")
print ("=========[ NIK & KK GENERATOR ]=========")
print ("====["+R+"GUNAKAN TOOLS INI DENGAN BAIK!"+W+"]====")
print ("=======[" + waktu + "]=======")

choose = True
while choose:
	print (W+"""
	[1]. Generate NIK & KK
	[2]. About
	[3]. Exit
	""")
	choose = raw_input('Choose your want : ' )
	if choose =="1":
		y = random.choice(here)
		x = y.split('|')
		print ("="*40+"\nGenerating...")
		t.sleep(3)
		print ("\nNIK : " + x[0])
		print ("KK  : " + x[1])
		print ("\nDone.\n"+R+"./isilent\n"+W+"="*40)
		print ("Jika tidak valid, silahkan bisa generate kembali :)\n")
		sys.exit()
	elif choose =="2":
		print ("="*40)
		print ("\nGunakan tools ini dengan baik ya bro:)\n\nNIK & KK GENERATOR v1.0\n."+R+"/isilent\n\n"+W+"="*40)
		t.sleep(2)
	elif choose =="3":
		break
	elif choose !="":
		print (R+"\nWrong input :)")
# Gunakan tools ini dengan baik bro:)
# Sengaja tools ini dibuat hanya untuk generate nik&kk,
# supaya bisa registrasi menggunakan nik&kk hasil generate ini
