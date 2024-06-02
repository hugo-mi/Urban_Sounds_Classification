# Boat_Sounds_Classification
Classification of boat sounds audio using deep learning

## Database

This contribution presents a database of underwater sounds produced by vessels of various types. Besides sound recordings, the database contains details of the conditions for obtaining each recording: type of vessel, location of the recording equipment, weather conditions, etc. For its realization, a methodology for recording sounds and gathering additional information has been established, that will facilitate its use to the research community, and expanding the number of records in the database in the future.

The sounds are recorded in shallow waters and in real conditions. Therefore, the recordings contain both natural and anthropogenic environment noise. It aims to provide a database of real sounds that researchers can use, for example, to train boat detectors and classifiers, usable in monitoring maritime traffic.

### Database field description

| **Field**                            | **Description**                                                                                                                                                                                                                                              |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                 | A unique identifier for each record.                                                                                                                                                                                                                         |
| `name`                               | The name of the recording. Usually it is a ship name, except for records containing recordings of unknown ships or records of ambient noise.                                                                                                                 |
| `type`                               | Boat category.                                                                                                                                                                                                                                               |
| `pic`                                | Link to a picture of the boat.                                                                                                                                                                                                                               |
| `location`                           | GPS position of the recording equipment shown in a Google map.                                                                                                                                                                                               |
| `date`                               | Time and date of the recording. The format is YYYY-MM-DD HH:MM:SS. If no precise information is available, the registered time is 00:00:00.                                                                                                                 |
| `H_G_D`                              | Hydrophone-Gain-Depth. This field contains three sets of one to three figures each, related to the hydrophones used for the recording. The first vector indicates the numbers of the hydrophones, the second the gains and the third the heights measured from the sea bottom (p1, p2, p3 in Fig. 1). For instance, a value `H_G_D = (1, 2) (16, 32) (5, 7.5)` means that hydrophones 1 and 2 were used for the recording, with gains x16 and x32, and at distances of 5m and 7.5m from the bottom. |
| `audio`                              | Link to download the audio file, and a streaming player to listen to the recording.                                                                                                                                                                           |
| `video`                              | Indicates if there is a video documenting the recording.                                                                                                                                                                                                     |
| `channelDepth`                       | Sea depth (m) at the hydrophone position (c in Fig. 1).                                                                                                                                                                                                      |
| `wind`                               | Wind speed (km/h) measured in-situ.                                                                                                                                                                                                                          |
| `ais link`                           | Link to the AIS (Automatic Identification System) of the vessel, when available.                                                                                                                                                                              |
| `distance`                           | Approximate distance between the vessel recorded and the vertical of the hydrophone (d in Fig. 1). There are four intervals of approximation (except where the exact distance is known): <50m, 50-100m, 100-150m, >150m.                                     |
| `atmospheric and oceanographic data` | Information taken from the meteorological stations with information on temperature, humidity, wind speed, and rain.                                                                                                                                           |
| `notes`                              | Information obtained during recording, or from the video file, not contained elsewhere.                                                                                                                                                                       |
| `duration`                           | Duration in minutes:seconds of the audio clip.                                                                                                                                                                                                                |

> Universidad de Vigo, Telecomunications faculty. Campus Universitario Lagoas-Marcosende, 36310 VIGO (Pontevedra)
©Uvigo-Sonitum 2016 | Contact: dsantos(at)gts.uvigo.es

**Online Database:**
https://underwaternoise.atlanttic.uvigo.es/indexDB.php
