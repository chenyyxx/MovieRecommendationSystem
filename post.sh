for i in {300001..300015}
do
    ((id=$i-300000))
    echo @$id.file
    curl --data-binary @$id.file http://0.0.0.0:8080/$i/ratings 
done