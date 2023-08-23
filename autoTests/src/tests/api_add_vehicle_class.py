import requests

urlGetToken = "https://fueldirectapi-qa.azurewebsites.net/user/login"

payload = json.dumps({
  "Login": "qa44",
  "Password": "Qaz1Wsx2Edc3Rfv4~!"
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'token 33d5203e-42f1-4323-900c-daed994dc115',
  'Cookie': 'ARRAffinity=3bc95a0a907b373b7281dbab7510fee65c0d02b1386194a9530165823f0e06fa; ARRAffinitySameSite=3bc95a0a907b373b7281dbab7510fee65c0d02b1386194a9530165823f0e06fa'
}

response = requests.request("PUT", urlGetToken, headers=headers, data=payload)
url = "https://fueldirectapi-qa.azurewebsites.net/User/134"

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'token 21bd8e10-0fcb-48de-b239-2c01c6f3d232',
  'Cookie': 'ARRAffinity=3bc95a0a907b373b7281dbab7510fee65c0d02b1386194a9530165823f0e06fa; ARRAffinitySameSite=3bc95a0a907b373b7281dbab7510fee65c0d02b1386194a9530165823f0e06fa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)