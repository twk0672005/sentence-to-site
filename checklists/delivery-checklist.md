# Delivery Checklist

交付時先給可見結果，再給同claim匹配嘅fresh evidence。

## 好格式

```text
Artifact: /path/to/result
Preview: /path/to/representative-screenshot.png

而家可以睇到：...
判斷：...
下一步：...

Evidence receipt: /path/to/readback.json
Verdict: PASS / PARTIAL / FAIL / WAITING_FOR_NOVA
```

## 避免

- 一開始丟 terminal log
- 長篇講用了什麼 package
- 沒截圖就說完成
- 把 partial 說成 pass
- 沒看 screenshot 就說高質
- 將HTTP 200、build、file exists或agent success當產品PASS
- 將全部base64／raw logs／完整JSON貼入root conversation
