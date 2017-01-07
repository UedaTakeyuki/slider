# https://hydrocul.github.io/wiki/commands/sed.html
sid=`/home/pi/SCRIPT/slider/getserialnumber.sh | cut -c 9-`
hostname=`hostname`
sudo sed -i -E "s/^(agent_name[\t ]*)(.*)/\1${hostname}_${sid}/" /etc/pandorafms/pandora_agent.conf
#sudo /etc/init.d/pandora_agent_daemon restart
sudo systemctl restart pandorafms-agent.service
