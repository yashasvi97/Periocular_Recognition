test_i="/home/yashasvi/Desktop/BTAS_2010/UBIris_v2/C10_S1_I15.tiff"
for (( i = 1; i <= 10; i++ )); do
	train_i="/home/yashasvi/Desktop/BTAS_2010/UBIris_v2/C"
	train_i+=$i
	train_i+="_S1_I1.tiff"
	echo "checking with subject "$i
	python final.py $train_i $test_i
	bash base.sh
	python cal_gist.py
	echo " "
done