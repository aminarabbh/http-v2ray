import os, json, sys, pprint

PRXUSER = os.environ['PRXUSER']
PRXPASS = os.environ['PRXPASS']
PRXIP = os.environ['PRXIP']
PRXPORT = os.environ['PRXPORT']
CLDIP = os.environ['CLDIP']
VMESSID = os.environ['VMESSID']
VMESSDMN = os.environ['VMESSDMN']

file = """{
    "log": {
        "access": "",
        "error": "",
        "loglevel": "error"
    },
    "inbounds": [
        {
            "tag": "socks-in",
            "port": 1080,
            "listen": "::",
            "protocol": "socks"
        },
        
        {
            "tag": "http-in",
            "port": {PRXPORT},
            "listen": "::",
            "protocol": "http",
	    "allowTransparent": true,
            "settings": {
                "auth": "password",
                "accounts" :[
                    {
                        "user": "{PRXUSER}",
                        "pass": "{PRXPASS}"
                    }
                ],
                "udp": true,
                "ip": "{PRXIP}"
            }
        }
    ],
    "outbounds": [
        {
            "protocol": "vmess",
            "settings": {
                "vnext": [
                    {
                        "address": "{CLDIP}",
                        "port": 443,
                        "users": [
                            {
                                "email": "user@v2ray.com",
                                "id": "{VMESSID}",
                                "alterId": 64,
                                "security": "auto"
                            }
                        ]
                    }
                ]
            },
            "streamSettings": {
                "network": "ws",
                "security": "tls",
                "tlsSettings": {
                    "allowInsecure": true,
                    "serverName": "{VMESSDMN}"
                },
                "wsSettings": {
                    "connectionReuse": true,
                    "path": "/wikipedia",
                    "headers": {
                        "Host": "{VMESSDMN}"
                    }
                }
            },
            "mux": {
                "enabled": true
            },
            "tag": "proxy"
        },
        {
            "protocol": "freedom",
            "tag": "direct",
            "settings": {
                "domainStrategy": "UseIP"
            }
        }
    ],
    "dns": {
        "servers": [
            "127.0.0.53"
        ]
    },
    "routing": {
        "domainStrategy": "IPIfNonMatch",
        "rules": [
            {
                "type": "field",
                "ip": [
                    "geoip:private",
                    "geoip:cn"
                ],
                "outboundTag": "direct"
            },
            {
                "type": "field",
                "domain": [
                    "geosite:cn"
                ],
                "outboundTag": "direct"
            }
        ]
    }
}"""
file = file.replace("{PRXUSER}", PRXUSER)
file = file.replace("{PRXPASS}", PRXPASS)
file = file.replace("{PRXIP}", PRXIP)
file = file.replace("{PRXPORT}", PRXPORT)
file = file.replace("{CLDIP}", CLDIP)
file = file.replace("{VMESSID}", VMESSID)
file = file.replace("{VMESSDMN}", VMESSDMN)


with open("/config.json", "w") as config_file:
    config_file.write(file)
