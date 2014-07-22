#!/usr/bin/python

from urllib import urlopen
import simplejson


def getPublicIP():
	url = "http://www.realip.info/api/p/realip.php"
	json = '{"IP":"144.51.242.26"}'
	t= simplejson.loads(json)
	return t["IP"]

