#!/bin/sh
#script version 0.8.1
clear
echo -e "\033[1;30;36m################ Script version 0.8.1 ################"
echo
echo -e "\033[0mThis script is going to install\033[1;30;37m sfarkxtc\033[0m and \033[1;30;37msfArkLib\033[0m"
echo
echo -e "sfArkLib and sfarkxtc are made by\033[1;30;37m raboof\033[0m, please see this website:"
echo -e "http://arnout.engelen.eu/ and this one http://melodymachine.com/"
echo
echo -e "\033[1;30;37m!!! Important !!!\033[0m"
echo -e "Please make sure you have already installed \033[1;30;37mg++\033[0m and \033[1;30;37mzlib1g-dev\033[0m"
echo
echo -e "Script made by \033[1;30;37mmaltouzes\033[0m"
echo
echo -e "Do you want to continue and install \033[1;30;37msfArkLib\033[0m and \033[1;30;37msfarkxtc\033[0m? \033[1;30;37m\033[0m\033[1;30;37my\033[0m=yes \033[1;30;37mn\033[0m=no, for more informations please right \033[1;30;37minfo\033[0m"
read fich

if [ "$fich" = "info" ] || [ "$fich" = "INFO" ] || [ "$fich" = "Info" ];then
	clear
	cat INFO
	echo
	echo -e "Please press enter to continue"
	read
	bash installation_sfarkd

elif [ "$fich" = "y" ] || ["$fich" = "Y" ]; then
	# Download sfArkLib, install it and remove unused files
	wget https://github.com/raboof/sfArkLib/archive/master.zip
	unzip master.zip
	cd sfArkLib-master
	make
	sudo make install
	sudo ldconfig
	cd ..
	rm master.zip
	rm -rf sfArkLib-master

	# Download sfarkxtc, install it and remove unused files
	wget https://github.com/raboof/sfarkxtc/archive/master.zip
	unzip master.zip
	cd sfarkxtc-master
	sudo make install
	cd ..
	rm master.zip
	rm -rf sfarkxtc-master

	cp .CONVERSION sfarkxtc-master/CONVERSION

	#End
	echo -e "\033[1;30;37mInstallation complet, please run \033[1;30;33mmain.py\033[1;30;37m \033[1;30;37m. Enjoy!\033[0m"
	exit 0

else
	clear
	echo -e "\033[1;30;37mScript closed\033[0m"
	exit 0
fi
exit 0
