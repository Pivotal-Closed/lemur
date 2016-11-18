from lemur.common.utils import parse_certificate

VALID_USER_HEADER_TOKEN = {
    'Authorization': 'Basic ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0MzUyMzMzNjksInN1YiI6MSwiZXhwIjoxNTIxNTQ2OTY5fQ.1qCi0Ip7mzKbjNh0tVd3_eJOrae3rNa_9MCVdA4WtQI',
    'Content-Type': 'application/json'
}


VALID_ADMIN_HEADER_TOKEN = {
    'Authorization': 'Basic ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0MzUyNTAyMTgsInN1YiI6MiwiZXhwIjoxNTIxNTYzODE4fQ.6mbq4-Ro6K5MmuNiTJBB153RDhlM5LGJBjI7GBKkfqA',
    'Content-Type': 'application/json'
}


INTERNAL_VALID_LONG_STR = """
-----BEGIN CERTIFICATE-----
MIID1zCCAr+gAwIBAgIBATANBgkqhkiG9w0BAQsFADCBjDELMAkGA1UEBhMCVVMx
CzAJBgNVBAgMAkNBMRAwDgYDVQQHDAdBIHBsYWNlMRcwFQYDVQQDDA5sb25nLmxp
dmVkLmNvbTEQMA4GA1UECgwHRXhhbXBsZTETMBEGA1UECwwKT3BlcmF0aW9uczEe
MBwGCSqGSIb3DQEJARYPamltQGV4YW1wbGUuY29tMB4XDTE1MDYyNjIwMzA1MloX
DTQwMDEwMTIwMzA1MlowgYwxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDQTEQMA4G
A1UEBwwHQSBwbGFjZTEXMBUGA1UEAwwObG9uZy5saXZlZC5jb20xEDAOBgNVBAoM
B0V4YW1wbGUxEzARBgNVBAsMCk9wZXJhdGlvbnMxHjAcBgkqhkiG9w0BCQEWD2pp
bUBleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKeg
sqb0HI10i2eRSx3pLeA7JoGdUpud7hy3bGws/1HgOSpRMin9Y65DEpVq2Ia9oir7
XOJLpSTEIulnBkgDHNOsdKVYHDR6k0gUisnIKSl2C3IgKHpCouwiOvvVPwd3PExg
17+d7KLBIu8LpG28wkXKFU8vSz5i7H4i/XCEChnKJ4oGJuGAJJM4Zn022U156pco
97aEAc9ZXR/1dm2njr4XxCXmrnKCYTElfRhLkmxtv+mCi6eV//5d12z7mY3dTBkQ
EG2xpb5DQ+ITQ8BzsKcPX80rz8rTzgYFwaV3gUg38+bgka/JGJq8HgBuNnHv5CeT
1T/EoZTRYW2oPfOgQK8CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8B
Af8EBAMCAQYwHQYDVR0OBBYEFIuDY73dQIhj2nnd4DG2SvseHVVaMA0GCSqGSIb3
DQEBCwUAA4IBAQBk/WwfoWYdS0M8rz5tJda/cMdYFSugUbTn6JJdmHuw6RmiKzKG
8NzfSqBR6m8MWdSTuAZ/chsUZH9YEIjS9tAH9/FfUFBrsUE7TXaUgpNBm4DBLLfl
fj5xDmEyj17JPN/C36amQ9eU5BNesdCx9EkdWLyVJaM50HFRo71W0/FrpKZyKK68
XPhd1z9w/xgfCfYhe7PjEmrmNPN5Tgk5TyXW+UUhOepDctAv2DBetptcx+gHrtW+
Ygk1wptlt/tg7uUmstmXZA4vTPx83f4P3KSS3XHIYFIyGFWUDs23C20K6mmW1iXa
h0S8LN4iv/+vNFPNiM1z9X/SZgfbwZXrLsSi
-----END CERTIFICATE-----
"""
INTERNAL_VALID_LONG_CERT = parse_certificate(INTERNAL_VALID_LONG_STR)


