### dngnn

Нужно как-то скормить входной файл нейросети, Попробуем для этого понять, как устроен формат DNG

https://stackoverflow.com/questions/41496484/how-does-rawpy-reads-dng-frames
https://stackoverflow.com/questions/41453129/dng-raw-pictures-imported-as-16-bit-deep-but-unexpected-plt-show-result

https://www.odelama.com/photo/Developing-a-RAW-Photo-by-hand/

Будем подавать на вход нейросети сырые данные (метод raw.raw_image возвращает одноканальное изображение)

Для подготовки данных необходимо выполнить ноутбук [prepare_data.ipynb](https://github.com/altimerk/dngnn/blob/main/prepare_data.ipynb).

#### Пример сгенерированных данных

Оригинальное изображение

![alt_text](https://github.com/altimerk/dngnn/blob/main/img/original.png "Оригинальное изображение")

Сгенерированное изображение

![alt_text](https://github.com/altimerk/dngnn/blob/main/img/generated.png "Сгенерированное изображение")

#### Возможные дальнейшие улучшения

1. Можно облегчить сеть. Сейчас используется U-net с resnet18 backbone (4 блока), можно заменить более легкими слоями.
2. Подавать на вход сети дополнительную информацию из dng-файла (кроме raw_image)
3. Добавить аугменатцию (сейчас по сути используется только random crop)

