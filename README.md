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

## Exercise 03: NULL Not Found

`ex03`では、Pythonで「値がない」「空である」とみなされる代表的な値を、型と値の両方を使って判別します。

提出するファイルは`ex03/NULL_not_found.py`です。

### 処理内容

`NULL_not_found(object)`は、次の値をそれぞれ指定された形式で表示します。

- `None`を`Nothing`として表示します。
- 浮動小数点数の`NaN`を`Cheese`として表示します。
- 整数の`0`を`Zero`として表示します。
- 空文字列を`Empty`として表示します。
- 真偽値の`False`を`Fake`として表示します。

対象の値を正常に判別できた場合は`0`を返します。それ以外の場合は`Type not Found`と表示し、`1`を返します。

Pythonでは`False == 0`が成り立つため、値だけでなく型も確認することが重要です。また、`NaN`は自分自身とも等しくならないという性質を使って判別しています。

### 実行方法

課題文と同じテストは、次のコマンドで実行できます。

```sh
uv run python ex03/tester.py
```

出力は次のようになります。

```text
Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
```

## Exercise 04: The Even and the Odd

`ex04`では、コマンドライン引数として受け取った整数が偶数か奇数かを判定します。

提出するファイルは`ex04/whatis.py`です。

### 処理内容

- 引数がない場合は、何も表示せず終了します。
- 引数が整数の場合は、`2`で割った余りを使って偶数か奇数かを判定します。
- 引数が整数に変換できない場合は、`AssertionError: argument is not an integer`と表示します。
- 引数が2つ以上ある場合は、`AssertionError: more than one argument is provided`と表示します。
- 想定されるエラーはプログラム内で処理するため、トレースバックは表示されません。

コマンドライン引数は`sys.argv`から取得します。`sys.argv[0]`にはスクリプト名が入るため、ユーザーが指定した最初の引数は`sys.argv[1]`です。

### 実行例

```sh
uv run python ex04/whatis.py 14
uv run python ex04/whatis.py -5
uv run python ex04/whatis.py Hi!
```

```text
I'm Even.
I'm Odd.
AssertionError: argument is not an integer
```

## Exercise 05: First Standalone Python Program

`ex05`では、コマンドラインまたは標準入力から文章を受け取り、含まれている文字を種類別に数えます。入力の受け取りから結果の表示、エラー処理までを備えた、単体で動作するプログラムを作る課題です。

提出するファイルは`ex05/building.py`です。

### 処理内容

入力された文章について、次の5種類と全文字数を表示します。

- 大文字: `str.isupper()`で判定
- 小文字: `str.islower()`で判定
- 句読点・記号: `string.punctuation`に含まれるかで判定
- 空白文字: `str.isspace()`で判定
- 数字: `str.isdigit()`で判定
- 全文字数: `len()`で取得

文字ごとの判定結果を`sum()`で合計し、それぞれの文字数を求めます。

### 入力方法

引数を1つ指定した場合は、その引数を文章として使用します。

```sh
uv run python ex05/building.py "Hello World! 42"
```

引数がない場合や空文字列の場合は、次のメッセージを表示して標準入力を読み取ります。

```text
What is the text to count?
```

macOSやLinuxでは文章を入力したあとにCtrl+Dを押すと入力を終了できます。Enterで入力した改行も1つの空白文字として数えられます。

引数が2つ以上指定された場合は、プログラム内で例外を処理して次のように表示します。

```text
AssertionError: more than one argument is provided
```

### 出力例

`Hello World! 42`を指定した場合の出力です。

```text
The text contains 15 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
2 digits
```

## Exercise 06: Reimplementing Filter

`ex06`は、組み込みの`filter()`をリスト内包表記で再実装するパートと、その関数を使って文章から一定の長さを超える単語を抽出するパートで構成されています。

提出するファイルは`ex06/ft_filter.py`と`ex06/filterstring.py`です。

### `ft_filter.py`

`ft_filter(function, iterable)`は、iterableの各要素にfunctionを適用し、結果が真になる要素だけをリストで返します。

functionに`None`を指定した場合は、要素自体が真として評価されるものだけを返します。組み込みの`filter()`は使用せず、リスト内包表記で処理します。docstringは組み込み`filter`の説明と同じ内容です。

### `filterstring.py`

コマンドラインから文章`S`と整数`N`を受け取り、長さが`N`より大きい単語だけをリストとして表示します。単語は空白で区切り、判定条件にはlambda式を使用します。

```sh
uv run python ex06/filterstring.py "Hello the World " 4
```

```text
['Hello', 'World']
```

引数が2つでない場合や、第2引数を整数に変換できない場合は次のように表示します。

```text
AssertionError: the arguments are bad
```

### テスト方法

```sh
uv run python ex06/tester.py
```

成功すると`All tests passed.`と表示されます。

## Exercise 07: Dictionaries SoS

`ex07`では、受け取った文章をモールス信号へ変換するコマンドラインプログラムを作成します。

提出するファイルは`ex07/sos.py`です。

### 処理内容

ASCIIの英字、数字、空白をモールス信号へ変換します。

- 小文字は大文字へ変換してから処理します。
- 英字と数字は`.`と`-`で構成された符号へ変換します。
- 文章中の空白は`/`へ変換します。
- 変換後の各符号は1つの空白で区切ります。

文字とモールス信号の対応関係は辞書に保存し、文字をキーとして符号を取得します。グローバル変数を避けるため、辞書は関数内で定義しています。

### 実行例

```sh
uv run python ex07/sos.py "42 Tokyo"
```

```text
....- ..--- / - --- -.- -.-- ---
```

引数が1つでない場合や、英数字と空白以外の文字が含まれる場合は次のように表示します。

```text
AssertionError: the arguments are bad
```

### テスト方法

```sh
uv run python ex07/tester.py
```

成功すると`All tests passed.`と表示されます。