INTERNAL_INVALID_STR = """
-----BEGIN CERTIFICATE-----
MIIEFTCCAv2gAwIBAgICA+gwDQYJKoZIhvcNAQELBQAwgYwxCzAJBgNVBAYTAlVT
MQswCQYDVQQIDAJDQTEQMA4GA1UEBwwHQSBwbGFjZTEXMBUGA1UEAwwObG9uZy5s
aXZlZC5jb20xEDAOBgNVBAoMB0V4YW1wbGUxEzARBgNVBAsMCk9wZXJhdGlvbnMx
HjAcBgkqhkiG9w0BCQEWD2ppbUBleGFtcGxlLmNvbTAeFw0xNTA2MjYyMDM2NDha
Fw0xNTA2MjcyMDM2NDhaMGkxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEQMA4G
A1UEBxMHQSBwbGFjZTEQMA4GA1UEChMHRXhhbXBsZTETMBEGA1UECxMKT3BlcmF0
aW9uczEUMBIGA1UEAxMLZXhwaXJlZC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQCcSMzRxB6+UONPqYMy1Ojw3Wi8DIpt9USnSR60I8LiEuRK2ayr
0RMjLJ6sBEgy/hISEqpLgTsciDpxwaTC/WNrkT9vaMcwfiG3V0Red8zbKHQzC+Ty
cLRg9wbC3v613kaIZCQCoE7Aouru9WbVPmuRoasfztrgksWmH9infQbL4TDcmcxo
qGaMn4ajQTVAD63CKnut+CULZIMBREBVlSTLiOO7qZdTrd+vjtLWvdXVPcWLSBrd
Vpu3YnhqqTte+DMzQHwY7A2s3fu4Cg4H4npzcR+0H1H/B5z64kxqZq9FWGIcZcz7
0xXeHN9UUKPDSTgsjtIzKTaIOe9eML3jGSU7AgMBAAGjgaIwgZ8wDAYDVR0TAQH/
BAIwADAOBgNVHQ8BAf8EBAMCBaAwFgYDVR0lAQH/BAwwCgYIKwYBBQUHAwEwHQYD
VR0OBBYEFKwBYaxCLxK0csmV319rbRdqDllWMEgGA1UdHwRBMD8wPaA7oDmGN2h0
dHA6Ly90ZXN0LmNsb3VkY2EuY3JsLm5ldGZsaXguY29tL2xvbmdsaXZlZENBL2Ny
bC5wZW0wDQYJKoZIhvcNAQELBQADggEBADFngqsMsGnNBWknphLDvnoWu5MTrpsD
AgN0bktv5ACKRWhi/qtCmkEf6TieecRMwpQNMpE50dko3LGGdWlZRCI8wdH/zrw2
8MnOeCBxuS1nB4muUGjbf4LIbtuwoHSESrkfmuKjGGK9JTszLL6Hb9YnoFefeg8L
T7W3s8mm5bVHhQM7J9tV6dz/sVDmpOSuzL8oZkqeKP+lWU6ytaohFFpbdzaxWipU
3+GobVe4vRqoF1kwuhQ8YbMbXWDK6zlrT9pjFABcQ/b5nveiW93JDQUbjmVccx/u
kP+oGWtHvhteUAe8Gloo5NchZJ0/BqlYRCD5aAHcmbXRsDid9mO4ADU=
-----END CERTIFICATE-----
"""
INTERNAL_INVALID_CERT = parse_certificate(INTERNAL_INVALID_STR)


