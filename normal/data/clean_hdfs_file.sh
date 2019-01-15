for top_file in `hadoop fs -ls hdfs://liudanmeng/ | awk '{print $8}'`
do
    # echo ${top_file}
    for i in {30..100}
    do
        echo hadoop fs -rm -r ${top_file}/`date -d -${i}day +%Y-%m-%d`*
        hadoop fs -rm -r "${top_file}/`date -d -${i}day +%Y-%m-%d`*"
    done
done
