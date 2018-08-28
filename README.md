# Taiwan Stock Real Time Crawler

用multiprocessing爬台股即時資訊的爬蟲，[參考](https://github.com/Asoul/tsrtc)

## 功能
- 提供always run in backend 選項
- 提供python multiprocessing進行爬蟲
- 每3~5秒提供每日股票最新交易資訊，並寫入 `data` 中，當天的日期資料夾內（ex. `20150303`），裡面把所有抓的資料按股票編號放 `XXXX.csv` 中，`XXXX` 就是股票編號。

## 環境需求

- Python2 or Python3

## 安裝相關套件

```
pip install -r requirements.txt
```

## 使用方法

`python crawl.py`

可以爬當下當沖股票的即時資訊。

### 更改清單

若要改抓取的清單，可以把 `stocknumber.csv` 中的股票編號換掉就好了。

### 資料整理

每天跑完後，可以執行 `python cleanTodayDuplicateData.py` 刪除重複抓到的資料和依照時間排序。

### 背景執行

Linux/Mac:
- 修改sh檔權限:chmod 755 run_code.sh
- 背景always run: nohup bash -c "exec  ./run_code.sh&"
- 查看背景執行情況: ps -ef | grep python
- 停止執行: kill xxxx（run_code.sh編號）

## 資料來源

[台灣證券交易所 - 基本市況報導網站](http://mis.twse.com.tw/stock/fibest.jsp)

## 郭旻軍 (歡迎來信討論)
- `whane601@gmail.com`

最後更新時間：`2018/08/28`
