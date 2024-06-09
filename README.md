# Urban_Sounds_Classification
Classification of urban sounds audio using deep learning

## Database

**Description**
-----------

This dataset contains 8732 labeled sound excerpts (<=4s) of urban sounds from 10 classes: `air_conditioner`, `car_horn`, 
`children_playing`, `dog_bark`, `drilling`, `engine_idling`, `gun_shot`, `jackhammer`, `siren`, and `street_music`. The classes are 
drawn from the urban sound taxonomy described in the following article, which also includes a detailed description of 
the dataset and how it was compiled:

J. Salamon, C. Jacoby and J. P. Bello, "A Dataset and Taxonomy for Urban Sound Research", 
22nd ACM International Conference on Multimedia, Orlando USA, Nov. 2014.

All excerpts are taken from field recordings uploaded to www.freesound.org. The files are pre-sorted into ten folds
(folders named fold1-fold10) to help in the reproduction of and comparison with the automatic classification results
reported in the article above.

In addition to the sound excerpts, a CSV file containing metadata about each excerpt is also provided.

Link to the database;
[Link Text](https://urbansounddataset.weebly.com/urbansound8k.html)



**Audio Files Included**
--------------------

8732 audio files of urban sounds (see description above) in WAV format. The sampling rate, bit depth, and number of 
channels are the same as those of the original file uploaded to Freesound (and hence may vary from file to file).


**Meta-data Files Included**


`UrbanSound8k.csv`

This file contains meta-data information about every audio file in the dataset. This includes:

* slice_file_name: 
The name of the audio file. The name takes the following format: [fsID]-[classID]-[occurrenceID]-[sliceID].wav, where:
  * [fsID] = the Freesound ID of the recording from which this excerpt (slice) is taken
  * [classID] = a numeric identifier of the sound class (see description of classID below for further details)
  * [occurrenceID] = a numeric identifier to distinguish different occurrences of the sound within the original recording
  * [sliceID] = a numeric identifier to distinguish different slices taken from the same occurrence

* fsID:
The Freesound ID of the recording from which this excerpt (slice) is taken

* start
The start time of the slice in the original Freesound recording

* end:
The end time of slice in the original Freesound recording

* salience:
A (subjective) salience rating of the sound. 1 = foreground, 2 = background.

* fold:
The fold number (1-10) to which this file has been allocated.

* classID:
A numeric identifier of the sound class:
0 = air_conditioner
1 = car_horn
2 = children_playing
3 = dog_bark
4 = drilling
5 = engine_idling
6 = gun_shot
7 = jackhammer
8 = siren
9 = street_music

* class:
The class name: air_conditioner, car_horn, children_playing, dog_bark, drilling, engine_idling, gun_shot, jackhammer, 
siren, street_music.

## Data Exploration

### Audio Statistics

|       fsID      |    start    |     end     |  salience  |   fold   |  classID  |  length  |   bitrate   | channels | sample_rate | bits_per_sample |
|:---------------:|:-----------:|:-----------:|:----------:|:--------:|:---------:|:--------:|:-----------:|:--------:|:-----------:|:---------------:|
| count           | 2000.000000 | 2000.000000 | 2000.000000 | 2000.000 | 2000.000000 | 2000.00000 | 2000.000000 | 2000.000000 | 2000.000000 | 2000.000000 |
| mean            | 115516.149000 | 34.462350 | 38.150132 | 1.265000 | 5.387000 | 4.75700 | 3.687096 | 1.758314e+06 | 1.908500 | 48986.350000 | 18.480000 |
| std             | 29434.261664 | 69.599955 | 69.692708 | 0.441444 | 2.820498 | 2.83319 | 0.881551 | 8.093881e+05 | 0.288391 | 14081.103736 | 3.803266 |
| min             | 11722.000000 | 0.000000 | 0.261224 | 1.000000 | 1.000000 | 0.00000 | 0.190000 | 2.560000e+05 | 1.000000 | 16000.000000 | 8.000000 |
| 25%             | 105029.000000 | 3.500000 | 7.306557 | 1.000000 | 3.000000 | 3.00000 | 4.000000 | 1.411200e+06 | 2.000000 | 44100.000000 | 16.000000 |
| 50%             | 118278.000000 | 10.000000 | 13.994276 | 1.000000 | 5.000000 | 5.00000 | 4.000000 | 1.411200e+06 | 2.000000 | 44100.000000 | 16.000000 |
| 75%             | 135160.000000 | 31.133479 | 34.551082 | 2.000000 | 8.000000 | 7.00000 | 4.000000 | 2.116800e+06 | 2.000000 | 48000.000000 | 24.000000 |
| max             | 147926.000000 | 534.628805 | 538.628805 | 2.000000 | 10.000000 | 9.00000 | 4.000000 | 4.608000e+06 | 2.000000 | 96000.000000 | 24.000000 |

### Labels Distribution
![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/labels.png)

### Waveplots
![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/waveplots.png)

### Mel-Spectogram
![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/Mel_spectograms.png)

### MFCC
![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/MFFC.png)

## Results

The trained a end-to-end model achieves high accuracy in classifying urban sounds. The performance is validated on a separate test set, with metrics like precision, recall, and F1-score demonstrating the model's reliability and effectiveness. The model shows good overall performance with an accuracy of 82%, which is quite acceptable for urban sound classification given the diverse nature of the sounds. `Jackhammer` and `gun_shot` classes have a high recall, which is beneficial as these sounds could be critical in urban monitoring systems. The confusion matrix indicates that certain sound classes are more likely to be confused with others (e.g., `engine_idling` with `drilling`), suggesting that these classes have similar acoustic features.  `Children Playing` is often confused with `Dog Bark` and vice versa, suggesting that these sounds have overlapping acoustic features. We observe the same phenomenom for `Engine Idling` and `Drilling` show notable misclassification between each other, likely due to similar sound patterns.

![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/train_test.jpg)

![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/class_report.jpg)

![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/matrix_conf.jpg)


### Bibliography

* Huimei Han a b, Ying Li a, Xingquan Zhu b _Convolutional neural network learning for generic data classification_ **(2021)** [[link](https://www.sciencedirect.com/science/article/abs/pii/S0020025518308703)]
      
* Karol J. Piczak _ENVIRONMENTAL SOUND CLASSIFICATION WITH CONVOLUTIONAL NEURAL NETWORKS_ **(2015)** [[link](https://www.karolpiczak.com/papers/Piczak2015-ESC-ConvNet.pdf)]

* Aditya Khamparia et al. _Sound Classification Using Convolutional Neural Network and Tensor Deep Stacking Network_ **(2019)** [[link](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8605515)]
