while true
do
    python genCrontabScript.py
    python crawl.py
    python cleanTodayDuplicateData.py
    sleep 5
done
    python genCrontabScript.py
    python crawl.py
    python cleanTodayDuplicateData.py
    sleep 5
