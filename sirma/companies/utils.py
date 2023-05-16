from django.db import connection

def hostname_from_the_request(request):
    return request.get_host().split(":")[0].lower()

def tenant_db_from_the_request(request):
    hostname = hostname_from_the_request(request)
    tenants_map = get_tenants_map()
    if hostname =="f600-88-240-181-166.ngrok-free.app":
        hostname = "localhost"
  
    return tenants_map.get(hostname)

def get_tenants_map():
    return {
        "demo.local": "demo",
        "company2.local": "company2",
    }