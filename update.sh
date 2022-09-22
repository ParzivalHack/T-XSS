if [ -d "$HOME/T-XSS" ];
then
cd $HOME
rm -rf T-XSS
elif [ -d "$HOME/T-XSS" ];
then
cd $HOME
rm -rf T-XSS
else
echo
exit 1
fi
cd $HOME
sleep 1
echo -e "         Update is going on, please be patient :)"
echo
printf "                     ["
# While process is running...
while git clone https://github.com/ParzivalHack/T-XSS 2> /dev/null; do 
    printf  "▓▓▓▓▓▓▓▓▓▓▓▓▓"
    sleep 1
done
printf ""
echo
echo
echo
printf "           Updated successfully to the latest version!"
sleep 2.0
clear
cd $HOME
cd T-XSS
python T-XSS.py
