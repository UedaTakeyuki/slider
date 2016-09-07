#gpio wfi 28 falling
while :
do
  gpio wfi 28 rising
  echo "WATER!!!"
done
