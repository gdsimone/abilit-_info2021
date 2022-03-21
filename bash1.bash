echo "Hello World";
#es 1
#command [flag] [argument]

#es 2
mkdir esercizi_bash
cd esercizi_bash
mkdir lezione_1 
mkdir lezione_2 
mkdir lezione_3
cd lezione_1
touch testo.txt 
touch es.sh
cd ..
cd lezione_3
touch es.sh
mkdir dati 
cd dati
touch data1.txt 
touch data2.txt

mv data2.txt newdata.txt
cd ..
cd ..

cd lezione_1
cp testo.txt lezione_2
cd ..
cd lezione_2
touch es.sh

chmod +x es.sh
cd ..
cd lezione_1
chmod +x testo.txt
cd..
cd lezione_3
cd dati
chmod +x data1.txt 
chmod +x newdata.txt
cd..
cd..

#es 3
mkdir esercitazione
touch esercizio.txt
cd esercizio.txt
echo questa è una prova
cat esercizio.txt

cd esercitazione
cd..

#es 4
mkdir temp
cd temp
touch prova.txt
cd prova.txt
echo '*'
cd..
cd..

cp temp backup
cd temp
cp prova.txt copiaA.txt
cp prova.txt copiaB.txt
cd..
rm -rf temp

#
