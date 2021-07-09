# Playing sounds with QtMultimedia

## Installation

The standard PyQt5 installation does not include QtMultimedia, therefore a manual installation might be required.

```
sudo apt install python3-pyqt5.qtmultimedia
sudo apt install libqt5multimedia5-plugins
```

## Usage

First, create a QMediaPlayer object.
This class already provides a lot of useful functions, for example play, pause or setting the volume.
See the [official documentation](https://doc.qt.io/qtforpython-5/PySide2/QtMultimedia/QMediaPlayer.html) for all provided functions.

```
self.player = QMediaPlayer()
```

To load media files, a QUrl based on an absolute file path has to be provided.

```
fullpath = '/home/user/music/song.mp3'
url = QUrl.fromLocalFile(fullpath)
```

This QUrl is used to create a QMediaContent object which can then be played with the QMediaPlayer.

```
content = QMediaContent(url)
self.player.setMedia(content)
self.player.play()
```

For a more sophisticated media player, it is recommended to also use a [QMediaPlaylist](https://doc.qt.io/qtforpython-5/PySide2/QtMultimedia/QMediaPlaylist.html) for managing different media files.

## Further Reading

Have a look at [PyTunes](https://github.com/chaNcharge/PyTunes) for a lightweight music player based on PyQt5.
