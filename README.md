# YoutubeCC (`yt-cc`) - A Youtube Closed Captions (`.json3`) parser

`yt-cc` is a Python library that parses Youtube Closed Captions (`.json3`) files. It is a simple and easy-to-use library that can be used to query precise parts of the video transcript or iterate over the entire transcript.


```python
%load_ext autoreload
%autoreload 2
```


```python
from pathlib import Path

from yt_dlp import YoutubeDL
from yt_cc import YoutubeCC
```


```python
DATA_PATH = Path.cwd() / ".tmp"
```

## Downloading the Closed Captions with `yt-dlp`

To download the closed captions of a Youtube video, you can use the `yt-dlp` command-line tool. You can install `yt-dlp` using `pip`:

```bash
pip install yt-dlp
```

To download the closed captions of a Youtube video in the `.json3` format, you can use the following command:

```bash
yt-dlp --write-auto-sub --skip-download --sub-format json3 <video-url>
```

You can also download the closed captions with the `yt-dlp` Python API:


```python
YoutubeDL(
    params = dict(
        paths=dict(home=str(DATA_PATH)),
        skip_download=True,
        outtmpl="%(id)s.%(ext)s",
        subtitlesformat="json3",
        writeautomaticsub=True,
    )
).download(["https://www.youtube.com/watch?v=oHWuv1Aqrzk"])

yt_cc_file_path = next(DATA_PATH.glob("*.json3"))
yt_cc_file_path
```

    [youtube] Extracting URL: https://www.youtube.com/watch?v=oHWuv1Aqrzk
    [youtube] oHWuv1Aqrzk: Downloading webpage
    [youtube] oHWuv1Aqrzk: Downloading ios player API JSON
    [youtube] oHWuv1Aqrzk: Downloading android player API JSON


    WARNING: [youtube] Skipping player responses from android clients (got player responses for video "aQvGIIdgFDM" instead of "oHWuv1Aqrzk")


    [youtube] oHWuv1Aqrzk: Downloading m3u8 information
    [info] oHWuv1Aqrzk: Downloading subtitles: en
    [info] oHWuv1Aqrzk: Downloading 1 format(s): 248+251
    Deleting existing file /home/arthur/Documents/02.workspace/02.active/clips-analytics/yt-cc/.tmp/oHWuv1Aqrzk.en.json3
    [info] Writing video subtitles to: /home/arthur/Documents/02.workspace/02.active/clips-analytics/yt-cc/.tmp/oHWuv1Aqrzk.en.json3
    [download] Destination: /home/arthur/Documents/02.workspace/02.active/clips-analytics/yt-cc/.tmp/oHWuv1Aqrzk.en.json3
    [download] 100% of   71.66KiB in 00:00:00 at 1.28MiB/s





    PosixPath('/home/arthur/Documents/02.workspace/02.active/clips-analytics/yt-cc/.tmp/oHWuv1Aqrzk.en.json3')



## Parse the Closed Captions with `yt-cc`


```python
youtube_caption = YoutubeCC(yt_cc_file_path)
youtube_caption
```





<h3>YoutubeCC</h3>
<ul>
    <li>File: /home/arthur/Documents/02.workspace/02.active/clips-analytics/yt-cc/.tmp/oHWuv1Aqrzk.en.json3</li>
    <li>lines: 202</li>
    <li>Segments: 768</li>
</ul>





