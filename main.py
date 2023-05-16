import webbrowser
import time
import sys
import os
from os.path import exists
import socket





class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
############################################################
def googlehack():
    url = input("Please enter a URL/Keyword: ")
    ans=True
    while ans:
        print ("""
        1. ALL                                      8. Login Pages                            15. Signup Page
        2. Public Exposed Document                  9. SQL Errors                             16. Find Subdomains
        3. Directory Listing Vulnerabilities        10. PHP Errors/Warnings                   17. Find Sub-Subdomains
        4. Configuration Files Exposed              11. phpinfo()                             18. Seach Wayback Machine
        5. Database Files Exposed                   12. Pasting Sites                         19. Show only IP Addresses
        6. Log Files Exposed                        13. Search Github                         20. Exit
        7. Backup and Old Files                     14. Search StackOverFlow
        
        Press ENTER to run default scan
        """)
        ans=str(input("Please select an option: "))
        if ans =="2":
            publicexposed = ("https://www.google.com/search?q=site:"+url+"+ext:doc+|+ext:docx+|+ext:odt+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(publicexposed)
        elif ans =="3":
            dirtlist = ("https://www.google.com/search?q=site:"+url+"+intitle:index.of")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(dirtlist)
        elif ans =="4":
            conffile = ("https://www.google.com/search?q=site:"+url+"+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini+|+ext:env")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(conffile)
        elif ans =="5":
            db = ("https://www.google.com/search?q=site:"+url+"+ext:sql+|+ext:dbf+|+ext:mdb")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(db)
        elif ans =="6":
            log = ("https://www.google.com/search?q=site:"+url+"+ext:log")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(log)
        elif ans =="7":
            old = ("https://www.google.com/search?q=site:"+url+"+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(old)
        elif ans =="8":
            login = ("https://www.google.com/search?q=site:"+url+"+inurl:login+|+inurl:signin+|+intitle:Login+|+intitle:sign+in+|+inurl:auth")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(login)
        elif ans =="9":
            sql = ("https://www.google.com/search?q=site:"+url+"+intext:sql+syntax+near+|+intext:syntax+error+has+occurred+|+intext:incorrect+syntax+near+|+intext:unexpected+end+of+SQL+command+|+intext:Warning:+mysql_connect()+|+intext:Warning:+mysql_query()+|+intext:Warning:+pg_connect()")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(sql)
        elif ans =="10":
            phperr = ("https://www.google.com/search?q=site:"+url+" PHP+Parse+error+|+PHP+Warning+|+PHP+Error")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(phperr)
        elif ans =="11":
            phpinfo = ("https://www.google.com/search?q=site:"+url+"+ext:php+intitle:phpinfo+published+by+the+PHP+Group")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(phpinfo)
        elif ans =="12":
            paste = ("https://www.google.com/search?q=site:"+url+" site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org%20 | site:codeshare.io | site:trello.com")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(paste)
        elif ans =="13": 
            github = ("https://www. google.com/search?q=site:github.com | site:gitlab.com '"+ url +"'")
            print ("------Opening t he Browser: "+url+" ------")
            time.sleep(2) 
            webbrowser.open(r"{}".format(github))
        elif ans =="14":
            sof = ("https://www.google.com/search?q=site:stackoverflow.com '"+ url+"'")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(sof)
        elif ans =="15":
            signup = ("https://www.google.com/search?q=site:"+url+ "+inurl:signup+|+inurl:register+|+intitle:Signup" )
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(signup)
        elif ans =="16":
            sub = ("https://www.google.com/search?q=site:*."+url)
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(sub)
        elif ans =="17":
            subsub = ("https://www.google.com/search?q=site:*.*."+url)
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(subsub)
        elif ans =="18":
            wayback = ("https://web.archive.org/web/*/"+url+"/*" )
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(wayback)
        elif ans =="19":
            searchip = ("https://www.google.com/search?q=("+url+") (site:*.*.29.* |site:*.*.28.* |site:*.*.27.* |site:*.*.26.* |site:*.*.25.* |site:*.*.24.* |site:*.*.23.* |site:*.*.22.* |site:*.*.21.* |site:*.*.20.* |site:*.*.19.* |site:*.*.18.* |site:*.*.17.* |site:*.*.16.* |site:*.*.15.* |site:*.*.14.* |site:*.*.13.* |site:*.*.12.* |site:*.*.11.* |site:*.*.10.* |site:*.*.9.* |site:*.*.8.* |site:*.*.7.* |site:*.*.6.* |site:*.*.5.* |site:*.*.4.* |site:*.*.3.* |site:*.*.2.* |site:*.*.1.* |site:*.*.0.*)" )
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(2)
            webbrowser.open(searchip)
        elif ans =="menu":
            main()
    ################################################################################################################################
        elif ans =="1":
            publicexposed = ("https://www.google.com/search?q=site:"+url+"+ext:doc+|+ext:docx+|+ext:odt+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv")
            dirtlist = ("https://www.google.com/search?q=site:"+url+"+intitle:index.of")
            conffile = ("https://www.google.com/search?q=site:"+url+"+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini+|+ext:env")
            db = ("https://www.google.com/search?q=site:"+url+"+ext:sql+|+ext:dbf+|+ext:mdb")
            log = ("https://www.google.com/search?q=site:"+url+"+ext:log")
            old = ("https://www.google.com/search?q=site:"+url+"+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup")
            login = ("https://www.google.com/search?q=site:"+url+"+inurl:login+|+inurl:signin+|+intitle:Login+|+intitle:sign+in+|+inurl:auth")
            sql = ("https://www.google.com/search?q=site:"+url+"+intext:sql+syntax+near+|+intext:syntax+error+has+occurred+|+intext:incorrect+syntax+near+|+intext:unexpected+end+of+SQL+command+|+intext:Warning:+mysql_connect()+|+intext:Warning:+mysql_query()+|+intext:Warning:+pg_connect()")
            phperr = ("https://www.google.com/search?q=site:"+url+" PHP+Parse+error+|+PHP+Warning+|+PHP+Error")
            phpinfo = ("https://www.google.com/search?q=site:"+url+"+ext:php+intitle:phpinfo+published+by+the+PHP+Group")
            paste = ("https://www.google.com/search?q=site:"+url+" site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org%20 | site:codeshare.io | site:trello.com")
            github = ("https://www.google.com/search?q=site:github.com | site:gitlab.com '"+ url +"'")
            sof = ("https://www.google.com/search?q=site:stackoverflow.com '"+ url+"'")
            signup = ("https://www.google.com/search?q=site:"+url+ "+inurl:signup+|+inurl:register+|+intitle:Signup" )
            sub = ("https://www.google.com/search?q=site:*."+url)
            subsub = ("https://www.google.com/search?q=site:*.*."+url)
            wayback = ("https://web.archive.org/web/*/"+url+"/*" )
            searchip = ("https://www.google.com/search?q=("+url+") (site:*.*.29.* |site:*.*.28.* |site:*.*.27.* |site:*.*.26.* |site:*.*.25.* |site:*.*.24.* |site:*.*.23.* |site:*.*.22.* |site:*.*.21.* |site:*.*.20.* |site:*.*.19.* |site:*.*.18.* |site:*.*.17.* |site:*.*.16.* |site:*.*.15.* |site:*.*.14.* |site:*.*.13.* |site:*.*.12.* |site:*.*.11.* |site:*.*.10.* |site:*.*.9.* |site:*.*.8.* |site:*.*.7.* |site:*.*.6.* |site:*.*.5.* |site:*.*.4.* |site:*.*.3.* |site:*.*.2.* |site:*.*.1.* |site:*.*.0.*)" )
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(1)
            webbrowser.open(publicexposed)
            webbrowser.open(dirtlist)  
            webbrowser.open(conffile)
            webbrowser.open(db)  
            webbrowser.open(log)
            webbrowser.open(old)
            webbrowser.open(login)
            webbrowser.open(sql)
            webbrowser.open(phperr)
            webbrowser.open(phpinfo)
            webbrowser.open(paste)
            webbrowser.open(github)
            webbrowser.open(sof)
            webbrowser.open(signup)
            webbrowser.open(sub)
            webbrowser.open(subsub)
            webbrowser.open(wayback)
            webbrowser.open(searchip)
    ###################################################################################################################################
        elif ans =="":
            publicexposed = ("https://www.google.com/search?q=site:"+url+"+ext:doc+|+ext:docx+|+ext:odt+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv")
            conffile = ("https://www.google.com/search?q=site:"+url+"+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini+|+ext:env")
            log = ("https://www.google.com/search?q=site:"+url+"+ext:log")
            old = ("https://www.google.com/search?q=site:"+url+"+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup")
            login = ("https://www.google.com/search?q=site:"+url+"+inurl:login+|+inurl:signin+|+intitle:Login+|+intitle:sign+in+|+inurl:auth")
            print ("------Opening the Browser: "+url+" ------")
            time.sleep(1)
            webbrowser.open(publicexposed)
            webbrowser.open(conffile)
            webbrowser.open(log)
            webbrowser.open(old)
            webbrowser.open(login)
        elif ans =="20":
            sys.exit()
        else:
            print(bcolors.WARNING+"Not Valid Choice !!! Try again !!!"+bcolors.ENDC)
##################################################
def recon():
    recon=input("Please enter a URL or IP address: ")
    print("""
        1. Censys       3. GreyNoise
        2. Shodan       4. Security Trials

        Press ENTER to run ALL scan
        """)
    opt=input("Please select an option: ")
    if opt == "1":
        censys = ("https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q="+recon)
        print ("------Opening the Browser: "+recon+" ------")
        webbrowser.open(censys)
    elif opt == "2":
        shodan = ("https://www.shodan.io/search?query="+recon)
        print ("------Opening the Browser: "+recon+" ------")
        webbrowser.open(shodan)
    elif opt == "3":
        greyip=socket.gethostbyname(recon)
        greynoise=("https://viz.greynoise.io/ip/="+greyip)
        print ("------Opening the Browser: "+recon+" ------")
        webbrowser.open(greynoise)
    elif opt == "4":
    
        """   
       if recon.strip().isdigit():
            st=("https://securitytrails.com/list/ip/"+recon)
            print ("------Opening the Browser: "+recon+" ------")
            webbrowser.open(st)
        else: 
            st=("https://securitytrails.com/domain/"+recon+"/dns")
            print ("------Opening the Browser: "+recon+" ------")
            webbrowser.open(st)
        """
        reconip=socket.gethostbyname(recon)
        st=("https://securitytrails.com/list/ip/"+reconip)
        print ("------Opening the Browser: "+reconip+" ------")
        webbrowser.open(st)

    elif opt=="":
        censys = ("https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q="+recon)
        shodan = ("https://www.shodan.io/search?query="+recon)
        greyip=socket.gethostbyname(recon)
        greynoise=("https://viz.greynoise.io/ip/"+greyip)
        reconip=socket.gethostbyname(recon)
        st=("https://securitytrails.com/list/ip/"+reconip)
        print ("------Opening the Browser: "+recon+" ------")
        webbrowser.open(censys)
        webbrowser.open(shodan)
        webbrowser.open(greynoise)
        webbrowser.open(st)
    else:
            print(bcolors.WARNING+"Not Valid Choice !!! Try again !!!"+bcolors.ENDC)   
###########################################
def nmap():
    if os.geteuid() != 0:
        exit(bcolors.WARNING+"You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting."+bcolors.ENDC)
    else:
        print("Checking if Nmap is installed......")
        time.sleep(1)
        file_exists = os.path.exists("/usr/bin/nmap"or"/bin/nmap")
        if file_exists==True:
            print("""
            1. Single IP Scan
            2. Multiple IPs Scan    
                """)
            opt=input("Please select an option: ")
            #Single IP Scan    
            if opt == "1":
                ipadd=input("Please Enter an IP address: ")
                print("""
            1. All Ports Script/Service Scan            3. Check Alive Host
            2. Common Ports Script/Service Scan         4. Check Ports
                    """)
                nmap_opt=input("Please select an option: ")
                if nmap_opt =="1":
                    output=input("Please name the output file: ")
                    os.system("nmap "+ipadd+" -sV -sC -p- -oN "+output+".txt")
                elif nmap_opt =="2":
                    output=input("Please name the output file: ")
                    os.system("nmap "+ipadd+" -sV -sC -oN "+output+".txt")
                elif nmap_opt == "3":
                    os.system("nmap "+ipadd+" -sn")
                elif nmap_opt == "4":
                    os.system("nmap "+ipadd+" -p-")
            #Multiple IP Scan        
            if opt == "2":
                iplist=input("Please enter the path: ")
                print("""
            1. All Ports Script/Service Scan            3. Check Alive Host
            2. Common Ports Script/Service Scan         4. Check Ports
                    """)
                nmap_opt=input("Please select an option: ")
                if nmap_opt =="1":
                    output=input("Please name the output file: ")
                    os.system("nmap -iL "+iplist+" -sV -sC -p- -oN "+output+".txt")
                elif nmap_opt =="2":
                    output=input("Please name the output file: ")
                    os.system("nmap -iL "+iplist+" -sV -sC -oN "+output+".txt")
                elif nmap_opt == "3":
                    os.system("nmap -iL "+iplist+" -sn")
                elif nmap_opt == "4":
                    os.system("nmap -iL "+iplist+" -p-")

        elif file_exists==False:
            print("")
            print(bcolors.WARNING+"Please install Nmap"+bcolors.ENDC)
            print("")
            install=input("Install Nmap? y/n")
            if install =="y":
                os.system("apt-get install nmap")
                return main()
            elif install =="n":
                return main()
            elif install =="":
                os.system("apt-get install nmap")
                return main()
###############################
def bruteforcedirectory():
    if os.geteuid() != 0:
        exit(bcolors.WARNING+"You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting."+bcolors.ENDC)
    else:
        print("Checking if GoBuster is installed......")
        time.sleep(1)
        file_exists = os.path.exists("/usr/bin/gobuster"or"/bin/gobuster")
        if file_exists==True:
            print("""
            1. Fuzz Directory
            2. Fuzz Subdomain
            """)
            opt=input("Please select an option: ")
            if opt =="1":
                url=input("Please enter a URL: ")
                wordlistopt=input("""
Please enter a wordlist (Press ENTER to use default wordlist): 
                """)
                if wordlistopt =="":
                    wordlist=("data/common.txt")
                    os.system("gobuster -w "+wordlist+" dir -u "+url+" -t 100 -b 401,404")
                else: 
                    os.system("gobuster -w "+wordlistopt+" dir -u "+url+" -t 100 -b 401,404")

            if opt =="2":
                url=input("Please enter a domain: ")
                wordlistopt=input("""
Please enter a wordlist (Press ENTER to use default wordlist): 
                """)
                if wordlistopt =="":
                    wordlist=("data/common.txt")
                    os.system("gobuster -w "+wordlist+" dns -d "+url+" -t 100 -i")
                else:
                    os.system("gobuster -w "+wordlistopt+" dns -d "+url+" -t 100 -i")
            else:
                print(bcolors.WARNING+"Not Valid Choice !!! Try again !!!"+bcolors.ENDC)
        
        elif file_exists==False:
            print("")
            print(bcolors.WARNING+"Please install GoBuster"+bcolors.ENDC)
            print("")
            install=input("Install GoBuster? y/n ")
            if install =="y":
                os.system("apt-get install gobuster")
                return main()
            elif install =="n":
                return main()
            elif install =="":
                os.system("apt-get install gobuster")
            return main()
#####################################
def main():
    menu=True
    while menu:
        print("")
        print(bcolors.HEADER+"-----------------------------"+bcolors.ENDC+"Tools"+bcolors.HEADER+"---------------------------------"+bcolors.ENDC)
        print ("""
            1. GoogleDork                   
            2. Nmap
            3. Reconnaissance
            4. Brute Force Directory

            Press ENTER to exit the program
            """)
        print(bcolors.HEADER+"-------------------------------------------------------------------"+bcolors.ENDC)
        menu=input("Please select an option: ")
        if menu == "1":
            googlehack()
        if menu == "2":
            nmap()
        if menu == "3":
            recon()
        if menu =="4":
            bruteforcedirectory()
        elif menu=="":
            exit(bcolors.FAIL+"Exiting the Program......")
        else:
            print(bcolors.WARNING+"Not Valid Choice !!! Try again !!!"+bcolors.ENDC)

if __name__ == "__main__":
        main()
                   
