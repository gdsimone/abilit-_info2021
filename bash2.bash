# es 1
alias cp = 'cp -i'
alias mv = 'mv -i'
alias rm = 'rm -i'
alias ld = 'ls -l -t'
alias la = 'ls -r'

#es 2
ls | wc -l

#es 3
#cerca il file esercitazione.txt nella directory data ( comando find directory-name search-expression) 
#seleziona tutti i file nella directory data eccetto quelli .py seguendo il path. 
#Poi grep -v prende in input linea per linea e da come output solo quelle in cui Token non appare.   
#dev/null scarta il comando che viene scritto
#Infine cat legge i dati dal file /var/log/syslog e | passa l'output del comando precedente come input
#al file mylog.txt

#es 4
#find cerca un file in base a vari attributi: nome, dimensione, autorizzazioni e così via.
#il comando generale è find directory-name search-expression
#la prima linea cerca nella directory \etc il file networkmanager
#nelle ultime è presente > che è un comando di redirezione, ossia cattura l'output di un
#file e lo invia come input ad un altro file


#es 5
#assicura che il processo in esecuzione non venga terminato quando si esce dal terminale

#es 6
#un editor a linea di comando si usa quando si deve solo entrare in un file per una rapida modifica
#Un editor grafico consente di modificare e manipolare immagini grafiche
#un IDE è un software che consente lo sviluppo del codice sorgente di un programma 

