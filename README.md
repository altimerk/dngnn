### dngnn

Нужно как-то скормить входной файл нейросети, Попробуем для этого понять, как устроен формат DNG

https://stackoverflow.com/questions/41496484/how-does-rawpy-reads-dng-frames
https://stackoverflow.com/questions/41453129/dng-raw-pictures-imported-as-16-bit-deep-but-unexpected-plt-show-result

https://www.odelama.com/photo/Developing-a-RAW-Photo-by-hand/

Будем подавать на вход нейросети сырые данные (метод raw.raw_image возвращает одноканальное изображение)

Для подготовки данных необходимо выполнить ноутбук [prepare_data.ipynb](https://github.com/altimerk/dngnn/blob/main/prepare_data.ipynb).
