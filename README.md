# Python-0-Starting

## 開発環境

このプロジェクトでは、`uv`で管理されたPython 3.10を使用します。

```sh
uv sync
uv run python --version
```

仮想環境をシェルで有効化する場合は、`source .venv/bin/activate`を実行してください。

## Exercise 00: First Python Script

`ex00`では、Pythonの代表的な4種類のデータ構造を使い、それぞれの値を指定された挨拶に変更します。

提出するファイルは`ex00/Hello.py`です。

### 各データ型の説明

- リスト（`list`）は、複数の値を順番に保持します。`ft_list[1]`のように位置を指定して、作成後でも要素を変更できます。Pythonでは位置を`0`から数えるため、`[1]`は2番目の要素です。
- タプル（`tuple`）も複数の値を順番に保持しますが、作成後に要素を変更できません。そのため、今回は`ft_tuple`全体に新しいタプルを代入します。
- セット（`set`）は、重複しない値を順番なしで保持します。`remove()`で古い値を削除し、`add()`で新しい値を追加します。表示される要素の順番が変わることがありますが、問題ありません。
- 辞書（`dict`）は、キーと値の組み合わせを保持します。`ft_dict["Hello"]`のようにキーを指定すると、それに対応する値を変更できます。

### 実行方法

```sh
uv run python ex00/Hello.py
```

実行結果の内容は次のようになります。セットだけは要素の表示順が逆になる場合があります。

```text
['Hello', 'World!']
('Hello', 'Japan!')
{'Hello', 'Tokyo!'}
{'Hello': '42Tokyo!'}
```

## Exercise 01: First Use of Package

`ex01`では、Pythonの標準ライブラリを使って現在の時刻と日付を取得し、指定された形式で表示します。

提出するファイルは`ex01/format_ft_time.py`です。

### 処理内容

- `time.time()`は、1970年1月1日から現在までに経過した秒数を取得します。この値をUnix時間と呼びます。
- `{seconds:,.4f}`は、秒数を3桁ごとのカンマ区切り、小数点以下4桁で表示します。
- `{seconds:.2e}`は、秒数を`1.79e+09`のような科学表記で表示します。
- `datetime.datetime.now()`は、現在の日時を取得します。
- `strftime("%b %d %Y")`は、日付を`Aug 19 2026`のような「英語の月名・日・西暦」の形式に変換します。

取得するのは現在の時刻なので、実行するたびに秒数が変わり、日付も実行日のものになります。

### 実行方法

```sh
uv run python ex01/format_ft_time.py
```

出力は次のような形式になります。数値と日付は実行時点によって異なります。

```text
Seconds since January 1, 1970: 1,787,000,000.1234 or 1.79e+09 in scientific notation
Aug 19 2026
```

## Exercise 02: First Python Function

`ex02`では、渡されたオブジェクトの型を指定された形式で表示し、最後に`42`を返す関数を作成します。

提出するファイルは`ex02/find_ft_type.py`です。

### 処理内容

`all_thing_is_obj(object)`は、引数の型によって次の処理を行います。

- リスト、タプル、セット、辞書の場合は、型の名前と`type()`で取得した型を表示します。
- 文字列の場合は、文字列の内容を使って`<文字列> is in the kitchen`と型を表示します。
- それ以外の型の場合は、`Type not found`と表示します。
- どの型を渡した場合でも、戻り値は`42`です。

このファイルには関数の定義だけが含まれているため、単体で実行しても何も表示されません。

### 使用例

課題文と同じテストは、次のコマンドで実行できます。

```sh
uv run python ex02/tester.py
```

```python
from ex02.find_ft_type import all_thing_is_obj

all_thing_is_obj(["Hello", "World!"])
all_thing_is_obj("Brian")
print(all_thing_is_obj(10))
```

出力は次のようになります。

```text
List : <class 'list'>
Brian is in the kitchen : <class 'str'>
Type not found
42
```