INTERNAL_VALID_SAN_STR = """
-----BEGIN CERTIFICATE-----
MIIESjCCAzKgAwIBAgICA+kwDQYJKoZIhvcNAQELBQAwgYwxCzAJBgNVBAYTAlVT
MQswCQYDVQQIDAJDQTEQMA4GA1UEBwwHQSBwbGFjZTEXMBUGA1UEAwwObG9uZy5s
aXZlZC5jb20xEDAOBgNVBAoMB0V4YW1wbGUxEzARBgNVBAsMCk9wZXJhdGlvbnMx
HjAcBgkqhkiG9w0BCQEWD2ppbUBleGFtcGxlLmNvbTAeFw0xNTA2MjYyMDU5MDZa
Fw0yMDAxMDEyMDU5MDZaMG0xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEQMA4G
A1UEBxMHQSBwbGFjZTEQMA4GA1UEChMHRXhhbXBsZTETMBEGA1UECxMKT3BlcmF0
aW9uczEYMBYGA1UEAxMPc2FuLmV4YW1wbGUuY29tMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEA2Nq5zFh2WiqtNIPssdSwQ9/00j370VcKPlOATLqK24Q+
dr2hWP1WlZJ0NOoPefhoIysccs2tRivosTpViRAzNJXigBHhxe8ger0QhVW6AXIp
ov327N689TgY4GzRrwqavjz8cqussIcnEUr4NLLsU5AvXE7e3WxYkkskzO497UOI
uCBtWdCXZ4cAGhtVkkA5uQHfPsLmgRVoUmdMDt5ZmA8HhLX4X6vkT3oGIhdGCw6T
W+Cu7PfYlSaggSBbBniU0YKTFLfGLkYFZN/b6bxzvt6CTJLoVFAYXyLJwUvd3EAm
u23HgUflIyZNG3xVPml/lah0OIX7RtSigXUSLm7lYwIDAQABo4HTMIHQMAwGA1Ud
EwEB/wQCMAAwDgYDVR0PAQH/BAQDAgWgMBYGA1UdJQEB/wQMMAoGCCsGAQUFBwMB
MC8GA1UdEQQoMCaCEWV4YW1wbGUyLmxvbmcuY29tghFleGFtcGxlMy5sb25nLmNv
bTAdBgNVHQ4EFgQUiiIyclcBIfJ5PE3OCcTXwzJAM+0wSAYDVR0fBEEwPzA9oDug
OYY3aHR0cDovL3Rlc3QuY2xvdWRjYS5jcmwubmV0ZmxpeC5jb20vbG9uZ2xpdmVk
Q0EvY3JsLnBlbTANBgkqhkiG9w0BAQsFAAOCAQEAgcTioq70B/aPWovNTy+84wLw
VX1q6bCdH3FJwAv2rc28CHp5mCGdR6JqfT/H/CbfRwT1Yh/5i7T5kEVyz+Dp3+p+
AJ2xauHrTvWn0QHQYbUWICwkuZ7VTI9nd0Fry1FQI1EeKiCmyrzNljiN2l+GZw6i
NJUpVNtwRyWRzB+yIx2E9wyydqDFH+sROuQok7EgzlQileitPrF4RrkfIhQp2/ki
YBrY/duF15YpoMKAlFhDBh6R9/nb5kI2n3pY6I5h6LEYfLStazXbIu61M8zu9TM/
+t5Oz6rmcjohL22+sEmmRz86dQZlrBBUxX0kCQj6OAFB4awtRd4fKtkCkZhvhQ==
-----END CERTIFICATE-----
"""
INTERNAL_VALID_SAN_CERT = parse_certificate(INTERNAL_VALID_SAN_STR)


INTERNAL_VALID_WILDCARD_STR = """
-----BEGIN CERTIFICATE-----
MIIEHDCCAwSgAwIBAgICA+owDQYJKoZIhvcNAQELBQAwgYwxCzAJBgNVBAYTAlVT
MQswCQYDVQQIDAJDQTEQMA4GA1UEBwwHQSBwbGFjZTEXMBUGA1UEAwwObG9uZy5s
aXZlZC5jb20xEDAOBgNVBAoMB0V4YW1wbGUxEzARBgNVBAsMCk9wZXJhdGlvbnMx
HjAcBgkqhkiG9w0BCQEWD2ppbUBleGFtcGxlLmNvbTAeFw0xNTA2MjYyMTEzMTBa
Fw0yMDAxMDEyMTEzMTBaMHAxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEQMA4G
A1UEBxMHQSBwbGFjZTEQMA4GA1UEChMHRXhhbXBsZTETMBEGA1UECxMKT3BlcmF0
aW9uczEbMBkGA1UEAxQSKi50ZXN0LmV4YW1wbGUuY29tMIIBIjANBgkqhkiG9w0B
AQEFAAOCAQ8AMIIBCgKCAQEA0T7OEY9FxMIdhe1CwLc+TbDeSfDN6KRHlp0I9MwK
3Pre7A1+1vmRzLiS5qAdOh3Oexelmgdkn/fZUFI+IqEVJwmeUiq13Kib3BFnVtbB
N1RdT7rZF24Bqwygf1DHAekEBYdvu4dGD/gYKsLYsSMD7g6glUuhTbgR871updcV
USYJ801y640CcHjai8UCLxpqtkP/Alob+/KDczUHbhdxYgmH34aQgxC8zg+uzuq6
bIqUAc6SctI+6ArXOqri7wSMgZUnogpF4R5QbCnlDfSzNcNxJFtGp8cy7CNWebMd
IWgBYwee8i8S6Q90B2QUFD9EGG2pEZldpudTxWUpq0tWmwIDAQABo4GiMIGfMAwG
A1UdEwEB/wQCMAAwDgYDVR0PAQH/BAQDAgWgMBYGA1UdJQEB/wQMMAoGCCsGAQUF
BwMBMB0GA1UdDgQWBBTH2KIECrqPHMbsVysGv7ggkYYZGDBIBgNVHR8EQTA/MD2g
O6A5hjdodHRwOi8vdGVzdC5jbG91ZGNhLmNybC5uZXRmbGl4LmNvbS9sb25nbGl2
ZWRDQS9jcmwucGVtMA0GCSqGSIb3DQEBCwUAA4IBAQBjjfur2B6BcdIQIouwhXGk
IFE5gUYMK5S8Crf/lpMxwHdWK8QM1BpJu9gIo6VoM8uFVa8qlY8LN0SyNyWw+qU5
Jc8X/qCeeJwXEyXY3dIYRT/1aj7FCc7EFn1j6pcHPD6/0M2z0Zmj+1rWNBJdcYor
pCy27OgRoJKZ6YhEYekzwIPeFPL6irIN9xKPnfH0b2cnYa/g56DyGmyKH2Kkhz0A
UGniiUh4bAUuppbtSIvUTsRsJuPYOqHC3h8791JZ/3Sr5uB7QbCdz9K14c9zi6Z1
S0Xb3ZauZJQI7OdHeUPDRVq+8hcG77sopN9pEYrIH08oxvLX2US3GqrowjOxthRa
-----END CERTIFICATE-----
"""
INTERNAL_VALID_WILDCARD_CERT = parse_certificate(INTERNAL_VALID_WILDCARD_STR)


