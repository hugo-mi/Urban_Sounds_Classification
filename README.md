# Urban_Sounds_Classification
Classification of boat sounds audio using deep learning

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

## Results

The trained a end-to-end model achieves high accuracy in classifying urban sounds. The performance is validated on a separate test set, with metrics like precision, recall, and F1-score demonstrating the model's reliability and effectiveness. The model shows good overall performance with an accuracy of 82%, which is quite acceptable for urban sound classification given the diverse nature of the sounds. `Jackhammer` and `gun_shot` classes have a high recall, which is beneficial as these sounds could be critical in urban monitoring systems. The confusion matrix indicates that certain sound classes are more likely to be confused with others (e.g., `engine_idling` with `drilling`), suggesting that these classes have similar acoustic features.  `Children Playing` is often confused with `Dog Bark` and vice versa, suggesting that these sounds have overlapping acoustic features. We observe the same phenomenom for `Engine Idling` and `Drilling` show notable misclassification between each other, likely due to similar sound patterns.

![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/train_test.jpg)

![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/class_report.jpg)

![](https://github.com/hugo-mi/Urban_Sounds_Classification/blob/main/img/matrix_conf.jpg)
