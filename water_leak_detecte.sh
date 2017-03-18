#gpio wfi 28 falling
gpio mode 27 out
gpio write 27 1
while :
do
  gpio wfi 28 rising
  echo "WATER!!!"
done
