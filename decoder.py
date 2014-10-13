#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
str= ' '.join(sys.argv[1:len(sys.argv)])

dictionary = {'\xc2\xa1':'1', '\xe2\x84\xa2':'2', '\xc2\xa3':'3', '\xc2\xa2':'4', '\xe2\x88\x9e':'5', '\xc2\xa7':'6', '\xc2\xb6':'7', '\xe2\x80\xa2':'8', '\xc2\xaa':'9', '\xc2\xba':'0' , '\xc5\x93':'q', '\xe2\x88\x91':'w', '\xc2\xb4':'e', '\xc2\xae':'r', '\xe2\x80\xa0':'t', '\xc2\xa5':'y', '\xc2\xa8':'u', '\xcb\x86':'i', '\xc3\xb8':'o', '\xcf\x80':'p', '\xc3\xa5':'a', '\xc3\x9f':'s', '\xe2\x88\x82':'d', '\xc6\x92':'f', '\xc2\xa9':'g', '\xcb\x99':'h', '\xe2\x88\x86':'j', '\xcb\x9a':'k', '\xc2\xac':'l', '\xce\xa9':'z', '\xe2\x89\x88':'x', '\xc3\xa7':'c', '\xe2\x88\x9a':'v', '\xe2\x88\xab':'b', '\xcb\x9c':'n', '\xc2\xb5':'m'}
translation=''

for i in str.split():
	#dictionary["'¡':'1', '™:'2', £:'3', ¢:'4', ∞:'5', §:'6', ¶:'7', •:'8', ª:'9', º:'0', œ:'q', ∑:'w', ´:'e', ®:'r', †:'t', ¥:'y', ¨:'u', ˆ:'i', ø:'o', π:'p', å:'a', ß:'s', ∂:'d', ƒ:'f', ©:'g', ˙:'h', ∆:'j', ˚:'k', ¬:'l', Ω:'z', ≈:'x', ç:'c', √:'v', ∫:'b', ˜:'n', µ:'m"]
	translation+=dictionary[i]

print translation
