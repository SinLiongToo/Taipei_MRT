# 台北捷運四界走 — 歡喜學台語 (Taipei MRT Taigi Learning WebApp)

這是一個專為學習台灣話（台語 / Taigi）設計的網頁互動式交通學習工具，以台北捷運 (TRTC) 的路網結構為基礎，提供生動有趣的語音朗讀、線別詞彙檢索與檢定挑戰。

* 🌐 **GitHub Pages 線上直接玩**：[https://sinliongtoo.github.io/Taipei_MRT/](https://sinliongtoo.github.io/Taipei_MRT/)
* 📦 **GitHub Repository**：[https://github.com/SinLiongToo/Taipei_MRT](https://github.com/SinLiongToo/Taipei_MRT)

---

## 🌟 主要功能

1. **購票大冒險 (Ticket Booth Adventure)**：
   * 選擇台北捷運起訖站、票張數、乘車時間、車種。
   * **路網最短路徑 BFS 演算法**：自動計算轉乘路線（支援全系統 13 個轉乘站與 5 大主線）、月台號碼與票價。
   * **實體台語語音拼接**：採用教育部辭典真人發音 MP3，動態拼接成完整購票句型：「我欲去淡水，買兩張捷運票，下晡三點半開車...」。
   * **地圖火車動畫**：捷運車廂會沿著鐵路軌道路線動態行駛。

2. **交通詞彙牆 (Vocabulary Wall)**：
   * **全路網 114 車站完整收錄**：包含 15 個核心交通與捷運場景詞彙，以及台北捷運全部 114 個車站台語發音。
   * **依 5 大主線分組檢索**：支援依「🔴 淡水信義線」、「🔵 板南線」、「🟢 松山新店線」、「🟠 中和新蘆線」、「🟤 文湖線」色彩分類快速篩選。
   * **即點即聽真人語音**：點擊任一卡片即可聆聽教育部審定標準發音。
   * **📥 匯出 JSON 功能**：支援一鍵將詞彙庫、台羅拼音、英文與音檔 ID 完整匯出為 `taipei_mrt_taigi_vocab.json` 供後續教學與研究使用。

3. **時間鐘點師 (Clock Trainer)**：
   * 可任意拖動指針或使用微調按鈕、預設時間，聆聽台語的「時間」與「時段」發音。

4. **台語大檢定 (Challenge Mode)**：
   * 提供「售票員聽力挑戰」與「發車時刻聽力挑戰」，隨機出 10 題台語聽力選擇題。
   * 限時 20 秒回答，挑戰台語聽力！

5. **我的集章冊 (Stamp Album)**：
   * 檢定答對 8 題以上可解鎖隨機車站的限量印章。收集完 114 個車站印章以完成旅程！

---

## 🔊 語音引擎機制 (Speech Engine Mechanism)

本專案內建**雙語音引擎設計**，提供最佳的發音流暢度與穩定性：

1. **實體台語真人發音 (預設優先)**：
   * 購票大冒險與詞彙發音優先採用**教育部《臺灣台語常用詞辭典》**的真人錄音檔 (MP3)。
   * 語音採用動態單字/單詞拼接技術，將「我」+「欲」+「對」+「[起點站]」+「去」+「[終點站]」... 等音軌串聯播放，實現極具本土特色的真人購票句子。
   * **相同羅馬字語音備援機制 (Same-Romanization Fallback)**：承襲自 *Taiwanese Lô-má-jī Tone Sandhi Tool* 的觀念。當某個站名的特定漢字（例如「唭哩岸」的「唭」）在教育部辭典字庫中沒有直接錄音時，系統會自動在資料庫中尋找**拼音/羅馬字相同**的其他漢字音檔（例如「期」的台羅為 `kî`，對應拼音 `ki`）作為發音替代，確保所有 114 個車站皆能完整流暢地播放真人語音。

2. **本地合成發音 (離線/失敗備援)**：
   * 當網路連線異常或 MP3 音檔加載失敗時，會自動切換為瀏覽器內建的 `SpeechSynthesis` (語音合成 TTS)。
   * 透過 `twHomophones` 同音字庫對照（如將捷運站名「西門」替換為「誰門」，用國語 `zh-TW` 語音引擎模擬），以達到流暢自然的台語發音備援效果。

---

## 🔧 音檔 ID 與鏡像 CDN 維護記錄

### 1. 詞目 ID 校正（2026-07）

本專案音檔 ID 採用 **ChhoeTaigi KipSutianDataMirror** 的 `詞目id` 編號系統（即 CDN 路徑 `imtong/sutiau/{id}(1).mp3`）。

* **根本問題**：原始版本錯誤使用了萌典 API (`dict-twblg.json`) 的 `heteronyms.id`，導致播放錯誤詞彙（如「淡水」誤播為「清茶」）。
* **修正方案**：透過自動化腳本比對官方辭典索引，全面更正 114 個站名與詞彙的正確 ID。

| 車站/詞彙 | 舊（錯誤）ID | 新（正確）KipSutian 詞目id | 說明 |
|-----------|------------|--------------------------|------|
| 淡水 | 7546 | **7521** | `Tām-tsuí` |
| 台北車站 | 1416, 1395, 3463 | **21302** | 完整站名單一錄音 |
| 北投 | 1395, 3220 | **21290** | `Pak-tâu` |
| 大安森林公園 | 多個散字 | **27679** | 完整站名單一錄音 |
| 我 | 3139 | **3139** | ✅ 已正確（同 KipSutian ID） |
| 去 | 1405 | **1395** | `khì` |
| 台北101/世貿 | 散字 | **20637**, 2, **12091**, 2, **1292**, **9043** | 臺北+一+零(龍)+一+世+貿 |

### 2. CDN 版本動態同步機制（2026-10）

* **斷音問題排查**：開源鏡像庫在 2026-10-19 將舊版本目錄 `20260503-2330` 更新並移除，更換為 `20261019-0109`，導致固定字串的音檔請求出現 404 錯誤而無聲音。
* **動態同步解決方案**：
  在 `app.js` 啟動時加入動態同步邏輯，主動抓取鏡像庫的 `manifest.json`：
  ```javascript
  let kipsutianVersionDir = "20261019-0109";
  if (typeof fetch !== "undefined") {
      fetch("https://chhoetaigi.github.io/KipSutianDataMirror/public/manifest.json")
          .then(res => res.json())
          .then(data => {
              if (data && data.latest_version_dir) {
                  kipsutianVersionDir = data.latest_version_dir;
              }
          })
          .catch(err => console.warn("KipSutian manifest fetch fallback to default:", kipsutianVersionDir));
  }
  ```
  即使未來鏡像庫再次隨教育部辭典發布新版本目錄，系統也會自動獲取最新路徑，從根本上避免路徑失效。

---

## 📁 檔案結構

* `index.html` — 網頁主體結構。
* `style.css` — 台北捷運風格設計系統（支援淺色/深色模式切換與玻璃擬物化風格）。
* `app.js` — 核心運算邏輯，包含 114 個車站資料、音檔代碼、BFS 最短路徑邏輯與 CDN 動態同步。
* `compile.py` — 自動編譯腳本，可將 HTML/CSS/JS 打包成單一檔案。
* `index_single.html` — 編譯後的單一 HTML 檔案，包含所有 inline CSS/JS。
* `blogger_base64_embed.html` — 提供部落格 iframe 嵌入的 Base64 整合碼。

---

## 🚀 開始使用與部署

### 線上體驗
直接開啟 GitHub Pages 網址：
👉 **[https://sinliongtoo.github.io/Taipei_MRT/](https://sinliongtoo.github.io/Taipei_MRT/)**

### 本地運行
1. 直接在瀏覽器中打開 `index.html` 即可運行！
2. 或是使用 Python 在本地啟動伺服器：
   ```bash
   python -m http.server 8000
   ```
   然後在瀏覽器開啟 `http://localhost:8000`。

### 編譯單一檔案
執行 `compile.py` 將專案打包：
```bash
python compile.py
```
* `index_single.html`：整合了所有樣式與邏輯的單一 HTML，適合離線使用與傳送。
* `blogger_base64_embed.html`：產生 base64 編碼的 iframe 程式碼，可直接貼入 Blogger、WordPress 等部落格平台中嵌入展示。