EXTERNAL_VALID_STR = """
-----BEGIN CERTIFICATE-----
MIIFHzCCBAegAwIBAgIQGFWCciDWzbOej/TbAJN0WzANBgkqhkiG9w0BAQsFADCB
pDELMAkGA1UEBhMCVVMxHTAbBgNVBAoTFFN5bWFudGVjIENvcnBvcmF0aW9uMR8w
HQYDVQQLExZGT1IgVEVTVCBQVVJQT1NFUyBPTkxZMR8wHQYDVQQLExZTeW1hbnRl
YyBUcnVzdCBOZXR3b3JrMTQwMgYDVQQDEytTeW1hbnRlYyBDbGFzcyAzIFNlY3Vy
ZSBTZXJ2ZXIgVEVTVCBDQSAtIEc0MB4XDTE1MDYyNDAwMDAwMFoXDTE1MDYyNTIz
NTk1OVowgYMxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDQUxJRk9STklBMRIwEAYD
VQQHDAlMb3MgR2F0b3MxFjAUBgNVBAoMDU5ldGZsaXgsIEluYy4xEzARBgNVBAsM
Ck9wZXJhdGlvbnMxHjAcBgNVBAMMFXR0dHQyLm5ldGZsaXh0ZXN0Lm5ldDCCASIw
DQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALwMY/yod9YGLKLCzbbsSUBWm4ZC
DfcgbUNL3JLtZaFCaOeUPLa4YNqty+9ACXBLYPNMm+dgsRHix8N2uwtZrGazHILK
qey96eSTosPsvKFt0KLNpUl8GC/YxA69L128SJgFaaq5Dr2Mp3NP0rt0RIz5luPj
Oae0hkGOS8uS0dySlAmfOw2OsJY3gCw5UHcmpcCHpO2f7uU+tWKmgfz4U/PpQ0kz
WVJno+JhcaXIximtiLreCNF1LpraAjrcZJ+ySJwYaLaYMiJoFkdXUtKJcyqmkbA3
Splt7N4Hb8c+5aXv225uQYCh0HXQeMyBotlaIrAddP5obrtjxhXBxB4ysEcCAwEA
AaOCAWowggFmMCAGA1UdEQQZMBeCFXR0dHQyLm5ldGZsaXh0ZXN0Lm5ldDAJBgNV
HRMEAjAAMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYB
BQUHAwIwYQYDVR0gBFowWDBWBgZngQwBAgIwTDAjBggrBgEFBQcCARYXaHR0cHM6
Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYBBQUHAgIwGRoXaHR0cHM6Ly9kLnN5bWNi
LmNvbS9ycGEwHwYDVR0jBBgwFoAUNI9UtT8KH1K6nLJl7bqLCGcZ4AQwKwYDVR0f
BCQwIjAgoB6gHIYaaHR0cDovL3NzLnN5bWNiLmNvbS9zcy5jcmwwVwYIKwYBBQUH
AQEESzBJMB8GCCsGAQUFBzABhhNodHRwOi8vc3Muc3ltY2QuY29tMCYGCCsGAQUF
BzAChhpodHRwOi8vc3Muc3ltY2IuY29tL3NzLmNydDANBgkqhkiG9w0BAQsFAAOC
AQEAQuIfyBltvCZ9orqNdS6PUo2PaeUgJzkmdDwbDVd7rTwbZIwGZXZjeKseqMSb
L+r/jN6DWrScVylleiz0N/D0lSUhC609dQKuicGpy3yQaXwhfYZ6duxrW3Ii/+Vz
pFv7DnG3JPZjIXCmVhQVIv/8oaV0bfUF/1mrWRFwZiBILxa7iaycRhjusJEVRtzN
Ot/qkLluHO0wbEHnASV4P9Y5NuR/bliuFS/DeRczofNS78jJuZrGvl2AqS/19Hvm
Bs63gULVCqWygt5KEbv990m/XGuRMaXuHzHCHB4v5LRM30FiFmqCzyD8d+btzW9B
1hZ5s3rj+a6UwvpinKJoPfgkgg==
-----END CERTIFICATE-----
"""
EXTERNAL_CERT = parse_certificate(EXTERNAL_VALID_STR)


