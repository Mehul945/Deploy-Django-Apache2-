import os
import webbrowser
os.system("clear")
print("O)O)O)-> WELCOME TO DJANGO DEPLOYMENT PROGRAME<-(O(O(O")
website=input("Enter website name : ")

#ip=input("Enter your ip : ")
try:
    os.system("apt install python3-pip apache2 libapache2-mod-wsgi-py3")
except Exception as e:
    print(e)
    exit()
try:
    os.system("pip3 install virtualenv")
except Exception as e:
    print(e)
    exit()
os.system("clear")
print("O)O)O)-> WELCOME TO DJANGO DEPLOYMENT PROGRAMMER <-(O(O(O")

os.system(f"mv {website} /var/www/")

# os.system(f"sudo cd /var/www/{website}")
os.chdir(f"/var/www/{website}")
os.system("virtualenv myproject")
os.system(". myproject/bin/activate")
os.system("pip3 install django")
with open(f"/var/www/{website}/myproject/pyvenv.cfg",'r') as f:
    cfg=f.read()
    cfg=cfg.replace("include-system-site-packages = false","include-system-site-packages = true")
f.close()
with open("/home/pyvenv.cfg","w+") as f:
    f.write(cfg)
f.close()
os.system(f"mv /home/pyvenv.cfg /var/www/{website}/myproject")
os.system("deactivate")
os.chdir(rf"/etc/apache2/sites-available/")
APACHE_LOG_DIR='APACHE_LOG_DIR'
conf=fr"""
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www
    Alias /static /var/www/{website}/static
    <Directory /var/www/{website}/static>
        Require all granted
    </Directory>

    <Directory //var/www/{website}/{website}>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess {website} python-path=/var/www/{website} python-home=/var/www/{website}/myproject
    WSGIProcessGroup {website}
    WSGIScriptAlias / /var/www/{website}/{website}/wsgi.py
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
"""
# print(conf)
with open(website+".conf","w+") as f:
    f.write(conf)
f.close()
os.system(f"a2dissite 000-defual.conf")
os.system("systemclt reload apache2")
os.system(f"a2ensite {website}.conf")
os.system("systemclt reload apache2")
os.system("service apache2 restart")
#webbrowser.open_new_tab(ip)
