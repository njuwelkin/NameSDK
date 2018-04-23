# Overview
NameSDK is a python SDK library for the REST API of name.com(http://www.name.com).

# Code
* NameSDK/namehttpclient.py is a wrapper for http requests.
* NameSDK/nameclient.py provides wrapped python APIs.
* NameSDK/libs/models implements a django stype model.
* NameSDK/Domain/ NameSDK/DNS/ ... implement the business logic of each APIs.

# Using the SDK
There two ways to use the NameSDK.
* Using NameSDK.namehttpclient. Your need to have knowlodge about the API defin
** Sample code: namehttpclient_sample.py
* Using NameSDK.namehttpcliet. It wraps all http request and provides python interface. You don't need any background knowledge of http or name.com.
** Sample code: nameclient_sample.py

# Release
* version 0.1,	Implement all functions of DNS module and all non-write function of Domain module