PRIVATE_KEY_STR = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAnEjM0cQevlDjT6mDMtTo8N1ovAyKbfVEp0ketCPC4hLkStms
q9ETIyyerARIMv4SEhKqS4E7HIg6ccGkwv1ja5E/b2jHMH4ht1dEXnfM2yh0Mwvk
8nC0YPcGwt7+td5GiGQkAqBOwKLq7vVm1T5rkaGrH87a4JLFph/Yp30Gy+Ew3JnM
aKhmjJ+Go0E1QA+twip7rfglC2SDAURAVZUky4jju6mXU63fr47S1r3V1T3Fi0ga
3Vabt2J4aqk7XvgzM0B8GOwNrN37uAoOB+J6c3EftB9R/wec+uJMamavRVhiHGXM
+9MV3hzfVFCjw0k4LI7SMyk2iDnvXjC94xklOwIDAQABAoIBAGeykly5MeD70OgB
xPEMfoebkav88jklnekVxk6mz9+rw1i6+CyFLJqRN7NRoApdtOXTBrXUyMEUzxq9
7zIGaVptZNbqggh2GK8LM20vNnlQbVGVmdMX30fbgNv6lK1eEBTdxVsMvVRqhVIK
+LGTmlJmICKZ4XdTS9v/k4UGm2TZPCt2pvrNzIpT7TIm2QybCbZoOPY8SHx0U8c5
lmtdqmIsy2JPNSOsOCiJgzQIvkR/fMGWFgNE4fEHsHAfubgpK97TGzwLiFRmlTb+
QUDaz0YbwhF+5bQjHtaGUGATcg5bvV1UWBUvp+g4gRIfwzG+3PAGacYE/djouAdG
PHbxuCkCgYEAz/LsgMgsaV3arlounviSwc8wG9WcI5gbYw5qwX0P57ZoxS7EBAGu
yYtudurJrU9SfsSV44GL11UzBcAGOeS0btddrcMiNBhc7fY7P/1xaufQ3GjG06/v
kH4gOjzsGSTJliZ709g4J6hnMCxz0O0PS31Qg5cBD8UG8xO7/AV0is0CgYEAwGWy
A6YPinpZuenaxrivM5AcVDWmj7aeC29M63l/GY+O5LQH2PKVESH0vL5PvG3LkrCR
SUbaMKdKR0wnZsJ89z21eZ54ydUgj41bZJczl8drxcY0GSajj6XZXGTUjtoVrWsB
A0kJbjsrpd+8J316Y9iCgpopmbVd965pUHe4ACcCgYAamJlDB1cWytgzQHmB/4zV
mOgwRyvHKacnDir9QD+OhTf1MDwFvylZwamJMBJHRkPozr/U7zaxfcYe0CZ7tRKW
spjapoBzZUJNdRay4nllEO0Xo5b6cCAVvOvmRvBzbs8Rky53M8pK2DEKakUNzaQN
JaPskJ2kJLD02etLGm+DaQKBgQCTI/NNmQ2foUzHw1J+0jWjoJ4ZxOI6XLZoFlnk
aInMuZ7Vx92MjJF2hdqPEpkWiX28FO839EjgFsDW4CXuD+XUjEwi1BCagzWgs8Hm
n0Bk3q3MlnW3mnZSYMtoPvDUw3L6qrAenBfrRrNt6zsRlIQqoiXFzjLsi+luh+Oh
F74P1wKBgQCPQGKLUcfAvjIcZp4ECH0K8sBEmoEf8pceuALZ3H5vneYDzqMDIceo
t5Gpocpt77LJnNiszXSerj/KjX2MflY5xUXeekWowLVTBOK5+CZ8+XBIgBt1hIG3
XKxcRgm/Va4QMEAnec0qXfdTVJaJiAW0bdKwKRRrrbwcTdNRGibdng==
-----END RSA PRIVATE KEY-----
"""

INTERNAL_CERTIFICATE_A_STR = """
-----BEGIN CERTIFICATE-----
MIIDazCCAlOgAwIBAgIBATANBgkqhkiG9w0BAQsFADB5MQswCQYDVQQGEwJVUzET
MBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJTG9zIEdhdG9zMRYwFAYDVQQK
DA1OZXRmbGl4LCBJbmMuMRMwEQYDVQQLDApPcGVyYXRpb25zMRQwEgYDVQQDDAtB
Y29tbW9uTmFtZTAeFw0xNjA2MjkyMjE0NDdaFw0zNjA2MjkyMjE0NDdaMHkxCzAJ
BgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlMb3MgR2F0
b3MxFjAUBgNVBAoMDU5ldGZsaXgsIEluYy4xEzARBgNVBAsMCk9wZXJhdGlvbnMx
FDASBgNVBAMMC0Fjb21tb25OYW1lMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB
CgKCAQEAtkyvL6EqSgYSJX11635Hb8FBG/8Wey6C2KtG7M+GXvGCsSmfNqQMeZdf
W9Avxelkstp5/K+ilVJJ2TJRelu1yVUUkQcrP7imgf7CxKQAnPz2oXQImLFbm7OS
1zKA+qwtLGrId3vVQaotUtdI+wxx0YE66pyfOhQJsVOeuYwG8CCxnAj/lXeNLA1t
n39A8FLfj9nxjvZWWm2z8qXO2IYOWEMOOel1zixhypeJoTD2cJHDKNlUnXN4q5ej
psD4ehLFXIPXsKJv5XOtNYB9UHB3moXlEOuKAquRzBOfTP+rUYyfbHmzCN4eXekp
R6vze49hlg8QdCNjVY6jHRrOuVKGuwIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAt
rE2Ee6a0zRlJHiuP5Zr61s6ZnwIsPN5sjo3pFJ/goHeNWbq+02FUJLXROtxSMlo8
jLYpnQbm3Qoyd0KjGn9myP1vqBL6Yzf9dRI2li9XYmavxU7OK/KJtBo/Wnw3DVT5
jxYrn4YKJU9+T0hr57bWUQ7HjMNojwBcgglzPN9KOtfTfbPEUIeoRpCjeyjwBUSN
nrTDiYPV+XI4LAyDmuR7esSvm2+0h6C0dmUbVspkxBaKFEYUKIYaZbEFEBsyZGri
qDIyu9HSvu2MJ2lVxfMNsW+IYG74DOqJQsIFP+7hrfdPoMGm4GvAiHR1IuSmq+sf
L0Ew8hy0GG3nZ6uXLW7q
-----END CERTIFICATE-----
"""


INTERNAL_PRIVATE_KEY_A_STR = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAtkyvL6EqSgYSJX11635Hb8FBG/8Wey6C2KtG7M+GXvGCsSmf
NqQMeZdfW9Avxelkstp5/K+ilVJJ2TJRelu1yVUUkQcrP7imgf7CxKQAnPz2oXQI
mLFbm7OS1zKA+qwtLGrId3vVQaotUtdI+wxx0YE66pyfOhQJsVOeuYwG8CCxnAj/
lXeNLA1tn39A8FLfj9nxjvZWWm2z8qXO2IYOWEMOOel1zixhypeJoTD2cJHDKNlU
nXN4q5ejpsD4ehLFXIPXsKJv5XOtNYB9UHB3moXlEOuKAquRzBOfTP+rUYyfbHmz
CN4eXekpR6vze49hlg8QdCNjVY6jHRrOuVKGuwIDAQABAoIBACYPnqfwGzc3S0Se
jCctx1Zy39grixMO4+y+3eEFdwWNoP7CNOagm6YrT5KIxeCpWQfqi3uRY/2PH7IE
SnSkfzDY3aFmAMaeE82iViHeJ+6e9hNBeaX/qaO5e1gIyFsN5aSXauFfbmf2Ut4v
6qHXuE/Ijnd7WdczZc6rKcGNlck+f/QtsZhYEYbgHT3Nrt0ztlvkdrcyRIxZTeS7
7gvVWrVv6rviTobi/ZkeM9pqe5bbLuWgb/ArvI52pJwaUcz9LPGo+miank6e4gAd
cTudoREtBKVgXROhTSz33mdjjUTCDGdtILTztDSgLpJXYT0w2h1zmfV7t4tztzzQ
xW5LVCECgYEA33YG/gaZbfH6szC/heilojelrIG+n7GjsqpfMqGFofYNBAswUC3w
qZdeXxqGZEXC8mx8CufDhC50vJv353WAHaFFJcwy2QeGvHfPAZ4ZQ68o9XLeva4t
M6+ZtOiaK8u/mzxq43Jj7FbXmxxlJXY3B0uWdWpKGsPRTmSaUw0lKPECgYEA0NhG
74C6zRgHY2Eq2Qq7+NtlvpzUtVtalhiDoCEpDMhjzLUTBNy6yMsSdP8SyCy9O7Ng
rrXJdgKHvpjnJyUvB3hhEAurPIPWJArEfEHAF+V8mHY8f58xZqgHRsYsH3tWHYx4
2lzmposTES5KKV4xsYbjjyzXX+WNdaOkC4JBCmsCgYEA3j2JKL0xfMordmlmIWzG
xnWnnNCQ4EwQrVGKSlWgDPsj6MCj9Sorbs9veRBtVm6XOvkvyLzFk8GMMkTAIf+X
QmCw362daIF2vBw/0bEGGW2sQ6hR5L3EkOH08ZpgMmx6DI7jE4Ah5txbpBVydvaC
Ngw0AGSMfOABW4DshurM6VECgYEAxeH3rJ2r4gL/lSGPaOGr5At2Z1rQjRqHRarq
pQJmk+8X6PI1mCjRbspDrcm2cSc7EmNPm5sxzXhuSKE2fLfVzN06EusLkCZW9AWj
0Ry3t6zBFvEJN9+N/nf9lQjW6+mAWjUsmbLm9SzXnzLeID5ZFZ365kGVvQ6Tr8Cj
AiikGgsCgYEAlYGNwBKWClm797YVyPhmqrFX4T9Hpxc7oC3vVwd96tAbLlSrW8r5
o6ynBW1bG+qfjx9GyThgudvRtB+0vTSShrT5GftLCyMtOiYSHkGEvMOGFBuowzoz
3i841gR9+cwA0S1hy7fC0PDmTo0xC91JocwesPQ023MmECPfu6Frzog=
-----END RSA PRIVATE KEY-----
"""


