#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  openVpnCheck.py
#
#  Checks the connection to an OpenVPN Server and reconnects if down.
#  
#  Copyright 2013 Curtis Lee Bolin <CurtisLeeBolin@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import subprocess

class OpenVpnCheck:
	def __init__(self, ip):
		self.ip = ip

	def pingVpn(self):
		try:
			subprocess.check_call(['ping', '-c 1', self.ip])
			return True
		except:
			return False

	def reconnectVPN(self):
		subprocess.call(['sudo', '/etc/init.d/openvpn', 'restart'])

	def run(self):
		if not self.pingVpn():
			self.reconnectVPN()

def main():
	import argparse

	parser = argparse.ArgumentParser(description='Checks the connection to an OpenVPN Server and reconnects if down.')
	parser.add_argument('ip', type=str, help='The vpn IP Address of the OpenVPN Server is needed.')
	args = parser.parse_args()

	p = OpenVpnCheck(args.ip)
	p.run()
	return 0

if __name__ == '__main__':
	main()

