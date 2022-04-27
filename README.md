# README

## Описание работы

В данной работе мы будем искать уязвимости в open-source progect _doxygen_, используя файззер AFL++.
Кроме того, мы напишем собственный кастомный мутатор входных данных и запустим AFL++ с использованием этого мутатора.

## Запуск AFL++ на doxygen

Для начала склонируем AFL++ с оффициального репозитория и соберем.
```shell
git clone https://github.com/AFLplusplus/AFLplusplus.git
cd AFLplusplus
make
sudo make install
```

После этого склонируем целевой проект (_doxygen_) с официального репозитория
```shell
git clone https://github.com/doxygen/doxygen.git
```

## Использование doxygen без файззера

Программа _doxygen_ генерирует документацию к коду, основываясь на комментарии специального вида.

```shell
cd doxygen
mkdir build && cd build
cmake ..
make
sudo make install
```

После этого в дериктории __build__ будт создана папка __bin__, содержащая бинарный файл.

```shell
doxygen main.cpp
```
После этого в текущей дериктории будут сформированы папки __html__ и __latex__, содержащие документацию к файлу main.cpp в фарматах html и latex соответственно.

## Запускаем doxygen под файззером

При первом запуске файззера у вас могут возникнуть следующие сообщения ошибки:

```sell
Hmm, your system is configured to send core dump notifications to an
external utility. This will cause issues: there will be an extended delay
between stumbling upon a crash and having this information relayed to the
fuzzer via the standard waitpid() API.
If you're just testing, set 'AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1'.

To avoid having crashes misinterpreted as timeouts, please log in as root
and temporarily modify /proc/sys/kernel/core_pattern, like so:

echo core >/proc/sys/kernel/core_pattern
```

```sell
Whoops, your system uses on-demand CPU frequency scaling, adjusted
between 390 and 3906 MHz. Unfortunately, the scaling algorithm in the
kernel is imperfect and can miss the short-lived processes spawned by
afl-fuzz. To keep things moving, run these commands as root:

cd /sys/devices/system/cpu
echo performance | tee cpu*/cpufreq/scaling_governor

You can later go back to the original state by replacing 'performance'
with 'ondemand' or 'powersave'. If you don't want to change the settings,
set AFL_SKIP_CPUFREQ to make afl-fuzz skip this check - but expect some
performance drop.
```

Вэтом случае, выполните следующие действия:
```sell
sudo su
echo core >/proc/sys/kernel/core_pattern
cd /sys/devices/system/cpu
echo performance | tee cpu*/cpufreq/scaling_governor
```

### Запуск бинарника без инструментирования

Этот вид файззинга применяется в том случае, если в распоряжении имеется только бинарник целевой программы.

```shell
afl-fuzz -n -i ./testcases -o findings -- /full/path/to/doxygen
```
ключ __-n__ показывает, что бинарный файл не инструментирован.

### Запуск инструментированного бинарника

В этом случае необходимо пересобрать бинарник из исподников с использованием _afl-g++_, _afl-clang++_ или _afl-clang-fast++_.

```shell
cd doxygen
mkdir build && cd build
CXX=afl-clang++ CC=afl-clang cmake -G "Unix Makefiles" ..
make
```

После этого запускаем файззер

```sell
afl-fuzz -D -m 10000 -i ./testcases -o findings -- /full/path/to/doxygen
```

- ключ __-D__ включает детерминированный файззинг
- ключ __-m 10000__ расширяет лимит используемой оперативной памяти
- ключ __-i__ указывает на дерикторию, содержащую начальный тестовый корпус
- ключ __-o__ указывает на дерикторию, в которую будут записываться результаты

## Подключаем кастомный мутатор

В текущей дериктории находится файл __custom_mutator.py__. Данный файл представляет собой кастомную мутацию данны для файззера AFL++, написанную согласно API кастомных мутаций. Для того, чтобы запустить файззер с использованием кастомной мутации выполним следующие шаги

```shell
chmod + x custom_mutation.py
export PYTHONPATH=`dirname full/path/to/custom_mutator.py`
export AFL_PYTHON_MODULE=custom_mutator
afl-fuzz -i ./testcases -o findings -- full/path/to/doxygen
```
___

### Демонстрация работы кастомных мутаций

Для демонстрации работы кастомного мутатора предусмотрен отдельный файл main.py.
```shell
chmod +x main.py
```
Вы можете запустить этот файл без аргументов, в этом случае мутации подвернутся все файлы, находящиеся в дериктории __testcases__. В текущей дериктории появялтся мутированные файлы (откройте их и посмотрите, что изменилось по сравнению с исходниками).
```shell
./main.py
```
Кроме того, есть возможность мутировать конкретный файл. Для этого передайте его программе в качестве аргумента.
```shell
./main.py full/path/to/file.cpp
```