CSR_STR = """
-----BEGIN CERTIFICATE REQUEST-----
MIIC1zCCAb8CAQAwczEUMBIGA1UEAwwLQUNvbW1vbk5hbWUxFTATBgNVBAoMDG9y
Z2FuaXphdGlvbjEOMAwGA1UECwwFZ3VuaXQxCzAJBgNVBAYTAlVTMRMwEQYDVQQI
DApDYWxpZm9ybmlhMRIwEAYDVQQHDAlzb21ld2hlcmUwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQDNnY+Ap+V9+Eg/PAtd7bq27D7tDvbL10AysNUSazy7
gJyHfJyE3oiXm28zjFNzRQ35qhsCFpWg8M36FpdP9fIFG9sVXV/ye+YNBkZ2aTJi
RnbErZcy8qc+2MRd2JKE9g0pISp9hAEeEPLTwSoGqf5VqOaBehBqL5OKNUr7JAxV
TIH1oVU87w/6xg/WsUiyPo49WXxF/3DZNP1UOTYiffxIiARhTb9EtlXpt5iOlic3
w/vBX6qsH++XJIus2WE+ABlAVUQTCvc6bgpu4zjc8nlm3ClqkAKcxn2ubEder+Fh
hagMYGsbYG+/IWrKYN6S0BjE26tNMiOlmIebimjEdFpnAgMBAAGgHzAdBgkqhkiG
9w0BCQ4xEDAOMAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcNAQELBQADggEBAE5OKI/n
b1ZRJDL4SpjWggRjfwBdYmb96lGH0aGDoVUP9UUusLzpWLtutkgr9Hh29agSsLZF
j535NeXHf+Jc4UyR288WQVJthgAT1e5+jBNPxz4IcTnDW7ZMJLGm495XaKi6Krcg
+8Qn2+h04jBTbN2Z9+MXGak0B8ycrbDx/FYL4KgBJRvS805d43zC6L1aUfRbpZgN
QeQoBdLhFNB1kAYSWCyETwRQOeGEphBJYBPcXsQVBWbMtLpbhjRZ1uTVZEFIh8Oa
zm3Cn4Ul8DO26w9QS4fmZjmnPOZFXYMWoOR6osHzb62PWQ8FBMqXcdToBV2Q9Iw4
PiFAxlc0tVjlLqQ=
-----END CERTIFICATE REQUEST-----
"""