```python

for i, line_cc in enumerate(youtube_caption):
    print(line_cc)
    if i > 5:
        break
```

    LineCC(event_id=1.0, start_time_ms=0.0, duration_ms=218599.0, window_id=nan, window_style_id=1.0, window_position_id=1.0, append=nan, segments=[])
    LineCC(event_id=nan, start_time_ms=2820.0, duration_ms=5279.0, window_id=1.0, window_style_id=nan, window_position_id=nan, append=nan, segments=['is', ' there', ' cool', ' small', ' projects', ' like', ' uh'])
    LineCC(event_id=nan, start_time_ms=5510.0, duration_ms=2589.0, window_id=1.0, window_style_id=nan, window_position_id=nan, append=1.0, segments=['\n'])
    LineCC(event_id=nan, start_time_ms=5520.0, duration_ms=6180.0, window_id=1.0, window_style_id=nan, window_position_id=nan, append=nan, segments=['archive', ' sanity', ' and', ' and', ' so', ' on', ' that', " you're"])
    LineCC(event_id=nan, start_time_ms=8089.0, duration_ms=3611.0, window_id=1.0, window_style_id=nan, window_position_id=nan, append=1.0, segments=['\n'])
    LineCC(event_id=nan, start_time_ms=8099.0, duration_ms=5580.0, window_id=1.0, window_style_id=nan, window_position_id=nan, append=nan, segments=['thinking', ' about', ' the', ' the', ' the', ' the', ' world', ' the'])
    LineCC(event_id=nan, start_time_ms=11690.0, duration_ms=1989.0, window_id=1.0, window_style_id=nan, window_position_id=nan, append=1.0, segments=['\n'])



```python
youtube_caption.lines
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>event_id</th>
      <th>start_time_ms</th>
      <th>duration_ms</th>
      <th>window_id</th>
      <th>window_style_id</th>
      <th>window_position_id</th>
      <th>append</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>0</td>
      <td>218599.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>2820</td>
      <td>5279.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>5510</td>
      <td>2589.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>5520</td>
      <td>6180.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>8089</td>
      <td>3611.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>197</th>
      <td>NaN</td>
      <td>212580</td>
      <td>3900.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>198</th>
      <td>NaN</td>
      <td>214850</td>
      <td>1630.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>199</th>
      <td>NaN</td>
      <td>214860</td>
      <td>3739.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>200</th>
      <td>NaN</td>
      <td>216470</td>
      <td>2129.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>201</th>
      <td>NaN</td>
      <td>216480</td>
      <td>2119.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>202 rows × 7 columns</p>
</div>




```python
youtube_caption.segments
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>asr_confidence</th>
      <th>offset_ms</th>
      <th>pen_id</th>
      <th>start_time_ms</th>
      <th>line_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>is</td>
      <td>248.0</td>
      <td>NaN</td>
      <td>None</td>
      <td>2820</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>there</td>
      <td>248.0</td>
      <td>599.0</td>
      <td>None</td>
      <td>3419</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>cool</td>
      <td>248.0</td>
      <td>839.0</td>
      <td>None</td>
      <td>3659</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>small</td>
      <td>248.0</td>
      <td>1020.0</td>
      <td>None</td>
      <td>3840</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>projects</td>
      <td>248.0</td>
      <td>1380.0</td>
      <td>None</td>
      <td>4200</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>763</th>
      <td>sounds</td>
      <td>248.0</td>
      <td>1260.0</td>
      <td>None</td>
      <td>216120</td>
      <td>199</td>
    </tr>
    <tr>
      <th>764</th>
      <td>kind</td>
      <td>240.0</td>
      <td>1320.0</td>
      <td>None</td>
      <td>216180</td>
      <td>199</td>
    </tr>
    <tr>
      <th>765</th>
      <td>of</td>
      <td>248.0</td>
      <td>1500.0</td>
      <td>None</td>
      <td>216360</td>
      <td>199</td>
    </tr>
    <tr>
      <th>766</th>
      <td>\n</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>216470</td>
      <td>200</td>
    </tr>
    <tr>
      <th>767</th>
      <td>crazy</td>
      <td>248.0</td>
      <td>NaN</td>
      <td>None</td>
      <td>216480</td>
      <td>201</td>
    </tr>
  </tbody>
</table>
<p>768 rows × 6 columns</p>
</div>




```python
print(youtube_caption.get_text(start_time_ms=0, end_time_ms=10000))
```

    is there cool small projects like uh
    archive sanity and and so on that you're
    thinking about the the the



```python

```