CSR_PEM_STR = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEAzZ2PgKflffhIPzwLXe26tuw+7Q72y9dAMrDVEms8u4Cch3yc
hN6Il5tvM4xTc0UN+aobAhaVoPDN+haXT/XyBRvbFV1f8nvmDQZGdmkyYkZ2xK2X
MvKnPtjEXdiShPYNKSEqfYQBHhDy08EqBqn+VajmgXoQai+TijVK+yQMVUyB9aFV
PO8P+sYP1rFIsj6OPVl8Rf9w2TT9VDk2In38SIgEYU2/RLZV6beYjpYnN8P7wV+q
rB/vlySLrNlhPgAZQFVEEwr3Om4KbuM43PJ5ZtwpapACnMZ9rmxHXq/hYYWoDGBr
G2BvvyFqymDektAYxNurTTIjpZiHm4poxHRaZwIDAQABAoIBAQCm5MwVBrKtI/ko
colbbVoPngSZkHrcC9SNEKFyON7r5sGm64t0AdjnDgAd3DnkJ1nnm54efMxo/OyD
oRCik6QlZ23VkpwNi2m4iq5o8Iw33rAKhkhizzjXN0V0UxTinYEjMEt348ywZdtj
67c7/4F0cArhb32hYwqjtQwuex0Tofb37Aj5rNPv1n8ytbhz1vriAVZHZEcjdjdn
CSVeblufORQKRzK3wW5nRN721b9gSvEJHfHeNpXQO9X8Yl5tn7UxjoQWXLZK+khv
pawN8BFt7lVLkQR14Nq7bKwuJ6KR1ig698a1Ii8Luyh2BgfIc25ryuzs8fFCioKi
TK/nzMQ5AoGBAPxtbTrkTTNQ03hnfefRVKGwNHPqLhIQpI99FC4yLYYHsUwFmMVR
ccg4aqNUtI0zn1snKC58NICxIPP9c0NuHqBuNuwhuRPINfQfjg/aOpE2QycZcew1
BQxXH5d3zXWKLpN15kIS2s18/MpNgTFx2Z0EGqLezDXs6JaPJkqg04glAoGBANCG
h106B9hbuTPYCAlTwvaoWnbaxLmtlWzRpqYBuiiBPGvLc545faXkJKb5/zd002kK
wblGrPtCnhTvCtHbTg/KuR/R8EsAriPhpWK+N4hCADJ8SLOxMU5S9O24FEK50ltN
Q84LS2Wo9fWXQhojiBrctn/ws5ngRCfUbhQeA3ybAoGBAOW7vWaUswIZ9GwnXDon
lGuXDxXTslw0k2AXyM8GUdIinCSBD3m9Vt2PItZFWBEOQ2DVMUelOK9LBZ+pMkbT
KMJ/rDKZunQbiacFNOiOhzDzfohOKxV7Z33EqPbUTMRFn4ALFCVcPZA4yWRgx0y1
vgSd4JQMSzRkyYWFAKd42SuVAoGBAIG84aWQQGdNkin+Y+mhsrCSSE6giDtaE5jz
y7KHapJe7f/HQnUUIee/zUoSSsbvKcW2CpfCsEdXyFEP9PRidOwAXjO9A7s2fiIW
9zY7UQO2xLakevtJ6HppxLfOitSFFqr1pJUik9N5TyZw6JCowLqtzeJGGQhI7z60
vZRIpDS3AoGBAPYJgNB7EcWj5U39ol+8cofG1kPauoEaildTur5ftzyzjy4DXrOW
sfU/xhUp6EKLGSXEPqeXAWR6ARf1F4U9Ozp6KA93lGSrSY561jKoqhxxOXAf5il2
p7Fzh2CckUeiGd5el+h2WUCOcgtlPlfRyV/Mlvx1H0gFieGucXTP23Ox
-----END RSA PRIVATE KEY-----
"""
